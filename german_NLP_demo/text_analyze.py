"""
Author: Kyle Martin
Email: mkylemartin@gmail.com

This script performs a basic analysis of German text fed into the terminal.

"""
import re
import pandas as pd
from glob import glob

import features
print('Modules loaded...')

filename = input('Enter the filename followed by the .txt extention:\n')

# Text source: https://bit.ly/2IGWWov
raw_text = open(filename).read()
# preprocesses document
preprocessed = re.sub(r'\n', ' ', raw_text)


# process the text
nlp_text = features.nlp(preprocessed)

# extract relevant features
result_dict = {
    'spell_checker': features.spell_checker(nlp_text)['percent_score'],
    'sentence_count': features.sentence_count(nlp_text),
    'ttr': features.ttr(nlp_text),
    'cttr': features.ttr(nlp_text, kind='cttr'), # TTR accounting for size
    'ttr-lemma': features.ttr(nlp_text, kind='lemma'),
    'ttr-NOUN': features.ttr(nlp_text, kind='NOUN'),
    'word_count': features.word_count(nlp_text),
    'words_per_sentence': features.words_per_sentence(nlp_text,
                                                      stop_words=True),
    'words_per_sentence_no_stop_words':
        features.words_per_sentence(nlp_text, stop_words=False),
    'not_stop_words': features.not_stop_words(nlp_text),
    'stop_words': features.stop_words(nlp_text),
    'mispelled_words': features.spell_checker(nlp_text)['incorrect_words']
}

# print output to console
for k, v in result_dict.items():
    print(k, v, sep='\t')

# write output to .csv
df = pd.DataFrame.from_dict(result_dict, orient='index')
df.to_csv(f'{filename}-output.csv')
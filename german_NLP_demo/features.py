"""
Author: Kyle Martin
Email: mkylemartin@gmail.com

Features to be used on texts

"""
import enchant
import spacy
import numpy as np
nlp = spacy.load('de')

# enchant setup
enchant.set_param('enchant.myspell.dictionary.path',
                  'dict_de')
spell_check = enchant.Dict('de_DE_frami')

def spell_checker(doc):
    """ uses an open office german dictionary and the `enchant` library 
        prints the incorrect words to the console. """
    words = [token.text for token in doc
             if token.is_punct is False]

    correct_words = 0
    incorrect_words = []
    for word in words:
        if spell_check.check(word) is True:
            correct_words += 1
        else:
            incorrect_words.append(word)
    if len(words) > 1:
        score = correct_words / len(words)
    else:
        score = 0


    results = {'percent_score': round(score, 3),
               'correct_words': correct_words,
               'incorrect_words': incorrect_words}

    return results


def words_per_sentence(doc, stop_words=True):
    """ average number of words divided by the no. of sentences

    `doc`: spacy document
    `stop_words=True/false`: whether or not you want to include stopwords
    """

    # if you want stopwords included
    if stop_words is True:
        num_words = word_count(doc)

    # if you do not want stopwords included
    elif stop_words is False:
        num_words = len(not_stop_words(doc))

    try:
        wps = num_words / sentence_count(doc)
    except ZeroDivisionError:
        wps = 0

    return round(wps, 3)


def word_count(doc):
    """ gets the word count of a given response
        returns a list of words. """
    # doc = nlp(comment)
    words = len([token.text for token in doc
                 if token.is_punct is False])

    return words


def sentence_count(doc):
    # doc = nlp(response)
    length = len([sent for sent in doc.sents])
    return length


def stop_words(doc):
    """takes a whole comment and then returns a list of stop words """
    stop_words = []
    # for token in nlp(comment):
    #   if token.is_stop == True
    #       stop_words.append(token)

    [stop_words.append(token.text)
     for token in doc if token.is_stop is True and
     token.is_punct is False]

    return stop_words


def not_stop_words(doc):
    """ This returns a list of all the words that are NOT stop words """
    not_stop_words = []

    [not_stop_words.append(token.text)
     for token in doc if token.is_stop is False and
     token.is_punct is False]

    return not_stop_words


def ttr(doc, kind='normal'):
    """ Type to token ratio, does normal unless another kind is
        specified. Possible values for `kind` are:
            - cttr      (corrected for size)
            - lemma
            - any part of speech see http://universaldependencies.org/u/pos/
    """

    # Filter out all stop words
    tokens = [token.text for token in doc if
              token.is_stop is False and
              token.is_punct is False]

    if kind == 'normal':
        types = set(tokens)
        try:
            ttr = len(types) / len(tokens)
        except ZeroDivisionError:
            ttr = 0
        return round(ttr, 3)

    elif kind == 'cttr':
        types = set(tokens)
        if len(tokens) != 0:
            cttr = len(types) / np.sqrt(2 * len(tokens))
        else:
            cttr = 0
        return round(cttr, 3)

    elif kind == 'ttrAdjAdv':
        # I hesitate to call this `ttr-modifiers` because I would need to
        # do tregex to find cases where an adj or adv appears before a noun
        # to determine if is a true modifier.
        adjAdv = [token.text for token in doc if token.pos_ == 'ADJ' or
                  token.pos_ == 'ADV']
        try:
            ttrAdjAdv = len(set(adjAdv)) / len(tokens)
        except ZeroDivisionError:
            ttrAdjAdv = 0
        return round(ttrAdjAdv, 3)

    elif kind == 'lemma':
        """ Takes the whole resposne and does Lemma TTR on it"""
        data = []
        for token in doc:
            data.append((token.text, token.lemma_, token.is_stop))

        lemmas = [word[1] for word in data if word[2] is True]
        # do I take the set of stuff??
        # num of unique lemma divided by tokens
        try:
            lemma_ttr = len(set(lemmas)) / len(tokens)
        except ZeroDivisionError:
            lemma_ttr = 0
        return round(lemma_ttr, 3)

    else:
        pos = [token.text for token in doc if token.pos_ == kind]
        try:
            ttr = len(set(pos)) / len(tokens)
        except ZeroDivisionError:
            ttr = 0
        return round(ttr, 3)

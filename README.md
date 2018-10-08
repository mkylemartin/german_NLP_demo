
# German Natural Language Processing
## 9 Oct 2018

###  Installation Instructions
**Install Python** (https://www.python.org/downloads/)

- _Make sure and check the box that you want Python installed on your PATH._


**Use the `pip` command** to install the following packages (just copy/paste): 


- `pip install pyenchant numpy pandas`

- _(Note: you might have to use `pip3` instead of `pip` on Mac OS)_

Now we'll install a library called `spacy`:

- `pip install -U spacy`

And now install the `de` module, which contains all the required German data:

- `python -m spacy download de`

### Usage Instruction

Make sure that the file you would like to analyze is in a `.txt` format. 

Put the text file in the folder that contains the `text_analyze.py` file.

Type the following command into your terminal window:
- `python3 text_analyze.py`

Type the file name (including the `.txt` extension) into the terminal and type `[ENTER]`

### Customization

Change the variables in the `result_dict` on line 27 in `text_analyze.py` to modify the output. The default output should include the following:
```
spell_checker
sentence_count
ttr
cttr
ttr-lemma
ttr-NOUN
word_count
words_per_sentence
words_per_sentence_no_stop_words
not_stop_words
stop_words
mispelled_words```

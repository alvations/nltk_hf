# Intro

Cos I'm itching to code something and this is what I see people wanted. So Punkt tokenizer reimplementation, here comes...

# Recon

To reimplement OSS, the first thing I usually do is to trace back from how the function is called in the original code:

When you do `from nltk import sent_tokenize` this is essentially what's happening:

```python
from nltk.data import load

# Standard sentence tokenizer.
def sent_tokenize(text, language="english"):
    """
    Return a sentence-tokenized copy of *text*,
    using NLTK's recommended sentence tokenizer
    (currently :class:`.PunktSentenceTokenizer`
    for the specified language).

    :param text: text to split into sentences
    :param language: the model name in the Punkt corpus
    """
    tokenizer = load(f"tokenizers/punkt/{language}.pickle")
    return tokenizer.tokenize(text)
```

**Wait a minute** does that mean it's reinitializing the tokenizer object everytime I do `lambda x: sent_tokenize(x)`... 

Yeah it is -_-|||

Lets look at `load()` then. Argh, it's bunch of if-else... https://github.com/nltk/nltk/blob/develop/nltk/data.py#L734 
Okay, I'm just going to load the object and then see what class it gives. 


```python
>>> from nltk.data import load
>>> tokenizer = load(f"tokenizers/punkt/english.pickle")
>>> type(tokenizer)
nltk.tokenize.punkt.PunktSentenceTokenizer
```

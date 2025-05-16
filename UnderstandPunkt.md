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

So it comes from `nltk/tokenize/punkt.py`, 

```
class PunktSentenceTokenizer(PunktBaseClass, TokenizerI):
    """
    A sentence tokenizer which uses an unsupervised algorithm to build
    a model for abbreviation words, collocations, and words that start
    sentences; and then uses that model to find sentence boundaries.
    This approach has been shown to work well for many European
    languages.
    """
```

Nested inheritance... So what's in `PunktBaseClass`?

```
class PunktBaseClass:
    """
    Includes common components of PunktTrainer and PunktSentenceTokenizer.
    """

    def __init__(self, lang_vars=None, token_cls=PunktToken, params=None):
        if lang_vars is None:
            lang_vars = PunktLanguageVars()
        if params is None:
            params = PunktParameters()
        self._params = params
        self._lang_vars = lang_vars
        self._Token = token_cls
        """The collection of parameters that determines the behavior
        of the punkt tokenizer."""
```

For sub-ojects... `PunktLanguageVars` and `PunktParameters`. Lets start with the lang vars

```
class PunktLanguageVars:
    """
    Stores variables, mostly regular expressions, which may be
    language-dependent for correct application of the algorithm.
    An extension of this class may modify its properties to suit
    a language other than English; an instance can then be passed
    as an argument to PunktSentenceTokenizer and PunktTrainer
    constructors.
    """

    __slots__ = ("_re_period_context", "_re_word_tokenizer")

    def __getstate__(self):
        # All modifications to the class are performed by inheritance.
        # Non-default parameters to be pickled must be defined in the inherited
        # class.
        return 1

    def __setstate__(self, state):
        return 1

    sent_end_chars = (".", "?", "!")
    """Characters which are candidates for sentence boundaries"""

    @property
    def _re_sent_end_chars(self):
        return "[%s]" % re.escape("".join(self.sent_end_chars))

    internal_punctuation = ",:;"  # might want to extend this..
    """sentence internal punctuation, which indicates an abbreviation if
    preceded by a period-final token."""

    re_boundary_realignment = re.compile(r'["\')\]}]+?(?:\s+|(?=--)|$)', re.MULTILINE)
    """Used to realign punctuation that should be included in a sentence
    although it follows the period (or ?, !)."""

    _re_word_start = r"[^\(\"\`{\[:;&\#\*@\)}\]\-,]"
    """Excludes some characters from starting word tokens"""

    @property
    def _re_non_word_chars(self):
        return r"(?:[)\";}\]\*:@\'\({\[%s])" % re.escape(
            "".join(set(self.sent_end_chars) - {"."})
        )

    """Characters that cannot appear within words"""

    _re_multi_char_punct = r"(?:\-{2,}|\.{2,}|(?:\.\s){2,}\.)"
    """Hyphen and ellipsis are multi-character punctuation"""

    _word_tokenize_fmt = r"""(
        %(MultiChar)s
        |
        (?=%(WordStart)s)\S+?  # Accept word characters until end is found
        (?= # Sequences marking a word's end
            \s|                                 # White-space
            $|                                  # End-of-string
            %(NonWord)s|%(MultiChar)s|          # Punctuation
            ,(?=$|\s|%(NonWord)s|%(MultiChar)s) # Comma if at end of word
        )
        |
        \S
    )"""
    """Format of a regular expression to split punctuation from words,
    excluding period."""

    def _word_tokenizer_re(self):
        """Compiles and returns a regular expression for word tokenization"""
        try:
            return self._re_word_tokenizer
        except AttributeError:
            self._re_word_tokenizer = re.compile(
                self._word_tokenize_fmt
                % {
                    "NonWord": self._re_non_word_chars,
                    "MultiChar": self._re_multi_char_punct,
                    "WordStart": self._re_word_start,
                },
                re.UNICODE | re.VERBOSE,
            )
            return self._re_word_tokenizer

    def word_tokenize(self, s):
        """Tokenize a string to split off punctuation other than periods"""
        return self._word_tokenizer_re().findall(s)

    _period_context_fmt = r"""
        %(SentEndChars)s             # a potential sentence ending
        (?=(?P<after_tok>
            %(NonWord)s              # either other punctuation
            |
            \s+(?P<next_tok>\S+)     # or whitespace and some other token
        ))"""
    """Format of a regular expression to find contexts including possible
    sentence boundaries. Matches token which the possible sentence boundary
    ends, and matches the following token within a lookahead expression."""

    def period_context_re(self):
        """Compiles and returns a regular expression to find contexts
        including possible sentence boundaries."""
        try:
            return self._re_period_context
        except:
            self._re_period_context = re.compile(
                self._period_context_fmt
                % {
                    "NonWord": self._re_non_word_chars,
                    "SentEndChars": self._re_sent_end_chars,
                },
                re.UNICODE | re.VERBOSE,
            )
            return self._re_period_context
```

Cool, `__slots__` magic! This is a Pythonic mechanism to pre-initialize variables https://stackoverflow.com/questions/472000/usage-of-slots 

I see that the slots are going to hold bunch of regexes `__slots__ = ("_re_period_context", "_re_word_tokenizer")`, I think modern Python is fast enough to avoid this. For simplicity in reimplementation most probably we can avoid the `__slots__` mechanism.


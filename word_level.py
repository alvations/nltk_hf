import re

from patterns import sent_end_chars

    
class PunktWordTokenizer:
    # Hyphen and ellipsis are multi-character punctuation.
    _multi_char = r"(?:-{2,}|\.{2,}|(?:\.\s){2,}\.)"
    # Excludes some characters from starting word tokens.
    _word_start = r"[^\(\"`\{\[:;&#\*@\)\}\]\-,]"
    # Characters that cannot appear within words
    non_word_chars = re.escape("".join(set(sent_end_chars) - {"."}))
    _non_word = fr"[)\";}}\]*:@'(\{{\[{non_word_chars}]"

    # Format of a regular expression to split punctuation from words, excluding period.
    _word_tokenize_pattern = fr"""
    (
        {_multi_char}                              # Multi-char punctuation
        |
        (?={_word_start})\S+?                      # Word-like tokens
        (?=
            \s|$|{_non_word}|{_multi_char}|        # Whitespace, punctuation
            ,(?=$|\s|{_non_word}|{_multi_char})    # Trailing comma
        )
        |
        \S                                         # Any single non-space char
    )
    """
    _regex = re.compile(_word_tokenize_pattern, re.UNICODE | re.VERBOSE)

    def tokenize(self, text):
        return self._regex.findall(text)


class PunktBoundaryDetector:
    # Characters that cannot appear within words
    _sent_end_chars = re.escape("".join(set(sent_end_chars)))  # "!?"
    _non_word = fr"[)\";}}\]*:@'(\{{\[{_sent_end_chars}]"  # Non-word char class

    # Pattern to find sentence-ending punctuation followed by certain contexts
    _period_context_pattern = rf"""
        [{_sent_end_chars}]                  # potential sentence-ending char
        (?=(?P<after_tok>
            {_non_word}                      # followed by other punctuation
            |
            \s+(?P<next_tok>\S+)             # or whitespace + next token
        ))
    """
    _regex = re.compile(_period_context_pattern, re.UNICODE | re.VERBOSE)
    
    def detect(self, text):
        matches = [
            (m.group(), m.group('after_tok'), m.groupdict().get('next_tok')) 
            for m in self._regex.finditer(text)
        ]
        # Returns `Tuple[str, str, str]` that matches `punct, after_tok, next_tok` 
        return matches

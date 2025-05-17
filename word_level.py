import re
from typing import Any, Optional

from patterns import sent_end_chars


class PunktWordTokenizer:
    # Hyphen and ellipsis are multi-character punctuation.
    _multi_char = r"(?:-{2,}|\.{2,}|(?:\.\s){2,}\.)"
    # Excludes some characters from starting word tokens.
    _word_start = r"[^\(\"`\{\[:;&#\*@\)\}\]\-,]"
    # Characters that cannot appear within words
    non_word_chars = re.escape("".join(set(sent_end_chars) - {"."}))
    _non_word = rf"[)\";}}\]*:@'(\{{\[{non_word_chars}]"

    # Format of a regular expression to split punctuation from words, excluding period.
    _word_tokenize_pattern = rf"""
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
    _non_word = rf"[)\";}}\]*:@'(\{{\[{_sent_end_chars}]"  # Non-word char class

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
            (m.group(), m.group("after_tok"), m.groupdict().get("next_tok"))
            for m in self._regex.finditer(text)
        ]
        # Returns `Tuple[str, str, str]` that matches `punct, after_tok, next_tok`
        return matches


class PunktToken:
    """Stores a token of text with annotations produced during sentence boundary detection."""

    _RE_NON_PUNCT = re.compile(r"[^\W\d]", re.UNICODE)
    _RE_ELLIPSIS = re.compile(r"\.\.+$")
    _RE_NUMERIC = re.compile(r"^-?[\.,]?\d[\d,\.-]*\.?$")
    _RE_INITIAL = re.compile(r"[^\W\d]\.$", re.UNICODE)
    _RE_ALPHA = re.compile(r"[^\W\d]+$", re.UNICODE)

    # Annotation flags, set during Punkt processing passes.
    parastart: Optional[bool] = None
    linestart: Optional[bool] = None
    sentbreak: Optional[bool] = None
    abbr: Optional[bool] = None
    ellipsis: Optional[bool] = None
    # Store the string names of the annotations and override them when passed in.
    _properties = ["parastart", "linestart", "sentbreak", "abbr", "ellipsis"]

    def __init__(self, tok: str, **params: Any):
        # Stores the surface token and its type.
        self.tok = tok
        self.type = self._RE_NUMERIC.sub("##number##", token_text.lower())
        self.period_final = tok.endswith(".")

        # Override any parameters that was passed when initialized.
        for k, v in params.items():
            if k in _properties:
                setattr(self, k, v)

    @property
    def type_no_period(self) -> str:
        """The token's 'type' with its final period removed, if it has one."""
        if len(self.type) > 1 and self.type.endswith("."):
            return self.type[:-1]
        return self.type

    @property
    def type_no_sentperiod(self) -> str:
        """
        The token's 'type' with its final period removed if it's marked as a sentence break.
        Otherwise, returns the full 'type'.
        """
        return self.type_no_period if self.sentbreak else self.type

    @property
    def first_upper(self) -> bool:
        """True if the token's first character is uppercase."""
        return self.tok[0].isupper()

    @property
    def first_lower(self) -> bool:
        """True if the token's first character is lowercase."""
        return self.tok[0].islower()

    @property
    def first_case(self) -> str:
        """Returns 'lower', 'upper', or 'none' based on the token's first character."""
        if self.first_lower:
            return "lower"
        if self.first_upper:
            return "upper"
        return "none"

    @property
    def is_ellipsis(self) -> bool:
        """True if the token text matches the ellipsis pattern (e.g., '...')."""
        return self._RE_ELLIPSIS.match(self.tok)

    @property
    def is_number(self) -> bool:
        """True if the token's type is '##number##'."""
        return self.type.startswith("##number##")

    @property
    def is_initial(self) -> bool:
        """True if the token text matches the initial pattern (e.g., 'A.')."""
        return self._RE_INITIAL.match(self.tok)

    @property
    def is_alpha(self) -> bool:
        """True if the token text is all alphabetic."""
        return self._RE_ALPHA.match(self.tok)

    @property
    def is_non_punct(self) -> bool:
        """True if the token is either a number or is alphabetic."""
        return self._RE_NON_PUNCT.search(self.type)

    def __repr__(self):
        """
        A string representation of the token that can reproduce it
        with eval(), which lists all the token's non-default annotations.
        """
        type_str = f" type={repr(self.type)}," if self.type != self.tok else ""

        args = [repr(self.tok)]
        for p in self._properties:
            value = getattr(self, p)
            if value is not None:  # Only set True, False, or other non-None values
                args.append(f"{p}={value!r}")

        return f"{self.__class__.__name__}({', '.join(parts)})"

    def __str__(self):
        """
        A string representation akin to that used by Kiss and Strunk.
        """
        res = self.tok
        if self.abbr:
            res += "<A>"
        if self.ellipsis:
            res += "<E>"
        if self.sentbreak:
            res += "<S>"
        return res

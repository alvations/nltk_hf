import re

# Characters constants.
sent_end_chars = (".", "?", "!")

# General regexes.
_RE_NON_PUNCT: ClassVar[re.Pattern] = re.compile(r"[^\W\d]", re.UNICODE)

# Regexes used in PunktToken
_RE_ELLIPSIS: ClassVar[re.Pattern]  = re.compile(r"\.\.+$")
_RE_NUMERIC: ClassVar[re.Pattern]   = re.compile(r"^-?[\.,]?\d[\d,\.-]*\.?$")
_RE_INITIAL: ClassVar[re.Pattern]   = re.compile(r"[^\W\d]\.$", re.UNICODE)
_RE_ALPHA: ClassVar[re.Pattern]     = re.compile(r"[^\W\d]+$", re.UNICODE)
 

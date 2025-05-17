Inside the .zip file from https://github.com/nltk/nltk_data/blob/gh-pages/packages/tokenizers/punkt_tab.zip, there's a README.md that contains the source corpora from which the authors trained the Punkt tokenizers. 

```
There are pretrained tokenizers for the following languages:

File                Language            Source                             Contents                Size of training corpus(in tokens)           Model contributed by
=======================================================================================================================================================================
czech.pickle        Czech               Multilingual Corpus 1 (ECI)        Lidove Noviny                   ~345,000                             Jan Strunk / Tibor Kiss
                                                                           Literarni Noviny
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
danish.pickle       Danish              Avisdata CD-Rom Ver. 1.1. 1995     Berlingske Tidende              ~550,000                             Jan Strunk / Tibor Kiss
                                        (Berlingske Avisdata, Copenhagen)  Weekend Avisen
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
dutch.pickle        Dutch               Multilingual Corpus 1 (ECI)        De Limburger                    ~340,000                             Jan Strunk / Tibor Kiss
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
english.pickle      English             Penn Treebank (LDC)                Wall Street Journal             ~469,000                             Jan Strunk / Tibor Kiss
                    (American)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
estonian.pickle     Estonian            University of Tartu, Estonia       Eesti Ekspress                  ~359,000                             Jan Strunk / Tibor Kiss
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
finnish.pickle      Finnish             Finnish Parole Corpus, Finnish     Books and major national        ~364,000                             Jan Strunk / Tibor Kiss
                                        Text Bank (Suomen Kielen           newspapers
                                        Tekstipankki)
                                        Finnish Center for IT Science
                                        (CSC)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
french.pickle       French              Multilingual Corpus 1 (ECI)        Le Monde                        ~370,000                             Jan Strunk / Tibor Kiss
                    (European)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
german.pickle       German              Neue Zürcher Zeitung AG            Neue Zürcher Zeitung            ~847,000                             Jan Strunk / Tibor Kiss
                    (Switzerland)       CD-ROM
                    (Uses "ss"
                     instead of "ß")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
greek.pickle        Greek               Efstathios Stamatatos              To Vima (TO BHMA)               ~227,000                             Jan Strunk / Tibor Kiss
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
italian.pickle      Italian             Multilingual Corpus 1 (ECI)        La Stampa, Il Mattino           ~312,000                             Jan Strunk / Tibor Kiss
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
norwegian.pickle    Norwegian           Centre for Humanities              Bergens Tidende                 ~479,000                             Jan Strunk / Tibor Kiss
                    (Bokmål and         Information Technologies,
                     Nynorsk)           Bergen
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
polish.pickle       Polish              Polish National Corpus             Literature, newspapers, etc.  ~1,000,000                             Krzysztof Langner
                                        (http://www.nkjp.pl/)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
portuguese.pickle   Portuguese          CETENFolha Corpus                  Folha de São Paulo              ~321,000                             Jan Strunk / Tibor Kiss
                    (Brazilian)         (Linguateca)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
slovene.pickle      Slovene             TRACTOR                            Delo                            ~354,000                             Jan Strunk / Tibor Kiss
                                        Slovene Academy for Arts
                                        and Sciences
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
spanish.pickle      Spanish             Multilingual Corpus 1 (ECI)        Sur                             ~353,000                             Jan Strunk / Tibor Kiss
                    (European)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
swedish.pickle      Swedish             Multilingual Corpus 1 (ECI)        Dagens Nyheter                  ~339,000                             Jan Strunk / Tibor Kiss
                                                                           (and some other texts)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
turkish.pickle      Turkish             METU Turkish Corpus                Milliyet                        ~333,000                             Jan Strunk / Tibor Kiss
                                        (Türkçe Derlem Projesi)
                                        University of Ankara
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

```


# Related Works

https://www.google.com/search?q=inurl:s3.amazonaws.com/tm-town-nlp-resources/

- Using SRX standard for sentence segmentation in LanguageTool [ltc-043-milkowski.pdf](https://github.com/user-attachments/files/20261132/ltc-043-milkowski.pdf)
- Alinging sentence in bilingual corpora using lexical information [Aligning+sentences+in+bilingual+corpora+using+lexical+information.pdf](https://github.com/user-attachments/files/20261133/Aligning%2Bsentences%2Bin%2Bbilingual%2Bcorpora%2Busing%2Blexical%2Binformation.pdf)
- Thoughts on Word and Sentence Segmentation in Thai [snlp2007-wirote.pdf](https://github.com/user-attachments/files/20261146/snlp2007-wirote.pdf)
- A Sentence Boundary Detection System [SpResConf00 (1).pdf](https://github.com/user-attachments/files/20261148/SpResConf00.1.pdf)
- IBM Research Report (BLEU) [ibm_bleu_2001.pdf](https://github.com/user-attachments/files/20261156/ibm_bleu_2001.pdf)
- What's a word? What's a sentence? [GrefenstetteTapanainen1994.pdf](https://github.com/user-attachments/files/20261157/GrefenstetteTapanainen1994.pdf)
- Kiss and Strunk Punkt (2006) [ks2005FINAL.pdf](https://github.com/user-attachments/files/20261160/ks2005FINAL.pdf)
- Extrinsic Evaluation of Sentence Alignment Systems [sent-align.pdf](https://github.com/user-attachments/files/20261166/sent-align.pdf)
- An Analysis of Sentence Boundary Detection Systems for English and Portuguese Documents [An+Analysis+of+Sentence+Boundary+Detection+Systems+for+English+and+Portuguese+Documents.pdf](https://github.com/user-attachments/files/20261169/An%2BAnalysis%2Bof%2BSentence%2BBoundary%2BDetection%2BSystems%2Bfor%2BEnglish%2Band%2BPortuguese%2BDocuments.pdf)
- Automatic sentence break disambiguation for Thai [iccpol2001.pdf](https://github.com/user-attachments/files/20261177/iccpol2001.pdf)
- Evaluating Word Alignment Systems [Evaluating+Word+Alignment+Systems+-+STP.pdf](https://github.com/user-attachments/files/20261180/Evaluating%2BWord%2BAlignment%2BSystems%2B-%2BSTP.pdf)
- Sentence Boundary Detection and the Problem with the U.S. [sbd_naacl_2009.pdf](https://github.com/user-attachments/files/20261184/sbd_naacl_2009.pdf)
- Improved Sentence Alignment for Movie Subtitles [ranlp07-subalign.pdf](https://github.com/user-attachments/files/20261186/ranlp07-subalign.pdf)
- Period, Capital, etc. [cl-prop-compressed.pdf](https://github.com/user-attachments/files/20261207/cl-prop-compressed.pdf)
- Improved Unsupervised Sentence Alignment for Symmetrical and Asymmetrical Parallel Corpora [braune_coling2010.pdf](https://github.com/user-attachments/files/20261202/braune_coling2010.pdf)
- ALIGNING SENTENCES IN PARALLEL CORPORA [p169-brown.pdf](https://github.com/user-attachments/files/20261205/p169-brown.pdf)
- Sentence Boundary Detection: A Long Solved Problem? [C12-2096.pdf](https://github.com/user-attachments/files/20261210/C12-2096.pdf)
- Sentence Boundary Detection: A Comparison of Paradigms for Improving MT Quality [walker.pdf](https://github.com/user-attachments/files/20261215/walker.pdf)
- Elephant: Sequence Labeling for Word and Sentence Segmentation [Elephant-+Sequence+Labeling+for+Word+and+Sentence+Segmentation.pdf](https://github.com/user-attachments/files/20261216/Elephant-%2BSequence%2BLabeling%2Bfor%2BWord%2Band%2BSentence%2BSegmentation.pdf)
- A Maximum Entropy Approach to Identifying Sentence Boundaries [A97-1004.pdf](https://github.com/user-attachments/files/20261218/A97-1004.pdf)
- Segmentation and alignment of parallel text for statistical machine translation [JNLE-REF300-Dec05.pdf](https://github.com/user-attachments/files/20261219/JNLE-REF300-Dec05.pdf)
- Tagging Sentence Boundaries [A00-2035.pdf](https://github.com/user-attachments/files/20261223/A00-2035.pdf)
- Adaptive Multilingual Sentence Boundary Disambiguation [cl-palmer.pdf](https://github.com/user-attachments/files/20261237/cl-palmer.pdf)
- AUTOMATIC EXTRACTION OF RULES FOR SENTENCE BOUNDARY DISAMBIGUATION [Automatic+Extraction+of+Rules+For+Sentence+Boundary+Disambiguation.pdf](https://github.com/user-attachments/files/20261239/Automatic%2BExtraction%2Bof%2BRules%2BFor%2BSentence%2BBoundary%2BDisambiguation.pdf) - Brill Tagger
- [golden_rules.txt](https://github.com/user-attachments/files/20261249/golden_rules.txt)
- Evaluation of Sentence Alignment Systems [sentence_alignment (1).pdf](https://github.com/user-attachments/files/20261260/sentence_alignment.1.pdf)

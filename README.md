# PyShawpack
 ![image](https://github.com/AbdelrahmanShahrour/PyShawpack/blob/main/logo/SHAWPACK-LOGO.png?raw=true) 

###  Now with PyShawpack, dealing with Arabic texts has become easy, and in the future it will become easier with PyShawpack 

## Installation

```python
pip3 install PyShawpack==0.5
```
---
## Structure 

|> PyShawpack

| ------> | `Normalization`

|---------| ------> | `Normalization_ar`

|---------|---------| ------> | alef

|---------|---------| ------> | lamalef

|---------|---------| ------> | hamza

|---------|---------| ------> | tah

|---------|---------| ------> | madah

|---------|---------| ------> | normalization_all

| ------> `Processor`

|---------| ------> | `Arabic_Processor`

|---------|---------| ------> | remove_stopword

|---------|---------| ------> | remove_other_lang

|---------|---------| ------> | remove_diacritics

|---------|---------| ------> | remove_arabic_punctuations

|---------|---------| ------> | arabic_only

|---------|---------| ------> | with_out_num

|---------| ------> | `English_Processor`

|---------|---------| ------> | remove_stopword

|---------|---------| ------> | english_only

|---------|---------| ------> | remove_english_punctuations

|---------|---------| ------> | with_out_num

|---------| ------> | `General_Processor`

|---------|---------| ------> | remove_mentions

|---------|---------| ------> | remove_hasgtag

|---------|---------| ------> | remove_links

|---------|---------| ------> | remove_punctation

|---------|---------| ------> | keep_text

|---------|---------| ------> | remove_emojis

|---------|---------| ------> | remove_whitespace

---

## Example:

```python
pip3 install PyShawpack==0.5
```

```python
from PyShawpack.Processor import Arabic_Processor
from PyShawpack.Processor import General_Processor
from PyShawpack.Normalization import Normalization_ar
```

```python
def clean_tweet(tweet):
    tweet = General_Processor.remove_emojis(tweet)
    tweet = General_Processor.remove_hasgtag(tweet)
    tweet = General_Processor.remove_links(tweet)
    tweet = General_Processor.remove_mentions(tweet)
    tweet = General_Processor.remove_whitespace(tweet)
    tweet = General_Processor.remove_whitespace(tweet)
    tweet = Arabic_Processor.remove_arabic_punctuations(tweet)
    tweet = Arabic_Processor.remove_diacritics(tweet)
    tweet = Arabic_Processor.remove_other_lang(tweet)
    return tweet
```


```python
text = 'akhhh !تَوقَعْت اذا جات داريا بشوفهم كاملين بس لي للحين احس فيه احد ناقْصهم 💔 #Avlu https://www.messenger.com/ @pyshawpack '

clean_tweet(text)

```

output:
`' توقعت اذا جات داريا بشوفهم كاملين بس لي للحين احس فيه احد ناقصهم '
`

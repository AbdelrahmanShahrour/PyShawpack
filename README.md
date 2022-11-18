# PyShawpack
 ![image](https://github.com/AbdelrahmanShahrour/PyShawpack/blob/main/logo/SHAWPACK-LOGO.png?raw=true) 

###  Now with PyShawpack, dealing with Arabic texts has become easy, and in the future it will become easier with PyShawpack 

## Installation

```python
pip3 install PyShawpack==0.2
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

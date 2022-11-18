import re

from PyShawpack.ar import *
from PyShawpack.en import *
from PyShawpack.general import *


class Normalization_ar:
    def alef(text:str) -> str:
        for tam in ALEF_CHARS:
            output = text.replace(tam, NORMAL_ALEF)
        return output

    def lamalef(text:str) -> str:
        for tam in LAM_ALEF_COMBINED:
            output = text.replace(tam, LAM_ALEF_NORMAL)
        return output

    def hamza(text:str) -> str:
        for tam in HAMZA_CHARS:
            output = text.replace(tam, NORMAL_HAMZA)
        return output

    
    def tah(text:str) -> str:
        output = text.replace(TAH_MARBOTA, HA)
        return output


    def madah(text:str) -> str:
        output = text.replace(TATWEEL, "")
        return output
    
    def normalization_all(text:str) -> str:
        output = alef(text).lamalef(text).hamza(text).tah_marbota(text)
        return output

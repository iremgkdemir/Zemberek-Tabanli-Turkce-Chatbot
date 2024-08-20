import jpype
import jpype.imports
from jpype.types import *
import string
from helpers import correction_dict, TurkishMorphology, TurkishSpellChecker

class NLPProcessor:
    def __init__(self):
        self.morphology = TurkishMorphology.createWithDefaults()
        self.spell_checker = TurkishSpellChecker(self.morphology)
        self.pending_correction = None  # Düzeltme bekleyen kelimeyi tutar

    def normalize_input(self, user_input):
        # Noktalama işaretlerini kaldır
        user_input = user_input.translate(str.maketrans('', '', string.punctuation))

        # Düzeltme sözlüğünü kullanarak yaygın hataları düzelt
        words = user_input.split()
        corrected_words = []
        for word in words:
            # Eğer kelimenin ilk harfi büyükse, özel isim olduğunu varsay
            if word.isupper():
                word = word.lower()  # Büyük harfle yazılmış kelimeyi küçük harfe çevir

            # Önce düzeltme sözlüğünde kontrol et
            if word in correction_dict:
                corrected_words.append(correction_dict[word])
            else:
                # Zemberek ile kelime doğrulama ve düzeltme
                if not self.spell_checker.check(word):
                    suggestions = self.spell_checker.suggestForWord(word)
                    if suggestions:
                        suggestion = str(suggestions[0])
                        # Tek öneri varsa otomatik olarak düzelt
                        corrected_words.append(suggestion)
                    else:
                        corrected_words.append(word)
                else:
                    corrected_words.append(word)

        return " ".join(corrected_words)

import jpype
import jpype.imports

# correction_dict.py
correction_dict = {
    'nbr': 'naber',
    'slm': 'selam',
    'mrb': 'merhaba',
    'gorusuruz': 'görüşürüz',
    'tskr': 'teşekkür',
    'ii': 'iyi',
    'tm': 'tamam',
    'tmm': 'tamam',
}

# Zemberek dosyası için yardımcı importlar
zemberek_jar_path = "C:\\rulabased zemberek\\lib\\zemberek-full.jar"

# JVM'in zaten başlatılıp başlatılmadığını kontrol et
if not jpype.isJVMStarted():
    jpype.startJVM(classpath=[zemberek_jar_path])

TurkishMorphology = jpype.JClass('zemberek.morphology.TurkishMorphology')
TurkishSpellChecker = jpype.JClass('zemberek.normalization.TurkishSpellChecker')

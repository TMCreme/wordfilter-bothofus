from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from .models import UploadedFile
import logging


def processfile(data):
    new_file = UploadedFile.objects.get(file_id=data)
    f = new_file.file.open("r").read()
    word_tokens = word_tokenize(f)
    unique_words = set(word_tokens)
    en_stopwords = stopwords("english")
    result = [w for w in unique_words if not w.lower() in en_stopwords]
    new_file.result = result
    new_file.save()
    return result














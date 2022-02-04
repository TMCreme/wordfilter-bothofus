from unittest import result
from django.db import models


# file_id will be generated during form validation
# fie_id will be a unique reference for the various files uploaded. 
# file_id will also be used to query the files for reading. 
# The file field is taking the actual file input 
# the result will be null or blank at the time of upload 
# and be populated after the tokenization and removing stopwords
class UploadedFile(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modifieed = models.DateTimeField(auto_now=True)
    file_id = models.CharField(max_length=30, unique=True, db_index=True)
    file = models.FileField(upload_to="uploads")
    result = models.TextField(null=True, blank=True)








# Create your models here.


from django.db import models

class RagaDB(models.Model):
    name = models.TextField(default = "")
    name_hindi = models.TextField(default = "")
    thaat = models.TextField(default = "")
    thaat_hindi = models.TextField(default = "")
    vadi = models.TextField(default = "")
    vadi_hindi = models.TextField(default = "")
    samvadi = models.TextField(default = "")
    samvadi_hindi = models.TextField(default = "")
    time = models.TextField(default = "")
    time_hindi = models.TextField(default = "")
    aaroh = models.TextField(default = "")
    aaroh_hindi = models.TextField(default = "")
    aavaroh = models.TextField(default = "")
    aavaroh_hindi = models.TextField(default = "")
    info = models.TextField(default = "")
    info_hindi = models.TextField(default = "")
    video_link = models.TextField(default = "")
    link_slug = models.TextField(default = "")
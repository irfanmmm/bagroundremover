from django.db import models


class Removebaground(models.Model):
    uplodedimage = models.ImageField(upload_to="media/", blank=True, null=True)
    remove_bg = models.ImageField(upload_to="removed_images/", blank=True, null=True)

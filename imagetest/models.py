from django.db import models

class Test(models.Model):
    csv = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    def __unicode__(self):
        return self.csv


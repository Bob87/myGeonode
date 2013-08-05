from django.db import models

class Test(models.Model):
    csv = models.CharField(max_length=255)
    image = models.ImageField("Image",upload_to='imagetest',blank=True, null=True)
    def __unicode__(self):
        return self.csv


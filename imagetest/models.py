from django.db import models

class Test(models.Model):
    test1 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.test1

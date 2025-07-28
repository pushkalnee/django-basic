from django.db import models

# Create your models here.
class trans(models.Model):
    bike=models.CharField(max_length=50)
    amt=models.FloatField()
    transaction=models.CharField(max_length=100,
                                 choices=(("credit","credit"),
                                          ("debit","debit"))
                                          )
    def save(self,*args,**kwargs):
        if(self.transaction=="debit"):
            self.amt=self.amt*-1
        return super().save(*args,**kwargs)

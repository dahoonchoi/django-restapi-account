from django.db import models

class User(models.Model):
    useracct = models.CharField(max_length=128, null=False)
    userpass = models.CharField(max_length=128, null=False)
    useradrl = models.CharField(max_length=256, null=True)
    usercrdt = models.DateTimeField(auto_now=True)
    userupdt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "User"

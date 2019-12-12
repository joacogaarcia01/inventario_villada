from django.db import models

# Create your models here.


class Lab(models.Model):
    id_lab = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Type(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    id_type = models.AutoField(primary_key=True)

    def __str__(self):
        return '{}'.format(self.name)


class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    id_lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    entry_date = models.DateField(null=True, blank=True)
    id_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    dismissed = models.BooleanField(default=False)

    def __str__(self):
        return '{}, {}'.format(self.name, self.entry_date)
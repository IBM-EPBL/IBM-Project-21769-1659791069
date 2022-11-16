from django.db import models

# Create your models here.
# Creating the about models.

class Members(models.Model):

    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mem_email = models.EmailField(unique=True)
    mobile_no = models.IntegerField()
    field = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name, self.position, self.address, self.email, self.mobile_no, self.field)


class Office(models.Model):

    off_email = models.EmailField(unique=True)
    off_address = models.CharField(max_length=200)
    tel_no  = models.IntegerField()

    def __str__(self):
        return str(self.off_email, self.off_address, self.tel_no)

class AboutForm(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    callback_date = models.IntegerField(null=True)
    callback_time = models.IntegerField(null=True   )
    message = models.TextField(default=None)

    def __str__(self):
        return self.name, self.email , self.callback_date, self.callback_time, self.message



class quote(models.Model):

    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name, self.email, self.message






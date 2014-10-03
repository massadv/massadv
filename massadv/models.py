from django.db import models
from django import forms

class StUsers(models.Model):
    username = models.CharField(db_index=True, max_length=32, blank=False)
    password = models.CharField(max_length=32, blank=False)
    firstname = models.CharField(db_index=True, max_length=32, blank=False)
    lastname = models.CharField(db_index=True, max_length=32, blank=False)
    email = models.EmailField(max_length=128, blank=False)
    url = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=False)
    street1 = models.CharField(blank=False, max_length=80)
    street2 = models.CharField(blank=True, max_length=80)
    city = models.CharField(blank=False, max_length=32)
    state = models.CharField(blank=False, max_length=2)
    country = models.CharField(blank=False, max_length=80)
    zipcode = models.CharField(blank=False, max_length=10)

    def __unicode__(self):
        msg = u'Username: ' + self.username + "\n"
        #msg += 'Password: ' + self.password + "\n"
        msg += '---Name: ' + self.firstname + ' ' + self.lastname + '\n'
        msg += '---Email: ' + self.email + '\n'
        #msg += 'Url: ' + self.url + '\n'
        #msg += 'Phone: ' + self.phone + '\n'
        #msg += 'Street1: ' + self.street1 + '\n'
        #msg += 'Street2: ' + self.street2 + '\n'
        #msg += 'City: ' + self.city + '\n'
        #msg += 'State: ' + self.state + '\n'
        #msg += 'Country: ' + self.country + '\n'
        #msg += 'Country: ' + self.zipcode + '\n'        
        return msg
    
class StItems(models.Model):
    title = models.CharField(db_index=True, blank=False, max_length=128)
    consignor = models.ForeignKey(StUsers)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=False)
    state = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    days = models.IntegerField(default=0)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
        
    def __unicode__(self):
        msg = u'Title: ' + self.title + '\n'
        msg += '---Price: $' + self.price.__str__() + '\n'
        #msg += 'Description: ' + self.description + '\n'
        #msg += 'State: ' + self.state.__str__() + '\n'
        #msg += 'Featured: ' + self.featured.__str__() + '\n'
        #msg += 'Days: ' + self.days.__str__() + '\n'
        #msg += 'Startdate: ' + self.startdate.__str__() + '\n'
        #msg += 'Enddate: ' + self.enddate.__str__() + '\n'
        return msg

class StImages(models.Model):
    item = models.ForeignKey(StItems)
    image = models.ImageField(blank=False)
    
    def __unicode__(self):
        return 'Image: ' + self.image.__str__()
            
class StCategories(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __unicode__(self):
        return 'Category: ' + self.name

    class Meta: ordering = ['name']


class StCat(models.Model):
    category = models.ForeignKey(StCategories)
    item = models.ForeignKey(StItems)
    
    def __unicode__(self):
        return self.category.__str__() + " / " + self.item.__str__()

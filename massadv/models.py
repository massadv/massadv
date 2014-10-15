from django.db import models

class Users(models.Model):
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
    rating = models.IntegerField(default=0);
    
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
    
class Items(models.Model):
    user = models.ForeignKey(Users)
    title = models.CharField(db_index=True, blank=False, max_length=128)
    description = models.TextField(blank=False)
    startprice = models.IntegerField(default=0)
    endprice = models.IntegerField(default=0)
    currentprice = models.IntegerField(default=0)
    daysleft = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
        
    def __unicode__(self):
        msg = u'Title: ' + self.title + '\n'
        msg += '---StartPrice: $' + self.startprice.__str__() + '\n'
        msg += '---EndPrice: $' + self.endprice.__str__() + '\n'
        #msg += 'Description: ' + self.description + '\n'
        #msg += 'State: ' + self.state.__str__() + '\n'
        #msg += 'Featured: ' + self.featured.__str__() + '\n'
        #msg += 'Sold: ' + self.sold.__str__() + '\n'
        #msg += 'Expired: ' + self.expired.__str__() + '\n'
        #msg += 'Daysleft: ' + self.days.__str__() + '\n'
        #msg += 'Startdate: ' + self.startdate.__str__() + '\n'
        #msg += 'Enddate: ' + self.enddate.__str__() + '\n'
        return msg

class Claim(models.Model):
    user = models.ForeignKey(Users)
    item = models.ForeignKey(Items)
    price = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.user.__str__() + " / " + self.item.__str__()

class Images(models.Model):
    item = models.ForeignKey(Items)
    image = models.ImageField(blank=False)
    
    def __unicode__(self):
        return 'Image: ' + self.image.__str__()
            
class Categories(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __unicode__(self):
        return 'Category: ' + self.name

    class Meta: ordering = ['name']


class Cat(models.Model):
    category = models.ForeignKey(Categories)
    item = models.ForeignKey(Items)
    
    def __unicode__(self):
        return "Claim: "  + self.category.__str__() + " / " + self.item.__str__()

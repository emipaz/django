from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name
class Iso(models.Model):
    name = models.CharField(max_length = 4 )
    def __str__(self) :
        return self.name
class Region(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name
class State(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name
class Site(models.Model):
    name          = models.CharField(max_length = 128)
    year          = models.IntegerField( null   = True)
    description   = models.CharField(max_length = 1024)
    justification = models.CharField(max_length = 1024)
    longitude     = models.DecimalField(max_digits = 30, decimal_places = 15, null=True)
    latitude      = models.DecimalField(max_digits = 30, decimal_places = 15, null=True)
    area_hectares = models.DecimalField(max_digits = 30, decimal_places = 15, null=True)
    category      = models.ForeignKey(Category, on_delete = models.CASCADE,null=True)
    iso           = models.ForeignKey(Iso,     on_delete = models.CASCADE,null=True)
    region        = models.ForeignKey(Region,  on_delete = models.CASCADE,null=True)
    state         = models.ForeignKey(State,   on_delete = models.CASCADE,null=True)

    def __str__(self) :
        return self.name 


"""
class Membership(models.Model):
    site       = models.ForeignKey(Site,     on_delete = models.CASCADE)
    category   = models.ForeignKey(Category, on_delete = models.CASCADE)
    iso        = models.ForeignKey(Iso,      on_delete = models.CASCADE)
    region     = models.ForeignKey(Region,   on_delete = models.CASCADE)
    state      = models.ForeignKey(State,    on_delete = models.CASCADE)

    def __str__(self):
        st = "Categoria"+ str(self.category.id) + "Iso  " + str(self.iso.id) + "\n"
        st += "Region"+ str(self.region.id) + "State  " + str(self.state.id)
        return st
"""
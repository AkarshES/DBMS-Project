from django.db import models
from django.forms import ModelForm
# Create your models here.
class Customer(models.Model):
	customer_name = models.CharField(max_length = 50)
	customer_adderss = models.CharField(max_length = 200)
	register_date = models.DateField()
	email = models.EmailField()
	def __unicode__(self):
		return self.customer_name	

class Set(models.Model):
        set_Name = models.CharField(max_length = 50)
	def __unicode__(self):
		return self.set_Name
class Venue(models.Model):
        venue_Name = models.CharField(max_length = 50)
        venue_Address = models.CharField(max_length = 200)
        venue_Phone_list = models.CharField(max_length = 20)
        venue_Manager = models.CharField(max_length = 30,blank=True)
        stage_Heigth = models.FloatField(blank=True)
        stage_Length = models.FloatField(blank=True)
        stage_Depth = models.FloatField(blank=True)
	def __unicode__(self):
		return self.venue_Name

class MuhurthamOrder(models.Model):
        date = models.DateField()
        set_name = models.ForeignKey(Set,related_name='+')
        mantapa = models.BooleanField()
        entrance = models.BooleanField()
        gowri_Pooja_Stage_Decoration = models.BooleanField()
        bagina_Mara = models.BooleanField()
        vadhu_Welcome = models.BooleanField()
        kashi_Yatra = models.BooleanField()
        saptapadi = models.BooleanField()
	meals_Decoration = models.BooleanField()
	naming_Ceremony_for_Dolls = models.BooleanField()
	elephants = models.IntegerField()
	def __unicode__(self):
		return str(self.date)+' - '+str(self.set_name)

class Reception(models.Model):
	ENTRANCE_CHOICE = (('G','Ganesha'),('K','Krishna'),)
	date = models.DateField()
	set_name = models.ForeignKey(Set,related_name='+')
	stage_Decoration = models.BooleanField()
	entrance = models.CharField(max_length=7,choices = ENTRANCE_CHOICE)
	door_Decoration = models.BooleanField()
	carpet = models.BooleanField()
	pots = models.BooleanField()
	ramp = models.BooleanField()
	orchestra_Stage = models.BooleanField()
	lightings_for_Stage = models.BooleanField()
	garlands = models.IntegerField()

class HaldiFunction(models.Model):
	date = models.DateField()
	set_name = models.ForeignKey(Set,related_name='+')
	kalasa = models.BooleanField()
	gowri = models.BooleanField()
	chappara = models.BooleanField()
	door_Decoration = models.BooleanField()
	pooja_Room_Decoration = models.BooleanField()
	onake_Oralu = models.BooleanField()

class VaraPooja(models.Model):
	ENTRANCE_CHOICE = (('G','Ganesha'),('K','Krishna'),)
	date = models.DateField()
        set_name = models.ForeignKey(Set,related_name='+')
	vara_Pooja_Welcome = models.ForeignKey(Set,related_name='+')
	welcome_Bouquet = models.BooleanField()
	name_Board = models.CharField(max_length=7,choices=ENTRANCE_CHOICE)
	door_Decoration = models.BooleanField()
	welcome_Garland = models.IntegerField()
	vara_Pooja_Garlands = models.IntegerField()
	kanth_Samanu = models.BooleanField()
	kumbalakaye = models.BooleanField()
	belladachhu = models.IntegerField()

class MakeUp(models.Model):
	haldi_Fucntion = models.BooleanField()
	welcome = models.BooleanField()
	vara_Pooja = models.BooleanField()
	reception = models.BooleanField()
	muhurtham = models.BooleanField()
	matching_Flowers = models.BooleanField()

class Order(models.Model):
	customer_details = models.ForeignKey(Customer)
	muhurtham_Order = models.OneToOneField(MuhurthamOrder,blank=True,null=True)
	reception_Order = models.OneToOneField(Reception,blank=True,null=True)
	haldi_Order = models.OneToOneField(HaldiFunction,blank=True,null=True)
	vara_Pooja = models.OneToOneField(VaraPooja,blank=True,null=True)
	is_over = models.BooleanField()
	venue = models.ForeignKey(Venue)
	car_Decoration = models.BooleanField()
	make_Up = models.OneToOneField(MakeUp,blank=True,null=True)
	def __unicode__(self):
		return str(self.venue)
class OrderForm(ModelForm):
	class meta:
		model = Order

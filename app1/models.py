from django.db import models
from django.forms import ModelForm
# Create your models here.

ENTRANCE_CHOICE = (('G','Ganesha'),('K','Krishna'),('O','Others'),)

class Customer(models.Model):
	customer_name = models.CharField(max_length = 50)
	customer_address = models.CharField(max_length = 200)
	landline = models.CharField(max_length=20,blank = True,null=True)
	modile = models.CharField(max_length=20,blank=True,null=True)
	register_date = models.DateField()
	email = models.EmailField()
	notes = models.CharField(max_length = 50,blank=True,null=True)
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
        stage_Heigth = models.FloatField(blank=True,null=True)
        stage_Length = models.FloatField(blank=True,null=True)
        stage_Depth = models.FloatField(blank=True,null=True)
	notes = models.CharField(max_length = 50,blank=True,null=True)
	def __unicode__(self):
		return self.venue_Name

class MuhurthamOrder(models.Model):
	date = models.DateField()
	set_name = models.ForeignKey(Set,related_name='+')
	mantapa = models.BooleanField()
	mantapa_note = models.CharField(max_length = 50,blank=True,null=True)
	entrance = models.BooleanField()
	entrance_note = models.CharField(max_length = 50,blank=True,null=True)
	gowri_Pooja_Decoration = models.BooleanField()
	gowri_Pooja_note = models.CharField(max_length = 50,blank=True,null=True)
	bagina_Mara = models.BooleanField()
	bagina_Mara_note = models.CharField(max_length = 50,blank=True,null=True)
	vadhu_Welcome = models.BooleanField()
	vadhu_Welcome_note = models.CharField(max_length = 50,blank=True,null=True)
	kashi_Yatra = models.BooleanField()
	kashi_Yatra_note = models.CharField(max_length = 50,blank=True,null=True)
	saptapadi = models.BooleanField()
	saptapadi_note = models.CharField(max_length = 50,blank=True,null=True)
	meals_Decoration = models.BooleanField()
	meals_Decoration_note = models.CharField(max_length = 50,blank=True,null=True)
	naming_Ceremony_for_Dolls = models.BooleanField()
	naming_Ceremony_note = models.CharField(max_length = 50,blank=True,null=True)
	elephants = models.CharField(max_length=20,blank=True,null=True)
	order_Notes = models.CharField(max_length = 50,blank=True,null=True)
	def __unicode__(self):
		return str(self.date)+' - '+str(self.set_name)

class Reception(models.Model):
	date = models.DateField()
	set_name = models.ForeignKey(Set,related_name='+')
	stage_Decoration = models.BooleanField()
	entrance = models.CharField(max_length=2,choices = ENTRANCE_CHOICE)
	entrance_note = models.CharField(max_length = 50,blank=True,null=True)
	door_Decoration = models.BooleanField()
	door_Decoration_note = models.CharField(max_length = 50,blank=True,null=True)
	carpet = models.BooleanField()
	carpet_note = models.CharField(max_length = 50,blank=True,null=True)
	pots = models.BooleanField()
	pots_note = models.CharField(max_length = 50,blank=True,null=True)
	ramp = models.BooleanField()
	ramp_note = models.CharField(max_length = 50,blank=True,null=True)
	orchestra_Stage = models.BooleanField()
	orchestra_Stage_note = models.CharField(max_length = 50,blank=True,null=True)
	lightings_for_Stage = models.BooleanField()
	lightings_note = models.CharField(max_length = 50,blank=True,null=True)
	garlands = models.CharField(max_length=50,blank=True,null=True)
	order_Notes = models.CharField(max_length = 50,blank=True,null=True)
	def __unicode__(self):
		return str(self.date)+' - '+str(self.set_name)

HALDI_ADDRESS_CHOICE = (('HA','Home Address'),('O','Other'),)

class HaldiFunction(models.Model):
	date = models.DateField()
	set_name = models.ForeignKey(Set,related_name='+')
	address = models.CharField(max_length=2,choices = HALDI_ADDRESS_CHOICE)
	other_Address = models.CharField(max_length=75,blank=True,null=True)
	kalasa = models.BooleanField()
	gowri = models.BooleanField()
	chappara = models.BooleanField()
	door_Decoration = models.BooleanField()
	pooja_Room_Decoration = models.BooleanField()
	onake_Oralu = models.BooleanField()
        notes = models.CharField(max_length = 50,blank=True,null=True)
	def __unicode__(self):
                return str(self.date)+' - '+str(self.set_name)

class VaraPooja(models.Model):
	date = models.DateField()
        set_name = models.ForeignKey(Set,related_name='+')
	vara_Pooja_Welcome = models.ForeignKey(Set,related_name='+')
	welcome_Bouquet = models.BooleanField()
	door_Decoration = models.CharField(max_length=2,choices=ENTRANCE_CHOICE)
	name_Board = models.BooleanField()
	welcome_Garland = models.IntegerField()
	garlands = models.CharField(max_length=50,blank=True,null=True)
	kanth_Samanu = models.BooleanField()
	kumbalakaye = models.BooleanField()
	belladachhu = models.IntegerField()
	notes = models.CharField(max_length = 50,blank=True,null=True)

	def __unicode__(self):
                return str(self.date)+' - '+str(self.set_name)


class MakeUp(models.Model):
	haldi_Fucntion = models.BooleanField()
	welcome = models.BooleanField()
	vara_Pooja = models.BooleanField()
	reception = models.BooleanField()
	muhurtham = models.BooleanField()
	matching_Flowers = models.BooleanField()
	

class Order(models.Model):
	customer_details = models.ForeignKey(Customer)
	start_date = models.DateField(blank = True,null=True)
	muhurtham_Order = models.OneToOneField(MuhurthamOrder,blank=True,null=True)
	reception_Order = models.OneToOneField(Reception,blank=True,null=True)
	haldi_Order = models.OneToOneField(HaldiFunction,blank=True,null=True)
	vara_Pooja = models.OneToOneField(VaraPooja,blank=True,null=True)
	venue = models.ForeignKey(Venue)
	car_Decoration = models.BooleanField()
	make_Up = models.OneToOneField(MakeUp,blank=True,null=True)
	def __unicode__(self):
		return str(self.venue)
class OrderForm(ModelForm):
	class meta:
		model = Order

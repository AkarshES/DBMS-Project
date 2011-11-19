from django.contrib import admin
from djangoP1.app1.models import Customer,Order,OrderForm,Set,Venue,MuhurthamOrder,Reception,HaldiFunction,VaraPooja,MakeUp
from django.forms import TextInput, Textarea
from django.db import models

class OrderAdmin(admin.ModelAdmin):
	list_display = ('venue','muhurtham_Order')
	date_hierarchy = 'start_date'

class MuhurthamOrderAdmin(admin.ModelAdmin):
	fieldsets = ((None,{'fields':('date','set_name',('mantapa','mantapa_note'),('entrance','entrance_note'),('gowri_Pooja_Decoration','gowri_Pooja_note'),('bagina_Mara','bagina_Mara_note'),('vadhu_Welcome','vadhu_Welcome_note'),('kashi_Yatra','kashi_Yatra_note'),('saptapadi','saptapadi_note'),('meals_Decoration','meals_Decoration_note'),('naming_Ceremony_for_Dolls','naming_Ceremony_note'),'elephants','order_Notes')}),)
	formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }

class ReceptionAdmin(admin.ModelAdmin):
	fieldsets = ((None,{'fields':('date','set_name','stage_Decoration',('entrance','entrance_note'),('door_Decoration','door_Decoration_note'),('carpet','carpet_note'),('pots','pots_note'),('ramp','ramp_note'),('orchestra_Stage','orchestra_Stage_note'),('lightings_for_Stage','lightings_note'),'garlands','order_Notes')}),)
        formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
	radio_fields = {'entrance': admin.VERTICAL}
class HaldiFunctionAdmin(admin.ModelAdmin):
	fieldsets = ((None,{'fields':('date','set_name',('address','other_Address'),'kalasa','gowri','chappara','door_Decoration','pooja_Room_Decoration','onake_Oralu','notes')}),)
        formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
	radio_fields = {'address': admin.VERTICAL}

class VaraPoojaAdmin(admin.ModelAdmin):
        formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }



admin.site.register(Customer)
admin.site.register(Order,OrderAdmin)
admin.site.register(Set)
admin.site.register(Venue)
admin.site.register(MuhurthamOrder,MuhurthamOrderAdmin)
admin.site.register(Reception,ReceptionAdmin)
admin.site.register(HaldiFunction,HaldiFunctionAdmin)
admin.site.register(VaraPooja,VaraPoojaAdmin)
admin.site.register(MakeUp)

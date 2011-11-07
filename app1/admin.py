from django.contrib import admin
from djangoP1.app1.models import Customer,Order,OrderForm,Set,Venue,MuhurthamOrder,Reception,HaldiFunction,VaraPooja,MakeUp
from django.forms import TextInput, Textarea
from django.db import models

class OrderAdmin(admin.ModelAdmin):
	list_display = ('venue','muhurtham_Order')
	date_hierarchy = 'start_date'

class MuhurthamOrderAdmin(admin.ModelAdmin):
	formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

class ReceptionAdmin(admin.ModelAdmin):
        formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

class HaldiFunctionAdmin(admin.ModelAdmin):
        formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

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

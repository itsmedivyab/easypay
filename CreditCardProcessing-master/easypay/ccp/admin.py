from django.contrib import admin

# Register your models here.
#from .models import Question
from .models import Customer
from .models import historydata
admin.site.register(Customer)
admin.site.register(historydata)
#admin.site.register(Choice)
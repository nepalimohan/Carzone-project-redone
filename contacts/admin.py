from django.contrib import admin
from .models import Inquiry

# Register your models here.
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','car_title','city','created_date']
    list_display_links = ['id','first_name', 'last_name','email' ]
    search_fields = ['first_name', 'last_name','email' ,'car_title'] 
    list_per_page = 25
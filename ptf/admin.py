from django.contrib import admin

# Register your models here.
from .models import Contact,Service,Aboutm,Postcmnt
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Aboutm)
admin.site.register(Postcmnt)





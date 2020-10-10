from django.contrib import admin

# Register your models here.


from product.models import Brand,Mobile

admin.site.register(Brand)
admin.site.register(Mobile)
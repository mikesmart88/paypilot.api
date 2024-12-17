from django.contrib import admin
from .models import company, product, exchange, spot
# Register your models here.

admin.site.register(company)
admin.site.register(product)
admin.site.register(exchange)
admin.site.register(spot)
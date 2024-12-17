from django.db import models
import os, datetime, string, random
from django.utils import timezone
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse
from django.utils.text import slugify 
from django.utils.timezone import now
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from .function import s_remove, rand_string_generator

# Create your models here.

class company(models.Model):

    name = models.CharField('company name', null=False, blank=False, max_length=200)
    logo = models.ImageField('company logo', null=False)
    email = models.EmailField('company email', null=False, blank=False,)
    phone = models.BigIntegerField('company phone phone number write in the discription eg +123 09135762867', null=False, blank=False)
    is_edit = models.BooleanField('do not click to edit company', default=False)
    w_link = models.URLField(' company whatsapp link', null=False, blank=False)
    F_link = models.URLField(' company facebook link', null=False, blank=False)
    t_link = models.URLField(' company twitter link', null=False, blank=False)
    in_link = models.URLField(' company instargram link', null=False, blank=False)

    def __str__(self):
        return self.name
    

class product(models.Model):

    pro_name = models.CharField('product name', null=False, blank=False, max_length=500)
    price = models.IntegerField('products pricing', default=0)
    shot_des = models.CharField('short title discription', null=False, blank=False, max_length=200)
    prod_id = models.CharField('product id to get the particular product', blank=True, null=True, max_length=100)
    features1 = models.CharField('features1 in a strait line short features', blank=True, null=True, max_length=100)
    features2 = models.CharField('features2 in a strait line short features', blank=True, null=True, max_length=100)
    features3 = models.CharField('features3 in a strait line short features', blank=True, null=True, max_length=100)
    is_ver = models.BooleanField('do not click to verify products', default=False)

    def __str__(self):
        return self.pro_name
    
    def get_absolute_url(self):
        return reverse('paypilot:productprofile', kwargs= { 'pro_id':self.prod_id })
    
    def save(self, *args, **kwargs):

        if self.is_ver == False:
            self.prod_id = f'{s_remove(self.pro_name)}_{rand_string_generator(7)}'
            self.is_ver = True
        else:
            pass
        return super(product, self).save(*args, **kwargs)
    
class  spot(models.Model):
    
    name = models.CharField('spots name that will be purchased', null=False, blank=False, max_length=2000)
    price = models.IntegerField('spot priceing', default=0)
    
class exchange(models.Model):
    
    currency = models.CharField('surrency name thta are avalible for exchnage', null=False, blank=False, max_length=200)
    ex_price = models.IntegerField('price in usd exchnage', default=0)
    limits = models.CharField('exchange limits', null=True, blank=True, default='No limits', max_length=300)
    time_speep  = models.CharField('specify how long it will take to exchnage the coins', null=True, blank=True, max_length=100)
    

 


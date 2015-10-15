from django.db import models
import os
from django.conf import settings
# Create your models here.

class anime(models.Model):
     anime_title  = models.CharField(max_length=63, blank=True)
     def __unicode__(self):
         return self.anime_title

class sc_data(models.Model):
     ani_ti    = models.ForeignKey(anime)
     anime_num = models.IntegerField()
     img_data  = models.ImageField(verbose_name="image")
     created   = models.DateField(auto_now_add=True)

     def __unicode__(self):
        return self.img_data.name

     def save(self, *args, **kwargs):
        super(sc_data, self).save(*args, **kwargs)

     def admin_image_view( self):
         return "<img src='%s' style='max-width: 100px; max-height: 100px;'>" % ('/media/'+ str(self.img_data))
     admin_image_view.short_description = "image"
     admin_image_view.allow_tags = True




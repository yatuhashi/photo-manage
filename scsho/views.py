from django.shortcuts import render
from scsho.models import anime,sc_data

# Create your views here.
from selenium import webdriver

def rec_sc(request):
     URL = "http://animosa.alice-tech.net:63030/tv/3893.localized/mp4/MHD-3893-1-20151010-2230-16.MP4    "
     driver = webdriver.Firefox()
     driver.set_window_size(1280, 720) 
     driver.get(URL)
     for i in range(30):
        ani=sc_data(ani_ti=anime.objects.get(pk=1),anime_num=2)
        ani.img_data.save(str(i)+"screen.png",driver.get_screenshot_as_png() , save=True)
     driver.quit()
     return HttpResponse("end")





from django.urls import path
from recycling import views

urlpatterns = [
    path('', views.home, name="Recycles"),
    path('impact', views.impact, name="impact"),
    path('about', views.about, name="about"),
    path('media', views.media, name="media"),
    path('request', views.request, name="request"),
    path('dashboard', views.make_trash_request, name="dashboard"),
    path('faq', views.faq, name="faq"),
]

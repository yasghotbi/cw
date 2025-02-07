from django.urls import path
from .views import ContactUs


urlpatterns = [
    path('message/',ContactUs.as_view(), name='contactus'),

]
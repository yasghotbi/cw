from django.shortcuts import render

# Create your views here.



def contact_us(request):
    return render(request,'about_us.html')
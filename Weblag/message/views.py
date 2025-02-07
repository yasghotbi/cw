from django.shortcuts import render,redirect
from django.views import View
from .forms import  MessageForm
# Create your views here.



class ContactUs(View):
    def get(self, request, *args, **kwargs):
        form = MessageForm()
        return render(request, 'message.html', {'form': form})

    def post(self ,request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'message.html',{'form': form})


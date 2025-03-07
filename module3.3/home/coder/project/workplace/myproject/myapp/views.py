from django.shortcuts import render
from .forms import BookingForm  

def form_view(request):
    form = BookingForm()  
    return render(request, 'form_template.html', {'form': form}) 
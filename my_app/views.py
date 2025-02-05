

from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request,'contact.html')

def components(request):
    return render (request,'components.html')
def home(request):
    all_member = Contact.objects.all
    return render(request,'home.html',{'all':all_member})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            # return redirect('success_page')  # Redirect to a success page after submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
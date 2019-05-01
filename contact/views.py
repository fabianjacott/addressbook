from django.shortcuts import render, redirect
from .models import Contact


def index(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'contact/index.html', context)


def create_contact(request):
    if request.method == 'POST':
        if request.POST['firstname'] and request.POST['lastname'] and request.POST['number']:
            contact = Contact()
            contact.firstname = request.POST['firstname']
            contact.lastname = request.POST['lastname']
            contact.number = request.POST['number']
            contact.save()
            return redirect('contact:index')
        else:
            return render(request, 'contact/create.html')
    else:
        return render(request, 'contact/create.html')



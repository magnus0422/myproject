from django.shortcuts import render
from .models import FormData


def form_view(request):
    if request.method == 'POST':
        # Save the form data to the database
        FormData.objects.create(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number']
        )
        # Clear the form and show a success message
        return render(request, 'myapp/form.html', {'message': 'Data saved successfully!'})
    return render(request, 'myapp/form.html')

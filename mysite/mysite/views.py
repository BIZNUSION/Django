from django.shortcuts import render
from .forms import StudentForm
def registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstName']
            lastname = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            course = form.cleaned_data['course']
            year = form.cleaned_data['year']
            gender = form.cleaned_data['gender']
            dob = form.cleaned_data['dob']
            form.save()  
            return render(request, 'success.html', {'data': form.cleaned_data})  # Redirect to a success page
    else:
        form = StudentForm()
    
    return render(request, 'home.html', {'form': form})

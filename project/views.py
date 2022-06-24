from django.shortcuts import render,redirect
from .models import Company
from .forms import AddSiteForm

# Create your views here.
massive = []


def main_page(request):
    al_company = Company.objects.all()

    return render(request, 'main_page.html', {'user': request.user, 'company': al_company})


def add_site(request):
    if request.method == 'POST':
        form = AddSiteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('main')
    else:
        form = AddSiteForm()

    return render(request, 'add_site_page.html', {'form': form})

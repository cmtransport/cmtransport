from django.shortcuts import render, get_object_or_404
from .models import Package
from .forms import TrackingForm

def home(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            package = get_object_or_404(Package, tracking_id=tracking_id)
            return render(request, 'track.html', {'package': package})
    else:
        form = TrackingForm()
    return render(request, 'index.html', {'form': form})

def track(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            package = get_object_or_404(Package, tracking_id=tracking_id)
            return render(request, 'track.html', {'package': package})
    else:
        form = TrackingForm()
    return render(request, 'track.html', {'form': form})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request,'services.html')

def expeditedshipment(request):
    return render(request,'expeditedshipment.html')

def services_details(request):
    return render(request, 'services-details.html')

def AIRCHARTERSERVICES(request):
    return render(request, 'AIRCHARTERSERVICES.html')

def PMANAGEMENT(request):
    return render(request, '3PMANAGEMENT.html')

def agents(request):
    return render(request, 'agents.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')
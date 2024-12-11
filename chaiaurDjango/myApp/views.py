from django.shortcuts import render
from myApp.models import ChaiVariety, Store
from django.shortcuts import get_object_or_404
from myApp.forms import ChaiVarietyForm

# Create your views here.
def myAppIndex(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'myApp/myAppIndex.html', {"chais": chais})

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'myApp/chai_details.html', {"chai": chai})

def chai_store(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety_ = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varieties=chai_variety_)
    
    else:
        form = ChaiVarietyForm()
            
    return render(request, 'myApp/chai_store.html', {'stores': stores, 'form': form})

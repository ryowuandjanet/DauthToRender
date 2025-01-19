from django.shortcuts import render, redirect, get_object_or_404
from .models import Yfcase
from .forms import YfcaseForm

def yfcase_list(request):
    yfcases = Yfcase.objects.all()
    return render(request, 'yfcase/yfcase_list.html', {'yfcases': yfcases})

def yfcase_detail(request, id):
    yfcase = get_object_or_404(Yfcase, id=id)
    return render(request, 'yfcase/yfcase_detail.html', {'yfcase': yfcase})

def yfcase_create(request):
    if request.method == 'POST':
        form = YfcaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yfcase_list')
    else:
        form = YfcaseForm()
    return render(request, 'yfcase/yfcase_form.html', {'form': form})

def yfcase_update(request, id):
    yfcase = get_object_or_404(Yfcase, id=id)
    if request.method == 'POST':
        form = YfcaseForm(request.POST, instance=yfcase)
        if form.is_valid():
            form.save()
            return redirect('yfcase_list')
    else:
        form = YfcaseForm(instance=yfcase)
    return render(request, 'yfcase/yfcase_form.html', {'form': form})

def yfcase_delete(request, id):
    yfcase = get_object_or_404(Yfcase, id=id)
    if request.method == 'POST':
        yfcase.delete()
        return redirect('yfcase_list')
    return render(request, 'yfcase/yfcase_confirm_delete.html', {'yfcase': yfcase})

from django.shortcuts import render,redirect
from .models import Voter
from .forms import VoterForm


def voter_add(request):
    template_name = 'voterapp/votaradd.html'
    form = VoterForm()
    if request.method == 'POST':
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def show_details(request):
    template_name = 'voterapp/show.html'
    data = Voter.objects.all()
    print(data)
    context = {'Voter': data}
    return render(request, template_name, context)


def candidate_details(request, pk):
    template_name = 'voterapp/details.html'
    data = Voter.objects.get(pk=pk)
    context = {'voter': data}
    return render(request, template_name, context)

def update_Details(request,pk):
    template_name = 'voterapp/votaradd.html'
    obj = Voter.objects.get(pk=pk)
    form = VoterForm(instance=obj)
    if request.method == 'POST':
        form = VoterForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def delete_Details(request,pk):
    template_name = 'voterapp/delete.html'
    obj = Voter.objects.get(pk=pk)
    if request.method == 'GET':
        context = {'form': obj}
        return render(request, template_name, context)
    obj.delete()
    return redirect('show_url')
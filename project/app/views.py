from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required()
def otu_table(request):
    return render(request, 'app/otu_table.html')

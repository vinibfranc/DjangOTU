from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd

def index(request):
    return render(request, 'index.html')

#@login_required(redirect_field_name='after')
def otu_table(request):
    if request.user.is_authenticated:
        df = pd.read_csv("app/files/otu_table_tax_amostras_editada.tsv", delimiter='\t')
        print(df)
        return render(request, 'app/otu_table.html', {'columns': df.columns, 'rows': df.to_dict('records')})
    else:
        messages.add_message(request, messages.WARNING, 'Área restrita para uso dos colaboradores. Por favor, faça o login ou converse com o administrador do site.')
        messages.add_message(request, messages.WARNING, 'Depois, que você logar, acesse a URL: http://127.0.0.1:8000/otu_table/ para visualizar a OTU table!')
        return redirect('/admin/')

from django.shortcuts import render
#from .forms import ContatoForm
from core.models import Curso
from core.forms import ContactForm

# Create your views here.
def index(request):
    contexto={
        "usuario":"Ser Humano",
        #aluno,professor,sbruble
        "perfil":"aluno",
    }
    return render(request,"index.html",contexto)

def disciplina(request):
    return render(request,"disciplina.html")

def detalhe_curso(request):
    return render(request,"detalhe_curso.html")

def lista_cursos(request):
    contexto={
        "cursos":Curso.objects.all()
    }
    return render(request,"lista_cursos.html",contexto)

def noticias(request):
    return render(request,"noticias.html")

def contato(request):
    if request.POST:
        form = ContactForm(request.POST)
        #form.enviar_email()
    else:
        form = ContactForm(request.POST)
    contexto = {
        "form":form
    }
    return render(request,"contato.html",contexto)

def login(request):
    return render(request,"login.html")


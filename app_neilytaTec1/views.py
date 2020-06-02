from django.shortcuts import render, redirect
from app_neilytaTec1.models import Professores, Alunos
from app_neilytaTec1.models import Evento, Cursos 
from app_neilytaTec1.formsApp import ProfForm, AlunoForm, CursoForm


def home(request):

    dados_evento = {'title': 'Minicurso Django 2.2.1'}
    dados_evento['title_secao_ev'] = 'evento'
    dados_evento['evento'] = Evento.objects.all()

    return render(
        request, 
        'app_neilytaTec1/saada_home.html', 
        dados_evento
    )


def listagem(request):
    dados = {'info':'Listagem de professores, alunos, cursos, wm teste listagem com base'}
    return render(
        request, 
        'app_neilytaTec1/listagemteste.html',
        dados
    )
    

# CRUD -> CREATE | READ | UPDATE | DELETE

# -------------------------------------
# 1            CREATE
# -------------------------------------
def create(request, code):
    if code == 1:  # create professor
        dados = {}
        dados['acao'] = 'Cadastro de Professores'
        dados['info'] = 'Cadastro de um(a) novo(a) Prof(ra). '
        form = ProfForm(request.POST or None)
        dados['form'] = form

        if form.is_valid():
            form.save()
            return redirect('go2listarprof')

        return render(
            request, 
            'app_neilytaTec1/cadastro.html', 
            dados
        )

    if code == 2: # create aluno
        dados = {}
        dados['acao'] = 'Cadastro de Alunos'
        dados['info'] = 'Cadastro de um(a) novo(a) Aluno(a)'
        form = AlunoForm(request.POST or None)
        dados['form'] = form

        if form.is_valid():
            form.save()
            return redirect('go2listaralunos')

        return render(
            request, 
            'app_neilytaTec1/cadastro.html', 
            dados
        )

    if code == 3:  # create curso
        dados = {}
        dados['acao'] = 'Cadastro de Cursos'
        dados['info'] = 'Cadastro de um novo Curso '
        form = CursoForm(request.POST or None)
        dados['form'] = form

        if form.is_valid():
            form.save()
            return redirect('go2listarcursos')

        return render(
            request, 
            'app_neilytaTec1/cadastro.html', 
            dados
        )
    else:
        return redirect('url_listagem')

# -------------------------------------
# 2            READ
# -------------------------------------
def listarProf(request):
    dadosProf = {}
    dadosProf['info'] = 'Listagem de professores com  algumas de suas respectivas informações'
    dadosProf['professores'] = Professores.objects.all()
    return render(request, 
        'app_neilytaTec1/listarProf.html', 
        dadosProf
    )

def listarAlunos(request):
    dadosAlunos = {}
    dadosAlunos['info'] = 'Listagem de alunos com  algumas de suas respectivas informações'
    dadosAlunos['alunos'] = Alunos.objects.all()
    return render(
        request, 
        'app_neilytaTec1/listarAlunos.html', 
        dadosAlunos
    )

def listarCursos(request):
    dadosCursos = {}
    dadosCursos['cursos'] = Cursos.objects.all()
    return render(
        request, 
        'app_neilytaTec1/listarCuros.html', 
        dadosCursos
    )

# -------------------------------------
# 3            UPDATE
# -------------------------------------
def update(request, code, pk):
    if code == 1:  # update professor
        dados = {}
        dados['info'] = 'Atualização de dados do Prof. '
        profData = Professores.objects.get(id = pk)
        form = ProfForm(request.POST or None, instance=profData)

        if form.is_valid():
            form.save()
            return redirect('go2listarprof')

        dados['update_prof'] = profData
        dados['form'] = form
        return render(
            request, 
            'app_neilytaTec1/formUpdateProf.html', 
            dados
        )

    if code == 2: # update aluno
        dados = {}
        dados['info'] = 'Atualização de dados do(a) aluno(a) '
        alunoData = Alunos.objects.get(id = pk)
        dados['update_aluno'] = alunoData

        form = AlunoForm(request.POST or None, instance=alunoData)

        if form.is_valid():
            form.save()
            return redirect('go2listaralunos')

        dados['form'] = form
        return render(
            request, 
            'app_neilytaTec1/formUpdateAluno.html', 
            dados
        )

    if code == 3:  # update curso
        dados = {}
        dados['info'] = 'Atualização de dados do Curso '
        cursoData = Cursos.objects.get(id = pk)
        form = CursoForm(request.POST or None, instance=cursoData)

        if form.is_valid():
            form.save()
            return redirect('go2listarcursos')

        dados['update_curso'] = cursoData
        dados['form'] = form
        return render(
            request, 
            'app_neilytaTec1/formUpdateCurso.html', 
            dados
        )
    else:
        return redirect('url_listagem')


# -------------------------------------
# 4            DELETE
# -------------------------------------
def remove(request, code, pk):
    if code == 1:  # remove professor
        profData = Professores.objects.get(id = pk)
        profData.delete()
        return redirect('go2listarprof')

    if code == 2: # remove aluno
        alunoData = Alunos.objects.get(id = pk)
        alunoData.delete()
        return redirect('go2listaralunos')

    if code == 3:  # remove curso
        cursoData = Cursos.objects.get(id = pk)
        cursoData.delete()
        return redirect('go2listarcursos')
    else:
        return redirect('url_listagem')
    

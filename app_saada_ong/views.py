from django.shortcuts import render, redirect
from django.contrib import admin
from django.urls import path

from app_saada_ong.models import Professores
from app_saada_ong.models import Alunos
from app_saada_ong.models import Evento
from app_saada_ong.models import Cursos
from app_saada_ong.models import Projetos
from app_saada_ong.models import Noticias

from app_saada_ong.formsApp import ProfForm
from app_saada_ong.formsApp import AlunoForm
from app_saada_ong.formsApp import CursoForm
from app_saada_ong.formsApp import UserForm

from app_saada_ong.controllers.cae_helper import new_clean_string
from app_saada_ong.controllers.lib_register import LibRegister
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login

import hashlib



# TODO: SHOW SIGNAL  ALERT
# TODO: make logic to filter by active


'''
----------------------------------------------------------
                   CAE USER PROJECTS
----------------------------------------------------------
'''

def home(request):

    dados_evento = {'title': 'Home'}
    dados_evento['title_secao_ev'] = 'evento'
    dados_evento['evento'] = Evento.objects.all()
    dados_evento['projects'] = Projetos.objects.filter(ativo=True)

    return render(
        request,
        'app_saada_ong/saadaHome.html',
        dados_evento
    )


# @app.route('/login', methods=['GET', 'POST'])
# not used
def cae_login(request):

    print('\n\n\n\n ENTREI NO LOGIN \n\n\n')

    form = UserForm()
    # form = UserRegiserForm()

    if request.method != 'POST':
        dadosLogin = {'title': 'Login'}
        dadosLogin['myform'] = form

        return render(
            request,
            'app_saada_ong/loginWithoutForm.html',
            dadosLogin
        )

    if  request.method == 'POST':

        # clean_username = new_clean_string(form.username.data)
        clean_username = request.POST.get('usernameField')
        password = request.POST.get('pwdField')

        print('\n\n\n clean_username:  ', clean_username)
        print('\n\n\n password:  ', password)
        user = User.objects.get(username=clean_username)

        if not user:
            # flash(u'Invalid Login. Wrong username', 'danger')
            print('Invalid Login. Wrong username danger')
            return redirect('login')

        '''
        if not check_password(user.password, password):
            # flash(u'Invalid Login. Wrong password.', 'danger')
            # print('Invalid Login. Wrong password danger')
            print(u'Invalid Login. Wrong password danger')
            return redirect('login')

        if check_password(user.password, password):
        '''

        real_user = authenticate(
            request,
            username=clean_username,
            password=password
        )

        if real_user is not None:
            login(request, real_user)
            # flash(u'Logged in.', 'success')
            print('Logged in. --> success')
            # return redirect('admin')
            return redirect('url__real_login')
        else:
            print('Invalid Login. Wrong username informed')
            return redirect('login')


# not used
def cae_register_not_used(request):

    print('\n\n\n\n ENTREI NO REGISTER \n\n\n')

    form = UserForm()

    if not form.is_valid() or request.method != 'POST':
        dadosLogin = {'title': 'Register'}
        dadosLogin['myform'] = form
        # import pdb; pdb.set_trace()
        return render(
            request,
            'app_saada_ong/pre-register-cae.html',
            dadosLogin
        )


# working
def cae_register(request):
    print("\n\n\n\n ENTREI NO REGISTER 2....\n\n\n\n")

    form = UserForm()
    lib_r = LibRegister()


    userdata = {'title': 'Register'}
    userdata['myform'] = form

    if request.method != 'POST':

        return render(
            request,
            'app_saada_ong/pre-register-cae.html',
            userdata
        )


    if request.method == 'POST':

        exists_user = User.objects.all()

        # clean all come in register data
        clean_first_name = new_clean_string(request.POST.get('firstName'))
        clean_last_name = new_clean_string(request.POST.get('lastName'))
        clean_pwd = new_clean_string(request.POST.get('pwdField'))
        clean_confirm_pwd = new_clean_string(request.POST.get('pwdConfirmField'))
        clean_email = new_clean_string(request.POST.get('emailField'))

        custom_username = 'cae' + '.' + clean_first_name + clean_last_name
        # personal_username model: cae.idelfridesjorge

        for usr in exists_user[::-1]:
            if usr.username == custom_username:
                # flash("Username already exists", 'warning')
                print("Username already exists warning")
                return render(
                    request,
                    'app_saada_ong/pre-register-cae.html',
                    userdata
                )

            if usr.email == clean_email:
                # flash("User email already exists", 'warning')
                print("User email already exists warning")
                return render(
                    request,
                    'app_saada_ong/pre-register-cae.html',
                    userdata
                )

        if clean_pwd != clean_confirm_pwd or (len(clean_pwd) != 6):
            # flash('Passwords do not match', 'danger')
            print('Passwords do not match danger')
            return render(
                request,
                'app_saada_ong/pre-register-cae.html',
                userdata
            )


        new_user = User.objects.create_user(
            username=custom_username,
            password=clean_pwd,
            first_name=clean_first_name,
            last_name=clean_last_name,
            email=clean_email
        )
        new_user.save()

        last_user_id = new_user.id

        # flash('User created successfuly', 'success')

        connect_group = Group.objects.get(name='connectUserGroup')
        new_user.groups.add(connect_group)

        respect_pronoun = (request.POST.get('chamar')
            if request.POST.get('chamar') != 'nenhuma' else ''
        )

        data_to_send_email = {
            "id": last_user_id,
            "username": custom_username,
            "password": clean_pwd,
            "email": clean_email,
            "tratamento": respect_pronoun,
            "first_name": clean_first_name,
            "last_name": clean_first_name
        }

        lib_r.cae_send_email(data_to_send_email)
        # return redirect(url_for('login'))

        return redirect('url_home')


# @login_required
def listAllProjects(request):

    dadosProjeto = {'title': 'Projetos'}
    dadosProjeto['project'] = Projetos.objects.filter(ativo=True)
    # dadosProjeto['project'] = Projetos.objects.filter(nome_projeto)
    # nome_projeto = dados.name_projetos
    return render(
        request,
        'app_saada_ong/listarCuros.html',
        dadosProjeto
    )


def showProjeto(request, id_project):

    if not id_project:
        raise KeyError('WARNING: Param  "code_project" is Required \n INFORME the project id to retrieve\n\n')

    dadosProjeto = {'title': 'Projeto'}
    dadosProjeto['projects'] = Projetos.objects.all()
    dadosProjeto['chosen_id_project'] = id_project

    return render(
        request,
        'app_saada_ong/projetos.html',
        dadosProjeto
    )


def listAllNews(request):

    news_data = {'title': 'Noticias'}
    news_data['allnews'] = Noticias.objects.filter(ativa=True)
    news_data['projects'] = Projetos.objects.filter(ativo=True)

    '''
    dadosProjeto = {}
    dadosProjeto['projects'] = Projetos.objects.all()
    '''
    # import pdb; pdb.set_trace()

    return render(
        request,
        'app_saada_ong/allNews.html',
        news_data
    )


def showOneNews(request, id_news):
    if not id_news:
        raise KeyError('WARNING: Param  "id_news" is Required \n INFORME the NEWS id to retrieve\n\n')

    news_data = {'title': 'Noticias'}
    news_data['one_news'] = Noticias.objects.get(id=id_news)
    news_data['projects'] = Projetos.objects.filter(ativo=True)

    return render(
        request,
        'app_saada_ong/oneNews.html',
        news_data
    )








































# ================================= NEILITA TEC 1 =====================================

def listagem(request):
    dados = {'info':'Listagem de professores, alunos, cursos, wm teste listagem com base'}
    return render(
        request,
        'app_saada_ong/listagem.html',
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
            'app_saada_ong/cadastro.html',
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
            'app_saada_ong/cadastro.html',
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
            'app_saada_ong/cadastro.html',
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
        'app_saada_ong/listarProf.html',
        dadosProf
    )

def listarAlunos(request):
    dadosAlunos = {}
    dadosAlunos['info'] = 'Listagem de alunos com  algumas de suas respectivas informações'
    dadosAlunos['alunos'] = Alunos.objects.all()
    return render(
        request,
        'app_saada_ong/listarAlunos.html',
        dadosAlunos
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
            'app_saada_ong/formUpdateProf.html',
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
            'app_saada_ong/formUpdateAluno.html',
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
            'app_saada_ong/formUpdateCurso.html',
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

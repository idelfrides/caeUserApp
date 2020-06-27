from django.forms import ModelForm
from app_saada_ong.models import Professores, Alunos
from app_saada_ong.models import Cursos
from django.contrib.auth.models import User




class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'groups',
        ]


# ***************************************************

class ProfForm(ModelForm):
    class Meta:
        model = Professores
        fields = [
            'nome_Prof',
            'formacao',
            'titulo_Academico',
            'curso_Leciona',
            'ano_Inicio',
            'turmas',
            'membro_Organizacao'
        ]


class AlunoForm(ModelForm):
    class Meta:
        model = Alunos
        fields = [
            'nome_aluno',
            'ano',
            'curso',
            'genero',
            'idade',
            'eh_destaque'
        ]


class CursoForm(ModelForm):
    class Meta:
        model = Cursos
        fields = [
            'nome_Curso',
            'data_Inicio',
            'num_Alunos',
            'num_Prof',
            'alunos_Formados',
            'descricao'
        ]


'''
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
'''
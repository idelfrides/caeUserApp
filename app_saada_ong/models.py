from django.db import models
from django.contrib.auth.models import User

'''
GENDER_CHOICE = [
    ('O Q FICA NO SISTEMA', 'O Q É APRESENTADO NO ADMIN DJANGO'),
]

'''
GENDER_CHOICE = [
    ('MASCULINO', 'Masculino'),
    ('FEMININO', 'Feminino'),
]

PROF_TITLE_CHOICE = [
    ('BACHAREL', 'Bacharel'),
    ('ESPECIALISATA', 'Especialista'),
    ('MESTRE', 'Mestre'),
    ('PHD', 'PhD'),
]

COURSES_CHOICE = [
    ('TÉCNICO EM INFORMÁTICA', 'TÉCNICO EM INFORMÁTICA'),
    ('TÉCNICO EM AGROPECUÁRIA', 'TÉCNICO EM EM AGROPECUÁRIA'),
    ('TÉCNICO EM ELETROMECÂNICA', 'TÉCNICO EM ELETROMECÂNICA'),
    ('TÉCNICO EM FINANÇAS', 'TÉCNICO EM FINANÇAS'),
]


COUNTRY_CHOICE = [
    ('BRASIL', 'Brasil'),
    ('PORTUGAL', 'Portugal'),
    ('ESPANHA', 'Espanha'),
    ('FRANÇA', 'França'),
    ('CANADA', 'Canada'),
    ('HOLANDA', 'Holanda'),
    ('ALEMANHA', 'Alemanha'),
    ('USA', 'USA'),
    ('INGLATERRA', 'Inglaterra'),
    ('SUIÇA', 'Suiça'),
    ('BELGICA', 'Belgica'),
    ('IRLANDA DO NORTE', 'Irlanda do Norte'),
    ('AUSTRÁLIA', 'Austrália'),
    ('ARGENTINA', 'Argentina'),
    ('MÉXICO', 'México'),
    ('OUTRO', 'Outro [informar]'),
]

BR_STATES_CHOICE = [
    ('SÃO PAULO', 'São Paulo'),
    ('RIO DE JANEIRO', 'Rio de Janeiro'),
    ('MINAS GERAIS', 'Minas Gerais'),
    ('ESPÍRITO SANTO', 'Espírito Santo'),
    ('CEARÁ', 'Ceará'),
    ('BAHIA', 'Bahia'),
    ('SANTA CATARINA', 'Santa Catarina'),
    ('RIO GRANDE DO SUL', 'Rio Grande do Sul '),
    ('RIO GRANDE OD NORTE', 'Rio Grande do Norte'),
    ('ESPÍRITO SANTO', 'Paraná'),
    ('Mato Grosso', 'Mato Grosso'),
    ('OUTRO', 'OUTRO'),
]


STATES_CHOICE = [
    ('TÉCNICO EM INFORMÁTICA', 'TÉCNICO EM INFORMÁTICA'),
    ('TÉCNICO EM AGROPECUÁRIA', 'TÉCNICO EM EM AGROPECUÁRIA'),
    ('TÉCNICO EM ELETROMECÂNICA', 'TÉCNICO EM ELETROMECÂNICA'),
    ('TÉCNICO EM FINANÇAS', 'TÉCNICO EM FINANÇAS'),
]




''' -----------------------------------------------------------------
                            SAADA ONG
---------------------------------------------------------------------
'''


class ConnectPeople(models.Model):
    ''' connect people table/model '''

    # ONE-TO-ONE RELATIONSHIP
    usuario = models.OneToOneField(
        User,
        on_delete=models.PROTECT
    )

    # default=7
    nome_profissional = models.CharField(
        max_length=255
    )

    imagem_perfil = models.ImageField(upload_to='images/connectPeople/')

    frase_de_ordem = models.CharField(
        max_length=255,
        blank=True,
        default='Sua frase de guerra aqui'
    )

    cargo_atual = models.CharField(
        max_length=100
    )

    sua_empresa = models.CharField(
        max_length=200,
        blank=True,
        default='O nome da sua empresa *')

    site_da_sua_empresa = models.URLField(
        blank=True)

    pais_de_residencia = models.CharField(
        max_length=50,
        choices=COUNTRY_CHOICE
    )
    celular = models.CharField(
        blank=True,
        max_length=15,
        default='005588999965504'
    )

    br_estado = models.CharField(
        max_length=50,
        choices=BR_STATES_CHOICE
    )

    estado = models.CharField(
        max_length=25,
        default='O seu Estado/Província',
        help_text="<p>Se você marcou <strong>OUTRO</strong> no campo acima, digite aqui o seu Estado/Província !</p>",
        blank=True
    )

    pais_de_nacionalidade = models.CharField(
        max_length=70
    )

    data_do_nascimento = models.DateField()

    genero = models.CharField(max_length=9, choices=GENDER_CHOICE)

    formacao_academica = models.CharField(
        max_length=100
    )

    ocupacao = models.CharField(
        max_length=100,
        blank=True,
        default='Sua ocupação atual'
    )

    linguas = models.CharField(
        max_length=255
    )

    areas_de_interesse = models.TextField(
        blank=True,
        default='Seus interesses'
    )

    projetos = models.TextField(
        blank=True,
        default='Seus projetos...'
    )

    ativo = models.BooleanField(
        default=True,
        help_text="<p>Se você não quiser aparecer no site, DESMARQUE este campo!</p>"
    )

    peolple_atualizado = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    data_hora_criação = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )


    def __str__(self):
        return  self.nome_profissional

    class Meta:
        verbose_name_plural='Cadastro do Connect People'



class ConnectBusiness(models.Model):
    ''' Business model '''

    nome_projeto = models.CharField(max_length=225)

    # MANY-TO-ONE RELATIONSHIP
    dono_projeto = models.ForeignKey(
        ConnectPeople,
        on_delete = models.PROTECT
    )

    logotipo_projeto = models.ImageField(upload_to='images/connectBusiness/')

    slogan_projeto= models.CharField(max_length=255,
                                    blank=True,
                                    default='Slogan do projeto')


    descricao_resumida = models.TextField(
        max_length=180,
        help_text="<p><strong>AVISO: </strong> Esta é a descrição que irá aparecer na visualização de todos os business. 180 caractéres no máximo!</p>"
    )

    descricao = models.TextField(help_text="<p>Descreve aqui quais valores o seu business gera a outros business ou pessoas *</p>")

    link_do_site = models.URLField()

    link_linkedin = models.URLField(blank=True)

    link_facebook = models.URLField(blank=True)

    link_instagram = models.URLField(blank=True)

    ativo = models. BooleanField(
        default=True,
        help_text="<p>Se você não quiser que este projeto de Business seja visualizado no site, DESMARQUE este campo!</p>")


    atualizar = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    data_hora_criação = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return  self.nome_projeto

    class Meta:
        verbose_name_plural='Registro de Projetos de Business'




'''

class HashHolder(db.Model):
    """ Task model """

    __tablename__ = 'hash_register'

    id = db.Column(db.Integer, primary_key=True)
    _hash = db.Column(db.String)
    username = db.Column(db.String)

    def __init__(self, _hash, username):
        self._hash = _hash
        self.username = username

    def __repr__(self):
        return '<Owner %r>' % self.username

'''


class CarouselImages(models.Model):
    ''' Carousel images model '''

    imagem_carousel = models.ImageField(upload_to='images/')

    título_no_site = models.CharField(max_length=255, blank=True)

    sub_titulo_no_site= models.CharField(max_length=255, blank=True)

    nome_imagem = models.CharField(
        max_length=255,
        default='Nome da sua imagem aqui',
        help_text="<p><strong>AVISO: </strong> Copia o nome da sua imagem e cole-o aqui sem extensão!!!</p>"
    )

    ativo = models. BooleanField(
        default=True,
        help_text="<p><strong>AVISO: </strong> Se você não quiser que esta imagem apareça no banner, DESMARQUE este campo!</p>"
    )

    atualizada = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    data_hora_criação = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return  self.nome_imagem

    class Meta:
        verbose_name_plural='Imagens de destaque'


class Projetos(models.Model):
    ''' Projetos model '''

    nome_projeto = models.CharField(max_length=255, default='Nome do projeto *')

    logotipo_projeto = models.ImageField(upload_to='images/projects/')

    slogan_projeto= models.CharField(max_length=255,
                                    blank=True,
                                    default='Slogan do projeto')

    descricao = models.TextField(default='Descrição do projeto entra aqui * ')

    ativo = models. BooleanField(
        default=True,
        help_text="<p>Se você não quiser que este projeto seja visualizado no site, DESMARQUE este campo!</p>")

    atualizar = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    data_hora_criação = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return  self.nome_projeto

    class Meta:
        verbose_name_plural='Projetos'


class Noticias(models.Model):
    ''' Noticias model '''

    título_notícia = models.CharField(max_length=255,
                                    default='Título da notícia *')

    image_notícia = models.ImageField(upload_to='images/news/')

    sub_titulo_noticia= models.CharField(
        max_length=255,
        blank=True,
        default='Subtítulo da notícia'
    )

    noticia = models.TextField(default='Escreva a sua notícia aqui *')

    ativa = models. BooleanField(
        default=True,
        help_text="<p>Se você não quiser que esta notícia apareça no site, DESMARQUE este campo!</p>"
    )

    atualizada = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    data_hora_criação = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return  self.título_notícia

    class Meta:
        verbose_name_plural='Noticias'



class QuemSomos(models.Model):
    ''' Quem somos model '''

    headline = models.CharField(max_length=255, default='Título *')

    image = models.ImageField(upload_to='images/')

    # sub_titulo_noticia= models.CharField(max_length=255, blank=True, default='Subtítulo da notícia')

    texto_correspondente = models.TextField(default='Escreva o seu texto aqui *')

    ativo = models.BooleanField(
        default=True,
        help_text="<p>Se você não quiser que este item apareça no site, DESMARQUE este campo!</p>"
    )

    atualizar = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    data_hora_criação = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return  self.headline

    class Meta:
        verbose_name_plural='Quem Somos'



# ------------------------------------------------------------------------



class Evento(models.Model):
    nome_Evento = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    descricao = models.TextField()

    def __str__(self):
        return  self.nome_Evento

    class Meta:
        verbose_name_plural='Evento'


class Cursos(models.Model):
    nome_Curso = models.CharField(
        max_length=30,
        choices=COURSES_CHOICE
    )
    data_Inicio = models.DateField()
    num_Alunos = models.IntegerField()
    num_Prof = models.IntegerField()
    alunos_Formados = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return '%s' % (self.nome_Curso)


    class Meta:
        verbose_name_plural = 'Cursos'


class Professores(models.Model):
    nome_Prof = models.CharField(max_length=100)
    formacao = models.CharField(
        max_length=100,
        default='Eng. Computação'
    )
    titulo_Academico = models.CharField(
        max_length=30,
        choices=PROF_TITLE_CHOICE
    )
    curso_Leciona = models.ForeignKey(
        Cursos,
        on_delete=models.CASCADE
    )
    ano_Inicio = models.CharField(max_length=4)
    turmas = models.IntegerField()
    membro_Organizacao = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_Prof

    class Meta:
        verbose_name_plural = 'Professores'


class Alunos(models.Model):
    nome_aluno = models.CharField(max_length=100)
    ano = models.IntegerField(default=3)
    curso = models.ForeignKey(
        Cursos,
        on_delete=models.CASCADE
    )
    genero = models.CharField(
        max_length=30,
        choices=GENDER_CHOICE,
    )
    idade = models.IntegerField()
    eh_destaque = models.BooleanField()

    def __str__(self):
        return self.nome_aluno

    class Meta:
        verbose_name_plural = 'Alunos'


# TODO: restart models pk/id sequence
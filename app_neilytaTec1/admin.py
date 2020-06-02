from django.contrib import admin
from .models import Evento
from .models import Professores
from .models import Alunos
from .models import CarouselImages
from .models import Cursos
from .models import CarouselImages
from .models import Noticias
from .models import Projetos
from .models import QuemSomos



''' ------------------------------- --------------------------------
                MODEL ADMIN CUSTOMIZATION
-----------------------------------------------------------------'''

class CarouselImagesModelAdmin(admin.ModelAdmin):
    list_display = ['nome_imagem', "atualizada", 'data_hora_criação', 'ativo']
    list_display_links = ['atualizada']
    list_filter = ['nome_imagem', "atualizada", 'ativo']
    # search_fields = ['nome_imagem', 'atualizada', 'ativo']
    list_editable = ['nome_imagem']

    class Meta:
        model = CarouselImages


class NoticiasModelAdmin(admin.ModelAdmin):
    list_display = ['título_notícia', "atualizada", 'data_hora_criação', 'ativa']
    list_display_links = ['atualizada']
    list_filter = ['título_notícia', "atualizada", 'ativa']
    list_editable = ['título_notícia']

    class Meta:
        model = Noticias


class ProjetosModelAdmin(admin.ModelAdmin):
    list_display = ['nome_projeto', "atualizar", 'data_hora_criação', 'ativo']
    list_display_links = ['atualizar']
    list_filter = ['nome_projeto', "atualizar", 'ativo']
    list_editable = ['nome_projeto']

    class Meta:
        model = Projetos


class  QuemSomosModelAdmin(admin.ModelAdmin):
    list_display = ['headline', "atualizar", 'data_hora_criação', 'ativo']
    list_display_links = ['atualizar']
    list_filter = ['headline', "atualizar", 'ativo']
    list_editable = ['headline']

    class Meta:
        model = QuemSomos



''' ------------------------------- --------------------------------
                MODELS AND ADMINMODELS REGISTRATION
-----------------------------------------------------------------'''

admin.site.register(
    CarouselImages,
    CarouselImagesModelAdmin
)


admin.site.register(
    Projetos,
    ProjetosModelAdmin
)


admin.site.register(
    Noticias,
    NoticiasModelAdmin
)


admin.site.register(
    QuemSomos,
    QuemSomosModelAdmin
)



'''
admin.site.register(Professores)
admin.site.register(Alunos)
admin.site.register(Cursos)
admin.site.register(Evento)

'''

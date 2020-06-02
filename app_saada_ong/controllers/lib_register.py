#!/src/bin/python
# -*- coding: utf-8 -*-

""" Manager module to helper building this app """


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from neilytaTec1 import settings
import hashlib

# from app.static.js import custom_functions


class LibRegister(object):
    """Library to help user registration"""

    def cae_send_email(self, data_to_send_email=None):
        """ send an email to user in registration step """


        string2hash = data_to_send_email['username'] + data_to_send_email['email']
        string2hash += data_to_send_email['last_name']

        check_key = hashlib.sha224(string2hash).hexdigest()
        check_key = str(check_key)  # TODO: find the best way to do this

        print(check_key)

        endpoint = 'login2complete_register'
        link2finish_register = 'https://connectafricaeducation.com/{endpoint}?key={check_key}'.format(endpoint, check_key)

        content_msg = '''

            Seja bem-vindo(a) a CONNECT AFRICA EDUCATION.
            Estamos felizes por estar a juntar-se a nós nessa jornada de
            crescimento pessoal e financeiro.
            Asseguramos que esta é a melhor decisão que você tomou para
            sua vida.

            Confira os seus dados de acesso e clique no link indicado abaixo
            para completar o seu cadastro.


            INFORMAÇÕES DE ACESSO:

            - Usuário (Username): {username}
            - Senha (Password): {password}


            Complete o seu cadastro <a href="{link}" target="_blank"><buttom>Neste link</buttom></a>

            Muito obrigado...
            A gente lhe espera doutro lado.
            Grande abraço!

            ------------------------------
            Equipe CONNECT AFRICA EDUCATION
            <Unindo cérebros pra gerar riqueza>


            PS.: Os dados de acesso informados NÃO irão funcionar se não acessar pelo link acima.


        '''.format(
                username=data_to_send_email['username'],
                password=data_to_send_email['password'],
                link=link2finish_register
            )

        subject_help = data_to_send_email['tratamento'] + ' ' + data_to_send_email['first_name']
        pronoun_first_name = subject_help.strip()
        subject = 'Prezado(a) \n' + pronoun_first_name + ' ' + data_to_send_email['last_name']
        name_to_view = 'Prezado(a) \n' + pronoun_first_name + ' ' + data_to_send_email['last_name']
        '''
        user_message = Message(
            recipients=data_to_send_email['email'],
            body=content_msg,
            subject=subject
        )

        # mail.send_email(user_message)

        mail.send(user_message)

        # make redirect with JS
        # custom_functions.go2compete_register()
        # go2compete_register(data_to_send_email['username'])  passar username
        '''

        author_email =  settings.EMAIL_HOST_USER

        to_list = [data_to_send_email['email'], settings.EMAIL_HOST_USER]

        send_mail(subject, content_msg,
                author_email, to_list,
                fail_silently=True)

        print("""

            ENVIEI EMAIL PRA VC...

        """)


        #TODO: USE RENDER STEAD REDIRECT . otherwise ok

        return redirect('register_instructions')

        '''
        new_user_data = {'name': name_to_view}
        return render(
            #  request,
            'instruction_page.html',
            new_user_data
        )
        '''





'''

    subject = 'Teste | envio email python'
    message = 'Olá, este é um teste de django enviando email.'
    author_email =  settings.EMAIL_HOST_USER
    to_email = LeadsEmail.objects.last()
    time.sleep(3)
    print('\n\n Ultimo email: {}'
        .format(to_email)
    )
    to_list = [to_email, settings.EMAIL_HOST_USER]

    send_mail(
        subject,
        message,
        author_email,
        to_list,
        fail_silently=True
    )

    print("""

         ENVIEI EMAIL PRA VC

        """)

    return redirect('url_home')
'''

'''
    MAIL_SERVER=‘localhost’
    MAIL_PORT=25
    MAIL_USE_TLS=True
    MAIL_USE_SSL : default False
    MAIL_DEBUG : default app.debug
    MAIL_USERNAME='connectafricaeducation@gmail.com'
    MAIL_PASSWORD='1989connect1990'
    MAIL_DEFAULT_SENDER='connectafricaeducation@gmail.com'
    MAIL_MAX_EMAILS=None
    MAIL_SUPPRESS_SEND : default app.testing
    MAIL_ASCII_ATTACHMENTS : default False

    -------------------------------------

    MAIL_SERVER : default ‘localhost’
    MAIL_PORT : default 25
    MAIL_USE_TLS : default False
    MAIL_USE_SSL : default False
    MAIL_DEBUG : default app.debug
    MAIL_USERNAME : default None
    MAIL_PASSWORD : default None
    MAIL_DEFAULT_SENDER : default None
    MAIL_MAX_EMAILS : default None
    MAIL_SUPPRESS_SEND : default app.testing
    MAIL_ASCII_ATTACHMENTS : default False

    # MAIL_DEFAULT_SENDER='connectafricaeducation@gmail.com'

    # https://pythonhosted.org/Flask-Mail/

'''

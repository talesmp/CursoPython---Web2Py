# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def aluno():
    form = SQLFORM(Aluno)
    if form.process().accepted:
        session.flash = 'Novo Aluno Cadastrado: %s' %form.vars.nome
        redirect(URL('aluno'))
    elif form.errors:
        response.flash = 'Erros Encontrados'
    else:
        if not response.flash:
            response.flash = 'Preencha o Formulário'
    return dict(form=form)

def professor():
    form = SQLFORM(Professor)
    if form.process().accepted:
        session.flash = 'Novo Professor Cadastrado: %s' %form.vars.nome
        redirect(URL('professor'))
    elif form.errors:
        response.flash = 'Erros Encontrados'
    else:
        if not response.flash:
            response.flash = 'Preencha o Formulário'
    return dict(form=form)

def empresa():
    form = SQLFORM(Empresa)
    if form.process().accepted:
        session.flash = 'Nova Empresa Cadastrada: %s' %form.vars.nome
        redirect(URL('empresa'))
    elif form.errors:
        response.flash = 'Erros Encontrados'
    else:
        if not response.flash:
            response.flash = 'Preencha o Formulário'
    return dict(form=form)

def estagio():
    form = SQLFORM(Estagio)
    if form.process().accepted:
        session.flash = 'Nova Relação de Estágio Cadastrada: %s' %form.vars.nome
        redirect(URL('estagio'))
    elif form.errors:
        response.flash = 'Erros Encontrados'
    else:
        if not response.flash:
            response.flash = 'Preencha o Formulário'
    return dict(form=form)




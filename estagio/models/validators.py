# -*- coding: utf-8 -*-
# Tales

## Validadores de Alunos
Aluno.nome.requires = IS_NOT_EMPTY()
Aluno.matricula.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'aluno.matricula')]
Aluno.curso.requires = IS_IN_SET(['Administração', 'Engenharia de Produção', 'Sistemas de Informação', 'Licenciatura em Matemática'])
Aluno.email.requires = IS_EMAIL()
Aluno.periodo.requires = IS_NOT_EMPTY()

## Validadores de Professor
Professor.nome.requires = IS_NOT_EMPTY()
Professor.cpf.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'professor.cpf')]
Professor.curso.requires = IS_IN_SET(['Administração', 'Engenharia de Produção', 'Sistemas de Informação', 'Licenciatura em Matemática'])
Professor.email.requires = IS_EMAIL()

## Validadores de Empresa
Empresa.nome.requires = IS_NOT_EMPTY()
Empresa.razao.requires = IS_NOT_EMPTY()
Empresa.cnpj.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'empresa.cnpj')]
Empresa.email.requires = IS_EMAIL()

##Validadores de Estágio

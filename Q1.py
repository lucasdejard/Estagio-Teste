#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
arqWrite = open('funcionarios.json', 'ab',)
arqRead = open('funcionarios.json', 'r', encoding="utf-8")
dictlogs = str(arqRead.read())
dados_json = json.loads(dictlogs)

Gmin = [float(dados_json['funcionarios'][0]['salario'])]
min_nome = [0]
Gminlen = 0
Gmax = [0]
max_nome = [0]
Gmaxlen = 0
Gavg = 0
lines = 0


while lines < len(dados_json['funcionarios']):

    Gavg = Gavg + float(dados_json['funcionarios'][lines]['salario'])
    if float(dados_json['funcionarios'][lines]['salario']) >= int(Gmax[Gmaxlen]):

        if float(dados_json['funcionarios'][lines]['salario']) != int(Gmax[Gmaxlen-1]):
            Gmax = []
            max_nome = []
            max_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                            dados_json['funcionarios'][lines]['sobrenome'])
            Gmax.append(dados_json['funcionarios'][lines]['salario'])
        else:
            Gmax.append(dados_json['funcionarios'][lines]['salario'])
            max_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                            dados_json['funcionarios'][lines]['sobrenome'])

#calculo minimo
    if float(dados_json['funcionarios'][lines]['salario']) <= int(Gmin[Gminlen]):

        if float(dados_json['funcionarios'][lines]['salario']) != int(Gmin[Gminlen-1]):
            Gmin = []
            min_nome = []
            min_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                            dados_json['funcionarios'][lines]['sobrenome'])
            Gmin.append(dados_json['funcionarios'][lines]['salario'])
        else:
            Gmin.append(dados_json['funcionarios'][lines]['salario'])
            min_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                            dados_json['funcionarios'][lines]['sobrenome'])
    lines = lines + 1
print("global_avg|" + "{:.2f}".format(Gavg/lines))
lines = 0
while lines < len(max_nome):
    print("global max|" + str(max_nome[lines]) + "|" + str("{:.2f}".format(Gmax[0])))
    lines = lines+1

lines = 0
while lines < len(min_nome):
    print("global min|" + str(min_nome[lines]) + "|" + str("{:.2f}".format(Gmin[0])))
    lines = lines+1

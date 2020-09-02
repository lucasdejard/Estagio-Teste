#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
arqWrite = open('funcionarios.json', 'ab',)
arqRead = open('funcionarios.json', 'r', encoding="utf-8")
dictlogs = str(arqRead.read())
dados_json = json.loads(dictlogs)

sobren = []
sobrerep = []
idrep = []
lines = 0
finalNome = 'h'
finalSal = 'k'
finalsbrnom = 0
verfunc = 0

lastnome = []
lastsbrnom = []
lastSal = []

while lines < len(dados_json['funcionarios']):
    sobren.append(dados_json['funcionarios'][lines]['sobrenome'])
    lines = lines + 1
lines = 0
while lines < len(dados_json['funcionarios']):
    if sobren.count(sobren[lines]) > 1:
        idrep.append(dados_json['funcionarios'][lines]['id'])
        sobrerep.append(dados_json['funcionarios'][lines]['sobrenome'])
    lines = lines + 1

lines = 0
while lines < len(sobrerep):
    if dados_json['funcionarios'][verfunc]['sobrenome'] == sobrerep[lines]:
        if dados_json['funcionarios'][verfunc]['salario'] >= dados_json['funcionarios'][idrep[lines]]['salario']:
            if dados_json['funcionarios'][verfunc]['id'] != [idrep[lines]] and dados_json['funcionarios'][verfunc]['salario'] != dados_json['funcionarios'][idrep[lines]]['salario']:
                while lastsbrnom.count(sobrerep[lines]) > 0:
                    lastSal.remove(dados_json['funcionarios'][lines]['salario'])
                    lastnome.remove(dados_json['funcionarios'][lines]['nome'])
                    lastsbrnom.remove(sobrerep[lines])
                lastSal.append(dados_json['funcionarios'][verfunc]['salario'])
                lastnome.append(dados_json['funcionarios'][verfunc]['nome'])
                lastsbrnom.append(dados_json['funcionarios'][verfunc]['sobrenome'])
            if dados_json['funcionarios'][verfunc]['id'] != [idrep[lines]] and dados_json['funcionarios'][verfunc]['salario'] == dados_json['funcionarios'][idrep[lines]]['salario']:
                lastSal.append(dados_json['funcionarios'][idrep[lines]]['salario'])
                lastnome.append(dados_json['funcionarios'][idrep[lines]]['nome'])
                lastsbrnom.append(dados_json['funcionarios'][idrep[lines]]['sobrenome'])
            while sobrerep.count(sobrerep[lines]) > 1:
                idrep.remove(idrep[lines])
                sobrerep.remove(sobrerep[lines])

        finalSal = dados_json['funcionarios'][verfunc]['salario']
        finalNome = dados_json['funcionarios'][verfunc]['nome']
        finalsbrnom = dados_json['funcionarios'][verfunc]['sobrenome']
    verfunc = verfunc + 1
    if verfunc > len(dados_json['funcionarios'])-1:
        lines = lines + 1
        verfunc = 0

print(sobrerep)
print(idrep)
SDmax = [0]
SDmax_nome = [0]
SDmaxlen = 0
print(lastSal,lastnome,lastsbrnom)
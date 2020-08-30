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
while lines < len(dados_json['funcionarios']):
    sobren.append(dados_json['funcionarios'][lines]['sobrenome'])
    lines = lines + 1
lines = 0
while lines < len(dados_json['funcionarios']):
    if sobren.count(sobren[lines]) > 1:
        idrep.append(dados_json['funcionarios'][lines]['id'])
        sobrerep.append(dados_json['funcionarios'][lines]['sobrenome'])
    lines = lines + 1

while lines < len(dados_json['funcionarios']):
    if:
        
    lines = lines + 1

print(sobrerep)
print(idrep)
SDmax = [0]
SDmax_nome = [0]
SDmaxlen = 0
print(sobren)

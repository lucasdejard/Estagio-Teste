#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
arqWrite = open('funcionarios.json', 'ab',)
arqRead = open('funcionarios.json', 'r', encoding="utf-8")
dictlogs = str(arqRead.read())
dados_json = json.loads(dictlogs)
lines = 0

SDnum = 0
SMnum = 0
UDnum = 0

while lines < len(dados_json['funcionarios']):
    if dados_json['funcionarios'][lines]['area'] == "SD":
        SDnum = SDnum + 1
    elif dados_json['funcionarios'][lines]['area'] == "SM":
        SMnum = SMnum + 1
    elif dados_json['funcionarios'][lines]['area'] == "UD":
        UDnum = UDnum + 1
    lines = lines + 1

if SDnum >= SMnum and SDnum >= UDnum:
    print('most_employees|Desenvolvimento de Software|' + str(SDnum))
    if SDnum == SMnum:
        print('most_employees|Gerenciamento de Software|' + str(SMnum))
    if SDnum == UDnum:
        print('most_employees|Designer de UI/UX|' + str(UDnum))
elif SMnum >= UDnum and SMnum >= SDnum:
    print('most_employees|Gerenciamento de Software|' + str(SMnum))
    if UDnum == SMnum:
        print('most_employees|Designer de UI/UX|' + str(UDnum))
elif UDnum >= SDnum and UDnum >= SMnum:
    print('most_employees|Designer de UI/UX|' + str(UDnum))

if SDnum <= SMnum and SDnum <= UDnum:
    print('least_employees|Desenvolvimento de Software|' + str(SDnum))
    if SDnum == SMnum:
        print('least_employees|Gerenciamento de Software|' + str(SMnum))
    if SDnum == UDnum:
        print('least_employees|Designer de UI/UX|' + str(UDnum))
elif SMnum <= UDnum and SMnum <= SDnum:
    print('least_employees|Gerenciamento de Software|' + str(SMnum))
    if UDnum == SMnum:
        print('least_employees|Designer de UI/UX|' + str(UDnum))
elif UDnum <= SDnum and UDnum <= SMnum:
    print('least_employees|Designer de UI/UX|' + str(UDnum))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
arqWrite = open('funcionarios.json', 'ab',)
arqRead = open('funcionarios.json', 'r', encoding="utf-8")
dictlogs = str(arqRead.read())
dados_json = json.loads(dictlogs)

lines = 0

SDmin = [0]
SDmin_nome = []
SDminlen = 0
SDmax = [0]
SDmax_nome = [0]
SDmaxlen = 0
SDavg = 0
linessd = 0

SMmin = [0]
SMmin_nome = []
SMminlen = 0
SMmax = [0]
SMmax_nome = [0]
SMmaxlen = 0
SMavg = 0
linessm = 0

UDmin = [0]
UDmin_nome = [0]
UDminlen = 0
UDmax = [0]
UDmax_nome = [0]
UDmaxlen = 0
UDavg = 0
linesud = 0

# calculo SD
while lines < len(dados_json['funcionarios']):
    if dados_json['funcionarios'][lines]['area'] == "SD":

        linessd = linessd + 1
        SDavg = SDavg + float(dados_json['funcionarios'][lines]['salario'])
        if float(dados_json['funcionarios'][lines]['salario']) >= int(SDmax[SDmaxlen]):

            if float(dados_json['funcionarios'][lines]['salario']) != int(SDmax[0]):
                SDmax = []
                SDmax_nome = []
                SDmax_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])
                SDmax.append(dados_json['funcionarios'][lines]['salario'])
            else:
                SDmax.append(dados_json['funcionarios'][lines]['salario'])
                SDmax_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])

    # calculo minimo

    if dados_json['funcionarios'][lines]['area'] == "SD":
        if float(dados_json['funcionarios'][lines]['salario']) <= int(SDmin[SDminlen]) or SDmin[0] == 0:

            if float(dados_json['funcionarios'][lines]['salario']) != int(SDmin[0]):
                SDmin = []
                SDmin_nome = []
                SDmin_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])
                SDmin.append(dados_json['funcionarios'][lines]['salario'])
            else:
                SDmin.append(dados_json['funcionarios'][lines]['salario'])
                SDmin_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])

# calculo SM

    if dados_json['funcionarios'][lines]['area'] == "SM":
        linessm = linessm + 1
        SMavg = SMavg + float(dados_json['funcionarios'][lines]['salario'])
        if float(dados_json['funcionarios'][lines]['salario']) >= int(SMmax[SMmaxlen]):

            if float(dados_json['funcionarios'][lines]['salario']) != int(SMmax[0]):
                SMmax = []
                SMmax_nome = []
                SMmax_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])
                SMmax.append(dados_json['funcionarios'][lines]['salario'])
            else:
                SMmax.append(dados_json['funcionarios'][lines]['salario'])
                SMmax_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])

    # calculo minimo

    if dados_json['funcionarios'][lines]['area'] == "SM":
        if float(dados_json['funcionarios'][lines]['salario']) <= int(SMmin[SMminlen]) or SMmin[0] == 0:

            if float(dados_json['funcionarios'][lines]['salario']) != int(SMmin[0]):
                SMmin = []
                SMmin_nome = []
                SMmin_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])
                SMmin.append(dados_json['funcionarios'][lines]['salario'])
            else:
                SMmin.append(dados_json['funcionarios'][lines]['salario'])
                SMmin_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])

# calculo SD
    if dados_json['funcionarios'][lines]['area'] == "UD":
        linesud = linesud + 1
        UDavg = UDavg + float(dados_json['funcionarios'][lines]['salario'])
        if float(dados_json['funcionarios'][lines]['salario']) >= int(UDmax[UDmaxlen]):

            if float(dados_json['funcionarios'][lines]['salario']) != int(UDmax[0]):
                UDmax = []
                UDmax_nome = []
                UDmax_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])
                UDmax.append(dados_json['funcionarios'][lines]['salario'])
            else:
                UDmax.append(dados_json['funcionarios'][lines]['salario'])
                UDmax_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])

    # calculo minimo

    if dados_json['funcionarios'][lines]['area'] == "UD":
        if UDmin[0] == 0 or float(dados_json['funcionarios'][lines]['salario']) <= int(UDmin[UDminlen]):

            if float(dados_json['funcionarios'][lines]['salario']) != int(UDmin[0]):
                UDmin = []
                UDmin_nome = []
                UDmin_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])
                UDmin.append(dados_json['funcionarios'][lines]['salario'])
            else:
                UDmin.append(dados_json['funcionarios'][lines]['salario'])
                UDmin_nome.append(dados_json['funcionarios'][lines]['nome'] + " " +
                                  dados_json['funcionarios'][lines]['sobrenome'])

    lines = lines + 1
# output of SD
print("area_avg|Desenvolvimento de Software|" + "{:.2f}".format(SDavg/linessd))
lines = 0
while lines < len(SDmax_nome):
    print("area_max|Desenvolvimento de Software|" + str(SDmax_nome[lines]) + "|" + str("{:.2f}".format(SDmax[0])))
    lines = lines+1

lines = 0
while lines < len(SDmin_nome):
    print("area_min|Desenvolvimento de Software|" + str(SDmin_nome[lines]) + "|" + str("{:.2f}".format(SDmin[0])))
    lines = lines+1
lines = 0

# output of SM
print("area_avg|Gerenciamento de Software|" + "{:.2f}".format(SMavg/linessm))

while lines < len(SMmax_nome):
    print("area_max|Gerenciamento de Software|" + str(SMmax_nome[lines]) + "|" + str("{:.2f}".format(SMmax[0])))
    lines = lines+1

lines = 0
while lines < len(SMmin_nome):
    print("area_min|Gerenciamento de Software|" + str(SMmin_nome[lines]) + "|" + str("{:.2f}".format(SMmin[0])))
    lines = lines+1
lines = 0

# output of UD
print("area_avg|Designer de UI/UX|" + "{:.2f}".format(UDavg/linesud))
while lines < len(UDmax_nome):
    print("area_max|Designer de UI/UX" + str(UDmax_nome[lines]) + "|" + str("{:.2f}".format(UDmax[0])))
    lines = lines+1

lines = 0
while lines < len(UDmin_nome):
    print("area_min|Designer de UI/UX|" + str(UDmin_nome[lines]) + "|" + str("{:.2f}".format(UDmin[0])))
    lines = lines+1

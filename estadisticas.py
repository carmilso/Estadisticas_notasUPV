#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import sys
import string

if len(sys.argv) < 3:
    print "\nUso: ./estadisticas.py <documento> <notaMáxima> [notaPersonal]\n"
    sys.exit(1)

if len(sys.argv) == 4: notaP = True
else: notaP = False

f = string.replace(open(sys.argv[1], 'r').read(), ',', '.')

lista = [e.replace("<","").replace(">","") \
                for e in re.findall(">.[0-9]<", f)+\
                         re.findall(">.[0-9][0-9]<", f) +\
                         re.findall(">[0-9].[0-9]<", f) +\
                         re.findall(">[0-9].[0-9][0-9]<", f) +\
                         re.findall(">[0-9]<", f) +\
                         re.findall(">10<", f)]


presentados, aprobados, suspendidos, notas, notaMax, notaMin = 0, 0, 0, 0, 0, 10
mayorIgual = 0

for e in lista:
    presentados += 1
    notas += float(e)
    if float(e) >= float(sys.argv[2]) / 2: aprobados += 1
    else: suspendidos += 1
    if float(e) > float(notaMax): notaMax = e
    elif float(e) < float(notaMin): notaMin = e
    if notaP and float(e) >= float(sys.argv[3]): mayorIgual += 1

media = notas / presentados

print "\nPresentados: " + str(presentados) + '\n'

print "Nota máxima: " + str(notaMax)
print "Nota mínima: " + str(notaMin)
print "Nota media: " + str(round(media, 2)) + '\n'

print "Porcentaje aprobados: " + \
        str(round(float(aprobados) / presentados * 100, 2)) + '%'\
        + "\t(" + str(aprobados) + ")"
print "Porcentaje suspendidos: " + \
        str(round(float(suspendidos) / presentados * 100, 2)) + '%'\
        + "\t(" + str(suspendidos) + ")" + '\n'

if notaP:
    print str(mayorIgual) + " Personas con nota mayor o igual ("\
        + str(round(float(mayorIgual) / presentados * 100)) + "%)"

print

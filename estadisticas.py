#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import sys
import string
import argparse

parser = argparse.ArgumentParser(description='Estadísticas de notas.')

parser.add_argument('-d', '--doc', required=True,
    help='Ruta del documento de notas')
parser.add_argument('-m', '--notaMaxima', required=True,
    help='Nota máxima posible', type=float)
parser.add_argument('-p', '--notaPersonal', required=False,
    help='Nota personal', type=float)

args = vars(parser.parse_args())

if args['notaPersonal'] != None: notaP = True
else: notaP = False

f = string.replace(open(args['doc'], 'r').read(), ',', '.')

lista = re.findall(r'<td class="alignleft">(\d*.*\d+)</td', f)

presentados = len(lista)

aprobados, suspendidos, notas, notaMin, notaMax = 0, 0, 0, 10, 0
mayorIgual = -1

for e in lista:
    notas += float(e)

    if float(e) >= args['notaMaxima'] / 2: aprobados += 1
    else: suspendidos += 1

    if float(e) > notaMax: notaMax = float(e)
    elif float(e) < notaMin: notaMin = float(e)

    if notaP and float(e) >= args['notaPersonal']: mayorIgual += 1

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

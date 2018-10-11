#!/usr/bin
print 'Listar numeros'
number_start = int(raw_input('Ingrese el numero de inicio: '))
number_limit = int(raw_input('Ingrese el numero limite: '))
while (number_start < number_limit+1):
  print number_start
  number_start+=1


#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
from math import *

def     affichage(size):
   s = str(size) + " éléments"
   print s

def     checkArgs(mylist):
   i = 0
   while (i != len(mylist)):
      try :
         mylist[i] = float(mylist[i])
         i += 1
      except:
         return -1
   return 0

def     tri_selection(mylist, size):
   tmplist = list(mylist)
   cpt = 1
   for i in range(1, size - 1):
      mini = i
      cpt += 1
      for j in range(i + 1, size):
         if (tmplist[j] < tmplist[mini]):
            mini = j
         cpt += 1
      if (mini != i):
         tmp = tmplist[mini]
         tmplist[mini] = tmplist[i]
         tmplist[i] = tmp
   print "tri par sélection :",cpt, "comparaisons" 


def     tri_insertion(mylist, size):
   tmplist = list(mylist)
#   print (tmplist)
   count = 1
   for i in range(1, size, 1):
      x = tmplist[i]
      j = i
      while j > 0 and tmplist[j - 1] > x:
         tmplist[j] = tmplist[j - 1]
         j -= 1
         count += 1
      tmplist[j] = x
   print "tri par insertion :", count, "comparaisons"

def     tri_a_bulles(mylist, size):
   tmplist = list(mylist)
   n = size
   count = 0
   for i in range (n - 1, 0, -1):
      for j in range(0, i, 1):
         if tmplist[j] > tmplist[j + 1]:
            tmp = mylist[j]
            tmplist[j] = tmplist[j + 1]
            tmplist[j+1] = tmp
         count += 1
   print "tri a bulles :", count, "comparaisons"

def	main():
   try:
      file = open(sys.argv[1])
   except:
      return -1
   tmp = file.read()
   mylist = tmp.split(' ')
   size = len(mylist)
   if checkArgs(mylist) == 0:
      affichage(size)
      tri_selection(mylist, size)
      tri_insertion(mylist, size)
      tri_a_bulles(mylist, size)

if __name__ == '__main__':
   sys.exit(main())

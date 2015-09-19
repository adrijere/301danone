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
   cpt = 1
   for i in range(1, size - 1):
      mini = i
      cpt += 1
      for j in range(i + 1, size):
         if (mylist[j] < mylist[mini]):
            mini = j
         cpt += 1
      if (mini != i):
         tmp = mylist[mini]
         mylist[mini] = mylist[i]
         mylist[i] = tmp
   print "tri par sélection :",cpt, "comparaisons" 


def     tri_insertion(mylist, size):
   count = 1
   for i in range(1, size - 1):
      x = mylist[i]
      j = i
      while j > 0:
         if mylist[j - 1] > x:
            mylist[j] = mylist[j - 1]
         j = j - 1
         count += 1
      mylist[j] = x
   print "tri par insertion :", count, "comparaisons"


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

if __name__ == '__main__':
   sys.exit(main())

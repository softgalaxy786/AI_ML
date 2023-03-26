# Programmer: 	Raza Bhatti
# Company:	Softgalaxy Technologies Inc.
# Website:	https://www.linkedin.com/in/softgalaxy
#
# Observation or Principle to proposed solutions: There are mostly or always multiple ways to achieve same objective.
#
# Python 3.x AI_ML Program Function: 
# 1. Find the minimum effort (substitue, insert, delete) required to make two strings (s,t) equal.
#

import sys
import time

name_of_python_script = sys.argv[0]

def convertListToString(listStrings):                 #Reference: https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
 
    # initialize an empty string
    desiredString = ""
    return desiredString.join(listStrings)                    # return string

def computeMinToMakeBothSentencesSame(s,t):     # s: String #1, t: String #2
    global stringMatched
    totalInserts=0
    totalDeletes=0
    totalSubstitues=0  
    #----------------------------------------------------------------------------------#
    # The recursiveActions(m,n) functions transverses sentences, s and t from the end, # 
    # as an optimum approach to find the solution to the problem.                      # 
    #----------------------------------------------------------------------------------#
    cache={}                                                        # To store in cache (m,n)=result and save on CPU execution time. <<Dynaming programming>>
    def recursiveActions(m,n):                                      # m=len(s), n=len(t)
    
      if (m,n) in cache:                                             # No need to go further, saving execution time.
        return cache[(m,n)]
      
      if(m==0):
        result=n                                                    # result is the cost or efforts required to achieve the solution to the problem.
      elif(n==0):
        result=m
      elif(s[m-1]==t[n-1]):                                         # The last letter matches.
        result=recursiveActions(m-1,n-1)
      else:
        substitutionCost=1+recursiveActions(m-1,n-1)                # Substitution => replacing both characters in each string.
        deletionCost=1+recursiveActions(m-1,n)                      # Deletion => deleting character from string s.
        insertionCost=1+recursiveActions(m,n-1)                     # Insertion => adding character to m => deleting character from n.
        
        result=min(substitutionCost, deletionCost,insertionCost)
        
        cache[(m,n)]=result                                         # To store in cache(m,n)=result

      return (result)                                               # Return the minimum cost required to perform current action to achieve objective.
    return recursiveActions(len(s),len(t))                          # return recursively reduced length of both strings.
  #----------------------------------------------------------------------------------#
#--------------------------------------------#
#----Program Starting Point and Main Body----#
#--------------------------------------------#
#####################
# Program Functions #
#####################
#Function to check command line parameters and exit if missing expectations.
def fn_WrongNoOfParameters():
  print("")
  print("")
  print("\r\rKindly input parameter values for AI_ML_MakeSameStrings(x,y) as shown below,")
  print("")
  print("python script_name.py 'First String,Second String'")
  print("")
  print("")  
  exit()

strString1= sys.argv[1]
split_String=strString1.split(",")

#print(sys.argv[1])
#print(split_String)
#print(strString1)

if(len(split_String) < 2):
  fn_WrongNoOfParameters()  

strString1=split_String[0]
strString2=split_String[1]

if(strString1==strString2):
  print("\n\nBoth sentences are the same, so no efforts\n\n")
else:
  print("\n\nMinimum Efforts Required to Make Both Sentences Same: ")
  print(computeMinToMakeBothSentencesSame(strString1,strString2))
#  #print(strChar [::-1])
#  conversionListToString=convertListToString(strChar)
#  print("\n\nThe Matched String => ")
#  print(conversionListToString [::-1])
#  print(convertListToString(set(conversionListToString [::-1])))
#  print("\n\n")
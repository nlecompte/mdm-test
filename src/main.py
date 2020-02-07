#!/bin/python3
 
import math
import os
import random
import re
import sys
from collections import OrderedDict
 

def matchingStrings(strings, queries):
   queries_count = OrderedDict.fromkeys(queries, 0)

   for string in strings:
       string_counter = queries_count.get(string, None)
       if string_counter is not None:
        string_counter += 1
        queries_count[string] = string_counter
 
   return queries_count.values()
  
 
if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
   strings_count = int(input())
 
   strings = []
 
   for _ in range(strings_count):
       strings_item = input()
       strings.append(strings_item)
 
   queries_count = int(input())
 
   queries = []
 
   for _ in range(queries_count):
       queries_item = input()
       queries.append(queries_item)
 
   res = matchingStrings(strings, queries)
 
   fptr.write('\n'.join(map(str, res)))
   fptr.write('\n')
 
   fptr.close()

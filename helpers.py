# Just a tiny helper for getting the width and print the statement centered  ¯\_(ツ)_/¯ 
import os 
import re # RegEx

centeredPrint = lambda statement: print(statement.center(os.get_terminal_size().columns))

'''
Convert's a string list into a regular list:
F.ex. [0, 1, 2, 3] from type **String** -> to type **Int**

Let's deconstruct this:

1. In the for loop: Convert the 'String' list into a regular list by:
    * Remove the Square brackets
    * Split the string into a list
2. For each element in the created list convert it from string to int

Könnnen es gerne vereinfachen, wenn es wärend der Präzi zu verwirrungen kommen könnte 😅

'''
getIntListFromStringList = lambda stringList: [int(listElement) for listElement in re.sub("[\[\]]", "", stringList).split(',')]

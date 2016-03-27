Tautology Verifier
***************************
This module will detect whether a given propositional statement is
tautology or not. 

Assumptions
-------------
1 User should provide correct infix expression


How to use it: 
-------------

The below command will take input from user and print out whether a given
statment is tautology or not. 

python tautology_verifier.py 

The below command will run pre-defined unit  test cases

python tautology_test.py 


Steps used for the solution
----------------------------

1 Take infix expression in input from the user
2 Create a variable map and also check uniqueness of variables.
3 If all Unique not tautology
4 count no. of variables
5 convert expression from infix to postfix
6 Create a Expression tree.
7 then evaluate expressiontree for tautology
8 Once Main program is made do unit testing with the test cases

For giving expression u can select expressions from ip.txt


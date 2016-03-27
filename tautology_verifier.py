#!/usr/bin/env python
#Author=Nimish Devasthali
#Date=24 March 2016

from tautology import PropositionStatement

#main
if __name__ == '__main__':
    while True:
        try:
	    print "Enter the Expression\n"
            expr = raw_input()
	    #print ("Test1 ")   --------just for debugging
            propostionStatement = PropositionStatement(expr)
	    #print ("Test2 ")    ----------for debugging
            if propostionStatement.isTautology():
                print ("True")
            else:
                print ("False")
        except Exception as e:
            break
    

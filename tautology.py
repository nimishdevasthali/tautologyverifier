#!/usr/bin/env python
#Author=Nimish Devasthali
#Date=24 March 2016 , 25 March 2016
from utils import infixToPostfix, postfixToExpressionTree, isOperand
import logging

class PropositionStatement(object):
    def __init__(self, statement):
        '''
            This creates a proposition statement object
        @argsfrom utils import infixToPostfix, postfixToExpressionTree, isOperand

        statement - this has to be a valid infix statement no validation is
        done 
        '''
        self.statement = statement
        logging.debug (statement)

    def _getVariableMap(self, statement):
        logging.debug (statement)
        variableMap = {}
        uniqueVaraibles = True
        for e in statement:
          if isOperand(e):
            if e in variableMap:
                uniqueVaraibles = False
            else:
                variableMap[e] = 0
        return (variableMap, uniqueVaraibles)

    def _evaluateExprTree(self, root, variableMap):
        '''
           This function evaulates the expression using expression 
           tree
           Some optimization over postfix evaluation using expression 
           tree
        '''
        if root:
            value = root.data

	    #print root.data #debugger
            if isOperand(value):
                return variableMap[value]

	    #print variableMap #debugger
            left = self._evaluateExprTree(root.left, variableMap)
            if value == '!': 
                 return not left
            elif value == '&' and not left:
                 return False
            elif value == '|' and left:
                 return True
            right = self._evaluateExprTree(root.right, variableMap)
            if value == '&':
                 return left and right
            elif value == '|':
                 return left or right
            return True
        return True


    """
	**********************for debugging*****************
	**********************for checking expression tree is correctly made***********************	
	def in_traversal(self): 
        if self.left:
            self.left.in_traversal()
	#print "I am a debugging treenode"       ---------debugger
        print self,
        if self.right:
            self.right.in_traversal()
	***************************************************
	***************************************************
    """
    
    def isTautology(self):
        '''
           Determines whether a statement given is a tuatology or not

        Returns:
            This function returns whether a given statement is tautology or not
        '''
        logging.debug (self.statement)
        (variableMap, uniqueVaraibles) = self._getVariableMap(self.statement)
        #optimization step is that if all are unique variables, it won't be tautology

        logging.debug (variableMap, uniqueVaraibles)
        if uniqueVaraibles: 
            return False
        numVariables = len(variableMap)
        postfix = infixToPostfix(self.statement)
	#print postfix #debugger
        root = postfixToExpressionTree(postfix)

	#print root #debugger
	#print root.left #debugger
	#root.in_traversal() #debugger
	#print variableMap #debugger


        for i in range(pow(2, numVariables)):
            for e in enumerate(variableMap):
                offset = e[0]
		#print offset  #debugger
                key = e[1]
		#print key	#debugger
                variableMap[key] = (i & (1 << offset)) >> offset
		#print variableMap	#debugger
            if not self._evaluateExprTree(root, variableMap): 
                return False
        return True
    

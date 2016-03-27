#!/usr/bin/env python
#Author=Nimish Devasthali
#Date=25 March 2016 , 26 March 2016
class TreeNode(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return " " + str(self.data) + " " 

    def in_traversal(self): 
        if self.left:
            self.left.in_traversal()
	#print "I am a debugging treenode"       ---------debugger
        print self,
        if self.right:
            self.right.in_traversal()

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.in_traversal()


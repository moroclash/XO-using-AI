    #                 "  بسم الله الرحمن الرحيم    "

import Node
import copy
import ScoreManager

import sys
# to return the empty position in the matex of game




def Min_max(matrex , depth , type):
    nextplay = None
    successorise = ScoreManager.GetSuccessorise(matrex,type)
    if depth==0 or len(successorise)==0:
        node = Node.Node(matrex,ScoreManager.Score(copy.deepcopy(matrex),type))
        return node

    if(type == "x"):
        value = -20;
        for state in successorise:
            nodemat = Min_max(state,depth-1, "o")
            if nodemat.value  > value:
                value = nodemat.value
                nextplay = Node.Node(state,value)

    if(type == "o"):
        value = 20
        for state in successorise:
            nodemat = Min_max(state,depth-1, "x")
            if nodemat.value < value:
                value = nodemat.value
                nextplay = Node.Node(state,value)

    return nextplay;








#list = (node(x,y,list(node node)) , node(x,y,list(......)) , ...... )















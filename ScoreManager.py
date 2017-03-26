
import copy


def return_empty_positon(matrex):
    position = list()
    if Check_Win(matrex) !=0:
        return position
    for i in range(0,3):
        for j in range(0,3):
            if(matrex[i][j]== -1):
                tuple = (i,j)
                position.append(tuple)
    return position




# this function to generate stat space for specific node
def GetSuccessorise(matrex,type):
    states = list()
    positions = return_empty_positon(matrex)
    for i in range(0,len(positions)):
        x,y = positions[i]
        matrex2 = copy.deepcopy(matrex)
        matrex2[x][y] = type
        states.append(matrex2)
    return states







def Score(array,var):
 if(Check_Win(array)=='x'):
     return  10
 elif Check_Win(array) == 'o':
     num = deep_Score(array,var)
     return ((num*(-1)) -10)
 else:
     if(var == 'o'):
        return deep_Score(array,var)*-1
     return deep_Score(array,var)



def deep_Score(array,var):
    temparray = []
    counterRow = 0;
    counterCOl = 0
    maincounter = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if array[i][j] == -1:
                array[i][j] = var
                # check Row & COlumn
    for i in range(0, 3):  # 0
        counterRow = 0;
        counterCOl = 0
        for j in range(0, 3):  # 0
            if array[i][j] == var:  # 0 0  0  1  0 2
                counterRow += 1
            if array[j][i] == var:
                counterCOl += 1
        if counterRow == 3:
            maincounter += 1
        if counterCOl == 3:
            maincounter += 1
            # check  diagonall
    if array[0][0] == var:
        if array[1][1] == var:
            if array[2][2] == var:
                maincounter += 1
    if array[0][2] == var:
        if array[1][1] == var:
            if array[2][0] == var:
                maincounter += 1
    return maincounter






def  Check_Win(array):
     if Check_Win_deep(array, 'x') == 'x':
         return 'x'
     if Check_Win_deep(array, 'o') == 'o':
         return 'o'
     return 0






def  Check_Win_deep(array,var):
  # check Row & COlumn
  for i in range(0, 3):  # 0
   counterRow = 0;
   counterCOl = 0
   for j in range(0, 3):  # 0
    if array[i][j] == var:  # 0 0  0  1  0 2
     counterRow += 1
    if array[j][i] == var:
      counterCOl += 1
   if counterRow == 3 or counterCOl == 3:
     return var

    # check  diagonall
  if array[0][0] == var:
   if array[1][1] == var:
    if array[2][2] == var:
       return var
  if array[0][2] == var:
   if array[1][1] == var:
    if array[2][0] == var:
       return var








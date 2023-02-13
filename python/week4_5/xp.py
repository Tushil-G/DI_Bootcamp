print ("tic tac toe")
 
def board(row):  
    print("\t**********************")  
    print("\t*      |      |      *")  
    print("\t*     {}|  {}   | {}    *".format(value[0], value[1], value[2]))  
    print('\t* _____|______|_____ *')  
    print("\t*      |      |      *") 
    print("\t*    {} |  {}   | {}    *".format(value[3], value[4], value[5]))  
    print('\t* _____|______|_____ *')  
    print("\t*      |      |      *")    
    print("\t*   {}  |  {}   | {}    *".format(value[], value[7], value[8]))  
    print("\t*      |      |      *")  
    print("\t**********************") 

board("3X3XXXOOO")
def player_input(player):  
    row = [' ' for i in range(4)]  
position_player = {'X' : [], 'O' : []}

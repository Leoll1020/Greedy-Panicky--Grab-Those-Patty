#return a list with width*breadth size. Store state value
import Constants
def initializeTable(WIDTH,BREADTH):
	table = []                                       
	for i in range (0, WIDTH):       
		row = []                  
		for j in range (0, BREADTH):    
			row.append(0)       
		table.append(row) 
	return table

#am I at a different state now
def isSameState(x1,z1,x2,z2):
	return _currentState(x1,z1)==_currentState(x2,z2)

#set the entry at table[x][z]
def setTable(x,z,value):
	int_x, int_z=_currentState(x,z)
	table[int_x][int_z]=value

def getTable(x,z):
	int_x, int_z=_currentState(x,z)
	return table[int_x][int_z]

#Given A* and bestAngle policy (an angle), return the combined output
def choosePolicy(a_star_policy, best_angle_policy):
	return best_angle_policy #Please remove this line 

#transfer double position to integer
def _currentState(x,z, WIDTH, BREADTH):
	ind_x=(x+WIDTH//2)//1  #drop decimals
	ind_z=(z+BREADTH//2)//1  #drop decimals
	return (ind_x,ind_z)

#from all entities find the agent
def findUs(entities):
    for ent in entities:
        if ent.name == Constants.MOB_TYPE:
            continue
        elif ent.name == Constants.GOAL_TYPE:
            continue
        else:
            return ent

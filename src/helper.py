
import runner

#return a list with width*breadth size. Store state value
def initializeTable():
	table = []                                       
	for i in range (0, runner.WIDTH):       
		row = []                  
		for j in range (0, runner.BREADTH):    
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

#Given A* and bestAngle policy, return the combined output
def choosePolicy(a_start_policy, best_angle_policy):
	return

#transfer double position to integer
def _currentState(x,z):
	ind_x=(x+runner.WIDTH//2)//1  #drop decimals
	ind_z=(z+runner.BREADTH//2)//1  #drop decimals
	return (ind_x,ind_z)

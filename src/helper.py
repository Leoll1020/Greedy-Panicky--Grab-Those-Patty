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

#############################
#find the locations of the certain objects
#according to assignment2.py
#can be replaced if there is a similar one 
def object_position(object_type):
	positions = []
	while True:
		world_state = agent_host.getWorldState()
		msg = world_state.observations[-1].text
		ob = json.loads(msg)
		for i in ob[object_type]:
			positions.append((i['x'],i['z']))
		return positions

#given a list of objects and the position of the agent, return a list of distance^2
def calc_dis(ob_list,ob_pos):
	result = []
	for i in ob_list:
		result.append((i[0]-ob_pos[0])**2+(i[1]-ob_pos[1])**2)
	return result
###################################

#Given A* and bestAngle policy (an angle), return the combined output
def choosePolicy(a_start_policy, best_angle_policy, agent_position):
	#suppose here agent_position is (x,z) tuple of agent position
	walls = object_position('lava')   #should change the name of the trap and mob
	mobs = object_position(MOB_TYPE)
	wall_to_agent = calc_dis(walls,agent_position)
	w = min(wall_to_agent)
	mob_to_agent = calc_dis(mobs,agent_position)
	m = min(wall_to_agent)
	_w = w/(w+m)
	_m = m/(w+m)
	return _w*a_start_policy+_m*best_angle_policy

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

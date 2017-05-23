#return a list with width*breadth size. Store state value
import Constants
import json
# import MalmoPython
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
	# Constants.agent_host = MalmoPython.AgentHost()
	# while True:
	# world_state = Constants.agent_host.getWorldState()
	# print 'world_state.observations',len(world_state.observations)
	msg = Constants.world_state.observations[-1].text
	ob = json.loads(msg)
	try: 
		for i in ob[object_type]:
			positions.append((i['x'],i['z']))
	except KeyError:
		for i in ob['entities']:
			if i['name'] == object_type:
				positions.append((i['x'], i['z']))
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
	# print agent_position
	# walls = object_position('lava')   #should change the name of the trap and mob
	# mobs = object_position(MOB_TYPE)
	# wall_to_agent = calc_dis(walls,agent_position)
	# w = min(wall_to_agent)
	# mob_to_agent = calc_dis(mobs,agent_position)
	# m = min(wall_to_agent)
	# _w = w/(w+m)
	# _m = m/(w+m)
	# return _w*a_start_policy+_m*best_angle_policy
	# return best_angle_policy
	return a_start_policy

#transfer double position to integer
def _currentState(x,z, WIDTH, BREADTH):
	ind_x=(x+WIDTH//2)//1  #drop decimals
	ind_z=(z+BREADTH//2)//1  #drop decimals
	return (ind_x,ind_z)

def positionTOstate(x, z):
	return (int(z+Constants.ARENA_ROW//2),
			int(x+Constants.ARENA_COL//2))

def stateTOposition(row, col):
	return (col-Constants.ARENA_COL//2+0.5, 
			row-Constants.ARENA_ROW//2+0.5)

#from all entities find the agent
def findUs(entities):
    for ent in entities:
        if ent.name == Constants.MOB_TYPE:
            continue
        elif ent.name == Constants.GOAL_TYPE:
            continue
        else:
            return ent


def print_dict(dictionary, name = ''):
	print 'name:', name
	for key, val in sorted(dictionary.items(), key=lambda x: x[0]):
		print '\t',key, ':', val


def print_matrix(matrix):
    print '|' + '|'.join(str(i%10) for i in range(len(matrix)))
    for j in range(len(matrix)):
        print '|'+'|'.join(c for c in matrix[j])+'|' + str((j)%10)



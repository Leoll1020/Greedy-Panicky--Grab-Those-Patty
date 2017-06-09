import random
import errno
import math
import re
import os
import Constants
import helper

Lava_percent = 0.1

def generate_Matrix():
	''' Generate a matrix represent the map of the test
		Return number of lava block / total amount of block
		The starting point would never be lava
		No lava at the 3x3 matrix around the starting point
	'''
	Constants.MATRIX = []
	count_Lava = 0
	for i in range(Constants.ARENA_ROW):
		temp_row = []
		for j in range(Constants.ARENA_COL):
			if all(abs(coor-0.5) <= 1
					for coor in helper.stateTOposition(i,j)):
				temp_row.append(' ')
				continue 
			u = random.random()
			if u < Lava_percent:
				count_Lava += 1
				temp_row.append('l')
			else:
				temp_row.append(' ')
		Constants.MATRIX.append(temp_row)
	return float(count_Lava) / float(Constants.ARENA_ROW * Constants.ARENA_COL)


def getCorner(index,top,left,expand=0,y=206):
    ''' Return part of the XML string that defines the requested corner'''
    x = str(-(expand+Constants.ARENA_COL/2)) if left else str(expand+Constants.ARENA_COL/2)
    z = str(-(expand+Constants.ARENA_ROW/2)) if top else str(expand+Constants.ARENA_ROW/2)
    return 'x'+index+'="'+x+'" y'+index+'="' +str(y)+'" z'+index+'="'+z+'"'

def genLavaXML():
    # <DrawBlock x="0" y="206" z="0" type="lava" />
    xml = ""
    
    for i in range(len(Constants.MATRIX)):
        for j in range(len(Constants.MATRIX[i])):
            if Constants.MATRIX[i][j] == 'l':
                xml += '''<DrawBlock x="''' + str(j-Constants.ARENA_COL/2) + '''" y="206" z="''' + str(i-Constants.ARENA_ROW/2) + '''" type="lava"/>'''

    
    return xml


def genRandomGoalXML(num=Constants.NUM_GOALS):
    ''' Build an XML string that contains some randomly positioned goal items'''
    xml=""
    count = 0
    while count < num:
    	row = random.randint(0, Constants.ARENA_ROW-1)
    	col = random.randint(0, Constants.ARENA_COL-1)
        if Constants.MATRIX[row][col] != 'l':
        	x = str(row-Constants.ARENA_COL/2)
        	z = str(col-Constants.ARENA_ROW/2)
        	xml += '''<DrawItem x="''' + x + '''" y="210" z="''' + z + '''" type="''' + Constants.GOAL_TYPE + '''"/>'''
        	count += 1
        else:
        	continue
        
    return xml


def randomMapXML(mode='Survival'):
	# generate_Matrix()
	''' Build an XML mission string.'''
	spawn_end_tag = ' type="mob_spawner" variant="' + Constants.MOB_TYPE + '"/>'
	return '''<?xml version="1.0" encoding="UTF-8" ?>
	<Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	    <About>
	        <Summary>Test with randomized map</Summary>
	    </About>

	    <ModSettings>
	        <MsPerTick>20</MsPerTick>
	    </ModSettings>
	    <ServerSection>
	        <ServerInitialConditions>
	            <Time>
	                <StartTime>18000</StartTime>
	                <AllowPassageOfTime>false</AllowPassageOfTime>
	            </Time>
	        </ServerInitialConditions>
	        <ServerHandlers>
	            <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1" />
	            <DrawingDecorator>
	                <DrawCuboid ''' + getCorner("1",True,True,expand=1) + " " + getCorner("2",False,False,y=226,expand=1) + ''' type="stone"/>
	                <DrawCuboid ''' + getCorner("1",True,True,y=207) + " " + getCorner("2",False,False,y=226) + ''' type="air"/>

	                <DrawLine ''' + getCorner("1",True,True) + " " + getCorner("2",True,False) + spawn_end_tag + '''
	                <DrawLine ''' + getCorner("1",True,True) + " " + getCorner("2",False,True) + spawn_end_tag + '''
	                <DrawLine ''' + getCorner("1",False,False) + " " + getCorner("2",True,False) + spawn_end_tag + '''
	                <DrawLine ''' + getCorner("1",False,False) + " " + getCorner("2",False,True) + spawn_end_tag + '''
	                <DrawCuboid x1="-1" y1="206" z1="-1" x2="1" y2="206" z2="1" ''' + spawn_end_tag + '''
	                '''+ genLavaXML() +genRandomGoalXML() + '''
	            </DrawingDecorator>
	            <ServerQuitWhenAnyAgentFinishes />
	        </ServerHandlers>
	    </ServerSection>

	    <AgentSection mode="'''+ mode + '''">
	        <Name>The Hunted</Name>
	        <AgentStart>
	            <Placement x="0.5" y="207.0" z="0.5" yaw='180'/>
	            <Inventory>
	            </Inventory>
	        </AgentStart>
	        <AgentHandlers>
	            <ChatCommands/>
	            <ContinuousMovementCommands turnSpeedDegs="360"/>
	            <AbsoluteMovementCommands/>
	            <ObservationFromNearbyEntities>
	                <Range name="entities" xrange="'''+str(Constants.ARENA_COL)+'''" yrange="2" zrange="'''+str(Constants.ARENA_ROW)+'''" />
	            </ObservationFromNearbyEntities>
	            <ObservationFromFullStats/>
	            <RewardForCollectingItem>
	                <Item type="'''+Constants.GOAL_TYPE+'''" reward="'''+str(Constants.GOAL_REWARD)+'''"/>
	            </RewardForCollectingItem>
	        </AgentHandlers>
	    </AgentSection>

	</Mission>'''











if __name__ == '__main__':
    print 'Actual Percent: {:.3f}'.format(generate_Matrix())
    
    print helper.print_matrix(Constants.MATRIX)

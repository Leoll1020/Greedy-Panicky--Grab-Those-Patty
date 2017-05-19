import random
import errno
import math
import re
import os
# Task parameters:
GOAL_REWARD = 100
MOB_TYPE = "Endermite"  # Change for fun, but note that spawning conditions have to be correct - eg spiders will require darker conditions.
NUM_GOALS = 20
GOAL_TYPE = "apple"
ARENA_COL = 60   # number of columns
ARENA_ROW = 60 # number of rows
MATRIX = []  # Map represented by 2d array


# XML format documentation: http://microsoft.github.io/malmo/0.21.0/Schemas/Mission.html



##########################################################################
#
#               Read from TXT file
#
##########################################################################

def readMapTXT(filename):
    global MATRIX
    try:
    
        with open(filename,'r') as file:
            global NUM_GOALS, GOAL_TYPE, ARENA_ROW, ARENA_COL
            for line in file:
                if '=' in line:
                    exec(line, globals())
                    continue
                
                rest = line.partition('#')[0]
                if len(rest) == 0:
                    continue

                row = re.split('\|', rest)[:-1]
                assert len(row) == ARENA_COL, 'Error in reading maps: arena width does not match the number of columns'
                MATRIX.append(row)

            assert len(MATRIX) == ARENA_ROW, 'Error in reading maps: arena breadth does not match the number of rows'


    except IOError as e:
        print "Unable to find", filename 
        print 'cwd:', os.getcwd()
        raise IOError




##########################################################################
#
#               Matrix to XML
#
##########################################################################

def genRandomGoalXML(num):
    ''' Build an XML string that contains some randomly positioned goal items'''
    xml=""
    for item in range(num):
        x = str(random.randint(-ARENA_COL/2,ARENA_COL/2))
        z = str(random.randint(-ARENA_ROW/2,ARENA_ROW/2))
        xml += '''<DrawItem x="''' + x + '''" y="210" z="''' + z + '''" type="''' + GOAL_TYPE + '''"/>'''
    return xml

def genGoalXML():
    # <DrawItem  x="0" y="206" z="0" type="apple"/>
    xml = ""
    coors = []
    for i in range(len(MATRIX)):
        for j in range(len(MATRIX[i])):
            if MATRIX[i][j] == 'g':
                coors.append((j-ARENA_COL/2, i-ARENA_ROW/2,))

    for x, z in coors:
        xml += '''<DrawItem x="''' + str(x) + '''" y="210" z="''' + str(z) + '''" type="''' + GOAL_TYPE + '''"/>'''

    # if the number of goals in the map.txt is not sufficient, generate random goals as supplement
    xml += genRandomGoalXML(NUM_GOALS - len(coors))
    
    return xml

def genLavaXML():
    # <DrawBlock x="0" y="206" z="0" type="lava" />
    xml = ""
    
    for i in range(len(MATRIX)):
        for j in range(len(MATRIX[i])):
            if MATRIX[i][j] == 'l':
                xml += '''<DrawBlock x="''' + str(j-ARENA_COL/2) + '''" y="206" z="''' + str(i-ARENA_ROW/2) + '''" type="lava"/>'''

    
    return xml








##########################################################################
#
#               Helper
#
##########################################################################

def getCorner(index,top,left,expand=0,y=206):
    ''' Return part of the XML string that defines the requested corner'''
    x = str(-(expand+ARENA_COL/2)) if left else str(expand+ARENA_COL/2)
    z = str(-(expand+ARENA_ROW/2)) if top else str(expand+ARENA_ROW/2)
    return 'x'+index+'="'+x+'" y'+index+'="' +str(y)+'" z'+index+'="'+z+'"'



def print_task_parameters():
    global NUM_GOALS, GOAL_TYPE, ARENA_ROW, ARENA_COL
    print 'GOAL_REWARD:', GOAL_REWARD, 
    print 'MOB_TYPE:', MOB_TYPE,
    print 'NUM_GOALS:', NUM_GOALS,
    print 'GOAL_TYPE:', GOAL_TYPE,
    print 'ARENA_COL:', ARENA_COL,
    print 'ARENA_ROW:', ARENA_ROW

def print_matrix():
    print '|' + '|'.join(str(i%10) for i in range(1, ARENA_COL+1))
    for j in range(len(MATRIX)):
        print '|'+'|'.join(c for c in MATRIX[j])+'|' + str((j+1)%10)








##########################################################################
#
#               Public Function
#
##########################################################################
def readMapXML(filename = 'map0.txt', mode ='Survive'):
    readMapTXT(filename)
    return getMissionXML("Read from "+filename, mode = mode)


def getMissionXML(summary, mode='Survive'):
    ''' Build an XML mission string.'''
    spawn_end_tag = ' type="mob_spawner" variant="' + MOB_TYPE + '"/>'
    return '''<?xml version="1.0" encoding="UTF-8" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <About>
            <Summary>''' + summary + '''</Summary>
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
                    ''' + genGoalXML()+ genLavaXML() + '''
                </DrawingDecorator>
                <ServerQuitWhenAnyAgentFinishes />
            </ServerHandlers>
        </ServerSection>

        <AgentSection mode="'''+ mode + '''">
            <Name>The Hunted</Name>
            <AgentStart>
                <Placement x="0.5" y="207.0" z="0.5"/>
                <Inventory>
                </Inventory>
            </AgentStart>
            <AgentHandlers>
                <ChatCommands/>
                <ContinuousMovementCommands turnSpeedDegs="360"/>
                <AbsoluteMovementCommands/>
                <ObservationFromNearbyEntities>
                    <Range name="entities" xrange="'''+str(ARENA_COL)+'''" yrange="2" zrange="'''+str(ARENA_ROW)+'''" />
                </ObservationFromNearbyEntities>
                <ObservationFromFullStats/>
                <RewardForCollectingItem>
                    <Item type="'''+GOAL_TYPE+'''" reward="'''+str(GOAL_REWARD)+'''"/>
                </RewardForCollectingItem>
            </AgentHandlers>
        </AgentSection>

    </Mission>'''











if __name__ == '__main__':
    # readMapTXT('map0.txt')
    # print_task_parameters()
    # print_matrix()
    # print getMissionXML("TEST")
    readMapXML()


import random
import errno
import math
import re
import os
import Constants
import helper

# MATRIX = []  # Map represented by 2d array
# XML format documentation: http://microsoft.github.io/malmo/0.21.0/Schemas/Mission.html



##########################################################################
#
#               Read from TXT file
#
##########################################################################

def readMapTXT(filename):
    try:
    
        with open(filename,'r') as file:
            for line in file:
                if '=' in line:
                    # exec(line, globals())
                    continue
                
                rest = line.partition('#')[0]
                if len(rest) == 0:
                    continue

                row = re.split('\|', rest)[:-1]
                assert len(row) == Constants.ARENA_COL, 'Error in reading maps: arena width does not match the number of columns'
                Constants.MATRIX.append(row)

            assert len(Constants.MATRIX) == Constants.ARENA_ROW, 'Error in reading maps: arena breadth does not match the number of rows'
        helper.print_matrix(Constants.MATRIX)

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
        x = str(random.randint(-Constants.ARENA_COL/2,Constants.ARENA_COL/2))
        z = str(random.randint(-Constants.ARENA_ROW/2,Constants.ARENA_ROW/2))
        xml += '''<DrawItem x="''' + x + '''" y="210" z="''' + z + '''" type="''' + Constants.GOAL_TYPE + '''"/>'''
    return xml

def genGoalXML():
    # <DrawItem  x="0" y="206" z="0" type="apple"/>
    xml = ""
    coors = []
    for i in range(len(Constants.MATRIX)):
        for j in range(len(Constants.MATRIX[i])):
            if Constants.MATRIX[i][j] == 'g':
                coors.append((j-Constants.ARENA_COL/2, i-Constants.ARENA_ROW/2,))

    for x, z in coors:
        xml += '''<DrawItem x="''' + str(x) + '''" y="210" z="''' + str(z) + '''" type="''' + Constants.GOAL_TYPE + '''"/>'''

    # if the number of goals in the map.txt is not sufficient, generate random goals as supplement
    xml += genRandomGoalXML(Constants.NUM_GOALS - len(coors))
    
    return xml

def genLavaXML():
    # <DrawBlock x="0" y="206" z="0" type="lava" />
    xml = ""
    
    for i in range(len(Constants.MATRIX)):
        for j in range(len(Constants.MATRIX[i])):
            if Constants.MATRIX[i][j] == 'l':
                xml += '''<DrawBlock x="''' + str(j-Constants.ARENA_COL/2) + '''" y="206" z="''' + str(i-Constants.ARENA_ROW/2) + '''" type="lava"/>'''

    
    return xml








##########################################################################
#
#               Helper
#
##########################################################################

def getCorner(index,top,left,expand=0,y=206):
    ''' Return part of the XML string that defines the requested corner'''
    x = str(-(expand+Constants.ARENA_COL/2)) if left else str(expand+Constants.ARENA_COL/2)
    z = str(-(expand+Constants.ARENA_ROW/2)) if top else str(expand+Constants.ARENA_ROW/2)
    return 'x'+index+'="'+x+'" y'+index+'="' +str(y)+'" z'+index+'="'+z+'"'



# def print_task_parameters():
#     #global NUM_GOALS, GOAL_TYPE, ARENA_ROW, ARENA_COL
#     print 'GOAL_REWARD:', GOAL_REWARD, 
#     print 'MOB_TYPE:', MOB_TYPE,
#     print 'NUM_GOALS:', NUM_GOALS,
#     print 'GOAL_TYPE:', GOAL_TYPE,
#     print 'ARENA_COL:', ARENA_COL,
#     print 'ARENA_ROW:', ARENA_ROW

# def print_matrix():
#     print '|' + '|'.join(str(i%10) for i in range(1, ARENA_COL+1))
#     for j in range(len(Constants.MATRIX)):
#         print '|'+'|'.join(c for c in Constants.MATRIX[j])+'|' + str((j+1)%10)








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
    spawn_end_tag = ' type="mob_spawner" variant="' + Constants.MOB_TYPE + '"/>'
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
    # readMapTXT('map0.txt')
    # print_task_parameters()
    # print_matrix()
    # print getMissionXML("TEST")
    readMapXML()
    print helper.print_matrix(Constants.MATRIX)


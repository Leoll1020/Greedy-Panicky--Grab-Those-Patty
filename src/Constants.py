# Task parameters:
GOAL_REWARD = 100
MOB_TYPE = "Endermite"  # Change for fun, but note that spawning conditions have to be correct - eg spiders will require darker conditions.
NUM_GOALS = 20
GOAL_TYPE = "apple"
ARENA_COL = 15   # number of columns
ARENA_ROW = 15 # number of rows
MATRIX = []  # Map represented by 2d array


# x = col = width, z = row = breadth

# Display parameters:
CANVAS_BORDER = 20
CANVAS_WIDTH = 400
CANVAS_HEIGHT = CANVAS_BORDER + ((CANVAS_WIDTH - CANVAS_BORDER) * ARENA_ROW / ARENA_COL)
CANVAS_SCALEX = (CANVAS_WIDTH-CANVAS_BORDER)/ARENA_COL
CANVAS_SCALEY = (CANVAS_HEIGHT-CANVAS_BORDER)/ARENA_ROW
CANVAS_ORGX = -ARENA_COL/CANVAS_SCALEX
CANVAS_ORGY = -ARENA_ROW/CANVAS_SCALEY

# Agent parameters:
agent_stepsize = 1
agent_search_resolution = 30 # Smaller values make computation faster, which seems to offset any benefit from the higher resolution.
agent_goal_weight = 100
agent_edge_weight = -100
agent_mob_weight = -10
agent_turn_weight = 0 # Negative values to penalise turning, positive to encourage.


# 
agent_host = None
world_state= None

AStar_Policy = []
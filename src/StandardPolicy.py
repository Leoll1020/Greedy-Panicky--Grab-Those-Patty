import MalmoPython
import os
import random
import sys
import time
import json
import random
import errno
import math
import Tkinter as tk
from collections import namedtuple
from ReadMap import *
import Constants

import helper



def returnStandardPolicy(entities, current_yaw, current_health):
    '''Scan through 360 degrees, looking for the best direction in which to take the next step.'''
    us = helper.findUs(entities)
    scores=[]
    # Normalise current yaw:
    while current_yaw < 0:
        current_yaw += 360
    while current_yaw > 360:
        current_yaw -= 360

    # Look for best option
    for i in xrange(Constants.agent_search_resolution):
        # Calculate cost of turning:
        ang = 2 * math.pi * (i / float(Constants.agent_search_resolution))
        yaw = i * 360.0 / float(Constants.agent_search_resolution)
        yawdist = min(abs(yaw-current_yaw), 360-abs(yaw-current_yaw))
        turncost = Constants.agent_turn_weight * yawdist
        score = turncost

        # Calculate entity proximity cost for new (x,z):
        x = us.x + Constants.agent_stepsize - math.sin(ang)
        z = us.z + Constants.agent_stepsize * math.cos(ang)
        for ent in entities:
            dist = (ent.x - x)*(ent.x - x) + (ent.z - z)*(ent.z - z)
            if (dist == 0):
                continue
            weight = 0.0
            if ent.name == Constants.MOB_TYPE:
                weight = Constants.agent_mob_weight
                dist -= 1   # assume mobs are moving towards us
                if dist <= 0:
                    dist = 0.1
            elif ent.name == Constants.GOAL_TYPE:
                weight = Constants.agent_goal_weight * current_health / 20.0
            score += weight / float(dist)

        # Calculate cost of proximity to edges:
        distRight = (2+Constants.ARENA_COL/2) - x
        distLeft = (-2-Constants.ARENA_COL/2) - x
        distTop = (2+Constants.ARENA_ROW/2) - z
        distBottom = (-2-Constants.ARENA_ROW/2) - z
        score += Constants.agent_edge_weight / float(distRight * distRight * distRight * distRight)
        score += Constants.agent_edge_weight / float(distLeft * distLeft * distLeft * distLeft)
        score += Constants.agent_edge_weight / float(distTop * distTop * distTop * distTop)
        score += Constants.agent_edge_weight / float(distBottom * distBottom * distBottom * distBottom)
        scores.append(score)

    # Find best score:
    i = scores.index(max(scores))
    # Return as an angle in degrees:
    print 'best:', i * 360.0 / float(Constants.agent_search_resolution)

    return i * 360.0 / float(Constants.agent_search_resolution)
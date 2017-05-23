import random
import sys
import time
import json
import random
import errno
import math
import Tkinter as tk
from collections import namedtuple
# from ReadMap import *
import Constants
from priodict import priorityDictionary
from collections import defaultdict

import helper




'''
total of four  cases may happen:
1: No trap No apple
2: trap only
3: apple only
4: apple behind trap
'''


def decide_case(curr_state,n):
	#return the case number defined as above
	for i in range(n):
		if (has_apple(curr_state,n)):
			return 3
		elif (has_trap(curr_state,n)):
			#check if apple behind trap
			return 2/4
	return 1

def get_surrounding(state, map):
	result = []
	row, col = state
	for drow in range(-1, 2):
		for dcol in range(-1,2):
			if (drow, dcol) == (0,0):
				continue
			if (row + drow) in range(0, len(map)) and\
				(col + dcol) in range(0, len(map[0])):
				result.append((row+drow, col+dcol))

	return result


def distance(a, b, map):
	# return the distance between two states
	# use for gScore
	return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

def angle_between_state(a, b, map):
	'''
	|  135.00  |  180.00  |  225.00  |
	|  90.00   |  270.00  |  270.00  |
	|  45.00   |  360.00  |  315.00  |
	'''
	c = 0
	if a == b:
		return 0
	if b[1] >= a[1]:
		c = 270
	else: 
		c = 90
	if a[1] == b[1]:
		return (b[0]-a[0])*90.0 + c
	else:
		return math.degrees(
					math.atan(float(b[0]-a[0])/float(b[1]-a[1]))
				) + c
	
def angle_between_position(p1, p2):
	if helper.positionTOstate(p1[0], p1[1]) == helper.positionTOstate(p2[0], p2[1]):
		return 0
	
	if p2[0] > p1[0]:
		c = 270
	else: 
		c = 90
	dx = p2[0]-p1[0]
	dz = p2[1]-p1[1]
	if dx == 0:
		if dz > 0: return 0
		else: return 180
	else:
		return math.degrees(
					math.atan(dz/dx)
				) + c


def heuristic(state, goals, map, angle):
	# return heuristic estimate from state to scores
	# return float
	if map[state[0]][state[1]] == 'l':
		return float('inf')
	if map[state[0]][state[1]] == 'g':
		return -100.0
	else:
		return min( distance(state, goal,map) for goal in goals)
	
def retreive_path(start, dest, pred):
	path = [dest]
	# helper.print_dict(pred, name='pred')
	current = dest
	while current != start:
		# print current
		current = pred[current]
		path.append(current)
	path.reverse()
	return path

#def a_star(start,goal):
def a_star(position,angle, map, previous_start, previous_policy, depth=float('inf')):
	# start:(int, int),map:MATRIX, 
	# goals:coordinates of all goals
	#position of current position(start), and apple (goal)
	
	#TODO: 
	#	Check if the action of start state has been calculated

	# return 0
	
	
	goals_location = helper.object_position(Constants.GOAL_TYPE)
	goals_states = [helper.positionTOstate(*p) for p in goals_location]
	# for i in range(len(map)):
	# 	for j in range(len(map[i])):
	# 		if map[i][j] == 'g':
	# 			goals_states.append((i, j))

	# print "goals_location", goals_location
	# print 'goals_states', goals_states


	start = helper.positionTOstate(position[0],position[1])
	if start in previous_policy:
		at = previous_policy.index(start)
		if at != len(previous_policy):
			previous_policy = previous_policy[at:]
			return angle_between_position(position, 
					helper.stateTOposition(*previous_policy[1]))
	else:
		previous_policy = []


	unvisted = priorityDictionary(sort_by = lambda x: x[1])
	unvisted[start] = 0
	
	gScores = defaultdict(lambda : float('inf')) # cost from start to state
	fScores = defaultdict(None)  # ~cost from state to goal

	pred = defaultdict(lambda : (float('inf'), float('inf')))
	visited = set()
	gScores[start] = 0


	for curr in unvisted:
		visited.add(curr)
		if curr in goals_states:
			previous_policy = retreive_path(start, curr, pred)
			print start, 'to', curr, ':', previous_policy
			break

		# add positions arround curr that are not visited
		for sur in get_surrounding(curr, map):
			if distance(sur, start,map) > depth:
				continue
			dist = distance(curr, sur,map)
			
			if sur in visited and\
				 gScores[sur] < gScores[curr] + dist:
				 continue
			
			# calculate f values for new-added blocks
			if gScores[sur] > gScores[curr] + dist:

				pred[sur] = curr
				gScores[sur] = gScores[curr] + dist
				fScores[sur] = heuristic(sur, goals_states, map, angle) + gScores[sur]
				


			if sur not in visited:
				unvisted[sur] = fScores[sur]
			

	# helper.print_dict(gScores, name='gScore')
	# helper.print_dict(fScores, name='fScore')
		

	next_block = previous_policy[0]
	#find the angle of close_list
	# return 360
	return angle_between_position(position, 
			helper.stateTOposition(*next_block))



# def main(case,curr_state,n):
# 	#give case number return angle
# 	c = decide_case
# 	if c ==1:
# 		return random_angle
# 	elif c == 2:
# 		return opposite_to_trap
# 	elif c ==3:
# 		return toward_apple
# 	else:
# 		return a_star(curr_state,apple_position)



if __name__ == '__main__':
	from ReadMap import readMapTXT
	
	readMapTXT('map0.txt')
	# from ReadMap import MATRIX
	helper.print_matrix(Constants.MATRIX)

	# a_star((0,0), [(3, 8)], Constants.MATRIX,(0,0),(0,0),depth='inf')

	for i in range(-1, 2):
		# print (i,j), '-', (0,0), ':',
		# print angle_between_state((0,0), (i,j), MATRIX)
		print '|'+'|'.join('{:^10.2f}'.format(
			angle_between_state((0,0), (i,j), Constants.MATRIX)) 
				for j in range(-1, 2)
				)+ '|'


	for i in range(-1, 2):
		# for j in range(-1, 2):
		# 	print (j-), '-', (0,0), ':',
		# 	print angle_between_position((0.0,0.0), (j+0.5,i+0.5))
		print '|'+'|'.join('{:^10.2f}'.format(
			angle_between_position((0.5,0.5), (j+0.5,i+0.5))) 
				for j in range(-1, 2)
				)+ '|'
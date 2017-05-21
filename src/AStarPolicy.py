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

import Helper




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



#def a_star(start,goal):
def a_star(start, map, previous_start, previous_policy, depth=2):


	# #position of current position(start), and apple (goal)
	# open_list = []
	# close_list = [goal]
	# while(start not in close_list):
	# 	curr = close_list[-1]
	# 	# add positions arround curr that are not visited
	# 	# calculate f values for new-added blocks
	# 	# find the block m with min f (if same value, random)
	# 	# remove m in open_list
	# 	close_list.add(m)
	# #find the angle of close_list
	# return angle
	return 0

def main(case,curr_state,n):
	#give case number return angle
	c = decide_case
	if c ==1:
		return random_angle
	elif c == 2:
		return opposite_to_trap
	elif c ==3:
		return toward_apple
	else:
		return a_star(curr_state,apple_position)

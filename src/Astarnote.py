# curr_state: the position of the agent
# map_state: the may with the position of the wall and apple(update after eaten)
# n : level of the A* search


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



def a_star(start,goal):
	#position of current position(start), and apple (goal)
	open_list = []
	close_list = [goal]
	while(start not in close_list):
		curr = close_list[-1]
		# add positions arround curr that are not visited
		# calculate f values for new-added blocks
		# find the block m with min f (if same value, random)
		# remove m in open_list
		close_list.add(m)
	#find the angle of close_list
	return angle

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

import random
import sys

#2. Number of states: 26=1+5+10+10
#4. 100 As he uses all space to get pumpkin_pie
#5. 
#####20 Showing best policy: sugar, egg, pumpkin, c_pumpkin_pie, present_gift,  with reward 100.0
#####Found solution
#####Done
#7. Number of states: 130=1+9+36+84
#8. 205 as he will firstly get a pumpkin_pie as before. Then he gets mushroom_stew from bowl and red_mushroom. Eventually, he gets one more red_mushroom
#9. 
#####281 Learning Q-Table: egg, pumpkin, sugar, c_pumpkin_pie, egg, present_gift, Reward: 75
#####282 Learning Q-Table: pumpkin, red_mushroom, egg, present_gift, Reward: -25
#####283 Learning Q-Table: egg, planks, sugar, present_gift, Reward: -40
#####284 Learning Q-Table: sugar, planks, red_mushroom, present_gift, Reward: -10
#####285 Showing best policy: egg, pumpkin, sugar, c_pumpkin_pie, egg, present_gift,  with reward 75.0
#####286 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####287 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####288 Learning Q-Table: red_mushroom, egg, present_gift, Reward: -20
#####289 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####290 Showing best policy: red_mushroom, present_gift,  with reward 5.0
#####291 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####292 Learning Q-Table: pumpkin, sugar, red_mushroom, present_gift, Reward: -10
#####293 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####294 Learning Q-Table: pumpkin, c_pumpkin_seeds, planks, egg, present_gift, Reward: -80
#####295 Showing best policy: red_mushroom, present_gift,  with reward 5.0
#####296 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####297 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####298 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####299 Learning Q-Table: red_mushroom, egg, present_gift, Reward: -20
#####300 Showing best policy: egg, red_mushroom, present_gift,  with reward -20.0

#10. 
#####Intuition: In pratice, the dog tends to get distract by short-term benefits as it significantly favors getting red_mushroom and presents it to dad. 
#####So, we need to focus on long term bigger benefits more, resulting using a higher gamma value (3) and improving learning rate (0.7).
#####281 Learning Q-Table: planks, pumpkin, sugar, present_gift, Reward: -20
#####282 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####283 Learning Q-Table: red_mushroom, pumpkin, present_gift, Reward: 0
#####284 Learning Q-Table: sugar, red_mushroom, pumpkin, c_pumpkin_seeds, present_gift, Reward: -55
#####285 Showing best policy: sugar, red_mushroom, planks, present_gift,  with reward -10.0
#####286 Learning Q-Table: sugar, present_gift, Reward: -10
#####287 Learning Q-Table: planks, sugar, present_gift, Reward: -15
#####288 Learning Q-Table: planks, sugar, present_gift, Reward: -15
#####289 Learning Q-Table: planks, pumpkin, sugar, c_pumpkin_seeds, present_gift, Reward: -65
#####290 Showing best policy: planks, present_gift,  with reward -5.0
#####291 Learning Q-Table: planks, red_mushroom, present_gift, Reward: 0
#####292 Learning Q-Table: egg, red_mushroom, present_gift, Reward: -20
#####293 Learning Q-Table: egg, egg, red_mushroom, present_gift, Reward: -45
#####294 Learning Q-Table: red_mushroom, present_gift, Reward: 5
#####295 Showing best policy: red_mushroom, pumpkin, present_gift,  with reward 0.0
#####296 Learning Q-Table: pumpkin, sugar, present_gift, Reward: -15
#####297 Learning Q-Table: pumpkin, present_gift, Reward: -5
#####298 Learning Q-Table: red_mushroom, pumpkin, present_gift, Reward: 0
#####299 Learning Q-Table: sugar, red_mushroom, planks, present_gift, Reward: -10
#####300 Showing best policy: sugar, present_gift,  with reward -10.0
#12. Collaborator: Jenny Zeng: helped clarify the meaning of Q2 and Q4.


items=['pumpkin', 'sugar', 'egg', 'egg','red_mushroom','planks','planks']

food_recipes = {'pumpkin_pie': ['pumpkin', 'egg', 'sugar'],
				'pumpkin_seeds': ['pumpkin'],
				'bowl':['planks','planks'],
				'mushroom_stew':['bowl','red_mushroom']}

rewards_map = {'pumpkin': -5, 'egg': -25, 'sugar': -10,
			   'pumpkin_pie': 100, 'pumpkin_seeds': -50,
			   'red_mushroom':5, 'planks':-5,
			   'bowl':-1, 'mushroom_stew':100}

def is_solution(reward):
	#return reward == 100
	return reward ==205

def get_curr_state(items):
	return tuple(sorted(items))

def choose_action(curr_state, possible_actions, eps, q_table):
	rnd = random.random()
	action_list=[]
	max_q=-sys.maxint - 1
	for one_action in q_table[curr_state].items():
		if one_action[1]>=max_q:
			max_q=one_action[1]
	for one_action in q_table[curr_state].items():
		#print("\nQ:")
		#print(one_action[1])
		#print(max_q)
		if one_action[1]==max_q:
			action_list.append(one_action[0])
	b=random.randint(0,99)
	#print("Current states:")
	#print(q_table[curr_state].items())
	if b<100*eps:
		#print("\nRamdon:")
		#print(possible_actions)
		a=random.randint(0, len(possible_actions) - 1)
		return possible_actions[a]
	else:
		#print("\nNot Ramdon:")
		#print(action_list)
		a = random.randint(0, len(action_list) - 1)
		return action_list[a]
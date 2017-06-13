---
layout: default
title: Final Report
---
# Greedy-Panicky--Grab-Those-Patty Final Report
## Project Summary
### Background Story:
  Mr. Panicky, our protagonist, is a guy who loves apples and is afraid of bugs. Unfortunately, he has an evil boss who loves to trick Mr. Panicky. One day, the evil boss left pool Panicky in a place surrounded by his favorite apples, scary lethal endermite and hot lava. To survive, Panicky could not be caught by endermites nor step into lavas. Surviving longer is the main goal and getting apples can be a bonus.

### Settings of the World:
  In this world, apples and lavas are randomly generated at the beginning of each mission, the number of the endermites will increase if reach the spawners, and endermites will chase the agent when agent is not far from them.
  
### Goals:
  The main goal of the project is to train the agent to gain high scores in any maps: make movements without falling into lavas or getting caught by endermites; at the same time,get as much apples as possible.

  To achieve this goal, we setted up three goals in order to train the agent:
    1. Use A* policy to find the best angle to avoid lavas and reach apples;
    2. Find a balance between A* policy and the best angle policy to make the agent performs better (best angle policy was provided by mob_fun.py);
    3. Modify the policies to make the trained agent perform better.
    
### Challenges and Solutions:
1. The environment is complex: there are lavas, endermites and apples, in which case, the agent needs to avoid lavas and endermites and get apples. One policy can be hard to do everything.
        Solution: divide the problem into three parts:
              a. Run away from endermites and get apples: use the best angle policy from mob_fun.py to calculate the angle according to the position of endermites and the agent;
              b. Avoid lavas and get apples: use A* policy to find the best angle to avoid the lava and get the apple;
              c. Combine the two policies to solve the problem: a choose_policy function to combine the angles from both policies, and return the final angle.

2. In different situations, the weight of two policies can be different. The agent need to be trained to make the best decision.
        Solution: in the choose_policy function, we first weight two policies on the distance among the agent, and the closest lava and endermite. Then use hill climbing to find the best parameter alpha  to optimize the solution.
 
### Why AI?
  Since the task is complex and the agent needs to balance on different things, i.e. getting apples, avoiding lavas, running away from endermites, it is hard to give a simple solution to the project that can do well in any situation. Therefore, we need to use and combine AI/ML algorithms to train the agent and make it perform well in any situations (i.e. random maps).

## Approaches:
### Section 1: World setup
	
  The testing area is a 15 blocks x 15 blocks stone platform surrounded by walls and Agent is able to run freely inside of it without the ability to jump. The main element of the map include:
	Endermite spawner: It keeps generating the endermites, which are the enemy. Agent can walks safely on it, and thus can be regarded as stones.
	Lava: A block of lava that at the same level as the ground, which forms a pit. If agent steps on to it, it will fall into the pit and burn to death. Agent can use a matrix stores in the code to find out where the lava blocks are.
  Endermites: A groups of endermites will chase and attack the agent. Their speed are similar to the agent and their damage is one heart. The agent finds endermites by the instantaneous observation of the world and tries to avoid them as much as possible.
	Apple: Apples are served as the reward. Getting one apple gives 100 points. The agent finds the apple by observation and it is trying to get as much apple as possible.
 
  The map is randomly generated for each test. The proportion of lava blocks in the map and the number of the apples are given in order to generate a map. The map generator includes mainly two parts: randomized part and the constant part
 
#### Randomized part: 
  The position of lava and apples are randomly generated using the built-in random number generator in Python. 
  For each block in the map, the output of a Bernoulli-distributed random number generator will determine whether the block contains lava or not. However, to make sure the test is usable and meaningful, the agent’s spawn point and those 8 blocks that surrounding it will never be lava. With that exception, the probability of a block being lava (i.e. the probability of Bernoulli-distributed random number generator returns 1) is set to be equal to the proportion of lava in the map. Here is the pseudo code: 
  
  The position of apple is decided by the built-in random integer generator in Python. The algorithm will avoid putting an apple at a lava block. 
Here is the pseudo code:

  



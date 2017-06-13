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


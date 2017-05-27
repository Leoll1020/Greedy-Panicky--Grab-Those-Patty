---
layout: default
title: Status
---
# Greedy-Panicky--Grab-Those-Patty Status Report
## Project Summary:  
The agent, Mr. Panicky, loves apple and afraid of bugs. After being drop into a place surrounded by his favorite apples, scary lethal endermite and hot lava, his goal is to gather as much apples without being killed by endermite or falling into lava. The goal of the project is to build an algorithm that will help Mr. Panicky to survive in a random generated map as long as possible while collecting apples. 
 
 
## Approach:  

Currently, we divide the algorithm into three parts: a path-finding algorithm to lead Mr. Panicky away from the lava and towards the closest apple, a best-angle algorithm to find the best angle to avoid endermite and get close to an apple, and the combination algorithm that generates a final output using previous two algorithms. 
The best-angle algorithm evaluates all the possible by the distance to the endermite and apple and the difference between the new angle and the direction that the Mr. Panicky is currently facing. The angle with the best score (facing towards the apple, away from endermites, and requiring less change) will be chosen to be the final result.
The A-star algorithm is a combination of Dijkstra algorithm and greedy best-first-search algorithm. It has a heuristic function to estimate the distance from current block to the destination and a function to calculate the distance from start to current block and the summation of heuristic function and distance function is the value of one block and whichever block has the least value will be the next to explore. After it reaches a goal or explores all the blocks within the depth, it traces back to find the best path from start to the block with the best value. 
The heuristic function that we are currently using is depends on the sum of the distances from the block to the closest lava and apple. If the block itself contains lava or its surrounding contains lava, the heuristic function will return a really large number so that the algorithm will avoid it. The output of distance function is the summation of the Manhattan distance and the sharpness of turn. 
For the combination algorithm, we compute the weight for both angles to get the final angle. More specifically, we first found the positions of the closest mob and lava towards the agent. Then we use these positions to find the distance between the agent and the closest lava (set it as w), and the distance between the agent and closest mob (set it as m). Then we got the weight for A* policy as _w= a*(m/(w+m)) , so the weight for best angle policy is just 1-_w. Simply multiply each angle with its weight and we can get the final angle. To evaluate the efficiency for each policy, we multiply a parameter a with _w, and change the value of a to see the performance of the agent.
 

## Evaluation:

![Screenshot](docs/evaluation_table.png)

The performance of policy will is evaluated based on the number of command it survives(it gets a new command for every 0.02 second) and the rewards of this mission. The following chart includes the average performance of the corresponding policy: A star algorithm with various depth and combination of both algorithm with various weight. 
 
For qualitative evaluation, see the video demo of project, starting from 2:04. There are several examples of agents changing its direction as the endermite approaches or as it is getting close to lava.




## Remaining Goals and Challenges: 

The depth of A star has somewhat negative impact on the performance of algorithm. We think it is because one node is relatively large for agent and only few nodes will contains enough information for him to make a good decision. Having knowledge of further state actually introduces unstabilizing factor and therefore affects the performance.
 
For the purpose of testing and evaluation process, the program builds map based on txt files using a map parser and we run the test using different maps. For the final project, we are going to build a random map generator to prove its performance in indeed random maps.
 
The weighted average with unified parameter is not flexible enough to advance the performance. Instead, it actually causes the performance to decrease. We think that the reason is that in some cases, one algorithm should be weighted more while in the other cases, it is another way around, and the both cases can occur within the same map. We want to use reinforcement learning to make it more intelligent and therefore boost the performance of the algorithm. Also, we can set and evaluation the policy based on different parameters instead of just depth for A* and a for combination function. 
 


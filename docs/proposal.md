---
layout: default
title: Proposal
---

Summary of the Project

Not every Minecraft player likes encountering enemies, especially among players who prefer exploring and building instead of combating. We hope to help players automatically escape from enemies when enemies approach. Based on reinforcement learning, we train our agents the best ways to escape, given number of enemies, enemy types (we need to apply different strategies against zombies and Creepers), size of the map and their initial locations. We output “strategy”, which is a pool of situations and our reactions. All outputs and inputs should be represented in JSON format.

AI/ML Algorithms
reinforcement learning. 

Evaluation Plan 

In this project, we evaluate the performance of a policy on both the complexity of the set-up and the length of agent’s lifetime, assuming both the agent and zombies take steps simultaneously at a static rate. The absolute baseline would be the average lifetime of an agent in a 30x30 map with multiple zombies (for instance, 5) under the policy of running straight towards a randomly chosen direction. We expect our approach will make at least 90% of agents, with different initial location of agent and enemies, be able to survive for the infinity amount of time. 

For qualitative analysis, we are going to set couple of sanity cases to see if the algorithm works. One important case we need to check is whether the trained agent avoids walking towards zombies. Another case we thought about is to check the whether the algorithm results in similar policies under the same enemy settings (including enemy’s locations, policies and quantity). We may use Monte Carlo method to visualize the algorithm and check if it works. The moonshot case for our project is that the trained agent can survive for infinite length of lifetime in any complex situations, which means it can permanently get rid of enemies.


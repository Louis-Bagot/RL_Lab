# Instructions for RL Lab Session 2
This lab session is divided into two parts.
None of them is graded. Relax!

The first part, about half the session, will consist of 3 similar written exercises.
You will have to turn a problem statement into its corresponding MDP.

The second part, over the second half, will be a programming exercise on the Value Iteration algorithm.

## First part: From problem statements to MDPs
We will shortly study the robot problem from Sutton&Barto, drawing its MDP as a graph.
Please do the same for the following problems, by groups of 2 if you wish so.
When done, discuss your solutions with a group that is also done.
When you think it is correct, come study it with us (please already start the 2nd part if you're busy with others).

### 1st problem: a healthy lifestyle
The probabilities and rewards are up to you, but they should be consistent with the problem statement.

> You are a healthy, sane person, but with a weak immune system.
> Every year, you have some probability to fall sick, which lowers if you remember to do a health check. When do do a health check and you stay healthy, you sometimes notice it and are happy about it.
> If you are sick, your condition is bad and doing nothing will result in high chances of death, and no chance of recovery whatsoever.
> Your doctor prescribes some medicine for you, which - if you remember to take it- have some probability to cure you. However, even then, chances to die remain, although lowered.

When designing the MDP, make sure that the optimal behavior is to stay healthy and alive!

### 2nd problem: Clean&Guide bot
For this part of assignment please read the instructions carefully:-
1) Refer to only first 3 paragraphs of this published article for your problem-statement
https://www.theverge.com/2017/7/21/16007680/lg-airport-robot-cleaning-guide-south-korea-incheon
2) Based on these, you have to design an MDP for a rechargable battery powered L.G Robot. The robot strictly operates inside the airport with access to only the Reception, Terminal and Charging Station. Assuming you are Principle machine learning engineer within the company, your MDP needs to propose a robot that combines the properties of both Cleaning and Guide robots. The robot can choose to escort the user to the terminal and every interaction with the user has feedback in (-1, 0, +1) (always provided).
3) While designing the MDP, ignore the feature of the cleaning robot mentioned in the article as "detects the areas that require the most frequent cleaning, stores those locations in its database and calculates the most efficient routes to get there." Just use a general "clean" action.

### 3rd problem:
```
          |||
          |||
          _._
        .' ..`.
        |     |  <--- ball
         `---'          
           0
          0 0
         0 0 0   <--- pins
        0 0 0 0
```
We want to model the game of bowling, but we will need to severely simplify it.
The scoring system is quite complex, so let's just say the goal is to hit all the pins in the least tries possible.
The player can choose to throw the ball {left, middle, right}, but the transitions are highly stochastic (player's skill and consistency; hard to know the precise outcome of a throw).
What would the states of the environment be?
Draw a subset of the MDP, with initial and terminal state, and some possible transitions from all 3 actions from the start state (stay below 10 states).
If you have some time to waste, compute the total number of states of the environment.

## Second part: Programming
Using the skeleton code from the `programming` folder, you will implement Value Iteration on the environment for Steven's course.
We used code from Berkeley; you can find their instructions at http://ai.berkeley.edu/reinforcement.html#Q1
Make sure to read the `MDP` section as well, which details how to launch the code. Note that you can even try it with option `-m`.
As they say, you need to implement three functions of the ValueIterationAgent class from valueIterationAgents.py module:
* the \_\_init\_\_ function, where the iterations are made and the V values are computed
* the computeQValueFromValues function, which outputs the Q values form the MDP and Vs
* the computeActionFromValues function, greedy policy over our Vs

Visualize the code by launching it as they say, with `python gridworld.py -a value -i 5`.
Make sure your result is the same as the one they show, which also corresponds to our screenshot available in the solution_plots folder.
Also compare the q values with ours, by pressing an arrow from the V visualization.
Press an arrow again to visualize the agent's optimal policy!

You can play around with hyperparameters; but you're done.
Good job!

# Instructions for the Control exercises.
This is exactly the same API as lab session 2 and 3 with the Gridworld with a diamond and a pit.


## Implementation
In both
* valueIterationAgents
* policyIterationAgent

please implement
* `__init__` to play the algorithm out. This is technically enough if you can get the printing of the number of steps to convergence out

Optional (but it won't crash, so satisfying)
* computeQValueFromValues
* computeActionFromValues
These have been done in the Value Iteration lab session.
Be careful, it is different methods for Policy Iteration!

## Running
You have to run until convergence - so give a very big number of iterations, so that it doesn't stop the algorithm. A non-inf value is important to detect divergence.
`python gridworld.py -a value -i 10000`
Use `-a policy` for the PolicyIterationAgent.

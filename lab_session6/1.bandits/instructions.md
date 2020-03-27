# Instruction for Bandits
This is exactly the same API as you used before - barely any changes have been made.

## Implementation
You have to implement Eps Greedy with both Sample Average and Weighted Average.
Please use learning rate lr=0.1
If you believe your previous code was alright, you can reuse it.

You have to implement the Mixture_Bandit_NonStat class.
It is different than the Gaussian Bandits from before: the reward distribution now follows a Gaussian mixture with 2 components and random weighting, rather than a single Gaussian. Please follow the documentation.

The KBandit_NonStat is simply a set of k of these, as before.

## Running
Same as the first lab session; run the launcher with python. Be careful of the new instructions for the exercise (refer to the report).
Please copy the performance plot you get and paste it on the report.

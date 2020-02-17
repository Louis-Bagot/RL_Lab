"""
Module to solve the bandit problems with an agent.

Complete the code wherever TODO is written.
"""
# -*- coding: utf-8 -*-
import numpy as np

def run_bandit(agent, kbandit, max_steps) -> (np.array, np.array):
    """
    Runs a Bandit problem once. The kbandit and agent are reinitializated,
    then for max_steps, we run the bandit-agent interactions with learning.
    We return the performance of the agent, i.e. the rewards along the way,
    as well as a boolean array of the best action being performed.
    Parameters
    ----------
    agent: Bandit_Agent
        An instance of a Bandit_Agent to solve the problem.
    kbandit: KBandit
        k-armed bandit problem, i.e. k slot machines with a reward distribution.
    max_steps: positive int
        Number of steps to run the problem.
    Returns
    -------
    perf, best_action : np.array, np.array
        Arrays of size max_steps containing all
            - perf: rewards obtained by the agent during the run.
            - best_action: boolean array, whether the agent did the best action.
    """
    # TODO: implement this function.

    # return perf, best_action
    pass

def run_multiple_bandits():
    # TODO: implement this function.
    # Reminder: averages the perf and best_action of the agent over a given number of runs.
    pass

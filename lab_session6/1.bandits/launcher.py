"""
Module to solve the bandit problems with an agent.

Complete the code wherever TODO is written.
"""
# -*- coding: utf-8 -*-
import numpy as np
from utils import *
from agents import *
from bandit import *

## FUNCTIONS ===================================================================

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
        Arrays of size max_steps:
            - perf: rewards obtained by the agent during the run.
            - best_action: boolean array, whether the agent did the best action.
                For computing the mean afterwards, best_action can be an array
                of ones and zeros rather than actual booleans.
    """
    agent.reset()
    kbandit.reset()
    perf = np.empty(max_steps)
    best_action = np.empty(max_steps)
    for step in range(max_steps):
        action = agent.act()
        reward = kbandit.pull(action)
        agent.learn(action, reward)

        perf[step] = reward
        best_action[step] = int(action == kbandit.best_action)

    return perf, best_action

def run_multiple_bandits(n_runs, **kwargs) -> (np.array, np.array):
    """
    Runs multiple independent bandit problems; outputs the mean of the results.
    Can be seen as a wrapper executing the run_bandit function n_runs times.
    Parameters
    ----------
    n_runs : positive int
        Number of runs to average the results on.
    **kwargs: dictionary
        Inputs for the function run_bandit (agent, kbandit, max_steps)
    Returns
    -------
    ret : np.array, np.array
        n_runs averaged outputs from the run_bandit function calls.
    """
    perfs = []
    best_actions = []
    for run in range(n_runs):
        perf, best_action = run_bandit(**kwargs)
        perfs.append(perf)
        best_actions.append(best_action)

    return np.mean(perfs,axis=0), np.mean(best_actions,axis=0)

def run_multiple_agents(agents, **kwargs):
    """
    Launches run_multiple_bandits for a list of agents.
    Outputs a list of the returns.
    Parameters
    ----------
    agents : list of agents
        instantiated agents on which to perform the runs on.
    **kwargs: dictionary
        Inputs for the function run_multiple_bandits
    Returns
    -------
    ret : list
        list of the outputs from the run_multiple_bandits function for each
        agent from the agents list.
    """
    perfs = []
    best_actions = []
    for agent in agents:
        print(agent.__class__.__name__)
        kwargs['agent'] = agent
        perf, best_action = run_multiple_bandits(**kwargs)
        perfs.append(perf)
        best_actions.append(best_action)

    return perfs, best_actions

def run_spectrum(spectrum, **kwargs):
    """
    Launches run_multiple_bandits for a spectrum of hyperparameters specified
    in a vector. Outputs a list of the returns for each value.
    Alternative to run_multiple_agents to focus on one agent and one of its
    hyperparameters.
    Parameters
    ----------
    spectrum : tuple
        A spectrum is a tuple containing the variable name (string) as first
        index, and the list of values this variable should take as second index.
    agent: Bandit_Agent
        the value of this agent's hyperparameter (given in spectrum[0])
        is changed before launching the multiple runs.
    kbandit, n_runs, max_steps: see
    Returns
    -------
    ret : list
        list of the outputs from the run_multiple_bandits function for each
        agent from the agents list.
    """
    perfs = []
    best_actions = []
    varname, values = spectrum
    for value in values:
        print("{} = {}".format(varname, value))
        setattr(kwargs['agent'], varname, value)
        perf, best_action = run_multiple_bandits(**kwargs)
        perfs.append(perf)
        best_actions.append(best_action)

    return np.array(perfs), np.array(best_actions)

## HYPERPARAMETERS =============================================================
config = {
    'k': 10,
    'lr': 0.1,
    'alpha': 0.25,
    'eps': 0.1,
    'c': 0.5,
    'q0': 1
}

n_runs = 2000
max_steps = 1000

## RUNNING =====================================================================
kbandit = KBandit(**config)

# Un-comment the one you want to use.
launch_type = 'multiple_agents'
#launch_type = 'spectrum'

if launch_type == 'multiple_agents':
    agents = [
        Random_Agent(**config),
        EpsGreedy_WeightedAverage(**config),
        EpsGreedy_SampleAverage(**config),
    ]
    perfs, best_actions = run_multiple_agents(agents, kbandit=kbandit, n_runs=n_runs, max_steps=max_steps)
    # You can change the labels, title and file_name
    labels = ['Random', 'EpsGreedyWA', 'EpsGreedySA']
    file_name = 'plots/agent_comparison'
    suptitle = 'Agent comparison on k-armed-Bandit'

elif launch_type == 'spectrum':
    agent = UCB(**config)
    spectrum =  ['c', [0.25,0.5,1,2]]
    # finally, running:
    perfs, best_actions = run_spectrum(spectrum, agent=agent, kbandit=kbandit, n_runs=n_runs, max_steps=max_steps
    # You can change the labels, title and file_name
    labels = ['{}={}'.format(spectrum[0], value) for value in spectrum[1]]
    file_name = 'plots/{}_study'.format(spectrum[0])
    suptitle = 'Varying {} for {} on k-armed-Bandit'.format(spectrum[0], agent.__class__.__name__)


## PLOTTING ====================================================================
title = dict_string(config)

action_plot (best_actions, file_name+'_action', suptitle, title, labels)
perf_plot   (perfs, file_name+'_perf', suptitle, title, labels)

"""
Module containing the agent classes to solve a Bandit problem.

Complete the code wherever TODO is written.
Do not forget the documentation for every class and method!
An example can be seen on the Bandit_Agent and Random_Agent classes.
"""
# -*- coding: utf-8 -*-
import numpy as np
from utils import my_random_choice
import time

class Bandit_Agent(object):
    """
    Abstract Agent to solve a Bandit problem.

    Contains the methods learn() and act() for the base life cycle of an agent.
    The reset() method reinitializes the agent.
    The minimum requirment to instantiate a child class of Bandit_Agent
    is that it implements the act() method.
    """
    def __init__(self, k:int):
        """
        Simply stores the number of arms of the Bandit problem.
        Parameters
        ----------
        k: positive int
            Number of arms of the Bandit problem.
        """
        assert isinstance(int, k) and k >=0, "Invalid k:{}".format(k)
        self.k = k

    def reset(self):
        """
        Reinitializes the agent to 0 knowledge, good as new.

        No inputs or outputs.
        """
        pass

    def learn(self, a:int, r:float):
        """
        Learning method. The agent learns that action a yielded reward r.
        Parameters
        ----------
        a: positive int < k
            Action that yielded the received reward r.
        r: float
            Reward for having performed action a.
        """

        assert isinstance(int, a) and self.k >= a, "Invalid action: {}".format(a)
        assert isinstance(float, r), "Invalid reward: {}".format(r)
        pass

    def act(self) -> int:
        """
        Agent's method to select a lever (or Bandit) to pull.
        Returns
        -------
        a : positive int < k
            The action the agent chose to perform.
        """
        raise NotImplementedError("Calling act in Abstract class Bandit_Agent")

class Random_Agent(Bandit_Agent):
    """
    This agent doesn't learn, just acts purely randomly.
    """
    def act(self):
        """
        Random action selection.
        Returns
        -------
        a : positive int < k
            A randomly selected action.
        """
        return np.random.randint(self.k)


class EpsGreedy:
    # TODO: implement this class following the formalism above.
    pass


class OptimisticGreedy:
    # TODO: implement this class following the formalism above.
    pass


class Gradient_Bandit:
    # TODO: implement this class following the formalism above.
    pass


class UCB:
    # TODO: implement this class following the formalism above.
    pass

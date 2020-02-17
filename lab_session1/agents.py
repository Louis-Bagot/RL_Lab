"""
Module containing the agent classes to solve a Bandit problem.

Complete the code wherever TODO is written.
Do not forget the documentation for every class and method!
An example can be seen on the Bandit_Agent and Random_Agent classes.
"""
# -*- coding: utf-8 -*-
import numpy as np

class Bandit_Agent(object):
    """
    Abstract Agent to solve a Bandit problem.

    Contains the methods learn() and act() for the base life cycle of an agent.
    The reset() method reinitializes the agent.
    The minimum requirment to instantiate a child class of Bandit_Agent
    is that it implements the act() method.
    """
    def __init__(self, k:int, **kwargs):
        """
        Simply stores the number of arms of the Bandit problem.
        The __init__() method generally handles hyperparameters.
        Parameters
        ----------
        k: positive int
            Number of arms of the Bandit problem.
        kwargs: dictionary
            Additional parameters, ignored.
        """
        assert isinstance(k, int) and k >=0, "Invalid k:{}".format(k)
        self.k = k

    def reset(self):
        """
        Reinitializes the agent to 0 knowledge, good as new.

        No inputs or outputs.
        The reset() method handles variables.
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

        assert isinstance(a, int) and self.k >= a, "Invalid action: {}".format(a)
        assert isinstance(r, float), "Invalid reward: {}".format(r)
        pass

    def act(self) -> int:
        """
        Agent's method to select a lever (or Bandit) to pull.
        Returns
        -------
        a : positive int < k
            The action the agent chose to perform.
        """
        raise NotImplementedError("Calling method act() in Abstract class Bandit_Agent")

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


class EpsGreedy_SampleAverage:
    # TODO: implement this class following the formalism above.
    pass


class EpsGreedy:
    # TODO: implement this class following the formalism above.
    pass


class OptimisticGreedy:
    # TODO: implement this class following the formalism above.
    pass


class UCB:
    # TODO: implement this class following the formalism above.
    pass


class Gradient_Bandit:
    # TODO: implement this class following the formalism above.
    pass

"""
Module containing the k-armed bandit problem
Complete the code wherever TODO is written.
Do not forget the documentation for every class and method!
We expect all classes to follow the Bandit abstract object formalism.
"""
# -*- coding: utf-8 -*-
import numpy as np

class Bandit(object):
    """
    Abstract concept of a Bandit, i.e. Slot Machine, the Agent can pull.

    A Bandit is a distribution over reals.
    The pull() method samples from the distribution to give out a reward.
    """
    def __init__(self, **kwargs):
        """
        Empty for our simple one-armed bandits, without hyperparameters.
        Parameters
        ----------
        **kwargs: dictionary
            Ignored additional inputs.
        """
        pass

    def reset(self):
        """
        Reinitializes the distribution.
        """
        pass

    def pull(self) -> float:
        """
        Returns a sample from the distribution.
        """
        raise NotImplementedError("Calling method pull() in Abstract class Bandit")


class Gaussian_Bandit:
    # TODO: implement this class following the formalism above.
    # Reminder: the Gaussian_Bandit's distribution is a fixed Gaussian.
    pass

class Gaussian_Bandit_NonStat:
    # TODO: implement this class following the formalism above.
    # Reminder: the distribution mean changes each step over time,
    # with increments following N(m=0,std=0.01)
    pass

class KBandit(Bandit):
    """ Set of k Gaussian_Bandits. """
    def __init__(self, k, **kwargs):
        """
        Instantiates the k-armed bandit, with a number of arms, and initializes
        the set of bandits to new gaussian bandits in a bandits list.
        The reset() method is supposedly called from outside.
        Parameters
        ----------
        k: positive int
            Number of arms of the problem.
        """
        self.k = k
        self.bandits = [Gaussian_Bandit() for _ in range(self.k)]

    def reset(self):
        """ Resets each of the k bandits. """
        for bandit in self.bandits:
            bandit.reset()
        self.best_action = np.argmax([bandit.mean for bandit in self.bandits]) # printing purposes

    def pull(self, action:int) -> float:
        """
        Pulls the lever from Bandit #action. Returns the reward.
        Parameters
        ----------
        action: positive int < k
            Lever to pull.
        Returns
        -------
        reward : float
            Reward for pulling this lever.
        """
        return self.bandits[action].pull()


class KBandit_NonStat:
    # TODO: implement this class following the formalism above.
    # Reminder: Same as KBandit, with non stationary Bandits.
    pass

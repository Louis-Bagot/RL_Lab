from utils import assert_not_abstract, str2class
import numpy as np

class Bandit(object):
    """
    Abstract concept of a Bandit, i.e. Slot Machine, the Agent can pull.

    A Bandit is a distribution over reals.
    The pull() method samples from the distribution to give out a reward.
    """
    def __init__(self):
        """
        Simply calls the reset() method.
        """
        self.reset()

    def reset(self):
        """
        Reinitializes the distribution.
        """
        pass

    def pull(self) -> float:
        """
        Returns a sample from the distribution.
        """
        raise NotImplementedError("Calling pull in Abstract class Bandit")

class Gaussian_Bandit:
    # TODO: implement this class following the formalism above.
    # Reminder: the Gaussian_Bandit's distribution is a fixed Gaussian.
    pass

class Gaussian_Bandit_NonStat:
    # TODO: implement this class following the formalism above.
    # Reminder: the distribution mean changes each step over time, with increments following N(m=0,std=0.01)
    pass

class KBandit:
    # TODO: implement this class following the formalism above.
    # Reminder: The k-armed Bandit is a set of k Bandits.
    pass


class KBandit_NonStat:
    # TODO: implement this class following the formalism above.
    # Reminder: Same as KBandit, with non stationary Bandits.
    pass

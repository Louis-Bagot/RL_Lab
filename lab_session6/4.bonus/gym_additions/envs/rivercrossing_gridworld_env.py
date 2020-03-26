import gym
from gym import spaces
import numpy as np

class RiverCrossingEnv(gym.Env):
    """ Small 3x5 Gridworld with a river in the middle row."""
    def __init__(self):
        self.height = 3
        self.width = 5
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Tuple((
                spaces.Discrete(self.height),
                spaces.Discrete(self.width)
                ))
        self.moves = {
                0: (-1, 0),  # up
                1: (0, 1),   # right
                2: (1, 0),   # down
                3: (0, -1),  # left
                }

    def reset(self):
        """
        Resets the environment to the first state of the environment.
        Returns
        -------
        state : State
            First state of the episode.
        """
        # TODO: Implement this
        raise NotImplementedError()
        return state

    def step(self, action):
        """
        Performs a single step of the environment given an action.
        i.e. samples s',r from the p(s',r | s,a) distribution.
        Parameters
        ----------
        action: int
            The action performed by the agent
        Returns
        -------
        next_state : state
            State resulting from the transition
        reward : float
            Reward for this transition
        done : bool
            Whether next_state is a terminal state.
        info : dict
            ignore this
        """
        # TODO: code here
        raise NotImplementedError()
        return next_state, reward, done, info

    def render(self):
        """
        Optional.
        Prints the environment for visualization.
        """
        pass

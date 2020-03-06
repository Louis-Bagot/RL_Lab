import numpy as np
import gym
import random

from gym.envs.registration import register



# code to set a gym config
# 4x4 environment
kwargs = {'map_name': '4x4', 'is_slippery': False}
# 8x8 environment
# kwargs = {'map_name': '8x8', 'is_slippery': False}
register(
    id='FrozenLakeNotSlippery-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs=kwargs,
    max_episode_steps=100,
    reward_threshold=0.8196
)


# code to set environment
env = gym.make("FrozenLakeNotSlippery-v0")

# actions
action_size = env.action_space.n
# statess
state_size = env.observation_space.n


# TODO Declare your q-table based on number of states and actions.

qtable = 


class Agent(object):
    """
    Class declaring the agent. the qtable although handelled
    here gets passed from the Frozenlake.
    """

    def __init__(self, qtable):
        """
        Initialise the Agent.

        Paremeters
        -----------
        qtable: numpy 2d-array
        """
        self.qtable = qtable
        self.learning_rate = 0.1           # Learning rate
        self.gamma = 0.95                  # Discounting rate

        # Exploration parameters
        self.epsilon = 1.0                 # Exploration rate
        self.max_epsilon = 1.0             # Exploration probability at start
        self.min_epsilon = 0.01            # Minimum exploration probability
        self.decay_rate = 0.001             # Exponential decay rate for exploration prob

    def act(self, state, exp_exp_tradeoff):
        """
        Function where agent acts.

        Parameters
        ----------
        state: numpy int64
            current state of the environment

        exp_exp_tradeoff: float
            exploration and exploitation tradeoff

        Returns
        -------
        action: float
            action to take

        """
        # TODO Write code to check if your agent wants to explore or exploit

    def learn(self, state, action, reward, new_state):
        """
        Function to update the q table

        Parameters
        ----------
        state: numpy int64
            current state of the environment

        action: float
            action to update

        reward: int
            reward you get.

        new_state: numpy int64
            new state after action

        """
        #TODO Write code to update q-table

    def update_epsilon(self, episode):
        """
        Function to update the exploration.

        Parameters
        ----------
        episode: int
            episode number

        Returns
        -------
        """
        self.epsilon = self.min_epsilon + \
            (self.max_epsilon - self.min_epsilon) * \
            np.exp(-self.decay_rate*episode)

class Trainer(object):
    """Class to train the agent."""

    def __init__(self, qtable):
        """
        Initilisation of the class to train the agent.

        Parameters
        ----------
        qtable: numpy 2d array

        Returns
        -------

        """
        # config of your run.
        self.total_episodes = 20000        # Total episodes
        self.max_steps = 99                # Max steps per episode

        # q-table
        self.qtable = qtable
        self.agent = Agent(self.qtable)


    def run(self):
        """
        Function to run the environment.

        Parameters
        ----------

        Returns
        -------
        """
        rewards = []

        # number of episodes you want your trainer to run
        for episode in range(self.total_episodes):
            state = env.reset()
            step = 0
            self.done = False
            self.total_rewards = 0

            # Number of steps in each episode
            for step in range(self.max_steps):
                exp_exp_tradeoff = random.uniform(0, 1)

                # take an action
                action = self.agent.act(state, exp_exp_tradeoff)

                # get feedback from environment
                new_state, reward, done, info = env.step(action)

                # update your qtable
                self.agent.learn(
                    state, action, reward, new_state)

                # move your agent to new state
                state = new_state

                # record your reward
                self.total_rewards = self.total_rewards + reward

                # check if you are dead move to next episode
                if done:
                    break

            episode += 1

            # update your exploration rate
            agent.update_epsilon(episode)

            # global reward
            rewards.append(self.total_rewards)

        # print your scores
        print("Score over time: " + str(sum(rewards)/self.total_episodes))

        # print the qtable
        print(self.agent.qtable)

        # printing epsilon
        print(self.agent.epsilon)

        return self.qtable


def test():
    """Function to test your agent."""
    for episode in range(5):
        state = env.reset()
        print(type(state))
        step = 0
        done = False
        print("*****************************")
        print("EPISODE ", episode)
        for step in range(99):
            env.render()
            # Take the action (index) that have the maximum expected future reward given that state
            action = np.argmax(qtable[state, :])
            print(action)
            new_state, reward, done, info = env.step(action)
            print(reward)
            if done:
                print('\n \x1b[6;30;42m' + 'Success!' + '\x1b[0m')
                action = np.argmax(qtable[state, :])
                print(action)
                env.render()
                break
            state = new_state
    env.close()


if __name__ == '__main__':
    # Declare your trainer
    trainer = Trainer(qtable)

    # train your agent
    qtable = trainer.run()

    # reset environment and test
    env.reset()
    env.render()
    if kwargs['map_name'] == '4x4':
        print(np.argmax(qtable, axis=1).reshape(4, 4))
    elif kwargs['map_name'] == '8x8':
        print(np.argmax(qtable, axis=1).reshape(8, 8))
    test()

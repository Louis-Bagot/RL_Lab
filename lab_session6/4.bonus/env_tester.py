import gym
import gym_additions
import numpy as np
np.random.seed(0)

class Random_Agent(object):
    """ Random Agent for a RL problem"""

    def __init__(self, k):
        super(Random_Agent, self).__init__()
        self.k = k # number of actions

    def act(self, obs):
        return np.random.randint(self.k)

# Preparing environment
env = gym.make('RiverCrossingEnv-v0')

# Preparing agent
agent = Random_Agent(env.action_space.n)

# Setup
n_episodes = 1
n_steps = 20000 # virtually never

# Main loop
rewards_history = np.empty(n_episodes)
for ep in range(n_episodes):
    obs = env.reset()
    cumreward = 0
    for step in range(n_steps):
        env.render() # optional method
        action = agent.act(obs)
        print("\tAction is {} in state {}".format(action, obs))
        obs, reward, done, info = env.step(action)
        cumreward += reward

        if done:
            env.render() # optional method
            print("Episode finished after {} timesteps"
                  " with cumulated reward {}".format(step+1, cumreward))
            break
    rewards_history[ep] = cumreward
env.close()

# Printing
print("Average reward: {}".format(rewards_history.mean()))

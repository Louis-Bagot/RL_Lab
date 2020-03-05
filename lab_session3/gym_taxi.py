"""
This is a example code of gym and test your virtual env.
Action Space Discrete(6)
State Space Discrete(500)
The filled square represents the taxi, which is yellow without a passenger and green with a passenger.
The pipe ("|") represents a wall which the taxi cannot cross.
R, G, Y, B are the possible pickup and destination locations. The blue letter represents the current passenger pick-up location, and the purple letter is the current destination

Actions
-------
0 = south
1 = north
2 = east
3 = west
4 = pickup
5 = dropoff
"""

import gym
from IPython.display import clear_output
from time import sleep
env = gym.make("Taxi-v2")
env.render()
env.reset()

"""
We'll create an infinite loop which runs until one passenger reaches 
one destination (one episode), or in other words, when the received reward is 20.
The env.action_space.sample() method automatically selects one random action 
from set of all possible actions.
"""

env.s = 328  # set environment to illustration's state

epochs = 0
penalties, reward = 0, 0

frames = [] # for animation

done = False

while not done:
    action = env.action_space.sample() # returns a random action(0-5)
    new_state, reward, done, info = env.step(action) # take the action and get reward and next state

    if reward == -10:
        penalties += 1
    
    # Put each rendered frame into dict for animation
    frames.append({
        'frame': env.render(mode='ansi'),
        'state': new_state,
        'action': action,
        'reward': reward
		}
    )

    epochs += 1


print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))


def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'].getvalue())
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)

print_frames(frames)

# This is a sample script to show the gym functionality
import gym

env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    new_state, reward, done, info = env.step(env.action_space.sample())
    if done:
        env.reset()
print("number of actions possible are :-",env.action_space.n)

env.close()

env = gym.make('Acrobot-v1')
env.reset()
for _ in range(500):
    env.render()
    new_state, reward, done, info = env.step(env.action_space.sample())
    if done:
        env.reset()
print("number of actions possible are :-",env.action_space.n)
env.close()

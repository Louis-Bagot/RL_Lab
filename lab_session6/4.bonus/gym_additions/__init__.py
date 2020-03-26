from gym.envs.registration import register
# Different versions allow you to change the init method
register(
    id='RiverCrossingEnv-v0',
    entry_point='gym_additions.envs:RiverCrossingEnv',
    )

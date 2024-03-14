import gymnasium as gym
import pytest

from metastable_baselines2 import PPO

@pytest.mark.parametrize("env_id", ["LunarLanderContinuous-v2", "MountainCarContinuous-v0"])
def test_trpl(env_id):
    model = PPO("MlpPolicy", env_id, n_steps=128, seed=0, policy_kwargs=dict(net_arch=[16]), verbose=1)
    model.learn(total_timesteps=500)
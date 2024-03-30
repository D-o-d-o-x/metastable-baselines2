import gymnasium as gym
import pytest

from metastable_baselines2 import PPO

@pytest.mark.parametrize("env_id", ["LunarLanderContinuous-v2", "MountainCarContinuous-v0"])
def test_trpl(env_id):
    model = PPO("MlpPolicy", env_id, n_steps=128, seed=0, policy_kwargs=dict(net_arch=[16]), verbose=1)
    model.learn(total_timesteps=500)

@pytest.mark.parametrize("env_id", ["LunarLanderContinuous-v2"])
@pytest.mark.parametrize("par_strength", ['DIAG', 'FULL', 'CONT_DIAG', 'CONT_FULL'])
def test_ppo_pca(env_id, par_strength):
    model = PPO("MlpPolicy", env_id, n_steps=128, seed=0, use_pca=True, policy_kwargs=dict(net_arch=[16], dist_kwargs={'par_strength': par_strength, 'skip_conditioning': True}), verbose=1)
    model.learn(total_timesteps=100)

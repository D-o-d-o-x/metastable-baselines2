import gymnasium as gym
import pytest

from metastable_baselines2 import TRPL

PROJECTIONS = ["Frobenius", "Wasserstein"] #, "KL"]

@pytest.mark.parametrize("env_id", ["LunarLanderContinuous-v2", "MountainCarContinuous-v0"])
@pytest.mark.parametrize("projection", PROJECTIONS)
def test_trpl(env_id, projection):
    model = TRPL("MlpPolicy", env_id, n_steps=128, seed=0, policy_kwargs=dict(net_arch=[16]), projection_class=projection, verbose=1)
    model.learn(total_timesteps=500)

@pytest.mark.parametrize("env_id", ["LunarLanderContinuous-v2"])
@pytest.mark.parametrize("projection", PROJECTIONS)
@pytest.mark.parametrize("mean_bound", [0.03, 0.06])
@pytest.mark.parametrize("cov_bound", [1.0e-3, 2.0e-3])
def test_trpl_params(env_id, projection, mean_bound, cov_bound):
    model = TRPL("MlpPolicy", env_id, n_steps=128, seed=0, policy_kwargs=dict(net_arch=[16]), projection_class=projection, projection_kwargs={'mean_bound': mean_bound, 'cov_bound': cov_bound}, verbose=1)
    model.learn(total_timesteps=100)

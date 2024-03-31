# Metastable Baselines 2

<p align='center'>
  <img src='./icon.svg'>
</p>

An extension to Stable Baselines 3. Based on Metastable Baselines 1.

This repo provides:

- An implementation of ["Differentiable Trust Region Layers for Deep Reinforcement Learning" by Fabian Otto et al. (TRPL)](https://arxiv.org/abs/2101.09207)
- Support for Contextual Covariances (via PCA)
- Support for Full Covariances (via PCA)

## Installation

#### Install dependency: Metastable Projections

Follow instructions for the [Metastable Projections](https://git.dominik-roth.eu/dodox/metastable-projections) ([GitHub Mirror](https://github.com/D-o-d-o-x/metastable-projections)).
KL Projections require ALR's ITPAL as an additional dependecy.

#### Install as a package

Then install this repo as a package:

```bash
pip install -e .
```

If you want to be able to use full / contextual covariances, install with the optional dependency 'pca':
```bash
pip install -e '.[pca]'
```
## Usage

### TRPL

TRPL can be used just like SB3's PPO:

```python
import gymnasium as gym
from metastable_baselines2 import TRPL

env_id = 'LunarLanderContinuous-v2'
projection = 'Wasserstein' # or Frobenius or KL

model = TRPL("MlpPolicy", env_id, n_steps=128, seed=0, policy_kwargs=dict(net_arch=[16]), projection_class=projection, verbose=1)

model.learn(total_timesteps=100)
```

Configure TRPL py passing `projection_kwargs` to TRPL:

```python
model = TRPL("MlpPolicy", env_id, n_steps=128, seed=0, policy_kwargs=dict(net_arch=[16]), projection_class=projection, projection_kwargs={'mean_bound': mean_bound, 'cov_bound': cov_bound}, verbose=1)
```

For avaible projection_kwargs have a look at [Metastable Projections](https://git.dominik-roth.eu/dodox/metastable-projections).

### Full Covariance

SB3 does not support full covariances (only diagonal). We still provide support for full covariances via the seperate PCA package. (But since we don't actually want to use PCA ('Prior Conditioned Annealing'), we pass 'skip_conditioning=True'; this will lead to the underlying Noise being used directly.)

We therefore pass `use_pca=True` and `policy_kwargs.dist_kwargs = {'Base_Noise': 'WHITE', par_strength: 'FULL', skip_conditioning=True}`

```python
# We support PPO and TRPL, (SAC is untested, we are open to PRs fixing issues)
model = TRPL("MlpPolicy", env_id, n_steps=128, seed=0, policy_kwargs=dict(net_arch=[16], ), projection_class=projection, verbose=1)

model.learn(total_timesteps=100)
```

The supportted values for `par_strength` are:

​    SCALAR: We only learn a single scalar value, that is used along the whole diagonal. No covariance is modeled.

​    DIAG: We learn a diagonal covariance matrix. (e.g. only variances).

​    FULL: We learn a full covariance matrix, induced via cholesky decomp.

​    CONT_SCALAR: Same as SCALAR, but the scalar is not global, it is parameterized by the policy net.

​    CONT_DIAG: Same as DIAG, but the values are not global, they are parameterized by the policy net.

​    CONT_HYBRID: We learn a parameric diagonal, that is scaled by the policy net.

​    CONT_FULL: Same as FULL, but parameterized by the policy net.

## License

Since this Repo is an extension to [Stable Baselines 3 by DLR-RM](https://github.com/DLR-RM/stable-baselines3), it contains some of it's code. SB3 is licensed under the [MIT-License](https://github.com/DLR-RM/stable-baselines3/blob/master/LICENSE).

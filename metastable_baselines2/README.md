# Metastable Baselines 2

<p align='center'>
  <img src='./icon.svg'>
</p>

An extension to Stable Baselines 3. Based on Metastable Baselines 1.

This repo provides:

- An implementation of ["Differentiable Trust Region Layers for Deep Reinforcement Learning" by Fabian Otto et al. (TRPL)](https://arxiv.org/abs/2101.09207)
- Support for Prior Conditioned Annealing (WIP)
- Support for Contextual Covariances (Planned)
- Support for Full Covariances (Planned)

The resulting algorithms can than be tested for their ability of exploration in the enviroments provided by [Fancy Gym](https://github.com/ALRhub/fancy_gym) or [Project Columbus](https://git.dominik-roth.eu/dodox/Columbus)

## Installation

#### Install dependency: Metastable Projections

Follow instructions for the [Metastable Projections](https://git.dominik-roth.eu/dodox/metastable-projections) ([GitHub Mirror](https://github.com/D-o-d-o-x/metastable-projections)).
KL Projections require ALR's ITPAL as an additional dependecy.

#### Install as a package

Then install this repo as a package:

```
pip install -e .
```

## Usage

TRPL can be used just like SB3's PPO:

```
import gymnasium as gym
from metastable_baselines2 import TRPL

projection = 'Wasserstein' # or Frobenius or KL

model = TRPL("MlpPolicy", env_id, n_steps=128, seed=0, policy_kwargs=dict(net_arch=[16]), projection_class=projection, projection_kwargs={'mean_bound': mean_bound, 'cov_bound': cov_bound}, verbose=1)

model.learn(total_timesteps=100)
```

For avaible projection_kwargs have a look at [Metastable Projections](https://git.dominik-roth.eu/dodox/metastable-projections).

## License

Since this Repo is an extension to [Stable Baselines 3 by DLR-RM](https://github.com/DLR-RM/stable-baselines3), it contains some of it's code. SB3 is licensed under the [MIT-License](https://github.com/DLR-RM/stable-baselines3/blob/master/LICENSE).

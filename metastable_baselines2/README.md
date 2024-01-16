# Metastable Baselines 2

<p align='center'>
  <img src='./icon.svg'>
</p>

An extension to Stable Baselines 3. Based on Metastable Baselines 1.

During training of a RL-Agent we follow the gradient of the loss, which leads us to a minimum. In cases where the found minimum is merely a local minimum, this can be seen as a _false vacuum_ in our loss space. Exploration mechanisms try to let our training procedure escape these _stable states_: Making them _metastable_.

In order to archive this, this Repo contains some extensions for [Stable Baselines 3 by DLR-RM](https://github.com/DLR-RM/stable-baselines3)  
These extensions include:

- An implementation of ["Differentiable Trust Region Layers for Deep Reinforcement Learning" by Fabian Otto et al. (TRPL)](https://arxiv.org/abs/2101.09207)
- Support for Prior Conditioned Annealing
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

## License

Since this Repo is an extension to [Stable Baselines 3 by DLR-RM](https://github.com/DLR-RM/stable-baselines3), it contains some of it's code. SB3 is licensed under the [MIT-License](https://github.com/DLR-RM/stable-baselines3/blob/master/LICENSE).

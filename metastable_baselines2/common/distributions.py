from stable_baselines3.common.distributions import *
from metastable_baselines2.common.pca import PCA_Distribution

def _patched_make_proba_distribution(
    action_space: spaces.Space, n_envs: int = 1, use_sde: bool = False, use_pca: bool = False, dist_kwargs: Optional[Dict[str, Any]] = None
) -> Distribution:
    """
    Return an instance of Distribution for the correct type of action space

    :param action_space: the input action space
    :param use_sde: Force the use of StateDependentNoiseDistribution
        instead of DiagGaussianDistribution
    :param dist_kwargs: Keyword arguments to pass to the probability distribution
    :return: the appropriate Distribution object
    """

    assert not (use_sde and use_pca), 'Can not mix sde and pca!'

    if dist_kwargs is None:
        dist_kwargs = {}

    if isinstance(action_space, spaces.Box):
        if use_sde:
            cls = StateDependentNoiseDistribution
        elif use_pca:
            cls = PCA_Distribution
        else:
            cls = DiagGaussianDistribution
        return cls(get_action_dim(action_space), n_envs=n_envs, **dist_kwargs)
    elif isinstance(action_space, spaces.Discrete):
        return CategoricalDistribution(action_space.n, **dist_kwargs)
    elif isinstance(action_space, spaces.MultiDiscrete):
        return MultiCategoricalDistribution(list(action_space.nvec), **dist_kwargs)
    elif isinstance(action_space, spaces.MultiBinary):
        return BernoulliDistribution(action_space.n, **dist_kwargs)
    else:
        raise NotImplementedError(
            "Error: probability distribution, not implemented for action space"
            f"of type {type(action_space)}."
            " Must be of type Gym Spaces: Box, Discrete, MultiDiscrete or MultiBinary."
        )


_orig_make_propa_distribution, make_proba_distribution = make_proba_distribution, _patched_make_proba_distribution

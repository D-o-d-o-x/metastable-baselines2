from sbBrix.ppo import PPO
from sbBrix.sac import SAC

try:
    import priorConditionedAnnealing as pca
except ModuleNotFoundError:
    class pca():
        def PCA_Distribution(*args, **kwargs):
            raise Exception('PCA is not installed; cannot initialize PCA_Distribution.')

__all__ = [
    "PPO",
    "SAC",
]

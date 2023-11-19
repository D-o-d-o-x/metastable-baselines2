try:
    from priorConditionedAnnealing import PCA_Distribution
except ModuleNotFoundError:
    def PCA_Distribution(*args, **kwargs):
        raise Exception('PCA is not installed; cannot initialize PCA_Distribution.')
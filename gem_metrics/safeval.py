#!/usr/bin/env python3

from .metric import SourcedMetric
import numpy as np
from safeval.safeval_metric import QG_policy_scorer


class SAFEval(SourcedMetric):
    def __init__(self):
        # TODO: need to define default values
        self.metric = QG_policy_scorer(isCuda=True, qg_beam_size=1)

    def compute(self, predictions, sources):
        # TODO: need to use batched computation from safeval
        scores = [
            self.metric.compute_all(p, s)
            for p, s in zip(predictions.untokenized, sources.untokenized)
        ]
        return {'safeval': np.mean(scores)}

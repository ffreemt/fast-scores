"""Calculate fast_scores."""
from typing import List, Optional

import sklearn
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from logzero import logger

from fast_scores.cos_matrix2 import cos_matrix2
from fast_scores.gen_model import gen_model


# fmt: off
def fast_scores(
        text1: List[str],
        text2: List[str],
        model: Optional[TfidfVectorizer] = None,
        dot: bool = True,
        max_features: int = 1000,
) -> np.ndarray:
    # fmt: on
    """Calculate fast_scores.

    Args:
        text1: chinese text
        text2: chinese text
        max_features: used when model is None

    Returns:
        correlation matrix (float)
    """
    # logger.debug(" entry ")

    # create model on the fly
    if model is None:
        logger.debug("No model provided, creating one on the fly")

        try:
            # model = TfidfVectorizer().fit(text1 + text2)
            # or to make pyright happy
            model1 = gen_model(text1 + text2, max_features=max_features)
        except Exception:
            logger.exceptio("gen_model: ")
            raise

        logger.debug("Done creating model")
        # shake 10000x10000 ~7s-16s
    else:
        model1 = model

    # model = _

    vec1 = model1.transform(text1)  # scipy.sparse.csr.csr_matrix
    vec2 = model1.transform(text2)

    # supposed to be much faster
    if dot:
        return vec1.dot(vec2.T).toarray().T
    # shake 10000x11000 41.1 s ± 15.5 s
    # shake 5000x5100 11s
    # shake 2000x2100 3.7s
    # shake 1000x1100 2.1s
    # shake 10000x10100 3min 1min 13s
    # comfort zone length: j = math.sqrt(psutil.virtual_memory().available/64)
    # estimated time: j / 1000 * 2 s

    return cos_matrix2(vec1.toarray(), vec2.toarray()).T
    # shake 1000x1100 11s 21s
    # shake 2000x2100 45s
    # shake 10000x10000

import logging

import torch
import torch.utils.data

logger = logging.getLogger(__name__)


def _get_pytorch_version():
    version = torch.__version__
    major, minor = [int(x) for x in version.split(".")[:2]]
    return major, minor


MAJOR, MINOR = _get_pytorch_version()

if MINOR > 1:
    SingleProcessDataLoaderIter = (
        torch.utils.data.dataloader._SingleProcessDataLoaderIter
    )
    MultiProcessingDataLoaderIter = (
        torch.utils.data.dataloader._MultiProcessingDataLoaderIter
    )
else:
    SingleProcessDataLoaderIter = torch.utils.data.dataloader._DataLoaderIter
    MultiProcessingDataLoaderIter = torch.utils.data.dataloader._DataLoaderIter


from nonechucks.dataloader import SafeDataLoader
from nonechucks.dataset import SafeDataset
from nonechucks.sampler import SafeSampler

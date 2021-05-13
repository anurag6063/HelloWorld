import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init as weight_init
import matplotlib.pyplot as plt
import numpy as np
import random

from torch.utils.data import Subset
from torch.utils.data import Dataset

class FashionMNIST(Dataset):
    """
    Dataset class to load the EMNIST dataset
    """
    def __init__(self, split='train', frac=1.0):
        """
        split (str): training or test split
        frac (float): fraction of dataset to load. ['train', 'test']
        """
        self.frac = frac
        self.split = split
        dset = self.__process_dataset()
        self.dset = dset
        
        
    def __process_dataset(self):
        assert self.split == 'train' or self.split == 'test', 'Invalid split'
        
        if self.split == 'train':
            assert self.frac > 0 and self.frac <= 1.0, 'enter frac: a number in the range (0,1]'
            #Loading the train set file and select a fraction of the training data
            orig_dataset = dsets.FashionMNIST(root='../data',
                                        train=True,
                                        transform=transforms.ToTensor(),
                                        download=True)
            length = len(orig_dataset)        # Compute the size of the dataset
            inds = np.arange(0, length)       # Create a dummy index array
            random.shuffle(inds)              # Shuffle the index array
            sel_inds = inds[:round(self.frac*length)]    # select a fraction of indexes
            new_set = Subset(orig_dataset, sel_inds)    # create a new dataset with the selected indexes
            return new_set
        else:
            #Loading the test set file
            orig_dataset = dsets.FashionMNIST(root='../data',
                                        train=False,
                                        transform=transforms.ToTensor(),
                                        download=True)
            return orig_dataset
    
    
    def __len__(self):
        return len(self.dset)
    
    
    def __getitem__(self, index):
        return self.dset[index]
        
            
        
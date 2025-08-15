import heapq
import numpy as np

class popitem_pathmetric_dataprocessor:
    def __init__(self, remotebranch, lr_twdd, localcircuit):
        # Initialize with the given data
        self.remotebranch = remotebranch
        self.lr_twdd = lr_twdd
        self.localcircuit = localcircuit
        self._resd = []

    def process_data(self):
        # Clear the _resd list
        self._resd.clear()

        # Zip the three lists into tuples and store them in _resd
        _edge_data = zip(self.remotebranch, self.lr_twdd, self.localcircuit)
        self._resd = list(_edge_data)  # Convert to a list

    def optimize_lr_twdd(self):
        # Filter elements in lr_twdd that are greater than 1, without copying
        self.lr_twdd = list(filter(lambda x: x > 1, self.lr_twdd))

        # Convert the filtered list into a heap
        heapq.heapify(self.lr_twdd)

    def get_resd(self):
        # Return the processed result
        return self._resd

    def get_heapified_lr_twdd(self):
        # Return the heapified lr_twdd
        return self.lr_twdd


class popitem_pathmetric_edgedataprocessor:
    def __init__(self, remotebranch, lr_twd, localcircuit):
        # Initialize with the given data
        self.remotebranch = remotebranch
        self.lr_twd = lr_twd
        self.localcircuit = localcircuit
        self.edge_data = []
        self.lr_twdd_ = []

    def process_data(self):
        # Modify lr_twd with random values added, rounded to 2 decimals
        self.lr_twdd_ = [round(float(twd) + np.random.rand(), 2) for twd in self.lr_twd]

        # Zip the three lists into tuples (remotebranch, lr_twd_, localcircuit)
        self.edge_data = list(zip(self.remotebranch, self.lr_twdd_, self.localcircuit))

    def optimize_edge_data(self):
        # Filter out tuples where the second element (lr_twd_) is <= 1
        self.edge_data = list(filter(lambda x: x[1] > 1, self.edge_data))

    def get_edge_data(self):
        # Return the filtered edge data
        return self.edge_data

    def get_lr_twdd(self):
        return self.lr_twdd_
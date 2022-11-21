from config.base_config import BaseConfig

class GMAN_config(BaseConfig):
    def __init__(self, device, dataset_dir, dataset_name, train_ratio, test_ratio):
        # Data, Train
        super().__init__(device, dataset_dir, dataset_name, train_ratio, test_ratio)

        self.L = 1
        self.K = 8
        self.d = 8
        self.SE = None # TODO
        self.num_his = 12
        self.bn_decay = 0.1
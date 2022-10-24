'''This is the repo which contains the original code to the WACV 2021 paper
"Same Same But DifferNet: Semi-Supervised Defect Detection with Normalizing Flows"
by Marco Rudolph, Bastian Wandt and Bodo Rosenhahn.
For further information contact Marco Rudolph (rudolph@tnt.uni-hannover.de)'''

import config as c
from train import train
from utils import load_datasets, make_dataloaders
import logging_controller
from datetime import datetime

start_time = datetime.now()
print(f"start at {start_time.strftime('%Y-%m-%d_%H-%M-%S')}")
train_set, test_set = load_datasets(c.dataset_path, c.class_name)
train_loader, test_loader = make_dataloaders(train_set, test_set)
model = train(train_loader, test_loader)
end_time = datetime.now()
print(f"end at {end_time.strftime('%Y-%m-%d_%H-%M-%S')}")
print(f"It took {end_time - start_time} to complete.")

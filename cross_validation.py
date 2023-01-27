import main
import config as c
from sklearn.model_selection import KFold
from pathlib import Path as p
import shutil

class DataInDirectory:
    def __init__(self, path:p, label:int, group=None):
        self.path = path
    def transfer(self, dst:p):
        shutil.copy(self.path, dst)

def make_differnet_dataset(original_dataset_path, n_splits):
    original_dataset_path = p(original_dataset_path)
    anomaly_flag = []
    for d in original_dataset_path.iterdir():
        if d.is_dir():
            is_anomaly = input(f"Which of the folloing type is directory '{d.name}'?\n0. normal\n1. anomaly\n2. unused\n")
            assert is_anomaly == "0" or is_anomaly == "1" or is_anomaly == "2", "Please input 0, 1 or 2"
            anomaly_flag.append(int(is_anomaly))

    anomaly_class = []
    normal_class = []
    for f, d in zip(anomaly_flag, original_dataset_path.iterdir()):
        if f == 1:
            for f in d.iterdir():
                data = DataInDirectory(f, 1)
                anomaly_class.append(data)
        elif f == 0:
            for f in d.iterdir():
                data = DataInDirectory(f, 0)
                normal_class.append(data)

    kf = KFold(n_splits=n_splits, shuffle=True, random_state=c.seed)
    new_directory_name = "dataset_for_differnet_crossval"
    c.dataset_path = original_dataset_path.parent / new_directory_name / "dataset"
    directory_anomaly = c.dataset_path / r"class\test\anomaly"
    directory_anomaly.mkdir(parents=True, exist_ok=True)
    directory_normal_train = c.dataset_path / r"class\train\good"
    directory_normal_test = c.dataset_path / r"class\test\good"

    for anomaly_data in anomaly_class:
        anomaly_data.transfer(directory_anomaly)

    for i, (train, test) in enumerate(kf.split(normal_class)):
        shutil.rmtree(directory_normal_train, ignore_errors=True)
        shutil.rmtree(directory_normal_test, ignore_errors=True)
        directory_normal_train.mkdir(parents=True, exist_ok=True)
        directory_normal_test.mkdir(parents=True, exist_ok=True)
        for index in train:
            normal_class[index].transfer(directory_normal_train)
        for index in test:
            normal_class[index].transfer(directory_normal_test)
        
        main.main()

        if i > 10:
            break

if __name__ == "__main__":
    org_dataset = r"C:\Users\nktlab\Desktop\experiment\fujisawa\dataset"
    make_differnet_dataset(org_dataset, 24)

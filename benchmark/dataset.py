import os
import shutil
import tarfile
import urllib.request
from dataclasses import dataclass
from typing import Optional
import sys

sys.path.append('..')  # 解决控制台执行找不到 module 的问题

from benchmark import DATASETS_DIR
from dataset_reader.ann_h5_reader import AnnH5Reader
from dataset_reader.base_reader import BaseReader
from dataset_reader.json_reader import JSONReader


@dataclass
class DatasetConfig:
    """
    数据集配置
    """
    vector_size: int  # 向量维数
    distance: str  # cosine、l2
    name: str  # 数据集名称
    type: str  # h5 or jsonl
    path: str  # 文件位置
    link: Optional[str] = None  # link


READER_TYPE = {"h5": AnnH5Reader, "jsonl": JSONReader}


class Dataset:
    def __init__(self, config: dict):
        self.config = DatasetConfig(**config)
        print("init {}".format(self.config))

    def download(self):
        """
        下载并解压
        """
        target_path = DATASETS_DIR / self.config.path

        if target_path.exists():
            print(f"{target_path} already exists")
            return

        if self.config.link:
            print(f"Downloading {self.config.link}...")
            tmp_path, _ = urllib.request.urlretrieve(self.config.link)

            if tmp_path.endswith(".tgz") or tmp_path.endswith(".tar.gz"):
                print(f"Extracting: {tmp_path} -> {target_path}")
                (DATASETS_DIR / self.config.path).mkdir(exist_ok=True)
                file = tarfile.open(tmp_path)
                file.extractall(target_path)
                file.close()
                os.remove(tmp_path)
            else:
                print(f"Moving: {tmp_path} -> {target_path}")
                (DATASETS_DIR / self.config.path).parent.mkdir(exist_ok=True)
                shutil.copy2(tmp_path, target_path)
                os.remove(tmp_path)

    def get_reader(self, normalize: bool) -> BaseReader:
        """
        获得读取数据集的对象 /n
        Args:
            normalize: 归一化
        Returns: BaseReader
        """
        reader_class = READER_TYPE[self.config.type]
        return reader_class(DATASETS_DIR / self.config.path, normalize=normalize)

# if __name__ == "__main__":
#     dataset = Dataset(
#         {
#             "name": "glove-25-angular",
#             "vector_size": 25,
#             "distance": "Cosine",
#             "type": "h5",
#             "path": "glove-25-angular/glove-25-angular.hdf5",
#             "link": "http://ann-benchmarks.com/glove-25-angular.hdf5",
#         }
#     )

# 下载所有的数据集
# dataset = read_dataset_config()
# for ds in dataset.keys():
#     dataset_config = dataset[ds]
#     print(dataset_config)
#     dataset_manager = Dataset(dataset_config)
#     dataset_manager.download()
#     print("fini-sh---")

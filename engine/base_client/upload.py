import time
from multiprocessing import get_context
from typing import Iterable, List, Optional, Tuple

import tqdm

from dataset_reader.base_reader import Record
from engine.base_client.utils import iter_batches


class BaseUploader:
    client = None

    # connection_params 和 upload_params 均为字典类型
    def __init__(self, host, connection_params, upload_params):
        self.host = host
        self.connection_params = connection_params
        self.upload_params = upload_params

    @classmethod
    def get_mp_start_method(cls):
        return None

    @classmethod
    def init_client(cls, host, distance, connection_params: dict, upload_params: dict):
        raise NotImplementedError()

    def upload(
        self,
        distance,
        records: Iterable[Record],
    ) -> dict:
        latencies = []
        start = time.perf_counter()
        parallel = self.upload_params.pop("parallel", 1)
        batch_size = self.upload_params.pop("batch_size", 64)

        print("base upload, parallel {}, batch size is {}, upload params dict is {}".format(
            parallel,
            batch_size,
            self.upload_params
        ))
        self.init_client(
            self.host, distance, self.connection_params, self.upload_params
        )

        if parallel == 1:
            # 每次只会取 batch_size 的数据进行上传，通过 yield 继续读取下一次 batch
            for batch in iter_batches(tqdm.tqdm(records), batch_size):
                latencies.append(self._upload_batch(batch))
        else:
            # 并发上传
            ctx = get_context(self.get_mp_start_method())
            with ctx.Pool(
                processes=int(parallel),
                initializer=self.__class__.init_client,
                initargs=(
                    self.host,
                    distance,
                    self.connection_params,
                    self.upload_params,
                ),
            ) as pool:
                latencies = list(
                    pool.imap(
                        self.__class__._upload_batch,
                        iter_batches(tqdm.tqdm(records), batch_size),
                    )
                )

        upload_time = time.perf_counter() - start

        print("Upload time consume: {}".format(upload_time))

        print("after upload finished, post upload will create index, distance is {}".format(distance))
        post_upload_stats = self.post_upload(distance)

        total_time = time.perf_counter() - start

        return {
            "post_upload": post_upload_stats,
            "upload_time": upload_time,
            "total_time": total_time,
            "latencies": latencies,
        }

    # 上传 ids, vectors, metadata 并返回时间花费
    @classmethod
    def _upload_batch(
        cls, batch: Tuple[List[int], List[list], List[Optional[dict]]]
    ) -> float:
        ids, vectors, metadata = batch
        start = time.perf_counter()
        cls.upload_batch(ids, vectors, metadata)
        return time.perf_counter() - start

    @classmethod
    def post_upload(cls, distance):
        return {}

    @classmethod
    def upload_batch(
        cls, ids: List[int], vectors: List[list], metadata: List[Optional[dict]]
    ):
        raise NotImplementedError()

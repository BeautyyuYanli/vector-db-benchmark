from msgspec import Struct, field, to_builtins
from typing import (
    List,
)
import itertools
import json
import argparse


class ConnectionParam(Struct, kw_only=True):
    host: str = "localhost"
    port: int = 5432
    user: str = "root"
    password: str = "123456"


class SearchParam(Struct, kw_only=True):
    parallel: int
    top: int
    params: dict


class UploadParam(Struct, kw_only=True):
    parallel: int = 16
    batch_size: int = 64
    index_params: dict
    index_type: str
    engine_type: str = "rust"


class EngineParam(Struct, kw_only=True):
    name: str
    result_group: str = "single_search"
    engine: str
    platform: str = "unknown"
    index_type: str
    dataset: str = "laion-768-1m-ip"
    version: str
    branch: str = "unknown"
    commit: str = "unknown"
    remark: str
    other: str = "none"
    link: str = "https://github.com/tensorchord/pgvecto.rs"
    connection_params: ConnectionParam = field(default_factory=ConnectionParam)
    collection_params: dict = field(default_factory=dict)
    search_params: List[SearchParam]
    upload_params: UploadParam


SEARCH_PARALLEL = [16]
SEARCH_TOP = [10]
SEARCH_PARAMS = [
    {"vectors.hnsw_ef_search": 8},
    {"vectors.hnsw_ef_search": 16},
    {"vectors.hnsw_ef_search": 32},
    {"vectors.hnsw_ef_search": 64},
    {"vectors.hnsw_ef_search": 128},
    {"vectors.hnsw_ef_search": 256},
    {"vectors.hnsw_ef_search": 512},
]
INDEX_PARAMS = [
    (
        "hnsw",
        { "indexing": { "hnsw": { }  } }
    ),
    # (
    #     "flat",
    #     { "indexing": {"flat": {}}  }
    # ),
    # (
    #     "ivf",
    #     { "indexing": {"ivf": {}}  }
    # )
]


def generate(version: str):
    return [
        EngineParam(
            name=f"pgvecto.rs-{version}-{index_params[0]}",
            remark=f"pgvecto.rs-{version}-{index_params[0]}",
            engine="pgvector",
            index_type=index_params[0],
            version=version,
            search_params=[
                SearchParam(
                    parallel=search_parallel,
                    top=search_top,
                    params=search_params,
                )
                for search_parallel, search_top, search_params in itertools.product(
                    SEARCH_PARALLEL, SEARCH_TOP, SEARCH_PARAMS
                )
            ],
            upload_params=UploadParam(
                index_params=index_params[1],
                index_type=index_params[0],
            ),
        )
        for index_params in INDEX_PARAMS
    ]


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--version", type=str)
args = arg_parser.parse_args()
version = args.version

with open(f"experiments/configurations/pgvecto.rs-{version}.json", "w") as f:
    json.dump(
        [to_builtins(engine) for engine in generate(version)],
        f,
        indent=4,
    )

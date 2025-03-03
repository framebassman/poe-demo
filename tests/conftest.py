import logging
import sys
from fileinput import filename
from logging import Logger
import pytest

@pytest.fixture(scope="session")
def logger(pytestconfig, worker_id) -> Logger:
    if worker_id is not None:
        logging.basicConfig(
            format="%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)",
            level="INFO",
            # stream=sys.stdout
            filename=f'pytest_{worker_id}.log'
        )
    return logging.getLogger()

from hamcrest import assert_that, equal_to
from datetime import datetime, timedelta
import time


class TestThread2:
    def test_it_works(self, logger):
        logger.info("Start TestThread2 logs")
        time.sleep(timedelta(seconds=10).total_seconds())
        logger.info("Finish TestThread2 logs")
        assert_that(1, equal_to(1))

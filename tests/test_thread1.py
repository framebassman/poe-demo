from hamcrest import assert_that, equal_to
from datetime import datetime, timedelta
import time


class TestThread1:
    def test_it_works(self, logger):
        logger.info("Start TestThread1 logs")
        time.sleep(timedelta(seconds=10).total_seconds())
        logger.info("Finish TestThread1 logs")
        assert_that(1, equal_to(1))

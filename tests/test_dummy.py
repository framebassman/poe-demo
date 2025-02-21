from hamcrest import equal_to, assert_that


class TestDummy():
    def test_it_works(self):
        assert_that(1, equal_to(1))

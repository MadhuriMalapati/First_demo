import pytest
@pytest.mark.usefixtures("datalaod")
@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixturedemo(self,datalaod):
        print("data is ",datalaod)
        print("/n this indicates the fixtre demo")

    def test_anotherfixturedemo(self):
        print("/n this indicates the another fixtre demo")

    def test_thirdfixturedemo(self,crossbrowser):
        print("Pring the browsers",crossbrowser)

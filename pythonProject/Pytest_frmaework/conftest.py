import pytest


@pytest.fixture(scope='class')
def setup():
    print("Program Started")
    yield
    print("Program ended")

@pytest.fixture(scope='class')
def datalaod():
    print("userprofile")
    return ["neelam","1234","ert","bmw"]

@pytest.fixture(params=[("chrome","neeru",1234),"edge","firefox"])
def crossbrowser(request):
    print("usename")
    print("password")
    return request.param




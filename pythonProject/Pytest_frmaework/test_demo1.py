import pytest

# @pytest.mark.regression
def test_firstprogram():
    print("Hello this is my firstprogram")

# @pytest.mark.xfail
def test_secondprogram():
    print("This is pytest framework")

# @pytest.mark.skip
def test_thirdprogram():
    print("this is 3 rd program")



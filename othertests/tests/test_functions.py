import pytest
import othertests.functions as functions
import time

def test_add():
    result =  functions.add(1, 4)
    assert result == 5

def test_divide():
    result = functions.divide(10, 5)
    assert result == 2    

def test_divide_by_zero():
    with pytest.raises(ValueError):
        functions.divide(10, 0)

def test_add_strings():
    result = functions.add("i like,", " burgers")
    assert result == "i like, burgers"   

@pytest.mark.slow
def test_slow_time():
    time.sleep(1)
    result = functions.divide(10, 5)
    assert result == 2    


@pytest.mark.skip(reason="Currently broken")
def test_add():
    result = functions.add(1, 4)
    assert result == 5


@pytest.mark.xfail(reason="This test is expected to fail")
def test_divide_by_zero():
    functions.divide(10, 0)
    
        
import pytest
import othertests.shapes as shapes


@pytest.fixture
def the_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def non_rectangle():
    return shapes.Rectangle(11, 21)
import pytest

branch = "release/pi3_installer"


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# multiple tags


@pytest.fixture(scope="module")
def setup_teardown():
    # as we give scope as module we execute setup and tear down only once per test file
    # if we don't give the scope setup and tear down are executed for every tc
    # setup
    print('\n Hi Upendra')
    print('........................')
    yield
    # teardown
    print('\n........................')
    print('Bye Upendra')


@pytest.mark.regression
@pytest.mark.sanity
def test_example(setup_teardown):
    print("this is a pytest regression practice example")

# skipping a test case


@pytest.mark.skip("skipping as fn not working soon it will be fixed")
def test_skip():
    print("this is a pytest practice example 2")


@pytest.mark.skipif('release' in branch, reason="skipping as fn doesnt work in prod")
def test_skip_if():
    print("this is a pytest practice example 2")


@pytest.mark.regression
def test_factorial(setup_teardown):
    assert factorial(5) == 120, "expected and actual values are not same"

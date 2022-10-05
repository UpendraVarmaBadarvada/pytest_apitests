import pytest


@pytest.mark.regression
def test_method1():
    print("this is a pytest regression test method")


@pytest.mark.smoke
def test_smoke_basic1():
    print("this is a smoke test")


@pytest.mark.sanity
def test_sanity_basic1():
    print("this is a sanity test")
    
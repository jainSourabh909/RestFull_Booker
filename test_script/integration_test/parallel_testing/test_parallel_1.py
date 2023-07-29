import pytest
import requests

'''
xdist-->It distributing tests across multiple CPUs to speed up test execution.
to run the test test case in parallel we need pytest-xdist library.
install xdist command-->pip install pytest-xdist
test case run command automatically -->pytest -n auto -s -v  (inside your parralel_testing folder in terminal)
if we want to specify numbers of workers ([gw]) then the command we use below command.
command to run only 2 workers parallely-->pytest -n 2 -s -v (2--> number of CPUs or workers)
'''


def test_1():
    assert True

def test_2():
    assert 1==1
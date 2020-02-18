#Brandon Greer
#BCGBR5
#Software Engineering
#Assignment 5: Testing

import pytest
import System

def test_login_1(grading_system):
    username = 'calyam'
    password = '#yeet'
    grading_system.login(username, password)
    assert(grading_system.usr.name == username)

def test_check_password_2(grading_system):
    assert(grading_system.check_password('calyam', '#yeet') and
           grading_system.check_password('goggins', 'augurrox'))

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

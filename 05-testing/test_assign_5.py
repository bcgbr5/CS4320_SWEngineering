#Brandon Greer
#BCGBR5
#Software Engineering
#Assignment 5: Testing

import pytest
import System
import RestoreData

def test_login_1(grading_system):
    username = 'calyam'
    password = '#yeet'
    grading_system.login(username, password)
    assert(grading_system.usr.name == username)

def test_check_password_2(grading_system):
    assert(grading_system.check_password('calyam', '#yeet') and
           grading_system.check_password('goggins', 'augurrox') and
           grading_system.check_password('yted91', 'imoutofpasswordnames') and
           grading_system.check_password('saab', 'boomr345'))


def test_chage_grade_3(test_staff):
    RestoreData
    grade = 97
    # test_staff.usr.change_grade('hdjsr7', 'software_engineering', 'assignment1', grade)
    assert(test_staff.usr.check_grades('hdjsr7', 'software_engineering')[0][1] == grade)
    RestoreData

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

@pytest.fixture
def test_staff():
    grading_system = System.System()
    grading_system.load_data()
    grading_system.login('cmhbf5', 'bestTA')
    return(grading_system)

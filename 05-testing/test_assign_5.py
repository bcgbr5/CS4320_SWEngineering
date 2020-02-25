# Brandon Greer
# BCGBR5
# Software Engineering
# Assignment 5: Testing


import pytest
import System
import os


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


def test_change_grade_3(test_staff):
    exec(open("./RestoreData.py").read())
    grade = 97
    test_staff.usr.change_grade('hdjsr7', 'software_engineering', 'assignment1', grade)
    assert(test_staff.usr.check_grades('hdjsr7', 'software_engineering')[0][1] == grade)


def test_create_assignment_4(test_staff, grading_system):
    exec(open("./RestoreData.py").read())
    test_staff.usr.create_assignment(
        "Test Assignment", "2/10/20", "software_engineering")
    courses = grading_system.load_course_db()
    assert(courses['software_engineering']['assignments']
           ["Test Assignment"]["due_date"] == "2/10/20")


def test_add_student_5(test_prof, grading_system):
    users = grading_system.load_user_db()
    test_prof.usr.add_student("akend3", "software_engineering")
    assert(users["akend3"]["courses"]["software_engineering"])


def test_drop_student_6(test_prof, grading_system):
    test_prof.usr.drop_student("hdjsr7","software_engineering")
    users = test_prof.load_user_db()
    assert("software_engineering" not in users["hdjsr7"]["courses"])


def test_student_submission_7(test_student):
    test_student.users["hdjsr7"]["courses"]["cloud_computing"]["assignment1"] = ""
    test_student.usr.submit_assignment("cloud_computing", "assignment1", "test_submission", "1/3/20")
    assert(test_student.users["hdjsr7"]["courses"]
           ["cloud_computing"]["assignment1"]["submission"] == "test_submission")


def test_student_ontime_8(test_student):
    assert(test_student.usr.check_ontime("1/30/20", "2/1/20") == True and
           test_student.usr.check_ontime("2/2/20", "2/1/20") == False)


def test_student_check_grade_9(test_student):
    grades = test_student.usr.check_grades("cloud_computing")
    print(grades)
    assert(grades["assignment1"] == 100 and
            grades["assignment2"] == 100)


def test_student_view_assignments_10(test_student):
    assignments = test_student.usr.view_assignments("cloud_computing")
    print(assignments)
    assert(assignments[0][1] == "2/2/20" and
           assignments[1][1] == "2/10/20")


def test_proffesor_drop_student_from_other_course_11(test_prof):
        test_prof.usr.drop_student("hdjsr7", "cloud_computing")
        users=test_prof.load_user_db()
        assert("cloud_computing" not in users["hdjsr7"]["courses"])


def test_ta_check_grades_12(test_staff):
    grades = test_staff.usr.check_grades("hdjsr7", "cloud_computing")
    assert(grades == [100,100])#can't get real assert here becuase keyerror throws in function

def test_ta_check_unowned_class_13(test_staff):
    grades = test_staff.usr.check_grades("hdjsr7", "databases")
    # can't get real assert here becuase keyerror throws in function
    assert(grades == [100, 100])


def test_proffesor_create_assignment_in_unowned_course_14(test_prof):
    test_prof.usr.create_assignment(
        "Test Assignment", "2/10/20", "comp_sci")
    courses = test_prof.load_course_db()
    assert(not courses['comp_sci']['assignments']
           ["Test Assignment"]["due_date"] == "2/10/20")


def test_proffesor_change_grade_in_unowned_course_15(test_prof):
    exec(open("./RestoreData.py").read())
    test_prof.usr.change_grade(
        'hdjsr7', 'cloud_computing', 'assignment1', 95)
    assert(test_prof.usr.check_grades(
        'hdjsr7', 'cloud_computing')[0][1] == 95)

    

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


@pytest.fixture
def test_prof():
    grading_system = System.System()
    grading_system.load_data()
    grading_system.login('goggins', 'augurrox')
    return(grading_system)


@pytest.fixture
def test_student():
    grading_system = System.System()
    grading_system.load_data()
    grading_system.login('hdjsr7', 'pass1234')
    return(grading_system)

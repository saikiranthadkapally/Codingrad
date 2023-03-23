'''
Syntax: 

LMS = {}

LMS["USERS"] = {}

USERS = LMS["USERS"]

LMS["ADMINS"] = {}

ADMINS = LMS["ADMINS"] 

'''

LMS = {}

USERS = LMS["USERS"] = {}
ADMINS = LMS["ADMINS"] = {}
BOOK = LMS["BOOK"] = {}

STUDENTS = LMS["USERS"]["STUDENTS"] = {}
TEACHERS = LMS["USERS"]["TEACHERS"] = {}

LOGIN = LMS["USERS"]["STUDENTS"]["LOGIN"] = {}
STUDENT_MENU = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"] = {}
LOGOUT = LMS["USERS"]["STUDENTS"]["LOGOUT"] = {}

BOOKS = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["BOOKS"] = {}
ADMIN = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["ADMIN"] = {}
FIRST = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["BOOKS"]["FIRST"] = {}
SECOND = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["BOOKS"]["SECOND"] = {}
THIRD = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["BOOKS"]["THIRD"] = {}
FOURTH = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["BOOKS"]["FOURTH"] = {}
MATHS = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["BOOKS"]["FIRST"]["MATHS"] = {}
CPROG = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["BOOKS"]["FIRST"]["CPROG"] = {}
DATASTRUCTURES = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["BOOKS"]["SECOND"]["DATASTRUCTURES"] = {}
DBMS = LMS["USERS"]["STUDENTS"]["STUDENT_MENU"]["BOOKS"]["SECOND"]["DBMS"] = {}

LOGIN = LMS["USERS"]["TEACHERS"]["LOGIN"] = {}
TEACHER_MENU = LMS["USERS"]["TEACHERS"]["TEACHER_MENU"] = {}
LOGOUT = LMS["USERS"]["TEACHERS"]["LOGOUT"] = {}

BOOKS = LMS["USERS"]["TEACHERS"]["TEACHER_MENU"]["BOOKS"] = {}
CSE = LMS["USERS"]["TEACHERS"]["TEACHER_MENU"]["BOOKS"]["CSE"] = {}
CIVIL = LMS["USERS"]["TEACHERS"]["TEACHER_MENU"]["BOOKS"]["CIVIL"] = {}
CPROGRAMMING = LMS["USERS"]["TEACHERS"]["TEACHER_MENU"]["BOOKS"]["CSE"]["CPROGRAMMING"] = {}
STENGTH_OF_MATERIALS = LMS["USERS"]["TEACHERS"]["TEACHER_MENU"]["BOOKS"]["CIVIL"]["STENGTH_OF_MATERIALS"] = {}

LOGIN = LMS["ADMINS"]["LOGIN"] = {}
ADD_BOOKS = LMS["ADMINS"]["ADD_BOOKS"] = {}
REMOVE_BOOKS = LMS["ADMINS"]["REMOVE_BOOKS"] = {}
DISPLAY_BOOKS_OVER_YEAR = LMS["ADMINS"]["DISPLAY_BOOKS_OVER_YEAR"] = {}
DISPLAY_BOOKS_OVER_DEPARTMENT = LMS["ADMINS"]["DISPLAY_BOOKS_OVER_DEPARTMENT"] = {}
CREATE_NEW_USER = LMS["ADMINS"]["CREATE_NEW_USER"] = {}
DELETE_USER = LMS["ADMINS"]["DELETE_USER"] = {}
UPDATE_USER = LMS["ADMINS"]["UPDATE_USER"] = {}
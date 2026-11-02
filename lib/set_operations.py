
# This module contains functions for working with sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors.
    """
    return {student[2] for student in student_list}


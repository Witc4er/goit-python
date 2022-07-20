import sqlite3
import faker
import random
from datetime import datetime

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
SUBJECTS = ['History', 'Foreign History', 'Dance', 'Gym', 'Art']
NUMBER_PEDAGOGUE = 3
NUMBER_MARKS = 20


def gen_fake_data(students, groups, number_pedagogue, number_marks):
    fake_students = []
    fake_groups = []
    fake_pedagogue = []
    fake_set_marks = []
    fake_subjects = SUBJECTS
    fake_data = faker.Faker('ru-RU')

    # Create fake student name
    for _ in range(students):
        fake_students.append(fake_data.name())

    # Create fake groups
    for _ in range(groups):
        fake_groups.append('Group - ' + f'{_ + 1}')

    # Create fake pedagogue
    for _ in range(number_pedagogue):
        fake_pedagogue.append(fake_data.name())

    # Create set marks for student
    for st in range(students):
        for su in range(len(fake_subjects)):
            for m in range(number_marks):
                date_marks = datetime(2022, random.randint(1, 6), random.randint(1, 28)).date()
                fake_set_marks.append((st+1, su+1, random.randint(2, 5), date_marks))
    return fake_students, fake_groups, fake_subjects, fake_pedagogue, fake_set_marks


def prepare_data(students, groups, subjects, pedagogues, set_marks) -> tuple:
    for_groups = []
    for group in groups:
        for_groups.append((group,))

    for_students = []
    for i, student in enumerate(students):
        if i <= 10:
            for_students.append((student, 1))
        if 10 < i <= 20:
            for_students.append((student, 2))
        if 20 < i <= 30:
            for_students.append((student, 3))

    for_subjects = list(zip(subjects, pedagogues + pedagogues[:2]))


    return for_groups, for_students, for_subjects, set_marks


def insert_data_to_db(groups, students, subjects, set_marks):
    with sqlite3.connect('./hw.db') as conn:
        curs = conn.cursor()

        sql_to_groups = 'INSERT into groups (group_name) VALUES (?);'
        curs.executemany(sql_to_groups, groups)

        sql_to_students = 'INSERT into students (name, group_id) VALUES (?,?);'
        curs.executemany(sql_to_students, students)

        sql_to_subjects = 'INSERT into subjects (subject_name, pedagogue_name) VALUES (?,?);'
        curs.executemany(sql_to_subjects, subjects)

        sql_to_marks = 'INSERT INTO rating (student_id, subject_id, mark, time_adding) VALUES (?,?,?,?);'
        curs.executemany(sql_to_marks, set_marks)



if __name__ == '__main__':
    fake_students, fake_groups, fake_subjects, fake_pedagogue, fake_set_marks = gen_fake_data(NUMBER_STUDENTS,
                                                                                              NUMBER_GROUPS,
                                                                                              NUMBER_PEDAGOGUE,
                                                                                              NUMBER_MARKS)
    groups, students, subjects, set_marks = prepare_data(fake_students, fake_groups, fake_subjects,
                                                                     fake_pedagogue, fake_set_marks)
    insert_data_to_db(groups, students, subjects, set_marks)

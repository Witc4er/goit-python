import sqlite3


def get_info():
    with sqlite3.connect('./hw.db') as conn:
        sql_first = '''
        SELECT AVG(mark), name
        FROM rating r
        INNER JOIN students s 
        ON r.student_id = s.id 
        GROUP BY student_id
        ORDER BY AVG(mark) DESC LIMIT 5;
        '''
        first_response = conn.execute(sql_first).fetchall()
        print('5 студентов с наибольшим средним баллом по всем предметам: ', first_response, '\n')

        sql_second = '''
        SELECT subject_name, AVG(mark), name
        FROM rating r
        INNER JOIN subjects s ON r.subject_id = s.id
        INNER JOIN students s2 ON r.student_id =s2.id
        WHERE subject_name = 'Dance'
        GROUP BY name
        ORDER BY AVG(mark) DESC LIMIT 1;
        '''
        second_response = conn.execute(sql_second).fetchall()
        print('1 студент с наивысшим средним баллом по одному предмету:', second_response, '\n')

        sql_third = '''
        SELECT subject_name, AVG(mark), group_name FROM rating r
        INNER JOIN students s ON student_id = s.id
        INNER JOIN groups g ON group_id = g.id
        INNER JOIN subjects s2 ON subject_id = s2.id
        WHERE subject_name = 'Gym' AND group_name = 'Group - 2';
        '''
        third_response = conn.execute(sql_third).fetchall()
        print('средний балл в группе по одному предмету:', third_response, '\n')

        sql_fourth = '''SELECT AVG(mark) FROM rating;'''
        fourth_response = conn.execute(sql_fourth).fetchall()
        print('Средний балл в потоке: ', fourth_response, '\n')

        sql_fifth = '''SELECT pedagogue_name, subject_name FROM subjects s GROUP BY pedagogue_name;'''
        fifth_response = conn.execute(sql_fifth).fetchall()
        print('Какие курсы читает преподаватель: ', fifth_response, '\n')

        sql_sixth = '''
        SELECT name, group_name
        FROM students s 
        INNER JOIN groups g ON group_id = g.id
        WHERE group_name = 'Group - 3';
        '''
        sixth_response = conn.execute(sql_sixth).fetchall()
        print('Список студентов в группе: ', sixth_response, '\n')

        sql_seventh = '''
        SELECT group_name, name, subject_name, mark, time_adding
        FROM rating r
        INNER JOIN students s ON student_id = s.id 
        INNER JOIN subjects s2 ON subject_id = s2.id 
        INNER JOIN groups g ON s.group_id = g.id
        WHERE group_name = 'Group - 2' AND subject_name = 'Dance'
        ORDER BY time_adding;
        '''
        seventh_response = conn.execute(sql_seventh).fetchall()
        print('Оценки студентов в группе по предмету: ', seventh_response, '\n')

        sql_eighth = '''
        SELECT name, subject_name 
        FROM rating r 
        INNER JOIN students s ON r.student_id = s.id 
        INNER JOIN subjects s2 ON r.subject_id = s2.id
        WHERE student_id = 10
        GROUP BY subject_name;
        '''
        eighth_response = conn.execute(sql_eighth).fetchall()
        print('Список курсов, которые посещает студент: ', eighth_response, '\n')


if __name__ == '__main__':
    get_info()

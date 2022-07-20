PRAGMA foreign_keys=ON;

-- Create table students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(250) NOT NULL UNIQUE,
    group_id INTEGER NOT NULL,
    -- Many student to one group
    FOREIGN KEY (group_id) REFERENCES groups(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

-- Create table groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(50)
);

-- Create table rating
DROP TABLE IF EXISTS rating;
CREATE TABLE rating (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    mark INTEGER NOT NULL,
    time_adding DATE NOT NULL,
    -- Many rating to one student
    FOREIGN KEY (student_id) REFERENCES students(id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

-- Create table subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  subject_name VARCHAR(125) NOT NULL,
  pedagogue_name VARCHAR(125) NOT NULL
);





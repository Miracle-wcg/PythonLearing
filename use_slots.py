#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    _slots_ = ('name', 'age')


class GraduateStudent(Student):
    pass


s = Student()
s.name = 'Michael'
s.age = 15
try:
    s.score = 88
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print(g.score)

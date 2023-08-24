#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self):
        self.knowledge  = []
    
    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)
        
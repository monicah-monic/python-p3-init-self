#!/usr/bin/env python3

class Person:
    def __init__(self,name):
        self.name = name
        print(f"{name}")
        
person = Person("Guido")
person.name
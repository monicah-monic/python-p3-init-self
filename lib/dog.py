#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed= "Mutt"):
        self.name = name
        self.breed = breed
        print(f"{name}")
        print(f"{breed}")

dog = Dog("Fido", "Dalmatian")
dog.name
dog.breed      
        
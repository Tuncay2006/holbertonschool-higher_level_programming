#!/usr/bin/env python3

import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            # Hata olursa sessizce geç, gerekirse loglama yapılabilir
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.
        Returns:
            CustomObject instance or None if error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None

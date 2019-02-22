import copy

class School:
    
    def __init__(self, name=None):
        self.name = name
        self._roster = {}
        
    def roster(self):
        return self._roster
    
    def add_student(self, student_name=None, grade_level=None):
        if grade_level in self._roster: 
            self._roster[grade_level].append(student_name)
        else:
            self._roster[grade_level] = [student_name]
        return self._roster
    
    def grade(self, grade_level=None):
        return self._roster[grade_level]
    
    def sort_roster(self):
        new_dict = dict(sorted(self._roster.items()))
        return new_dict
        
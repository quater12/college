from datetime import datetime

class YourName:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = datetime.now().year
        age = current_year - self.birth_year
        course = age - 15 if age >= 15 else 0
        return course

    def name_list(self):
        return [self.first_name, self.last_name] if self.first_name and self.last_name else None

student = YourName("Борислав", "Гуменюк", 2008)
print("Курс:", student.calculate_course())
print("Ім'я та прізвище:", student.name_list())

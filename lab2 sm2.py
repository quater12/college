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

class ExtendedYourName(YourName):
    def __init__(self, first_name=None, last_name=None, birth_year=None, student_id=None, major=None, gpa=None):
        super().__init__(first_name, last_name, birth_year)
        self.student_id = student_id
        self.major = major
        self.__gpa = gpa
        self._enrollment_status = True

    def update_major(self, new_major):
        self.major = new_major

    def _calculate_honors(self):
        return "З відзнакою" if self.__gpa and self.__gpa >= 4.5 else "Без відзнаки"

    def display_info(self):
        honors = self._calculate_honors()
        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Курс": self.calculate_course(),
            "Факультет": self.major,
            "Середній бал": self.__gpa,
            "Статус": "Активний" if self._enrollment_status else "Неактивний",
            "Відзнака": honors
        }

extended_student = ExtendedYourName("Борислав", "Гуменюк", 2008, "S12345", "ICT", 0.0)
print("Інформація про студента:", extended_student.display_info())

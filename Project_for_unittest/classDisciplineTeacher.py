from Project_for_unittest.classTeacher import Teacher


class DisciplineTeacher(Teacher):

    def __init__(self, name, education, experience, discipline, job_title, phone):
        super().__init__(name, education, experience, phone)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, new_job_title):
        self.__job_title = new_job_title

    def get_teacher_data(self):
        return f"{super().get_teacher_data()}\nПредмет {self.get_discipline()}, должность {self.get_job_title()}"

    def add_mark(self, name_student, mark):
        return f"{super().add_mark(name_student, mark)}\nПредмет: {self.get_discipline()}"

    def remove_mark(self, name_student, mark):
        return f"{super().remove_mark(name_student, mark)}\nПредмет: {self.get_discipline()}"

    def give_a_consultation(self, grade):
        return f"{super().give_a_consultation(grade)}\nПо предмету {self.get_discipline()} как {self.get_job_title()}"
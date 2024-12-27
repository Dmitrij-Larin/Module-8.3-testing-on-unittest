class Teacher:
    teacher_dict = {}

    def __init__(self, name, education, experience, phone):
        self.__name = name
        self.__education = education
        self.__experience = experience
        self.__phone = phone
        Teacher.teacher_dict[self.__phone] = self.__name

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, new_experience):
        self.__experience = new_experience

    def get_phone(self):
        return self.__phone

    def get_teacher_data(self):
        return f"{self.__name}, образование {self.__education}, опыт работы {self.__experience} год(-а)(лет)."

    def add_mark(self, name_student, mark):
        return f"{self.__name} поставила оценку {mark} ученику {name_student}"

    def remove_mark(self, name_student, mark):
        return f"{self.__name} удалила оценку {mark} ученику {name_student}"

    def give_a_consultation(self, grade):
        return f"{self.__name} провёла консультацию в классе {grade}"

    def fire_teacher(self):
        if self.__phone in Teacher.teacher_dict.keys():
            Teacher.teacher_dict.pop(self.__phone)
            return f'Преподаватель {self.__name} был уволен'
        else:
            return f'Преподавателя {self.__name} уже уволили'
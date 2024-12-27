import unittest

from Project_for_unittest.classDisciplineTeacher import DisciplineTeacher
from Project_for_unittest.classTeacher import Teacher


class TestTeacher(unittest.TestCase):
    teacher = Teacher('test_name', 'test_education', 'test_experience', 'test_phone')

    def test_01_init(self):
        self.assertEqual(self.teacher.__init__('test_name', 'test_education', 'test_experience', 'test_phone'), None)
        self.assertEqual(self.teacher.teacher_dict['test_phone'], 'test_name')

    def test_02_get_name(self):
        self.assertEqual(self.teacher.get_name(), 'test_name')

    def test_03_get_education(self):
        self.assertEqual(self.teacher.get_education(), 'test_education')

    def test_04_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), 'test_experience')

    def test_05_set_experience(self):
        self.teacher.set_experience('test_new_experience')
        self.assertEqual(self.teacher.get_experience(), 'test_new_experience')
        self.teacher.set_experience('test_experience')

    def test_06_get_phone(self):
        self.assertEqual(self.teacher.get_phone(), 'test_phone')

    def test_07_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(),
                         'test_name, образование test_education, опыт работы test_experience год(-а)(лет).')

    def test_08_add_mark(self):
        self.assertEqual(self.teacher.add_mark('test_name_student', 'test_mark'),
                         'test_name поставила оценку test_mark ученику test_name_student')

    def test_09_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark('test_name_student', 'test_mark'),
                         'test_name удалила оценку test_mark ученику test_name_student')

    def test_10_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation('test_grade'),
                         'test_name провёла консультацию в классе test_grade')

    def test_11_fire_teacher(self):
        self.assertEqual(self.teacher.fire_teacher(), 'Преподаватель test_name был уволен')
        self.assertEqual(self.teacher.fire_teacher(), 'Преподавателя test_name уже уволили')
        self.assertEqual(self.teacher.teacher_dict, {})


class TestDisciplineTeacher(unittest.TestCase):
    discipline_teacher = DisciplineTeacher('test_name', 'test_education', 'test_experience', 'test_discipline',
                                           'test_job_title', 'test_phone')

    def test_12_init(self):
        self.assertEqual(self.discipline_teacher.__init__('test_name', 'test_education', 'test_experience', 'test_discipline',
                                           'test_job_title', 'test_phone'), None)

    def test_13_get_discipline(self):
        self.assertEqual(self.discipline_teacher.get_discipline(), 'test_discipline')

    def test_14_get_job_title(self):
        self.assertEqual(self.discipline_teacher.get_job_title(), 'test_job_title')

    def test_15_set_job_title(self):
        self.discipline_teacher.set_job_title('test_new_job_title')
        self.assertEqual(self.discipline_teacher.get_job_title(), 'test_new_job_title')
        self.discipline_teacher.set_job_title('test_job_title')

    def test_16_get_teacher_data(self):
        self.assertEqual(self.discipline_teacher.get_teacher_data(), 'test_name, образование test_education, опыт работы test_experience год(-а)(лет).\nПредмет test_discipline, должность test_job_title')

    def test_17_add_mark(self):
        self.assertEqual(self.discipline_teacher.add_mark('test_name_student', 'test_mark'), 'test_name поставила оценку test_mark ученику test_name_student\nПредмет: test_discipline')

    def test_18_remove_mark(self):
        self.assertEqual(self.discipline_teacher.remove_mark('test_name_student', 'test_mark'), 'test_name удалила оценку test_mark ученику test_name_student\nПредмет: test_discipline')

    def test_19_give_a_consultation(self):
        self.assertEqual(self.discipline_teacher.give_a_consultation('test_grade'), 'test_name провёла консультацию в классе test_grade\nПо предмету test_discipline как test_job_title')

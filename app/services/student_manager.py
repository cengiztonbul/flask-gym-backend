from ..models.student import Student
from ..services.user_manager import create_user


def create_student(first_name, last_name, email):
    student = Student()

    # TODO: question whether role_id is required or not
    role = None
    student.user_id = create_user(first_name, last_name, email, role)

    student.save()


def find_student_by_user_id(user_id):
    return Student.objects(user_id=user_id).get()

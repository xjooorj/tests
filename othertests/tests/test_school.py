import pytest

from othertests.school import (
    Classroom,
    Student,
    Teacher,
    ToManyStudents,
)



@pytest.fixture
def dumbledore():
    return Teacher("Albus Dumbledore")


@pytest.fixture
def snape():
    return Teacher("Severus Snape")


@pytest.fixture
def harry():
    return Student("Harry Potter")


@pytest.fixture
def ron():
    return Student("Ron Weasley")


@pytest.fixture
def hermione():
    return Student("Hermione Granger")


@pytest.fixture
def hogwarts_class(dumbledore, harry, ron, hermione):
    return Classroom(
        teacher=dumbledore,
        students=[harry, ron, hermione],
        course_title="Defence Against the Dark Arts",
    )



def test_classroom_is_created_correctly(hogwarts_class, dumbledore):
    assert hogwarts_class.teacher == dumbledore
    assert len(hogwarts_class.students) == 3
    assert hogwarts_class.course_title == "Defence Against the Dark Arts"


def test_add_student(hogwarts_class):
    luna = Student("Luna Lovegood")

    hogwarts_class.add_student(luna)

    assert luna in hogwarts_class.students
    assert len(hogwarts_class.students) == 4


def test_remove_student(hogwarts_class):
    hogwarts_class.remove_student("Ron Weasley")

    student_names = [student.name for student in hogwarts_class.students]

    assert "Ron Weasley" not in student_names
    assert len(hogwarts_class.students) == 2


def test_change_teacher(hogwarts_class, snape):
    hogwarts_class.change_teacher(snape)

    assert hogwarts_class.teacher == snape



@pytest.mark.parametrize(
    "student_name",
    [
        "Draco Malfoy",
        "Neville Longbottom",
        "Ginny Weasley",
    ],
)
def test_add_multiple_students(hogwarts_class, student_name):
    student = Student(student_name)

    hogwarts_class.add_student(student)

    assert student in hogwarts_class.students


@pytest.mark.parametrize(
    "name_to_remove",
    [
        "Harry Potter",
        "Ron Weasley",
        "Hermione Granger",
    ],
)
def test_remove_different_students(hogwarts_class, name_to_remove):

    hogwarts_class.remove_student(name_to_remove)

    names = [student.name for student in hogwarts_class.students]

    assert name_to_remove not in names



@pytest.mark.slow
def test_raise_exception_when_classroom_is_full(dumbledore):

    students = [
        Student(f"Wizard {i}")
        for i in range(11)
    ]

    classroom = Classroom(
        teacher=dumbledore,
        students=students,
        course_title="Potions",
    )

    with pytest.raises(ToManyStudents):
        classroom.add_student(Student("Cedric Diggory"))



def test_remove_nonexistent_student(hogwarts_class):

    original_count = len(hogwarts_class.students)

    hogwarts_class.remove_student("Lord Voldemort")

    assert len(hogwarts_class.students) == original_count


@pytest.mark.hogwarts
def test_teacher_can_be_changed_multiple_times(hogwarts_class):

    mcgonagall = Teacher("Minerva McGonagall")
    snape = Teacher("Severus Snape")

    hogwarts_class.change_teacher(mcgonagall)
    assert hogwarts_class.teacher == mcgonagall

    hogwarts_class.change_teacher(snape)
    assert hogwarts_class.teacher == snape
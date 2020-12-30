import pytest
from datetime import datetime
from .Lesson.lesson import Lesson


@pytest.fixture(scope="class")
def create_lesson_one():
    lesson1 = Lesson(
        lesson_name="lesson1",
        lesson_date="2020-12-21",
        course_name="Python QA Engineer",
        module="Introduction",
        link="",
    )
    return lesson1


@pytest.fixture()
def create_lesson_two():
    return Lesson(
        lesson_name="lesson2",
        lesson_date="2020-12-28",
        course_name="Python QA Engineer",
        module="Introduction",
        link="",
    )


class TestLesson:
    @pytest.mark.smoke
    def test_lesson_one(self, create_lesson_one, create_lesson_two, set_time):
        assert datetime.fromisoformat(create_lesson_one.get_lesson_date()) < \
               datetime.fromisoformat(create_lesson_two.get_lesson_date())

    def test_lesson_two(self, create_lesson_one, create_lesson_two):
        """
        TODO: "Проверить что тесты относятся к одному модулю"
        """
        assert create_lesson_one.get_module() == create_lesson_two.get_module()

    @pytest.mark.skipif("True", reason="because of true")
    def test_exit():
        assert True

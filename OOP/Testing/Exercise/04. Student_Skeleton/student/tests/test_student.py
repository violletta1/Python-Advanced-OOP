from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Test Guy1")
        self.student_with_course = Student("Test Guy2", {"math": ["some note"]})

    def test_correct_initialization(self):
        self.assertEqual("Test Guy1", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["some note"]}, self.student_with_course.courses)

    def test_add_notes_if_course_existing(self):
        result = self.student_with_course.enroll("math", ["second note"])
        self.assertEqual("second note", self.student_with_course.courses["math"][1])
        self.assertEqual("Course already added. Notes have been updated.", result)


    def test_add_notes_to_non_existing_course_without_third_param(self):
        result = self.student.enroll("math", ["math notes"])
        self.assertEqual("math notes", self.student.courses["math"][0])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_notes_to_non_existing_course_with_third_param(self):
        result = self.student.enroll("math", ["math notes"], "Y")
        self.assertEqual("math notes", self.student.courses["math"][0])
        self.assertEqual(result, "Course and course notes have been added.")


    def test_add_new_course_without_adding_notes(self):
        result = self.student.enroll("math", ["math notes"], "N")
        self.assertEqual(0, len(self.student.courses["math"]))
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.add_notes("math", "new notes")
        self.assertEqual("new notes", self.student_with_course.courses["math"][-1])
        self.assertEqual(result, "Notes have been updated")

    def test_raise_error_if_trying_to_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "note")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_removing_from_courses(self):
        result = self.student_with_course.leave_course("math")
        self.assertEqual(0, len(self.student_with_course.courses))
        self.assertEqual(result, "Course has been removed")

    def test_raise_error_trying_to_remove_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    main()
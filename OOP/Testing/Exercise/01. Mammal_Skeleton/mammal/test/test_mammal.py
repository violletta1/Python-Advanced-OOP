from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammmal = Mammal("some name", "some type", "some sound")

    def test_correct_initialization(self):
        self.assertEquals("some name", self.mammmal.name)
        self.assertEquals("some type", self.mammmal.type)
        self.assertEquals("some sound", self.mammmal.sound)

    def test_if_make_sound_with_correct_message(self):
        self.assertEquals("some name makes some sound", self.mammmal.make_sound())

    def test_if_get_kingdom_returns_kingdom(self):
        self.assertEquals("animals", self.mammmal.get_kingdom())

    def test_if_info_return_correct_message(self):
        self.assertEquals("some name is of type some type", self.mammmal.info())


if __name__ == "__main__":
    main()
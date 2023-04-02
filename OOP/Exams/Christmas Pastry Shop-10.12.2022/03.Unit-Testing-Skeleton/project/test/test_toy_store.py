from project.toy_store import ToyStore

from unittest import TestCase, main

class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_correct_init(self):
        for k in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[chr(k)])
        self.assertEqual(7, len(self.store.toy_shelf))

    def test_add_toy_to_non_existing_shelf_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "Teddy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_to_shelf_with_same_toy_raise_error(self):
        self.store.add_toy("A", "Teddy")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Teddy")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_to_full_shelf_raise_error(self):
        self.store.add_toy("A", "Teddy")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "new")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successful(self):
        result = self.store.add_toy("A", "Teddy")
        self.assertEqual("Toy:Teddy placed successfully!", result)
        self.assertEqual("Teddy", self.store.toy_shelf["A"])

    def test_remove_toy_from_non_existing_shelf_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "toy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_non_existing_toy_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "toy")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successful(self):
        self.store.toy_shelf["A"] = "Teddy" # create shelf with toy-Teddy
        result = self.store.remove_toy("A", "Teddy") # create result with store without toy Teddy
        self.assertEqual("Remove toy:Teddy successfully!", result)
        self.assertIsNone(self.store.toy_shelf["A"])


if __name__ == "__main__":
    main()
import unittest
from app import rota


class LibraryRouteTypesTests(unittest.TestCase):
    def test_unordered_stop_containers_are_rejected(self):
        for value in ({"Ceará-Mirim"}, {"first": "Ceará-Mirim"}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                rota("Natal", "Touros", paradas=value)

    def test_modes_and_toll_flags_are_strictly_typed(self):
        for mode in ([], {}, None):
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                rota("Natal", "Touros", modo=mode)
        for flag in (0, 1, "false"):
            with self.subTest(flag=flag), self.assertRaises(ValueError):
                rota("Natal", "Touros", evitar_pedagios=flag)


if __name__ == "__main__":
    unittest.main()

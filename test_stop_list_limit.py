import unittest
from app import run, textos


class StopListBoundTests(unittest.TestCase):
    def test_rejects_large_waypoint_list_before_processing(self):
        with self.assertRaisesRegex(ValueError, "até 3"):
            textos(["Parada"] * 100_000)

    def test_integration_rejects_more_than_three_stops(self):
        payload = {"origem": "Natal", "destino": "Touros", "modo": "carro",
                   "alternativas": [{"nome": "Opção", "paradas": ["A", "B", "C", "D"]}]}
        with self.assertRaisesRegex(ValueError, "até 3"):
            run(payload)

    def test_supports_three_stops(self):
        self.assertEqual(textos(["A", "B", "C"]), ["A", "B", "C"])


if __name__ == "__main__":
    unittest.main()

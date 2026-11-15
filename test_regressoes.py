import unittest
from app import run

class RouteOptionsTests(unittest.TestCase):
    def test_multiple_options(self):
        result = run({"origem":"Natal","destino":"Recife","modo":"carro","alternativas":[{"nome":"Direta","paradas":[]},{"nome":"Com parada","paradas":["João Pessoa"],"evitar_pedagios":True}]})
        self.assertEqual(result["quantidade"], 2)
        self.assertIn("waypoints=Jo%C3%A3o+Pessoa", result["rotas"][1]["google_maps"])
        self.assertIn("avoid=tolls", result["rotas"][1]["google_maps"])

    def test_empty_options_rejected(self):
        with self.assertRaises(ValueError):
            run({"origem":"Natal","destino":"Recife","modo":"carro","alternativas":[]})

    def test_invalid_tolls_flag_rejected(self):
        with self.assertRaises(ValueError):
            run({"origem":"Natal","destino":"Recife","modo":"carro","alternativas":[{"nome":"Rota","paradas":[],"evitar_pedagios":"sim"}]})

if __name__ == "__main__": unittest.main()

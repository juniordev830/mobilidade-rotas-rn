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

    def test_reject_duplicate_route_labels_case_insensitively(self):
        payload = {"origem": "Natal", "destino": "Recife", "modo": "carro",
                   "alternativas": [
                       {"nome": "Rota A", "paradas": []},
                       {"nome": " rota a ", "paradas": ["João Pessoa"]},
                   ]}
        with self.assertRaisesRegex(ValueError, "repetido"):
            run(payload)

    def test_reject_more_than_25_alternatives(self):
        payload = {"origem": "Natal", "destino": "Recife", "modo": "carro",
                   "alternativas": [{"nome": str(i), "paradas": []} for i in range(26)]}
        with self.assertRaisesRegex(ValueError, "25"):
            run(payload)

    def test_preserve_labels_and_order_for_distinct_routes(self):
        payload = {"origem": "Natal", "destino": "Recife", "modo": "carro",
                   "alternativas": [{"nome": "  Norte ", "paradas": []},
                                    {"nome": "Sul", "paradas": []}]}
        self.assertEqual([route["nome"] for route in run(payload)["rotas"]], ["Norte", "Sul"])


if __name__ == "__main__": unittest.main()

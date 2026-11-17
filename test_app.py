import json
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import sys
import unittest

from app import run

ROOT = Path(__file__).resolve().parent


class ProjetoTest(unittest.TestCase):
    def test_exemplo_documentado(self):
        data = json.loads((ROOT / "exemplo.json").read_text(encoding="utf-8"))
        result = run(data)
        self.assertEqual(result['quantidade'], 2)

    def test_modo_explicito_dispensa_modo_padrao(self):
        data = {"origem": "Natal", "destino": "Alecrim", "alternativas": [
            {"nome": "Bike", "modo": "bicicleta", "paradas": []},
            {"nome": "A pé", "modo": "a-pe", "paradas": []},
        ]}
        links = run(data)["rotas"]
        self.assertIn("travelmode=bicycling", links[0]["google_maps"])
        self.assertIn("travelmode=walking", links[1]["google_maps"])

    def test_cada_rota_precisa_de_um_modo_explicito_ou_padrao(self):
        data = {"origem": "Natal", "destino": "Alecrim", "alternativas": [
            {"nome": "Sem modo", "paradas": []},
        ]}
        with self.assertRaises(ValueError):
            run(data)

    def test_cli_aceita_json_utf8_com_bom(self):
        exemplo = (ROOT / "exemplo.json").read_text(encoding="utf-8")
        with TemporaryDirectory() as pasta:
            entrada = Path(pasta) / "entrada.json"
            entrada.write_text(exemplo, encoding="utf-8-sig")
            resultado = subprocess.run(
                [sys.executable, str(ROOT / "app.py"), str(entrada)],
                capture_output=True, text=True, encoding="utf-8", check=True,
            )
        self.assertEqual(json.loads(resultado.stdout), run(json.loads(exemplo)))

    def test_cli_com_exemplo(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "app.py"), str(ROOT / "exemplo.json")],
            capture_output=True, text=True, encoding="utf-8", check=True,
        )
        self.assertEqual(json.loads(result.stdout)['quantidade'], 2)

    def test_rejeita_dados_incompletos(self):
        with self.assertRaises((KeyError, ValueError, TypeError)):
            run({})

    def test_codifica_paradas_e_modo(self):
        from urllib.parse import parse_qs, urlparse
        data = json.loads((ROOT / "exemplo.json").read_text(encoding="utf-8"))
        link = urlparse(run(data)["rotas"][1]["google_maps"])
        self.assertEqual(link.netloc, "www.google.com")
        query = parse_qs(link.query)
        self.assertEqual(query["waypoints"], ["Igapó, Natal, RN"])
        self.assertEqual(query["travelmode"], ["driving"])
        self.assertEqual(query["avoid"], ["tolls"])

    def test_limite_paradas(self):
        from app import rota
        with self.assertRaises(ValueError):
            rota("Natal", "Recife", paradas=["A", "B", "C", "D"])
        with self.assertRaises(ValueError):
            rota("Natal", "Recife", paradas=["A|B"])

    def test_rejeita_string_como_booleano(self):
        with self.assertRaises(ValueError):
            run(dict(origem="A", destino="B", modo="carro", alternativas=[dict(nome="X", paradas=[], evitar_pedagios="false")]))

    def test_modo_por_alternativa_substitui_padrao(self):
        from urllib.parse import parse_qs, urlparse
        data = dict(origem="Natal, RN", destino="Parnamirim, RN", modo="carro", alternativas=[
            dict(nome="Pedal", modo="bicicleta", paradas=[]),
            dict(nome="Caminhada", modo="a-pe", paradas=[]),
            dict(nome="Carro", paradas=[]),
        ])
        result = run(data)
        modes = [parse_qs(urlparse(route["google_maps"]).query)["travelmode"][0]
                 for route in result["rotas"]]
        self.assertEqual(modes, ["bicycling", "walking", "driving"])

    def test_modo_desconhecido_na_alternativa_e_rejeitado(self):
        data = dict(origem="Natal", destino="Parnamirim", modo="carro",
                    alternativas=[dict(nome="Inválida", modo="teleporte", paradas=[])])
        with self.assertRaisesRegex(ValueError, "Modo desconhecido"):
            run(data)

import json
from pathlib import Path
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

import unittest
from app import run
class DiagnosticoRotas(unittest.TestCase):
    def test_agrupa(self):
        data={"origem":"Natal","destino":"Macaíba","modo":"carro","diagnostico":True,"alternativas":[{"nome":"A","paradas":["Centro"]},{"nome":"B","paradas":[]},{"nome":"C","modo":"bicicleta","paradas":[]}]}
        self.assertEqual(run(data)["resumo_por_modo"],{"carro":{"alternativas":2,"paradas":1},"bicicleta":{"alternativas":1,"paradas":0}})
        data["diagnostico"]=False
        self.assertNotIn("resumo_por_modo",run(data))

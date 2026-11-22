import unittest
from app import rota, run


class AddressValidationTests(unittest.TestCase):
    def test_rejects_control_character_and_oversized_address(self):
        for text in ("Natal\nRN", "Natal\x7fRN", "A" * 301):
            with self.subTest(text=repr(text)), self.assertRaises(ValueError):
                rota(text, "Parnamirim")

    def test_invalid_alternative_label_is_rejected(self):
        sample = dict(origem="Natal", destino="Touros", modo="carro",
                      alternativas=[dict(nome="Linha\nFalsa", paradas=[])])
        with self.assertRaises(ValueError):
            run(sample)

    def test_normal_address_is_preserved(self):
        self.assertIn("origin=Natal", rota(" Natal ", "Parnamirim"))


if __name__ == "__main__":
    unittest.main()

import unittest
import cambia_texto


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "fuera maduro"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "FUERA MADUR0")


if __name__ == '__main__':
    unittest.main()

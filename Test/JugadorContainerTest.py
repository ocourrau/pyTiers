import unittest
from containers import JugadorContainer

 jugadorCont = JugadorContainer()

 class JugadorContainerTest(unittest.TestCase):
     def setup(self):
         pass

    def testAgrega(self):
        val1 = (input('Ingrese Jugador '))
        val2 = (input('Ingrese otro jugador '))
        self.assertEqual(jugadorCont.len(val1,val2),2)

    def testRemove(self):
        list = []
        list.append('El Brandon Productions')
        list.remove()
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()

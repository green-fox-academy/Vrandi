import unittest
from ships import *

class TestShips(unittest.TestCase):
    def test_instantiate_ship(self):
        self.assertIsInstance(Ship(), Ship)

    def test_status(self):
        s = Ship()
        self.assertEqual(s.status, False)

    def test_statuschanger(self):
        s = Ship()
        s.statuschanger()
        self.assertEqual(s.status, True)

    def test_instantiate_aircraft(self):
        self.assertIsInstance(AircraftCarrier([]), AircraftCarrier)

    def test_instantiate_battleship(self):
        self.assertIsInstance(Battleship(), Battleship)

    def test_instantiate_destroyer(self):
        self.assertIsInstance(Destroyer(), Destroyer)

    def test_instantiate_submarine(self):
        self.assertIsInstance(Submarine(), Submarine)

    def test_instantiate_patrolboat(self):
        self.assertIsInstance(PatrolBoat(), PatrolBoat)

    def test_aircraft_shipfieldnumber(self):
        a = AircraftCarrier([])
        self.assertEqual(a.fieldnum, 5)

    def test_battle_shipfieldnumber(self):
        b = Battleship()
        self.assertEqual(b.fieldnum, 4)

    def test_destroyer_shipfieldnumber(self):
        d = Destroyer()
        self.assertEqual(d.fieldnum, 3)

    def test_submarine_shipfieldnumber(self):
        s = Submarine()
        self.assertEqual(s.fieldnum, 3)

    def test_patrol_shipfieldnumber(self):
        p = PatrolBoat()
        self.assertEqual(p.fieldnum, 2)

    def test_position(self):
        a = AircraftCarrier([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
        self.assertEqual(a.position, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
        self.assertEqual(a.status, False)



unittest.main()

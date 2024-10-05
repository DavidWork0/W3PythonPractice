import unittest
from ClassAndObjects import Character

class TestCharacter(unittest.TestCase):

    def setUp(self):
        self.character = Character("Test", 10, 20, 30)     
    
    def test_initial_values(self):
        self.assertEqual(self.character.name, "Test")
        self.assertEqual(self.character.health, 10)
        self.assertEqual(self.character.damage, 20)
        self.assertEqual(self.character.speed, 30)

    def test_double_health(self):
        self.character.double_health()
        self.assertEqual(self.character.health, 20) 

    def test_double_damage(self):
        self.character.double_damage()
        self.assertEqual(self.character.damage, 40)
    def test_double_speed(self):

        self.character.double_speed()
        self.assertEqual(self.character.speed, 60)
    
    def test_ultra_buff(self):
        self.character.ultra_buff()
        self.assertEqual(self.character.health, 20) 
        self.assertEqual(self.character.damage, 40)
        self.assertEqual(self.character.speed, 60)

    def test_print_char_details(self):
        pass

if __name__ == "__main__":
    unittest.main()
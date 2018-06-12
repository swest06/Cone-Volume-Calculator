import unittest
import ConeVolumeCalculator

class KnownValues(unittest.TestCase):
   

    def test_calculateConeVolume_for20r10h(self):
        
        result = ConeVolumeCalculator.calculateConeVolume(20.0, 10.0)
        
        self.assertEqual(4188.79, result)

    def test_calculateConeVolume_for100r10h(self):
        result = ConeVolumeCalculator.calculateConeVolume(100.0, 10.0)
        expected = 104719.76
        self.assertEqual(expected, result)


    def test_calculateConeVolume_for40r108h(self):
        result = ConeVolumeCalculator.calculateConeVolume(40.0, 108.0)
        expected = 180955.74
        self.assertEqual(expected, result)


    def test_calculateConeVolume_for65_5r80_5h(self):
        result = ConeVolumeCalculator.calculateConeVolume(65.5, 80.5)
        expected = 361665.51
        self.assertEqual(expected, result)


    def test_calculateConeVolume_for65r90h(self):
        result = ConeVolumeCalculator.calculateConeVolume(65, 90)
        expected = 398196.87
        self.assertEqual(expected, result)


    def test_calculateConeVolume_for60r100h(self):
        result = ConeVolumeCalculator.calculateConeVolume(60, 100)
        expected = 376991.12
        self.assertEqual(expected, result)


    def test_calculateConeVolume_for95r80h(self):
        result = ConeVolumeCalculator.calculateConeVolume(95, 80)
        expected = 756076.63
        self.assertEqual(expected, result)


    def test_calculateConeVolume_for100r90h(self):
        result = ConeVolumeCalculator.calculateConeVolume(100, 90)
        expected = 942477.80
        self.assertEqual(expected, result)


# Run the tests
if __name__ == '__main__':
    unittest.main()

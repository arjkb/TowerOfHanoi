import toi
import unittest

class ToiTests(unittest.TestCase):
    def test_spare_when_a_b(self):
        expected_value = 'C'
        result = toi.get_spare_peg(peg1='A', peg2='B')
        self.assertEqual(expected_value, result)

    def test_spare_when_b_a(self):
        expected_value = 'C'
        result = toi.get_spare_peg(peg1='B', peg2='A')
        self.assertEqual(expected_value, result)

    def test_spare_when_a_c(self):
        expected_value = 'B'
        result = toi.get_spare_peg(peg1='A', peg2='C')
        self.assertEqual(expected_value, result)

    def test_spare_when_c_a(self):
        expected_value = 'B'
        result = toi.get_spare_peg(peg1='C', peg2='A')
        self.assertEqual(expected_value, result)

    def test_spare_when_b_c(self):
        expected_value = 'A'
        result = toi.get_spare_peg(peg1='B', peg2='C')
        self.assertEqual(expected_value, result)

    def test_spare_when_c_b(self):
        expected_value = 'A'
        result = toi.get_spare_peg(peg1='C', peg2='B')
        self.assertEqual(expected_value, result)

    def test_spare_when_a_b_lower(self):
        expected_value = 'C'
        result = toi.get_spare_peg(peg1='a', peg2='b')
        self.assertEqual(expected_value, result)

    def test_spare_when_invalid(self):
        # result = toi.get_spare_peg(peg1='F', peg2='G')
        # self.assertIsNone(result)
        self.assertRaises(Exception, toi.get_spare_peg, 'F', 'G')

    def test_verify_hanoi_property(self):
        temp_peg = [5, 4, 1, 2]
        self.assertRaises(Exception, toi.verify_hanoi_property, temp_peg)

if __name__ == '__main__':
    # print(toi.get_spare_peg('a', 'h'))
    unittest.main()

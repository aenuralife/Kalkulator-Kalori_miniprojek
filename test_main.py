import unittest
from main import hitung_bmi, kategori_bmi, hitung_kalori_harian

class TestKalkulatorBMI(unittest.TestCase):

    # --- Test Case 1: hitung_bmi ---
    def test_hitung_bmi_valid(self):
        # Test Case Valid: Berat 70kg, Tinggi 170cm -> BMI = 24.22
        self.assertEqual(hitung_bmi(70, 170), 24.22)

    def test_hitung_bmi_invalid_input(self):
        # Test Case Invalid: Berat/Tinggi bernilai nol atau negatif
        with self.assertRaises(ValueError):
            hitung_bmi(-50, 170)
        with self.assertRaises(ValueError):
            hitung_bmi(70, 0)

    # --- Test Case 2: kategori_bmi ---
    def test_kategori_bmi_kurus(self):
        self.assertEqual(kategori_bmi(17.5), "Kurus")

    def test_kategori_bmi_normal(self):
        self.assertEqual(kategori_bmi(22.0), "Normal")

    def test_kategori_bmi_kelebihan_berat(self):
        self.assertEqual(kategori_bmi(27.5), "Kelebihan Berat Badan")

    def test_kategori_bmi_obesitas(self):
        self.assertEqual(kategori_bmi(32.0), "Obesitas")

    def test_kategori_bmi_invalid(self):
        with self.assertRaises(ValueError):
            kategori_bmi(-5.0)

    # --- Test Case 3: hitung_kalori_harian ---
    def test_hitung_kalori_pria(self):
        # Pria: (10*70) + (6.25*170) - (5*25) + 5 = 700 + 1062.5 - 125 + 5 = 1642.5
        self.assertEqual(hitung_kalori_harian("pria", 70, 170, 25), 1642.5)

    def test_hitung_kalori_wanita(self):
        # Wanita: (10*55) + (6.25*160) - (5*22) - 161 = 550 + 1000 - 110 - 161 = 1279.0
        self.assertEqual(hitung_kalori_harian("wanita", 55, 160, 22), 1279.0)

    def test_hitung_kalori_invalid_gender_atau_usia(self):
        with self.assertRaises(ValueError):
            hitung_kalori_harian("pria", 70, 170, -10)
        with self.assertRaises(ValueError):
            hitung_kalori_harian("unknown", 70, 170, 25)

if __name__ == '__main__':
    unittest.main()
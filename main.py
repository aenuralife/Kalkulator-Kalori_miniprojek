def hitung_bmi(berat_kg, tinggi_cm):
    """
    Menghitung nilai BMI berdasarkan berat badan (kg) dan tinggi badan (cm).
    Rumus: BMI = berat / (tinggi_m ^ 2)
    """
    if berat_kg <= 0 or tinggi_cm <= 0:
        raise ValueError("Berat dan tinggi badan harus lebih besar dari 0.")
    
    tinggi_m = tinggi_cm / 100
    bmi = berat_kg / (tinggi_m ** 2)
    return round(bmi, 2)


def kategori_bmi(skor_bmi):
    """
    Mengembalikan kategori status gizi berdasarkan skor BMI.
    - < 18.5: Kurus
    - 18.5 - 24.9: Normal
    - 25.0 - 29.9: Kelebihan Berat Badan
    - >= 30.0: Obesitas
    """
    if skor_bmi < 0:
        raise ValueError("Skor BMI tidak boleh negatif.")
    elif skor_bmi < 18.5:
        return "Kurus"
    elif skor_bmi <= 24.9:
        return "Normal"
    elif skor_bmi <= 29.9:
        return "Kelebihan Berat Badan"
    else:
        return "Obesitas"


def hitung_kalori_harian(gender, berat_kg, tinggi_cm, usia):
    """
    Menghitung kebutuhan kalori harian dasar (BMR) menggunakan rumus Mifflin-St Jeor.
    - Pria: (10 * berat) + (6.25 * tinggi) - (5 * usia) + 5
    - Wanita: (10 * berat) + (6.25 * tinggi) - (5 * usia) - 161
    """
    if berat_kg <= 0 or tinggi_cm <= 0 or usia <= 0:
        raise ValueError("Berat, tinggi, dan usia harus angka positif.")
    
    gender_clean = gender.strip().lower()
    if gender_clean not in ["pria", "wanita"]:
        raise ValueError("Gender harus 'pria' atau 'wanita'.")
    
    bmr = (10 * berat_kg) + (6.25 * tinggi_cm) - (5 * usia)
    
    if gender_clean == "pria":
        return round(bmr + 5, 2)
    else:
        return round(bmr - 161, 2)
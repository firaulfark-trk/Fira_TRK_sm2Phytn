import math

# ============================================
# Soal Trigonometri - Tinggi Menara
# ============================================
# Dari sebuah titik A di tanah, seseorang melihat
# ke arah puncak sebuah menara dengan sudut elevasi
# 30 derajat. Jika jarak mendatar dari titik A ke
# kaki menara adalah 50 meter, berapakah tinggi
# menara tersebut?
# ============================================

# Diketahui
sudut_elevasi = 30  # derajat
jarak_mendatar = 50  # meter

# Konversi derajat ke radian (karena math.tan() menggunakan radian)
sudut_radian = math.radians(sudut_elevasi)

# Rumus: tan(sudut) = tinggi / jarak_mendatar
# Maka:  tinggi = tan(sudut) x jarak_mendatar
tinggi_menara = math.tan(sudut_radian) * jarak_mendatar

# Hasil eksak: 50*sqrt(3) / 3
tinggi_eksak = (50 * math.sqrt(3)) / 3

# Output
print("=" * 45)
print("  PENYELESAIAN SOAL TRIGONOMETRI")
print("  Menghitung Tinggi Menara")
print("=" * 45)
print()
print("  Diketahui:")
print(f"    - Sudut elevasi      = {sudut_elevasi} derajat")
print(f"    - Jarak mendatar     = {jarak_mendatar} meter")
print()
print("  Rumus:")
print("    tan(sudut) = tinggi / jarak mendatar")
print(f"    tinggi = tan({sudut_elevasi}) x {jarak_mendatar}")
print(f"    tinggi = {math.tan(sudut_radian):.4f} x {jarak_mendatar}")
print()
print("  Jawaban:")
print("    Tinggi menara = 50*sqrt(3) / 3")
print(f"    Tinggi menara = {tinggi_menara:.2f} meter")
print("=" * 45)

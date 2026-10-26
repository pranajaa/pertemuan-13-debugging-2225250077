def status(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


nilai = 60
print("Nilai:", nilai)
print("Status:", status(nilai))
print("Program konversi Suhu")
print("Nama : Ilham Wahyu Purnomo")
print("NIM  : 1306624066")
print("-" * 50)

while True:
    print("Silakan masukkan rentang suhu yang ingin Anda konversi.")
    print("Ketik 's' pada input pertama untuk keluar dari program.")
    
    try:
        masukan_awal = input("- Suhu awal = ")
        if masukan_awal.lower() == 's':
            print("\nProgram selesai. Terima kasih!")
            break

        suhu_awal = int(masukan_awal)
        suhu_akhir = int(input("- Suhu akhir = "))
        selang = int(input("- Selang     = "))

    except ValueError:
        print("\nInput tidak valid! Pastikan Anda memasukkan bilangan bulat.\n")
        continue

    if selang <= 0:
        print("\nNilai 'Selang' harus lebih besar dari 0.\n")
        continue
    
    print("\n           TABEL KONVERSI")
    print("+" + "-"*7 + "+" + "-"*12 + "+" + "-"*15 + "+" + "-"*18 + "+")
    print(f"| {'No.':<5} | {'Celcius':<10} | {'Reamur':<13} | {'Fahrenheit':<16} |")
    print("+" + "="*7 + "+" + "="*12 + "+" + "="*15 + "+" + "="*18 + "+")
    
    nomor = 1
    
    for celcius in range(suhu_awal, suhu_akhir + 1, selang):
        reamur = (4/5) * celcius
        fahrenheit = (9/5) * celcius + 32
        
        print(f"| {nomor:<5} | {celcius:<10} | {reamur:<13.2f} | {fahrenheit:<16.2f} |")
        nomor += 1
    
    print("+" + "-"*7 + "+" + "-"*12 + "+" + "-"*15 + "+" + "-"*18 + "+")
    print("\n")
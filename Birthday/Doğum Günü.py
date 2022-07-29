from datetime import date


def günAlma():
    print("********Doğum Günü Hesapla*********")
    try:
        gün = int(input("Doğum gününüz(0-31): "))
        ay = int(input("Doğduğunuz ay(0-12): "))
        yıl = int(input("Doğum yılınız: "))
        günSayısı = date(yıl,ay,gün)
        bugün = date.today()
        tarih = date(bugün.year,ay,gün)

        günFarkı = bugün - tarih
        yaşamGünü = bugün - günSayısı
        return günFarkı.days,yaşamGünü.days
    except Exception as ex:
            print(f"Lütfen geçerli değerler girin. Hata kodu {ex}")
       


def dogumgGunu(günler):
    if günler > 0:
        print(f"Doğum gününüz {günler} gün önce idi😊.")
    elif günler < 0:
        print(f"Doğum gününüz {günler} sonra 😊.")
    else:
        print(f"Doğum günün kutlu olsun 😊.")


def main():
    durum = True
    while durum:
        try:
            ogün,toplamGün = günAlma()
            dogumgGunu(ogün)
            print(f"{toplamGün}, gündür hayattasınız...😊 ")
        except Exception as ex:
            print(f"Lütfen geçerli değerler girin. Hata kodu {ex}")
        else:
            durum = False

main()
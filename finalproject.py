isim = "Kerem"
soyisim = "Uçar"
dersler = ["türkçe" , "ingilizce" , "matematik" , "biyoloji" , "beden eğitimi"]
alınankurs=[]
notlar={}
girishakkı = 3

while True :
        isim_gir = str(input("İsim Giriniz"))
        soyisim_gir = str(input("Soyisim Giriniz"))

        if isim_gir == isim and soyisim_gir ==soyisim:
                print(f"Welcome {isim} {soyisim}")
                sayi=int(input("kaç ders almak istersiniz(en az 3 ders en fazla 5 ders alabilirsiniz!"))
                if 3<=sayi<=5:
                        print("derslerimiz {}".format(dersler))
                        while sayi>0:
                                
                                dersadi=str(input("Dersin adını giriniz :")).lower()
                                if dersadi not in dersler:
                                        print("Böyle bir kurs yok! Tekrar yaz")
                                        sayi += 1
                                else:
                                        if dersadi in alınankurs:
                                                print("Bu mektubu daha önce hatırladım. Lütfen başka bir mektup tahmin et.")
                                                continue
                                        alınankurs.append(dersadi)
                                        print("Kayıt, kurslarınıza başarıyla eklendi...")
                                sayi -= 1
                        print(f"List of courses you have selected -> {alınankurs}")
                        sınavdersi=str(input("Sınava hangi dersten gireceksiniz? :")).lower()
                        sınavnot={}
                        vize=int(input(f"{sınavdersi} ara sınavdan aldığınız notu girin : "))
                        final=int(input(f"{sınavdersi} final sınavdan aldığınız notu girin : "))
                        proje=int(input(f"{sınavdersi} proje sınavdan aldığınız notu girin : "))
                        sınavnot["vize"] = vize
                        sınavnot["Final"] = final
                        sınavnot["Proje"] = proje

                        ortalama = ((vize*30)/100) + ((final*50)/100) + ((proje*20)/100)
                        if ortalama>90:
                                print(f"{sınavdersi} tebrikler notunuz AA")
                                break
                        elif 70<ortalama<90:
                                print(f"{sınavdersi} Tebrikler notunuz BB")
                                break
                        elif 50<ortalama<70:
                                print(f"{sınavdersi} Tebrikler notunuz CC")
                                break
                        elif 30<ortalama<50:
                                print(f"{sınavdersi} Tebrikler notunuz Dd.")
                                break
                        else:
                                print(f"{sınavdersi} üZGÜNÜM SINIFTA KALDINIZ NOTUNU FF ")
                                break

        
                else:
                        print("Kurs numaranız 3'ten az ise 5'ten fazla olamaz.")
                        break       

        elif (isim != isim_gir or soyisim != soyisim_gir) and girishakkı != 0:
                girishakkı=girishakkı-1
                print("Bilgileriniz hatalı")
                if girishakkı >0:
                        tekrar=input("tekrar denemek ister misinz? e/h")
                        if tekrar=="e":
                                print("buyrun deneyin")
                                continue
                        elif tekrar=="h":
                                print("daha sonra tekrar deneyin")
                                break
                else:
                        print("hakkınız kalmadı daha sonra tekrar deneyiniz")
                        break
        
        
        



                
        
                        

                



        
               







    










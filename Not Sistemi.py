#Öğrenci Otomsayonu
def ekleme():
    
    name=input("Öğrenci adı:")
    surname=input("Öğrenci soyadı:")
    number=input("Öğrenci numarası:")
    vize=input("Vize notu:")
    final=input("Final notu:")
    with open("Öğrenci_Bilgileri.txt","a",encoding="utf-8") as file:
       file.write(name+" "+surname+" "+number+":"+vize+","+final+ "\n")
        
    
    
def listeleme():
    with open("Öğrenci_Bilgileri.txt","r",encoding="utf-8") as file:
       for satir in file:
          print(not_hesaplama(satir))

def kaydetme():
    
    with open("Öğrenci_Bilgileri.txt","r",encoding="utf-8") as file:
       liste=[]
       for i in file:
           liste.append(not_hesaplama(i))
       with open("notsonuclari.txt","w",encoding="utf-8") as file2:
           for i in liste:
               file2.write(i)
           
       
def not_hesaplama(satir):
   satir=satir[:-1]
   liste=satir.split(":")

   name=liste[0]
   notlar=liste[1].split(",")

   vize=int(notlar[0])
   final=int(notlar[1])

   ortalama=(vize*0.4)+(final*0.6)
   if ortalama>=90 and ortalama<=100:
        harf = "AA"
   elif ortalama>=85 and ortalama<=89:
        harf = "BA"
   elif ortalama>=80 and ortalama<=84:
        harf = "BB"
   elif ortalama>=75 and ortalama<=79:
        harf = "CB"
   elif ortalama>=70 and ortalama<=74:
        harf = "CC"
   elif ortalama>=65 and ortalama<=69:
        harf = "DC"
   elif ortalama>=60 and ortalama<=64:
        harf = "DD"
   elif ortalama>=50 and ortalama<=59:
        harf = "FD"
   else:
        harf = "FF"
    
   if harf=="AA" or harf=="BA" or harf =="BB" or harf=="CB" or harf=="CC":
            Durum=" Başarılı"
   else:
           Durum=" Başarısız"
   return name + ": " + harf + Durum+ "\n"




while True:
    decision=input("1-Öğrenci ekleme\n2-Öğrenci Listeleme\n3-Kaydetme\n4-Çıkış\n5-Öğrenci Silme\nSeçiniz:")
    if decision=="1":
        ekleme()
    elif decision=="2":
        listeleme()
    elif decision=="3":
        kaydetme()
    elif decision=="4":
        break
    elif decision=="5":
        file_path = "Öğrenci_Bilgileri.txt"
        silinecek_satir =input("Siliceğiniz Satiri Giriniz:")

        with open(file_path, "r", encoding="utf-8") as dosya:
         satirlar = dosya.readlines()

        with open(file_path, "w", encoding="utf-8") as dosya:
         for satir in satirlar:
          if silinecek_satir not in satir:  
             dosya.write(satir)

        print(f"'{silinecek_satir}' içeren satır dosyadan silindi.")

    else:
        print("*************Geçersiz işlem**************")
        

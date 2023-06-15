Birinci_Rakam= float(input("Birinci rakamı giriniz : "))
islem= input("Yapmak istediğiniz işlemi giriniz : ")
İkinci_Rakam= float(input("İkinci rakamı giriniz : "))
if islem == "+" or islem == "Toplama":
  print(Birinci_Rakam+İkinci_Rakam)


elif islem == "-" or islem == "Çıkarma":
  print(Birinci_Rakam-İkinci_Rakam)


elif islem == "X" or islem == "x" or islem == "*" or islem == "Çarpma":
  print(Birinci_Rakam*İkinci_Rakam)


elif islem == "÷" or islem == "/" or islem == "Bölme":
  print(Birinci_Rakam/İkinci_Rakam)


elif islem == "**" or islem == "üs" or islem == "üssü" or islem == "üs alma":
  print(Birinci_Rakam**İkinci_Rakam)


elif islem == "//" or islem == "mod" or islem == "mod alma":
  print(Birinci_Rakam//İkinci_Rakam)


else:
  print("Geçersiz İşlem !")
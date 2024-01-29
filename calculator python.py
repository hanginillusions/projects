ilksayi = int(input("ilk sayiyi giriniz"))
ikincisayi = int(input("ikinci sayiyi giriniz"))
islem = input("""yapmak istediğiniz işlemi giriniz
(Toplama: +, Cikarma: -, Carpma: x, Bolme: /)
""")
if islem == "+":
    print("Sonuc "+str(ilksayi + ikincisayi))

elif islem == "-":
    print("Sonuc "+str(ilksayi - ikincisayi))    

elif islem == "x":
    print("Sonuc "+str(ilksayi * ikincisayi))

elif islem == "/":
    print("Sonuc "+str(ilksayi / ikincisayi))

 



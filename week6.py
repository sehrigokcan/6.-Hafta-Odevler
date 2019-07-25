##6. HAFTA ODEVLER
##
##
##
##ODEV 1: Sayi Tahmin
##
##		-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.
##
##		-Yazdiginiz kod ile bu sayiyi tahmin etmeye calisin.
##
##		-Tahmin sonucunda, kullanicidan alacaginiz input, pc'nin tahmin ettigi sayi kullanicinin belirledigi 
##
##		 sayidan buyukse kullanici daha dusuk sayi tahmin etmelisin manasinda "-" seklinde olsun, pc'nin tahmin 
##
##		 ettigi sayi kullanicinin belirledigi sayidan kucukse "+" seklinde olsun.
##
##		-Pc'nin tahmini dogru oldugunda da kullanicidan bunu belirtebilecegi bir input isteyin.
##
##		-Gelistireceginiz algoritma sayesinde kullanicinin belirledigi sayiyi en az hamlede bilmeye calisin :)

##
##		Ornek:
##
##
##
##			 Kullanicinin aklindan tuttugu sayi: 56 (kullanicidan bunun icin bir input almayacagiz sadece 
##
##			 aklinizdan bir sayi belirlemis iseniz oyunumuza baslayabiliriz seklinde bir input alabiliriz. 
##
##			 Yani belirledigi sayiyi sisteme girmesini istemiyoruz.)
##
##
##
##			 Pc'nin tahmini = 89
##
##			 Kullanicinin inputu = -
##
##			 Pc'nin tahmini = 45
##
##			 Kullanicinin inputu = +
##
##			 Pc'nin tahmini = 56
##
##			 Kullanicinin inputu = "Enter"

import random

print("Aklindan 1-100 arasi bir sayi tahmin et ben de bulayim :)\n\nEger tuttugun sayi buyukse -, kucukse +, dogruysa 'evet' yaziniz..")
input("Hazir miyiz(Hazirsaniz herhangi bir tusa basiniz...")
sayi=random.randint(1,100)  # ilk olarak sayim 1 100 arasi en genis aralikta olacak 
count=0  # tahmini saydiracagiz 
eksi=[100] 
arti=[1]
while True:
  count+=1 # tahmin sayiyisini arttir 
  print(count,". tahminim: ",sayi) 
  kontrol=input("Dogru mu:  ").lower()
  if kontrol=="-":
    eksi+=[sayi]
  if kontrol=='+':
    arti+=[sayi]
  if kontrol=="evet":
    print("Tahmin ettigin sayi {} imis..{} tahminimde bildim..".format(sayi,count))
    break
  eksi.sort()
  arti.sort()
  sayi=random.randint(arti[-1],eksi[0])  #veya   sayi=random.randint(max(arti),min(eksi))



##ODEV 2: XOX Oyunu
##
##		Kitapta yer alan XOX oyunu iki kisinin karsilikli oynayabilecegi sekilde duzenlenmis. Sizden bu oyunu 
##
##		kullanicinin bilgisayara karsi oynayabilecegi versiyonunu yapmanizi istiyoruz. Ayrica gelistireceginiz 
##
##		algoritma sayesinde bilgisayarin tamamen rastgele hamleler yapmasindan ziyade mantikli hamleler yapmasini 
##
##		saglamanizi istiyoruz. Ornegin bilgisayarin "O" hamlesini yaptigini varsayalim: 
##
##					X O _  
##
##					_ X _   
##
##					_ _ _
##
##
##		seklinde olusan bir durumda hamle sirasi bilgisayarda ve bilgisayar kaybetmemek icin sag-alt koseye "O" 
##
##		koymalidir.
##
##
##
##
##
##		Farkli bir ihtimal:
##
##					O X X 
##
##					O _ X 
##
##					_ _ _ 
##
##
##
##		boyle bir durumda da hamle sirasi bilgisayarda ve bilgisayar kazanma hamlesi olarak sol-alt koseye "O" koyarak 
##
##		oyunu bitirmelidir.


import random
tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

print("\n"*15)
for i in tahta:
  print("\t".expandtabs(30), *i, end="\n"*2)
kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]

x_y=[[0,0,0],[0,0,0],[0,0,0]]
y=[[0,0,0],[0,0,0],[0,0,0]]
x_durumu = []
o_durumu = []
sıra = 0
mumkun=[]
while True:
  if sıra % 2 == 0:
    işaret = "X".center(3)
    print()
    print("İŞARET: {}\n".format(işaret))
    x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
    x = int(x)-1
    if x == "q":
      break
    y = input("soldan sağa [1, 2, 3]: ".ljust(30))
    y = int(y)-1
    if y == "q":
      break
    if tahta[x][y] == "___":
      tahta[x][y] = işaret
      x_durumu += [[x, y]]
      sıra+=1
    else:
      print("\nORASI DOLU! TEKRAR DENEYİN\n")
  else:   # isaret 0 ise
    mumkun.clear()
    uzunluk=0
    işaret = "O".center(3)
    for i in range(3):  # bos olan tum alanlari mumkun listesine atiyoruz 
      for a in range(3):
        if tahta[i][a]=="___":  
          mumkun+=[[i,a]]
          print("mumkun",mumkun)
    
    i_durumu=[] 
    for i in kazanma_ölçütleri:
      
      x = [z for z in i if z in x_durumu]
      o = [z for z in i if z in o_durumu]

      if len(x)==2 or len(o)==2:  #eger kazanma olcutlerinin 2 elemaninda ayni deger varsa
        i_durumu.append(i)   #i_durumu listesine at 
        #print("i durumu:",i_durumu)

    rastgele1=[]  # kazanma olcutundeki listede 2 deger esitse bu listeye 
    rastgele2=[]  # degilse bu listeye rastgele deger atiayacagiz 
    if len(i_durumu)==0:   # eger i_durumu listesinde herhangi bir deger yoksa 
      rastgele2+=[random.choice(mumkun)]  #rastgele2 listesine herhangi bir bos alani at 
      #print("rastgele2",rastgele2)
    else:   # degilse yani i durumu listesinde herhangi 2 deger esitse 
      for a in i_durumu:  # i durumu elemanlarini ic ice listede kontrol ediyoruz 
        for b in a:
          if b in mumkun:  # eger 3.deger mumkun listesinde varsa yani bossa 
            rastgele1.append(b)  # rastgele1 listesine ekle 
            #print("rastgele1",rastgele1)
          else:   # degilse 
            rastgele2+=[random.choice(mumkun)]  # rastgele2 listesine at 
            #print("rastgele3",rastgele2)
    if len(rastgele1)==0:  # en son bakiyoruz rastgele1 listesinde eleman yoksa
      rastgele=random.choice(rastgele2)  # rastgele2 listesindeki herhangi bos alandan birini rastgele degerini esitle 
    else:  # degilse rastgele1 listesinden herhangi deger al 
      rastgele=rastgele1[-1]
      
    o_durumu+=[rastgele]  # o durumuna yaziyoruz 
    x=rastgele[0] 
    y=rastgele[1]
    tahta[x][y]="O".center(3)  # tahtaya O yerlestiriyoruz 
    sıra+=1   # sira Xte 
        
 

  print("\n"*7)
    
  for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)
  for i in kazanma_ölçütleri:    # kazanma olcutu kontrolu 
    o = [z for z in i if z in o_durumu]
    x = [z for z in i if z in x_durumu]
    if len(o) == len(i):    
      print("BEN KAZANDIM! :)")
      quit()
    if len(x) == len(i):
      print("SEN KAZANDIN!  ")
      quit()
    if len(o_durumu)==4 and len(x_durumu)==5:   # beraberlik durumu
      print("BERABERE KALDIK...")
      quit()









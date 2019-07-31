"""    
--- En Küçük Kareler Yöntemi ile Basit Doğrusal Regresyon ---


LİNEER (BASİT DOĞRUSAL) REGRESYONUN HER ADIMININDA NE OLDUĞUNU GÖRMEK
VE ALGORİTMANIN ANLAŞILMASI AÇISINDAN; HAZIR METODLARDAN KAÇINILARAK,
ALGORİTMA TAMAMEN EL YORDAMIYLA MANUEL FORMULLER İLE GERÇEKLEŞTİRİLMİŞTİR..

@author: omerkocadayi"""


"""    KÜTÜPHANELERİ    İMPORT    ET    """
import numpy as np
import matplotlib.pyplot as plt


"""    MANUEL    OLARAK    VERİ    OLUŞTUR    """
x = np.array([1990,1995,2000,2003,2006,2009,2012,2015,2017,2019])
y = np.array([12405,17319,26709,32104,47237,52621,61875,67098,70409,74398])

sumx , sumx2 , sumy , sumxy, hata, n = 0, 0, 0, 0, 0, np.size(x)
x2 , xy, normalizedx, normalizedy, denormalizedx, denormalizedy  = np.zeros(shape=(10)),np.zeros(shape=(10)),np.zeros(shape=(10)),np.zeros(shape=(10)),np.zeros(shape=(10)),np.zeros(shape=(10))

"""    X[i]Y[i] , X^2[i]    HESAPLAMALARI    """
for i in range(0,n):
    x2[i] = x[i] * x[i]
    xy[i] = x[i] * y[i]
    sumx += x[i]
    sumx2 += x2[i]
    sumy += y[i]
    sumxy += xy[i]
    
"""    DENKLEMİ    YAZ    """
print("\n--- En Küçük Kareler Yöntemi ile Basit Doğrusal Regresyon ---"
    "\nDenklem 1 -> T(y) = n.a + T(x).b         -> ",int(sumy)," = ",n,"a +",int(sumx),"b"
    "\nDenklem 2 -> T(x*y) = T(x).a + T(x^2).b  -> ",int(sumxy),"= ",int(sumx),"a +",int(sumx2),"b")


"""    DENKLEM ÇÖZÜMÜ / ÇÖZÜMDE YOK ETME METODU UYGULANMIŞTIR    """
yoket = sumx / n
newt , newb = sumxy - (yoket * sumy), sumx2 - (yoket * sumx)
a = newt / newb
b = (sumy - (sumx*a)) / n

print("\na -> ",a,"    b -> ",b,
    "\nRegresyon  Doğrusu  Denklemi  ->  Y = (",round(a,1),"x )  +  (",round(b,1),")")


"""    ÇİZİMİ    GERÇEKLEŞTİR    """
plt.title("Yıl - Nüfus Doğrusal Regresyon Çizimi")
plt.scatter(x, y, color = "m", marker ="o", s = 30)
y_pred = a*x + b
plt.plot(x, y_pred, color = "g")
plt.xlabel('YIL')
plt.ylabel('NÜFUS')
plt.show()


"""    NORMALİZASYON  ve DENORMALİZASYON  UYGULA    0-1  / HATA PAYI HESAPLA   """
print("\nNormalize X\tDenormalize X\t| Normalize Y\tDenormalize Y")
for i in range (0,n):
    normalizedx[i] = (x[i] - np.min(x)) / (np.max(x) - np.min(x)) 
    normalizedy[i] = (y[i] - np.min(y)) / (np.max(y) - np.min(y))
    denormalizedx[i] = normalizedx[i] * (np.max(x) - np.min(x)) + np.min(x)
    denormalizedy[i] = normalizedy[i] * (np.max(y) - np.min(y)) + np.min(y)
    print(round(normalizedx[i],2),"\t\t",round(denormalizedx[i],2),"\t|",round(normalizedy[i],2),"\t\t",round(denormalizedy[i],2))

tahmin = float(input("Son 10 nüfus sayımına göre;\n"
                     "Nüfus Tahminini İstediğiniz Yılı Giriniz : "))
print("\n***",int(tahmin),"YILI İÇİM NÜFUS BEKLENTİSİ",int((tahmin*a)+b),"'dir !!")
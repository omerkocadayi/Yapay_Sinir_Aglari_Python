"""
*** numpy.array ve numpy metodları kullanılarak kod yarı yarıya düşürülebilir.
FAKAT OLAYIN HER ADIMININDA NE OLDUĞUNU GÖRMEK VE İLERİ YÖNLÜ ve GERİ YAYILIM
ALGORİTMASININ ANLAŞILMASI AÇISINDAN; HAZIR METODLARDAN KAÇINILARAK,
ALGORİTMA TAMAMEN EL YORDAMIYLA MANUEL FORMULLER İLE GERÇEKLEŞTİRİLMİŞTİR..

'BEN OLAYI ANLAMAK İSTEMİYORUM, BU KADAR KARMAŞIKLIK BANA FAZLA'
DİYENLER İÇİN İNTERNETTE HAZIR METODLAR İLE YAPILMIŞ BİR SÜRÜ ÖRNEK MEVCUT :)

İYİ ÇALIŞMALAR..

@author: omerkocadayi""" 

""" KÜTÜPHANELERİ AL """
import math
import random
import numpy as np


""" GİRİŞLERİ AL """
girdiSayisi = int(input("Kaç adet girdi veriniz var : "))
beklenenDeger = float(input("Beklenen çıktı değeri (Küsürat için nokta kullanın) : "))
katmanSayisi = int(input("Ara katman kaç elemanlı olacak : "))


""" GEREKLİ DEĞİŞKEN TANIMLAMALARI """
deger, lamda, alfa, cnt, hata = 0, 0.7, 0.05, 0, 165416
girdiDizi, girdi_katman_agirlik, girdi_katman_degisim = [], [], []
arakatmanDizi, katman_cikti_agirlik, katman_cikti_degisim = [], [], []
sigma = np.zeros(shape=(katmanSayisi+1))


""" DİZİLERİ OLUŞTUR """
for i in range(0,1):           
    girdiDizi += [[0] *girdiSayisi]
    arakatmanDizi += [[0] *katmanSayisi]
for i in range(0,girdiSayisi):           
    girdi_katman_agirlik += [[0] *katmanSayisi]    
    girdi_katman_degisim += [[0] *katmanSayisi] 
for i in range(0,katmanSayisi):        
    katman_cikti_agirlik += [[0] *1]
    katman_cikti_degisim += [[0] *1]
    
    
""" GİRDİ-KATMAN AĞIRLIKLARINI OLUŞTUR """    
for i in range (girdiSayisi):
    girdiDizi[0][i] = float(input("%s. Girdi İçin Değer Giriniz (Küsürat için nokta kullanın) :"%(i+1)))
    for j in range (katmanSayisi):   
        girdi_katman_agirlik [i][j] = round(random.uniform(-1,1),2)
#print("Girdi - Ara Katman Ağırlıkları : ", girdi_katman_agirlik)        
     
        
""" ARA KATMAN ÇIKTILARINI HESAPLA """        
for i in range(1):
    for j in range(katmanSayisi):
        for k in range(girdiSayisi):
            deger += girdiDizi[i][k] *  girdi_katman_agirlik[k][j]
        arakatmanDizi[i][j] = 1 / (1+math.exp(deger*-1))
        deger = 0
#print("Ara Katman Çıktıları : ", arakatmanDizi) 
        
        
""" KATMAN-ÇIKTI AĞIRLIKLARINI OLUŞTUR """        
for i in range (katmanSayisi):
    katman_cikti_agirlik [i][0] = round(random.uniform(-1,1),2)
#print("Ara Katman - Çıktı Ağırlıkları : ", katman_cikti_agirlik)
    

""" GERİ YAYILIM ALGORİTMASINI UYGULA """
while not(cnt<1000 and round(hata,8) == 0.00000000):
    
    """ SONUCU HESAPLA """
    for i in range (katmanSayisi):
        deger += arakatmanDizi[0][i] *  katman_cikti_agirlik[i][0]
    cikti = 1 / (1+math.exp(deger*-1))      
    hata = beklenenDeger - cikti
    sigma[katmanSayisi] = cikti * (1-cikti) * hata
    deger = 0
    
    """ SONUCU YAZDIR """
    if(cnt == 0 or cnt % 100 == 0):
        print("\n",cnt,". İterasyon Sonuç Çıktısı : ",round(cikti,6),"\nHata : ",round(hata,8))
       
    """ ARA KATMAN - ÇIKTI AĞIRLIKLARINI GÜNCELLE """   
    for i in range (katmanSayisi):
        katman_cikti_degisim[i][0] = (lamda * sigma[katmanSayisi] * arakatmanDizi[0][i]) + (alfa * katman_cikti_degisim[i][0])
        sigma[i] = ( arakatmanDizi[0][i] * (1-arakatmanDizi[0][i]) ) * (katman_cikti_agirlik[i][0] * sigma[katmanSayisi])
        katman_cikti_agirlik[i][0] +=  katman_cikti_degisim[i][0]
    
    """ GİRDİ - ARA KATMAN AĞIRLIKLARINI GÜNCELLE """
    for i in range (girdiSayisi): 
        for j in range (katmanSayisi):
            girdi_katman_degisim[i][j] = (lamda * sigma[j] * girdiDizi[0][i]) + (alfa * girdi_katman_degisim[i][j])
            girdi_katman_agirlik[i][j] += katman_cikti_degisim[i][0]        
    
    cnt += 1
    
print("\n----\t----\t----\nGirdiler : ", girdiDizi,
    "\n\n----\t----\t----\nGirdi - Ara Katman Ağırlıkları\n", girdi_katman_agirlik,
    "\n\n----\t----\t----\nAra Katman Çıktıları : \n", arakatmanDizi,
    "\n\n----\t----\t----\nAra Katman - Çıktı Ağırlıkları\n", katman_cikti_agirlik,
    "\n\n----\t----\t----\n Çıktı : ", round(cikti,8),
    "\n----\t----\t----\t----\n",cnt," İTERASYONDA HATA ORANI 1 / 100.000.000'in ALTINA DÜŞTÜ !!!")
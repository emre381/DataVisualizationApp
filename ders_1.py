
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
veri=input("lütfen excel dosyasını giriniz")
df=pd.read_excel(f'{veri}.xlsx')
df['Tarih']= pd.to_datetime(df['Tarih'])
df.set_index('Tarih',inplace=True)

def ekran_temizleme():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')    

# menü fonksiyonu 
def menu():
    print("Grafik Seçenekleri")
    print("1- Satışların zaman içerisindeki değişimi (Çizgi grafiği)")
    print("2. Aylık toplam satışlar (bar grafiği)")
    print("3. Kategorilere göre satış dağılımı (pasta grafiği)")
    print("4. Fiyat ve satış ilişkisi (scatter plot)")
    print("5. Fiyat dağılımı (Histogram)")
    print("6. ylık satış miktarları (çizgi grafiği)")
    print("7. Fiyat kategörisine göre toplam saışlar (bar grafiği)")
    print("0. Çıkış")

    return int(input("Seçim yapınız :"))

# kullanıcın seçimlerine göre işlmeleri yapan fonksiyon 
def grafik_secim(secilen):
    if secilen == 1:
        df['Satış'].plot(title='Satışların zaman içerisindeki değişimi', xlabel='Tarih',ylabel='Satış Miktarı')
        plt.show()
    elif secilen==2:
        aylik_satis =df.resample('ME')['Satış'].sum()
        aylik_satis.plot(kind='bar',title='Aylık Toplam Satışlar',xlabel='Ay',ylabel='Toplam Satışı')
    elif secilen==3:
         kategori_satis = df.groupby('Kategori')['Satış'].sum()
         kategori_satis.plot(kind='pie',autopct='%1.1f%%',title='Kategori Bazlı Toplam Satışlar')
         plt.ylabel('') # y eksenin gizle 
         plt.show()
    elif secilen ==4:
        df.plot(kind='scatter',x=('Fiyat (TL)'),y='Satış',title='Fiyat satış ilişkisi')
        z=np.polyfit(df['Fiyat (TL)'],df['Satış'],1)
        p=np.poly1d(z)
        plt.plot(df['Fiyat (TL)'],p(df['Fiyat (TL)']),color='red')
        plt.show()
    elif secilen == 5:
        df['Fiyat (TL)'].plot(kind='hist',bins=10,title='Fiyat dağılımı',color='red')
        plt.xlabel('Fiyat (TL)')
        plt.show()
    elif secilen ==6:
        aylik_satis=df.resample('ME')['Satış'].sum()
        aylik_satis.plot(kind='line',title='Aylık Toplam Satışlar')
        plt.xlabel('Ay')
        plt.ylabel('Satış miktarı')
        plt.show()
    elif secilen==7:
        bins=[0,2000,5000,10000,20000,30000]
        labels=["düşük","orta","yüksek","çok yüksek","lüks"]
        df['Fiyat Kategorisi']=pd.cut(df['Fiyat (TL)'],bins=bins,labels=labels)
        # fiyat kategorisine göre satış dağılımı 
        df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar',title='Fiyat Kategorisine Göre Toplam Satışlar')
        plt.xlabel('Fiyat Kategorisi')
        plt.ylabel('Toplam Satış')
        plt.show()    
                                


while True:
    ekran_temizleme()
    secim=menu()
    if secim==0:
        print("Çıkış yapılıyor")
        break
    elif 1 <= secim<=7:
        grafik_secim(secim)
    else:
        print("Geçersiz seçim. Lütfen 1-7 arasında bir seçim yapınız")










#  zaman içerisinde bir çizgi grafiği göster
# df['Satış'].plot(title='Satışların zaman içerisindeki değişimi', xlabel='Tarih',ylabel='Satış')

# aylik_satis =df.resample('ME')['Satış'].sum()
# aylik_satis.plot(kind='bar',title='Aylık Toplam Satışlar',xlabel='Ay',ylabel='Toplam Satışı')

# pasta grafiği 
# kategori_satis = df.groupby('Kategori')['Satış'].sum()

# kategori_satis.plot(kind='pie',autopct='%1.1f%%',title='Kategori Bazlı Toplam Satışlar')

# plt.ylabel('') # y eksenin gizle 
# plt.show()

# scatter plot dağılım grafiği 
# df.plot(kind='scatter',x='Fiyat (TL)',y='Satış',title='Fİyat ve satış ilişkisi')
# plt.show()
# df['Fiyat (TL)'].plot(kind='hist',bins=10,title='Fiyat dağılımı')
# plt.xlabel('Fiyat (TL)')
# plt.show()

# aylik_satis=df.resample('ME')['Satış'].sum()
# aylik_satis.plot(kind='line',title='Aylık Toplam Satışlar')
# plt.xlabel('Ay')
# plt.ylabel('Satış miktarı')
# plt.show()
# df.plot(kind='scatter',x=('Fiyat (TL)'),y='Satış',title='Fiyat satış ilişkisi')
# z=np.polyfit(df['Fiyat (TL)'],df['Satış'],1)
# p=np.poly1d(z)
# plt.plot(df['Fiyat (TL)'],p(df['Fiyat (TL)']),color='red')
# plt.show()

# çok işimize yarayacak kod bloğu :D

# bins=[0,2000,5000,10000,20000,30000]
# labels=["düşük","orta","yüksek","çok yüksek","lüks"]
# df['Fiyat Kategorisi']=pd.cut(df['Fiyat (TL)'],bins=bins,labels=labels)
# # fiyat kategorisine göre satış dağılımı 
# df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar',title='Fiyat Kategorisine Göre Toplam Satışlar')
# plt.xlabel('Fiyat Kategorisi')
# plt.ylabel('Toplam Satış')
# plt.show()
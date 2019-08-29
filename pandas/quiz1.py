import pandas as pd
import numpy as np

df1 = pd.read_excel("quiz1-1.xlsx", 'py_science')
df2 = pd.read_excel("quiz1-1.xlsx", 'py_sense')
df3 = pd.read_excel("quiz1-1.xlsx", 'py_opinion')
df4 = pd.read_excel("quiz1-1.xlsx", 'py_mind')

print(df1.columns)
print(df1.isim.unique())
#df1.info()
#print(df1.describe())
ortalama_not1 = df1.D.mean()
print("science sinifinin ortalamasi: ", ortalama_not1)
#print(df1.D)



print(df2.columns)
print(df2.isim.unique())
df2.replace("girmedi",np.nan,inplace=True)
#df2.info()
#print(df2.describe())
ortalama_not2 = df2.D.mean()
print("sense sinifinin ortalamasi: ", ortalama_not2)


print(df3.columns)
print(df3.isim.unique())
df3.replace("girmedi",np.nan,inplace=True)
#df3.info()
#print(df3.describe())
ortalama_not3 = df3.D.mean()
print("opinion sinifinin ortalamasi: ",ortalama_not3)
df3.columns = [each.lower() for each in df3.columns]

print(df4.columns)
print(df4.isim.unique())
df4.replace("girmedi",np.nan,inplace=True)
#df4.info()
#print(df4.describe())
ortalama_not4 = df4.D.mean()
print("mind sinifinin ortalamasi: ", ortalama_not4)

df4.columns = [each.lower() for each in df4.columns]
sinif_ortalamalari={'py_science':ortalama_not1, 'py_sence':ortalama_not2,'py_opinion':ortalama_not3, 'py_mind':ortalama_not4}
#print(sinif_ortalamalari)
en_basarili_sinif=max(sinif_ortalamalari, key=sinif_ortalamalari.get)
print('en basarili sinif: ',en_basarili_sinif,'\nve ortalamasi: ',sinif_ortalamalari[en_basarili_sinif])


df = pd.read_excel("quiz1-1.xlsx", sheet_name=None, ignore_index=True)
cdf = pd.concat(df.values(),sort=False)
cdf.replace("girmedi",np.nan,inplace=True)
#cdf.columns = [each.lower() for each in df]#########
print(cdf)
ortalama_not=cdf.D.mean()
print(ortalama_not)


filtre1 = cdf.D.isnull() &  cdf.Y.isnull() &  cdf.B.isnull()
filtrelenmis_data = cdf[filtre1]
print("sinava girmeyen ogrenci listesi: \n", filtrelenmis_data)
#print( cdf.count())
print("sinava girmeyen ogrenci sayisi: ",filtrelenmis_data.isim.count())

print("sinava giren toplam ogrenci sayisi:", cdf.isim.count()-filtrelenmis_data.isim.count())


filtre2 = cdf.D.isnull()  | cdf.Y.isnull() | cdf.B.isnull()
filtrelenmis_data2 = cdf[filtre2]
print("dogru yanlis ve bos sayilari olanlarin sayisi:",cdf.isim.count()-filtrelenmis_data2.isim.count())


filtre=cdf.D.notnull() &cdf.Y.notnull() &  (cdf.B.isnull())
filtre_data= cdf[filtre]
print(filtre_data)
print("sadece dogru yanlis  sayilari olanlarin sayisi:",filtre_data.isim.count())


a=cdf.sort_values(by='D', ascending=False)
print("quiz1 de en basarili ilk uc kisi:")
print(a.values[0][0])
print(a.values[1][0])
print(a.values[2][0])







    
    
    
    
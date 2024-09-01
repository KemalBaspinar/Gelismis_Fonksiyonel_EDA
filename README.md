Gelişmiş Fonksiyonel Keşifçi Veri Analizi, elimizdeki büyük veya küçük ölçekli veri setlerine hızlı bir bakış atmamızı sağlar. Veri setlerinin yapısını, dağılımını ve temel ilişkilerini hızlı bir şekilde anlamak için kullanılan bir süreçtir. Fonksiyonel EDA araçları, bu süreci fonksiyonlar yardımıyla otomatikleştirerek veri bilimcilere zaman kazandırır ve daha derin içgörüler elde etmelerini sağlar.

Bu süreci 5 adımda inceleyeceğiz;

1- Genel Resim

2- Kategorik Değişken Analizi

3- Sayısal Değişken Analizi

4- Hedef Değişken Analizi

5- Korelasyon Analizi

Seaborn kütüphanesinde yer alan "mpg" veri seti üzerinde bu adımları gerçekleştirelim.

Veri Seti Hikayesi:

"mpg" veri seti, 1970'lerdeki araçların yakıt verimliliği, motor özellikleri ve diğer ilgili bilgilerini içerir. Veri setinde yer alan değişkenler şunlardır:

mpg: Araçların mil başına galon (yakıt verimliliği) değeri. 

cylinders: Araç motorundaki silindir sayısı.

displacement: Motor hacmi (santimetreküp cinsinden). 

horsepower: Motor gücü (beygir gücü cinsinden).

weight: Araç ağırlığı (pound cinsinden). 

acceleration: Araç hızlanması (0'dan 60 mil/saat hıza kadar geçen süre, saniye cinsinden). 

model_year: Araç model yılı. 

origin: Araç üretim yeri (örneğin, ABD, Avrupa, Japonya). 

name: Araç modelinin adı.

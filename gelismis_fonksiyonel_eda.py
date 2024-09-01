# Veri Setinin ve Kütüphanelerin Yüklenmesi
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("mpg")


# 1- Genel Resim

def check_df(dataframe, head=5):
    print("################ Shape ################")
    print(dataframe.shape)
    print("################ Types ################")
    print(dataframe.dtypes)
    print("################ Head ################")
    print(dataframe.head(head))
    print("################ Tail ################")
    print(dataframe.tail(head))
    print("################ NA ################")
    print(dataframe.isnull().sum())
    print("################ Quantiles ################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)

# 2- Kategorik Değişken Analizi

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"] ]

num_but_cat = [col for col in df.columns if df[col].nunique() < 15 and df[col].dtypes in ["int","float"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]

# 3- Sayısal Değişken Analizi

num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

num_cols = [col for col in df.columns if col not in cat_cols + cat_but_car]

# Değişkenlerin Yakalanması ve İşlemelrin Genelleştirilmesi
def grab_col_names(dataframe, cat_th = 15, car_th=20, ):
    """
    Veri setindeki kategorik, numeric ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        numerik fakat kardinal olan değişkenler için sınıf eşik degeri

    Returns
    -------
    cat_cols: list
        Kategirk değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    -------
    cat_cols + num_cols + cat_but_car = toplam_değişken_sayısı
    num_but_car cat_cols'un içerisinde.
    """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < cat_th and df[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > car_th and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in df.columns if col not in cat_cols + cat_but_car]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car

grab_col_names(df)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

# 4. Hedef Değişken Analizi

# Hedef Değişkenin Kategorik Değişkenler ile Analizi
def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}))

for col in cat_cols:
    target_summary_with_cat(df, "mpg", col)

# Hedef Değişkenlerin Sayısal Değişkenler ile Analizi
def target_summary_with_num(dataframe, target, numerical_col):
    print(pd.DataFrame(dataframe.groupby(target).agg({numerical_col:"mean"})))

for col in num_cols:
    target_summary_with_num(df, "mpg", col)

# 5. Korelasyon Analizi

corr = df[num_cols].corr()

sns.set(rc = {'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()





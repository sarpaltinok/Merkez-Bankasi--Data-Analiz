import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import f_regression

# TCMB EVDS API KEY
from evds import evdsAPI
api_key = input("Lütfen EVDS API anahtarınızı girin: ")
evds = evdsAPI(api_key)

# Veri setini çekiyoruz
data_series = ['TP.METALIHR.G71', 'TP.METALITH.G71', 'TP_GSYIH26_GY_CF', 'TP_REESAVANS_AFO', 'TP.DK.USD.A.YTL']
start_date = "01-01-2024"
end_date = "01-01-2025"
df = evds.get_data(data_series, startdate=start_date, enddate=end_date, frequency=5)

# İhracat - İthalat farkı hesapla
df['ITH_IHR_Farki'] = abs(df['TP_METALIHR_G71'] - df['TP_METALITH_G71'])

# Değişkenleri tanımla
variables = {
    'X1': 'ITH_IHR_Farki',
    'X2': 'TP_REESAVANS_AFO',
    'X3': 'TP_GSYIH26_GY_CF',
    'Y': 'TP_DK_USD_A_YTL'
}

X = df[[variables['X1'], variables['X2'], variables['X3']]].values
Y = df[variables['Y']].values

# Eksik veri doldurma
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)
Y = imputer.fit_transform(Y.reshape(-1, 1)).ravel()

# Veri setini eğitim/test olarak böl
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Lineer regresyon modeli oluştur ve eğit
model = LinearRegression()
model.fit(X_train, y_train)

# Tahminler
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Performans değerlendirme
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)
print("Eğitim Verisi R-Kare:", round(r2_train, 3))
print("Test Verisi R-Kare:", round(r2_test, 3))

# Düzeltilmiş R-Kare (Test Verisi)
n = X_test.shape[0]
p = X_test.shape[1]
adjusted_r2 = 1 - (1 - r2_test) * (n - 1) / (n - p - 1)
print("Düzeltilmiş R-Kare (Test Verisi):", round(adjusted_r2, 3))

# F ve P değerleri
f_vals, p_vals = f_regression(X_train, y_train)

# Katsayılar ve özet tablo
coefficients = model.coef_
intercept = model.intercept_

summary = pd.DataFrame({
    'Özellikler': [variables['X1'], variables['X2'], variables['X3']],
    'Katsayılar': coefficients,
    'F Değerleri': f_vals,
    'P Değerleri': p_vals
})

print("Intercept:", intercept)
print(summary)

# Görselleştirme: Her bir X değişkeni ile Y arasındaki ilişki
plt.figure(figsize=(12, 6))

for i, var in enumerate([variables['X1'], variables['X2'], variables['X3']]):
    plt.subplot(1, 3, i+1)
    plt.scatter(df[var], df[variables['Y']], color='blue')
    plt.xlabel(var)
    plt.ylabel('TCMB Dolar Alış Kuru')

plt.tight_layout()
plt.show()

# Gerçek vs Tahmin
plt.figure(figsize=(8, 6))
plt.scatter(y_train, y_train_pred, color='orange', label='Eğitim Verisi')
plt.scatter(y_test, y_test_pred, color='purple', label='Test Verisi')
plt.plot([min(Y), max(Y)], [min(Y), max(Y)], color='blue', lw=2)
plt.title('Lineer Regresyon: Gerçek vs Tahmin')
plt.xlabel('Gerçek Değerler')
plt.ylabel('Tahmin Değerleri')
plt.legend()
plt.show()

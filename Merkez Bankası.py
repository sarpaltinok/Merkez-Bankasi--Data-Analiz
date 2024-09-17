import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import f_regression

# TCMB EVDS API KEY
from evds import evdsAPI
api_key = input("Lütfen EVDS API anahtarınızı girin: ")  # Kullanıcıdan API anahtarını alıyoruz
evds = evdsAPI(api_key)


# DATA
data_series = ['TP.METALIHR.G71', 'TP.METALITH.G71', 'TP_GSYIH26_GY_CF', 'TP_REESAVANS_AFO', 'TP.DK.USD.A.YTL']
start_date = "01-01-2020"
end_date = "06-09-2022"
df = evds.get_data(data_series, startdate=start_date, enddate=end_date, frequency=5)

# İhracat ve İthalat Farkı 
df['ITH_IHR_Farki'] = abs(df['TP_METALIHR_G71'] - df['TP_METALITH_G71'])

# Değişkenler
variables = {
    'X1': 'ITH_IHR_Farki',
    'X2': 'TP_REESAVANS_AFO',
    'X3': 'TP_GSYIH26_GY_CF',
    'Y': 'TP_DK_USD_A_YTL'
}
X = df[[variables['X1'], variables['X2'], variables['X3']]].values
Y = df[variables['Y']].values

# IMPUTATION
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)
Y = imputer.fit_transform(Y.reshape(-1, 1)).ravel()

# TEST ve EĞİTİM
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Polinom
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Model Eğitme
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Tahminlerde Bulunma
y_train_pred = model.predict(X_train_poly)
y_test_pred = model.predict(X_test_poly)

# Performans Değerlendirmesi
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)
print("Eğitim Verisi R-Kare:", r2_train)
print("Test Verisi R-Kare:", r2_test)

# Düzeltilmiş R-Kare Hesaplama
n = X_test_poly.shape[0]
p = X_test_poly.shape[1] - 1
adjusted_r2 = 1 - (1 - r2_test) * (n - 1) / (n - p - 1)
print("Düzeltilmiş R-Kare (Test Verisi):", adjusted_r2)

# P- Value
f_vals, p_vals = f_regression(X_train_poly, y_train)
print("F Değerleri:", f_vals)
print("P Değerleri:", p_vals)

# Katsayılar
intercept = model.intercept_
coefficients = model.coef_
print("Intercept:", intercept)
print("Coefficients:", coefficients)

# Özet 
features = poly.get_feature_names_out()
summary = pd.DataFrame({
    'Özellikler': features,
    'Katsayılar': coefficients,
    'F Değerleri': f_vals,
    'P Değerleri': p_vals
})
print(summary)

# Grafikleri Oluşturma
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.scatter(df[variables['X1']], df[variables['Y']], color='blue')
plt.xlabel('İhracat-İthalat Farkı')
plt.ylabel('TCMB Dolar Alış Kuru')

plt.subplot(1, 3, 2)
plt.scatter(df[variables['X2']], df[variables['Y']], color='green')
plt.xlabel('Reeskont ve Avans Faiz Oranı')
plt.ylabel('TCMB Dolar Alış Kuru')

plt.subplot(1, 3, 3)
plt.scatter(df[variables['X3']], df[variables['Y']], color='red')
plt.xlabel('GSYİH')
plt.ylabel('TCMB Dolar Alış Kuru')

plt.tight_layout()
plt.show()

#  Görselleştirme
plt.figure(figsize=(10, 6))
plt.scatter(y_train, y_train_pred, color='orange', label='Eğitim Verisi')
plt.scatter(y_test, y_test_pred, color='purple', label='Test Verisi')
plt.plot([min(y_train), max(y_train)], [min(y_train), max(y_train)], color='blue', lw=2)
plt.title('2. Dereceden Çoklu Polinom Regresyon Analizi')
plt.xlabel('Gerçek Değerler')
plt.ylabel('Tahmin Değerleri')
plt.legend()
plt.show()



# TCMB Döviz Kuru Tahminleme Projesi

Bu proje, Türkiye Cumhuriyet Merkez Bankası (TCMB) verilerini kullanarak ABD Doları alış kurunu tahmin eden bir makine öğrenimi modelini içerir. Python ve ilgili kütüphaneler kullanılarak veri analizi, ön işleme, modelleme ve görselleştirme adımları gerçekleştirilmiştir. Proje kapsamında, çoklu polinom regresyon modeli oluşturulmuş ve modelin performansı değerlendirilmiştir.

## İçindekiler

- [Kurulum](#kurulum)
- [Veri Seti](#veri-seti)
- [Kullanılan Kütüphaneler](#kullanılan-kütüphaneler)
- [Proje Yapısı](#proje-yapısı)
- [Model Eğitimi ve Değerlendirme](#model-eğitimi-ve-değerlendirme)
- [Görselleştirmeler](#görselleştirmeler)
- [Sonuçlar](#sonuçlar)

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. **Python 3.x sürümünü kurun.**
2. Gerekli kütüphaneleri yüklemek için terminal veya komut satırında şu komutu çalıştırın:
    ```bash
    pip install numpy pandas matplotlib scikit-learn evds
    ```

3. **EVDS API anahtarı edinin:**
   Proje, TCMB'nin EVDS API'si ile veri çekmektedir. API anahtarınızı [EVDS](https://evds2.tcmb.gov.tr/) web sitesinden alabilirsiniz. API anahtarını kodda kullanmadan önce ilgili yere ekleyin.

## Veri Seti

Projede kullanılan veri serileri, TCMB EVDS API aracılığıyla çekilmiştir. Kullanılan veri serileri şunlardır:

- **TP.METALIHR.G71:** Metal İhracat Verisi
- **TP.METALITH.G71:** Metal İthalat Verisi
- **TP_GSYIH26_GY_CF:** Gayri Safi Yurtiçi Hasıla (GSYİH)
- **TP_REESAVANS_AFO:** Reeskont ve Avans Faiz Oranı
- **TP.DK.USD.A.YTL:** TCMB ABD Doları Alış Kuru

Veri serileri 01-01-2020 ile 06-09-2022 tarihleri arasındaki dönemi kapsamaktadır.

## Kullanılan Kütüphaneler

Projede aşağıdaki Python kütüphaneleri kullanılmıştır:

- `numpy`: Sayısal hesaplamalar için.
- `pandas`: Veri analizi ve veri çerçevesi işleme için.
- `matplotlib`: Veri görselleştirme için.
- `scikit-learn`: Makine öğrenimi modelleme ve metrik hesaplamaları için.
- `evds`: TCMB EVDS API'sinden veri çekmek için.

## Proje Yapısı

1. **Veri Çekme:** 
   - EVDS API kullanılarak belirlenen veri serileri çekilir ve bir veri çerçevesinde toplanır.

2. **Veri Ön İşleme:**
   - Eksik veriler `SimpleImputer` ile ortalama yöntemiyle doldurulur.
   - `PolynomialFeatures` ile polinom özellikler oluşturulur.

3. **Model Eğitimi:**
   - Çoklu polinom regresyon modeli eğitilir.
   - Eğitim ve test veri setleri kullanılarak modelin performansı değerlendirilir.

4. **Model Değerlendirme:**
   - Modelin R² skoru ve düzeltilmiş R² hesaplanır.
   - `f_regression` kullanılarak F ve P değerleri hesaplanır.

## Model Eğitimi ve Değerlendirme

Model, 2. derece polinom regresyon kullanılarak eğitilmiştir. Modelin performans metrikleri şunlardır:

- **Eğitim Verisi R-Kare:** Modelin eğitim setinde ne kadar iyi performans gösterdiğini ifade eder.
- **Test Verisi R-Kare:** Modelin test verisi üzerindeki genel başarımını gösterir.
- **Düzeltilmiş R-Kare:** Modelin test verisi üzerindeki başarımını düzeltilmiş R² ile değerlendirir.

Ayrıca, F ve P değerleri hesaplanarak bağımsız değişkenlerin anlamlılığı analiz edilmiştir.

## Görselleştirmeler

Modelin performansını ve bağımsız değişkenler ile bağımlı değişken arasındaki ilişkileri görselleştirmek için çeşitli grafikler oluşturulmuştur:

- İhracat-İthalat Farkı, Reeskont ve Avans Faiz Oranı, GSYİH ile TCMB Dolar alış kuru arasındaki dağılım grafikleri.
- Gerçek ve tahmin edilen değerlerin karşılaştırıldığı polinom regresyon analizi grafiği.

## Sonuçlar

Bu proje, TCMB verilerini kullanarak ABD Doları alış kurunu etkileyen bazı ekonomik göstergeler arasında anlamlı ilişkiler olduğunu göstermektedir. Model, polinom regresyon analizi ile döviz kuru tahminlerinde bulunmuş ve performansını R² ve düzeltilmiş R² metrikleri ile değerlendirmiştir.

---

Bu projeyi geliştirmek için verileri artırabilir, farklı modelleme teknikleri deneyebilir ve daha fazla bağımsız değişken ekleyebilirsiniz.

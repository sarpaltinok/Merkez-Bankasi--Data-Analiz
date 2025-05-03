# TCMB Döviz Kuru Tahminleme Projesi

Bu proje, Türkiye Cumhuriyet Merkez Bankası (TCMB) döviz kuru tahminleme amacıyla çeşitli ekonomik göstergeleri kullanarak USD/TRY kuru üzerine tahminler yapmayı hedeflemektedir. Projede lineer regresyon modeli kullanılmakta, verilerin temizlenmesi, özellik mühendisliği ve model değerlendirmesi adımları uygulanmaktadır.

> **Not:** Bu proje ilk olarak üniversite ödevi olarak hazırlanmış, sonrasında geliştirilerek revize edilmiştir.

## İçindekiler

- [Proje Hedefi](#proje-hedefi)
- [Kullanılan Veriler](#kullanılan-veriler)
- [Kullanılan Kütüphaneler](#kullanılan-kütüphaneler)
- [Modelin Eğitim ve Değerlendirilmesi](#modelin-eğitim-ve-değerlendirilmesi)
- [Kurulum Talimatları](#kurulum-talimatları)
- [Nasıl Kullanılır](#nasıl-kullanılır)
- [Lisans](#lisans)

## Proje Hedefi

Projenin amacı, TCMB'nin USD/TRY döviz kuru ile diğer ekonomik göstergeler arasındaki ilişkiyi modellemek ve bu ilişkiyi kullanarak tahminler yapmaktır. Modelin performansı, R² (R-kare) ve Düzeltilmiş R² metriği ile değerlendirilmiştir.

## Kullanılan Veriler

Veriler, Türkiye Cumhuriyet Merkez Bankası (TCMB) EVDS API’si kullanılarak çekilmiştir.

Kullanılan veri serileri:

| Veri | Kod | Açıklama |
|------|-----|----------|
| İhracat | TP.METALIHR.G71 | Metal İhracat Tutarı |
| İthalat | TP.METALITH.G71 | Metal İthalat Tutarı |
| GSYİH | TP_GSYIH26_GY_CF | Gayri Safi Yurt İçi Hasıla |
| Reeskont Faiz Oranı | TP.REESAVANS_AFO | Reeskont ve Avans Faiz Oranı |
| Dolar Alış Kuru | TP.DK.USD.A.YTL | USD/TRY Döviz Kuru (Alış) |

Kapsanan tarih aralığı: **01-01-2024** – **01-01-2025**

## Kullanılan Kütüphaneler

- `numpy` — Matematiksel işlemler
- `pandas` — Veri analizi ve manipülasyonu
- `matplotlib` — Veri görselleştirme
- `scikit-learn` — Makine öğrenmesi modelleri ve değerlendirme
- `evds` — TCMB EVDS API üzerinden veri çekme

## Modelin Eğitim ve Değerlendirilmesi

Veri seti eğitim (%80) ve test (%20) olarak ikiye ayrılmıştır. Projede aşağıdaki adımlar izlenmiştir:

1. **Veri Temizliği**: Eksik değerler, değişkenlerin ortalama değeri ile doldurulmuştur.
2. **Özellik Mühendisliği**: `İhracat - İthalat` farkı (`ITH_IHR_Farki`) hesaplanmıştır.
3. **Model Eğitimi**: Lineer regresyon modeli eğitilmiştir.
4. **Model Değerlendirmesi**: Modelin başarısı R² ve Düzeltilmiş R² metrikleri ile ölçülmüştür.
5. **İstatistiksel Analiz**: Modelin katsayıları, F-değerleri ve p-değerleri raporlanmıştır.

### Model Sonuçları

| Metrik | Değer |
|--------|-------|
| Eğitim Verisi R² | [Eğitim R² değeri] |
| Test Verisi R² | [Test R² değeri] |
| Düzeltilmiş R² (Test) | [Düzeltilmiş R² değeri] |

> **Not:** R² değerleri model çalıştırıldığında otomatik hesaplanmaktadır.

## Kurulum Talimatları

1. Python 3.x yüklü olduğundan emin olun.
2. Aşağıdaki komutu çalıştırarak bağımlılıkları yükleyin:

```bash
pip install numpy pandas matplotlib scikit-learn evds

Nasıl Kullanılır
TCMB EVDS API üzerinden ücretsiz API anahtarınızı alın.

Projeyi çalıştırın ve istendiğinde API anahtarınızı girin.

Model otomatik olarak veri çekip analiz yapacaktır.
 ```

## Nasıl Kullanılır
1. **TCMB EVDS API üzerinden ücretsiz API anahtarınızı alın.**
2. **Projeyi çalıştırın ve istendiğinde API anahtarınızı girin.**
3. **Model otomatik olarak veri çekip analiz yapacaktır**

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakabilirsiniz.


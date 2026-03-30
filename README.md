# Mystery Module - Quadratic Equation Solver

## 📋 Proje Özeti

**Mystery Module** çözmek gizli olan modülün işlevi Türkçe ve İngilizce belirtilmiştir. Bu modül, matematiksel ikinci dereceden denklemleri (quadratic equations) çözmek için kullanılır. Verilen katsayılardan denklemin gerçek köklerini bulmak için **Quadratic Formula** (ikinci dereceden denklem formülü) algoritmasını uygulamaktadır.

## 🎯 Amaç

Bu modül, aşağıdaki formatta ikinci dereceden denklemlerin köklerini bulur:

$$ax^2 + bx + c = 0$$

## 📚 İçerik

### Modüller ve Bağımlılıklar

```python
import math  # Karekök hesaplaması için
```

---

## 🔧 Fonksiyonlar

### `fn_x(a, b, c)`

İkinci dereceden denklemin köklerini hesaplar.

#### Parametreler

| Parametre | Tür     | Açıklama                                                         |
| --------- | ------- | ---------------------------------------------------------------- |
| `a`       | `float` | İkinci dereceden terimin katsayısı (x² katsayısı) - **0 olamaz** |
| `b`       | `float` | Birinci dereceden terimin katsayısı (x katsayısı)                |
| `c`       | `float` | Sabit terim                                                      |

#### Dönüş Değeri

- **Tuple[float, float]**: İki kökü içeren tuple → `(root1, root2)`
  - `root1`: Pozitif işaretli kök (büyük değer)
  - `root2`: Negatif işaretli kök (küçük değer)
- **None**: Diskriminant negatif ise (karmaşık kökleri vardır)

#### Matematiksel Temeli

Diskriminant hesaplaması:
$$\Delta = b^2 - 4ac$$

Kökleri bulma formülü:
$$x_1, x_2 = \frac{-b \pm \sqrt{\Delta}}{2a}$$

#### Çalışma Mantığı

1. **Diskriminant Hesaplama**: $\Delta = b^2 - 4ac$
2. **Diskriminant Kontrolü**:
   - Eğer $\Delta < 0$ → Gerçek kök yok → `None` döndür
   - Eğer $\Delta \geq 0$ → İki gerçek kök var → Kökler hesapla
3. **Kök Formülü Uygulaması**: Quadratic Formula kullanılır

---

## 💡 Kullanım Örnekleri

### Örnek 1: İki Farklı Gerçek Kök

İkinci dereceden denklem: $x^2 - 5x + 6 = 0$

```python
from mystery_module import fn_x

# a=1, b=-5, c=6
roots = fn_x(1, -5, 6)
print(roots)  # Çıkış: (3.0, 2.0)
```

**Doğrulama:**

- $x_1 = 3$: $3^2 - 5(3) + 6 = 9 - 15 + 6 = 0$ ✓
- $x_2 = 2$: $2^2 - 5(2) + 6 = 4 - 10 + 6 = 0$ ✓

### Örnek 2: Çift Kök (Tek Kök)

İkinci dereceden denklem: $x^2 - 4x + 4 = 0$

```python
roots = fn_x(1, -4, 4)
print(roots)  # Çıkış: (2.0, 2.0)
```

Diskriminant: $\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0$

### Örnek 3: Karmaşık Kök (Gerçek Kök Yok)

İkinci dereceden denklem: $x^2 + 2x + 5 = 0$

```python
roots = fn_x(1, 2, 5)
print(roots)  # Çıkış: None
```

Diskriminant: $\Delta = 2^2 - 4(1)(5) = 4 - 20 = -16 < 0$

### Örnek 4: Negatif Katsayılar

İkinci dereceden denklem: $2x^2 - 7x - 4 = 0$

```python
roots = fn_x(2, -7, -4)
print(roots)  # Çıkış: (4.0, -0.5)
```

Diskriminant: $\Delta = (-7)^2 - 4(2)(-4) = 49 + 32 = 81 = 9^2$

---

## 📊 Diskriminant Analizi Tablosu

| Diskriminant ($\Delta$) | Durum                 | Kök Sayısı | Fonksiyon Çıkışı     |
| ----------------------- | --------------------- | ---------- | -------------------- |
| $\Delta > 0$            | İki farklı gerçek kök | 2          | Tuple (root1, root2) |
| $\Delta = 0$            | Çift kök (tekil kök)  | 1          | Tuple (root, root)   |
| $\Delta < 0$            | Gerçek kök yok        | 0          | None                 |

---

## ⚠️ Sınırlamalar ve Bilmeniz Gerekenler

### 1. **a ≠ 0 Şartı**

```python
fn_x(0, 5, 3)  # ❌ Hata! a sıfır olamaz (0x² terim yok = lineer denklem)
```

### 2. **Başlangıç Kök Sırası**

Döndürülen tuple'da ilk kök her zaman daha büyüktür (pozitif işaretli).

### 3. **Sayısal Kesinlik**

Floating-point aritmetik sınırlamaları nedeniyle çok büyük veya çok küçük sayılarla çalışırken kesinlik problemleri olmabilir.

### 4. **Karmaşık Sayılar**

Diskriminant negatif olduğunda, karmaşık köklere erişim sağlanmaz. Bu durumda `None` döndürülür.

---

## 🛠️ Teknik Özellikler

- **Dil**: Python 3.x
- **Bağımlılıklar**: `math` modülü (built-in)
- **Fonksiyon Sayısı**: 1 ana fonksiyon (`fn_x`)
- **Kod Türü**: Procedural / Mathematical Utility

---

## 📝 Uygulama Senaryoları

1. **Fizik Problemleri**: Hareketli cisim yörüngesi hesaplamaları
2. **Mühendislik**: Yapısal analiz ve tasarım hesaplamaları
3. **Finans**: Kar-zarar analizi ve break-even noktası hesaplamaları
4. **Eğitim**: Öğrencilerin quadratic formula öğrenmesi

---

## 🎓 Matematiksel Arka Plan

### Quadratic Formula (İkinci Dereceden Denklem Formülü)

Herhangi bir ikinci dereceden denklem $ax^2 + bx + c = 0$ için kökleri bulmak için:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Bu formül, tüm ikinci dereceden denklemleri çözmek için evrensel bir yöntemdir.

### Diskriminant ($\Delta$)

Diskriminant değeri, denklemin kök sayısını ve türünü belirler:

- **$\Delta > 0$**: İki farklı gerçek kök (denklem x-ekseni ile iki noktada kesişir)
- **$\Delta = 0$**: Bir çift kök (denklem x-ekseni ile bir noktada teğet)
- **$\Delta < 0$**: Gerçek kök yok (denklem x-ekseni ile kesişmez)

---

## ✅ Kalite Kontrol

### Test Senaryoları

```python
# Test 1: Normal durum - iki farklı kök
assert fn_x(1, -5, 6) == (3.0, 2.0)

# Test 2: Çift kök
assert fn_x(1, -4, 4) == (2.0, 2.0)

# Test 3: Karen kök yok (diskriminant < 0)
assert fn_x(1, 2, 5) is None

# Test 4: Negatif katsayılar
assert fn_x(2, -7, -4) == (4.0, -0.5)
```

---

## 📚 Referanslar

- [Quadratic Formula - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_formula)
- [Discriminant - MathWorld](https://mathworld.wolfram.com/Discriminant.html)
- Python `math` Module Documentation

---

## 📄 Lisans

Bu proje eğitim amaçlı oluşturulmuştur.

---

## 👨‍💻 Yazar Notları

Mystery Module, ikinci dereceden denklemleri çözmek için basit fakat kuvvetli bir araçtır. Quadratic Formula'nın doğru uygulanması sayesinde, tüm ikinci dereceden denklemleri analitik olarak çözebilir.

**Son Güncelleme**: 30 Mart 2026

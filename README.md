# Zemberek Tabanlı Türkçe Chatbot

Bu proje, Zemberek doğal dil işleme (NLP) kütüphanesi kullanılarak geliştirilmiş bir Türkçe chatbot uygulamasıdır. Chatbot, kullanıcının girdiği metinleri analiz ederek Türkçe dil bilgisi hatalarını tespit eder, yaygın olarak yapılan hataları düzeltir ve kullanıcıyla doğal bir diyalog sürdürür. Projede ayrıca kelimelerin özel isim olup olmadığını belirlemek için Zemberek morfolojik analiz özelliği kullanılır ve özel isimlere yönelik düzeltme önerisi sunulmaz.

Chatbot ayrıca kullanıcı girdilerini SQL tabanlı bir veritabanına kaydeder, böylece bu girdilerin gelecekteki analiz ve incelemeler için saklanması sağlanır. Kullanıcıya hava durumu gibi bilgiler de sunulabilir ve bu bilgiler bir API üzerinden çekilir.

## Özellikler

- **Doğal Dil İşleme:** Zemberek kütüphanesi kullanılarak Türkçe metinlerin morfolojik analizi.
- **Yazım Hataları Düzeltme:** Yaygın yazım hataları ve kısaltmalar otomatik olarak düzeltilir.
- **Özel İsim Tanıma:** Özel isimler doğru bir şekilde tanınır ve düzeltilmez.
- **Veritabanı Entegrasyonu:** Kullanıcı girdileri SQL veritabanına kaydedilir.
- **API Entegrasyonu:** Hava durumu gibi bilgiler, API'ler üzerinden alınır ve kullanıcıya sunulur.

## Gereksinimler

- Python 3.x
- jpype1
- zemberek-nlp
- sqlite3
- requests

## Kurulum

1. **Depoyu klonlayın:**

2. **Gerekli bağımlılıkları yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Zemberek JAR dosyasını indirin ve projeye dahil edin:**
    - [Zemberek JAR İndir](https://github.com/ahmetaa/zemberek-nlp/releases)
    - JAR dosyasını `lib` klasörüne ekleyin ve `zemberek_jar_path` değişkenini güncelleyin.

4. **Veritabanını başlatın:**
    - `database.py` dosyasını çalıştırarak SQL veritabanını başlatın:
    ```bash
    python database.py
    ```

## Kullanım

1. **Chatbot'u çalıştırın:**
    ```bash
    python main.py
    ```

2. **Chatbot ile sohbet edin:**
    - Girdilerinizi terminal üzerinden yazın ve chatbotun verdiği yanıtlara bakın.
    - "evet" veya "hayır" gibi cevaplar vererek önerileri onaylayın ya da reddedin.

3. **Veritabanı Kayıtlarını Görüntüleyin:**
    - Veritabanında kayıtlı kullanıcı girdilerini incelemek için `main.py` dosyasındaki ilgili fonksiyonları kullanın.


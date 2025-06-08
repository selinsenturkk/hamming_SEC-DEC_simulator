# Hamming SEC-DED (Single Error Correcting - Double Error Detecting) Simülatörü

Bu proje, BTÜ Bilgisayar Mühendisliği BLM230 Bilgisayar Mimarisi dersi kapsamında, hata düzeltme kodlarını anlamak ve uygulamak amacıyla geliştirilmiştir. Hamming SEC-DED algoritması kullanılarak hem tek bit düzeltme, hem de çift bit tespit etme yapılmaktadır.

Bu çalışma, 8, 16 ve 32 bitlik veriler üzerinde Hamming SEC-DED algoritmasını uygulayan kullanıcı dostu bir grafiksel simülatördür. Python programlama dili ve tkinter arayüz kütüphanesi kullanılarak geliştirilmiştir.


---


## Özellikler

- 8, 16 veya 32 bitlik veriyi Hamming kodu ile belleğe yazma  
- Tek bit hatasını tespit edip otomatik düzeltme  
- Çift bit hatasını algılama (düzeltilemez olarak bildirir)  
- Bellekten veri okuma ve bit bozma  
- GUI üzerinden tüm işlemleri görsel olarak yapabilme  
- Simülasyonun çalışmasını gösteren demo video


---


## Nasıl Çalışır?

1. **Tkinter kütüphanesi** kullanılarak kullanıcı dostu bir arayüz geliştirilmiştir.  
   <img src="screenshots/img1.png" width="500"/>

2. Girilen veri, **'Kodla ve Belleğe Yaz'** butonuna basıldığında kodlanarak belleğe kaydedilir.  
   Uygulama yalnızca **8, 16 veya 32 bitlik** ikili verileri kabul eder. Aksi takdirde kullanıcıya uyarı mesajı gönderir.  
   <img src="screenshots/img2.png" width="500"/>
   <img src="screenshots/img6.png" width="500"/>

3. Arayüzün sol alt köşesindeki girdilere **adres** ve **bit konumu** girilir.  
   Eğer girilen adres veya bit konumu bellekte mevcut değilse hata mesajı gösterilir.  
   <img src="screenshots/img3.png" width="500"/>

4. Geçerli bir adres ve bit konumu girildikten sonra **'Bit Hatası Oluştur'** butonuna basılarak, ilgili konumda tek bitlik hata oluşturulur.  
   Ardından **'Analiz Et ve Düzelt'** butonuna basıldığında, sistem hatalı biti tespit eder ve otomatik olarak düzeltir.  
   <img src="screenshots/img4.png" width="500"/>

5. Aynı adreste **iki farklı bitte hata oluşturulmuşsa**, analiz sonucunda sistem kullanıcıya **'Çift Bit Hatası (düzeltilemez)'** uyarısı verir.  
   <img src="screenshots/img5.png" width="500"/>

6. Ayrıca bir adres girilerek **'Rastgele Double Bit Hatası Oluştur'** butonuna basıldığında, o adreste rastgele seçilen iki konumda çift bit hatası oluşturulur.


---


## Demo Videosu

Simülatörün çalışma videosunu [buradan](https://youtu.be/pI2KC0LIOi8) izleyebilirsiniz.

---

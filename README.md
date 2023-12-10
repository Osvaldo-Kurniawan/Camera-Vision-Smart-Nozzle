# RSBP Project

## Contributors

| Name              |NRP| GitHub Profile                       |
|-------------------|----------------------------|-------------------------------------|
| Gabrielle immanuel Osvaldo Kurniawan |5025211135| [Osvaldo](https://github.com/Osvaldo-Kurniawan)|
| Victor Gustinova |5025211159| [Victor](https://github.com/VictorGstn)|
| Rayssa Ravelia |5025211219| [Rayssa](https://github.com/rayrednet) |

## Deskripsi
Repository ini menyajikan implementasi sistem integrasi kamera yang dilengkapi dengan deteksi objek secara real-time oleh model object detection. Sistem ini memanfaatkan kamera web untuk menangkap frame, dan menggunakan model deteksi objek dari Roboflow API untuk mengidentifikasi objek pada setiap frame. Deteksi objek ini dapat berguna dalam pengenalan objek khusus.

## Fitur
- Deteksi Objek Real-Time:
Sistem ini mampu melakukan deteksi objek secara langsung pada frame yang ditangkap oleh kamera, memberikan informasi aktual tentang objek yang terdeteksi serta menggunakan thread untuk mengirim data ke roboflow.

- Integrasi dengan Roboflow:
Model deteksi objek yang digunakan dalam sistem berasal dari Roboflow, sebuah platform yang menyederhanakan penggunaan model machine learning untuk task deteksi objek.

- Subsidi Berdasarkan Jenis Mobil:
Sistem ini dapat mengenali jenis mobil tertentu, seperti "Honda Brio," "Honda Jazz," dan "Toyota Avanza," yang dapat digunakan sebagai indikator untuk memberikan subsidi atau tindakan khusus.

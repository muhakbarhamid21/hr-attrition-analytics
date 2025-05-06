# Proyek Pertama - Menyelesaikan Permasalahan Human Resources: Analisis Faktor Penyebab Tingginya Tingkat Attrition (Pengunduran) Karyawan Jaya Jaya Maju

- [Proyek Pertama - Menyelesaikan Permasalahan Human Resources: Analisis Faktor Penyebab Tingginya Tingkat Attrition (Pengunduran) Karyawan Jaya Jaya Maju](#proyek-pertama---menyelesaikan-permasalahan-human-resources-analisis-faktor-penyebab-tingginya-tingkat-attrition-pengunduran-karyawan-jaya-jaya-maju)
  - [Business Understanding](#business-understanding)
    - [Latar Belakang](#latar-belakang)
    - [Permasalahan Bisnis](#permasalahan-bisnis)
    - [Cakupan Proyek](#cakupan-proyek)
    - [Persiapan](#persiapan)
      - [Sumber data](#sumber-data)
      - [Setup environment](#setup-environment)
  - [Business Dashboard](#business-dashboard)
  - [Modeling \& Evaluation](#modeling--evaluation)
  - [Conclusion](#conclusion)
    - [Rekomendasi Action Items](#rekomendasi-action-items)

## Business Understanding

### Latar Belakang

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan beroperasi di berbagai sektor industri. Dengan jumlah karyawan lebih dari 1000 orang yang tersebar di berbagai kota di Indonesia, perusahaan ini memiliki kebutuhan manajemen SDM yang sangat tinggi.

Seiring dengan pertumbuhan perusahaan, tantangan dalam pengelolaan sumber daya manusia menjadi semakin signifikan. Salah satu isu krusial yang dihadapi adalah tingginya tingkat attrition (pengunduran diri karyawan), yang telah tercatat melebihi 10%. Angka ini berada di atas rata-rata normal dan berpotensi menimbulkan kerugian jangka panjang, baik dari sisi biaya rekrutmen ulang, hilangnya pengetahuan organisasi, hingga menurunnya produktivitas.

Dalam rangka meningkatkan efisiensi dan efektivitas pengelolaan SDM, departemen HR merasa perlu melakukan pendekatan berbasis data untuk mengetahui akar permasalahan dan mengambil langkah proaktif dalam mencegah tingginya angka pengunduran diri di masa depan. Oleh karena itu, dilakukanlah proyek ini dengan pendekatan data science dan visualisasi dashboard untuk membantu manajemen HR memahami situasi dan mengambil keputusan yang lebih tepat.

### Permasalahan Bisnis

Beberapa permasalahan utama yang diidentifikasi dan akan diselesaikan dalam proyek ini antara lain:

1. Tingginya tingkat attrition karyawan (>10%) yang berisiko mengganggu stabilitas operasional dan menambah beban biaya rekrutmen.
2. Tidak adanya sistem pemantauan visual (dashboard) yang membantu manajer HR dalam memantau tren dan faktor-faktor penyebab attrition secara real-time.
3. Kurangnya pemahaman berbasis data tentang faktor-faktor utama yang mendorong karyawan untuk mengundurkan diri, seperti usia, gaji, departemen, dan lain-lain.
4. Belum adanya sistem prediksi/klasifikasi risiko attrition yang dapat membantu HR dalam mengantisipasi karyawan yang berpotensi resign.

### Cakupan Proyek

Untuk menyelesaikan permasalahan di atas, proyek ini memiliki cakupan kerja sebagai berikut:

1. Data Preparation:
   - Memuat dan membersihkan dataset karyawan dari sumber data atau yang sudah disediakan.
   - Menangani data yang hilang dan menyiapkan variabel-variabel yang relevan.
2. Data Exploration dan Analisis:
   - Menganalisis tren dan pola attrition berdasarkan variabel seperti usia, jenis kelamin, gaji, jabatan, kepuasan kerja, lama bekerja, dan lain-lain.
   - Menampilkan korelasi antara faktor-faktor tersebut dengan status atrition (pengunduran diri).
3. Dashboard Interaktif:
   - Membuat dashboard untuk visualisasi data attrition dan faktor-faktornya.
   - Dashboard dapat diakses oleh tim HR dan digunakan untuk evaluasi berkala.
4. Modeling Machine Learning:
   - Membangun model prediksi/klasifikasi sederhana untuk memprediksi kemungkinan karyawan mengundurkan diri.
   - Menggunakan model yang dibangun sebagai alat bantu deteksi dini bagi HR.
5. Kesimpulan dan Rekomendasi Strategis:
   - Menyusun insight utama dari analisis.
   - Memberikan rekomendasi actionable yang dapat diimplementasikan oleh manajemen HR.

### Persiapan

#### Sumber data

Dataset yang digunakan dalam proyek ini berasal dari simulasi data karyawan perusahaan Jaya Jaya Maju dan telah disediakan oleh Dicoding melalui tautan resmi kelas yang terdapat pada link berikut: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee.

#### Setup environment

1. Clone repository atau copy project

   ```bash
   git clone https://github.com/muhakbarhamid21/project-hr-attrition.git
   ```

   ```bash
   cd project-hr-attrition
   ```

2. Buat virtual environment (opsional namun direkomendasikan)

   ```bash
   python -m venv venv
   ```

   - untuk macOS/Linux

     ```bash
     source venv/bin/activate
     ```

   - Untuk Windows

     ```bash
     venv\Scripts\activate
     ```

3. Install depencies

   ```bash
   pip install -r requirements.txt
   ```

## Business Dashboard

Business dashboard ini dibangun menggunakan Looker Studio untuk membantu departemen Human Resources (HR) Jaya Jaya Maju dalam memahami dan memantau fenomena tingginya tingkat attrition. Dashboard dirancang dengan dua halaman utama yang menyajikan pendekatan statistik deskriptif dan analisis prediktif berbasis machine learning, disertai elemen visual yang mudah dipahami.

URL Dashboard:
[https://lookerstudio.google.com/reporting/9b4af3f4-6c39-4688-b50a-f5815bf7d3de](https://lookerstudio.google.com/reporting/9b4af3f4-6c39-4688-b50a-f5815bf7d3de)

**Halaman 1: General Workforce Analytics (Statistical Overview of Employee Attrition & Retention):**

![Dashboard - Halaman 1](<Assets/muhakbarhamid21_-_HR_Attrition_Dashboard_(Jaya_Jaya_Maju)_1.jpg>)

Halaman pertama menampilkan analitik deskriptif untuk mengeksplorasi distribusi karyawan yang bertahan dan mengundurkan diri berdasarkan beberapa dimensi penting:

- Key Metrics Cards: Total karyawan, jumlah attrition, attrition rate, rata-rata usia, gaji bulanan, dan masa kerja rata-rata.
- Distribution Attrition: Diagram donut untuk memvisualisasikan proporsi attrition vs retention.
- Attrition by Department: Diagram batang horizontal menunjukkan distribusi attrition per departemen.
- Attrition by Job Role: Distribusi attrition per jabatan/role untuk mengetahui jabatan mana yang paling terdampak.
- Attrition by Age Generation: Donut chart berdasarkan kategori generasi (Gen Z, Y/Millennial, X).
- Attrition by Marital Status: Diagram batang horizontal yang menunjukkan hubungan antara status pernikahan dengan attrition.
- Attrition by Monthly Income: Visualisasi bertingkat untuk menggambarkan proporsi attrition dalam berbagai rentang pendapatan bulanan.

Fitur tambahan seperti filter interaktif department dan gender memungkinkan pengguna melakukan segmentasi data dengan fleksibel.

**Halaman 2: Attrition Prediction & Probability Analysis (Insights from Machine Learning-Based Forecasting):**

![Dashboard - Halaman 2](<Assets/muhakbarhamid21_-_HR_Attrition_Dashboard_(Jaya_Jaya_Maju)_2.jpg>)

Halaman kedua menyajikan hasil analisis prediktif yang dibangun dengan pendekatan machine learning menggunakan algoritma Stacking Ensemble pada tiga algoritma yaitu Logistic Regression, Random Forest, dan XGBoost. Tujuannya adalah untuk pengambilan keputusan berbasis prediksi. Adapun dimensi penting yang digunakan adalah:

- Key Metrics Cards: Sama dengan halaman pertama namun berdasarkan prediksi model.
- Distribution Attrition Prediction: Donut chart yang menunjukkan proporsi karyawan yang diprediksi akan resign vs bertahan.
- Correlation Factor (Numeric) by Attrition: Diagram batang vertikal menunjukkan korelasi antara fitur numerik (seperti DistanceFromHome, MonthlyIncome) dengan status attrition.
- Distance from Home by Attrition: Diagram batang vertikal untuk menunjukkan keterkaitan antara jarak rumah dengan kecenderungan attrition.
- Prediction Table: Tabel interaktif yang menampilkan informasi detail tiap karyawan meliputi: Employee ID, job role, total working years, income, probability attrition, dan prediksi akhir.

Tabel prediktif ini sangat membantu tim HR untuk fokus pada karyawan berisiko tinggi dan mengambil tindakan preventif.

## Modeling & Evaluation

Dalam proyek ini, dilakukan pengujian terhadap beberapa model machine learning untuk memprediksi kemungkinan seorang karyawan akan melakukan attrition (mengundurkan diri). Model-model yang digunakan antara lain:

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- Stacking Ensemble (gabungan dari ketiga model di atas) **[MODEL YANG DIGUNAKAN]**

**Evaluasi Model:**

Evaluasi dilakukan menggunakan metrik klasifikasi yang mencakup:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC AUC Score

Berikut ringkasan hasil evaluasi dari masing-masing model (menggunakan data validasi):

| Model                         | Accuracy  | Precision | Recall    | F1 Score  | ROC AUC   |
| ----------------------------- | --------- | --------- | --------- | --------- | --------- |
| Logistic Regression (Tuned)   | 0.712     | 0.338     | 0.722     | 0.460     | 0.811     |
| Random Forest (Tuned)         | **0.858** | **0.667** | 0.333     | 0.444     | 0.808     |
| XGBoost (Tuned + Thresh 0.35) | 0.844     | 0.560     | 0.389     | 0.459     | 0.814     |
| Stacking Ensemble             | 0.755     | 0.389     | **0.778** | **0.519** | **0.815** |

**Analisis Tiap Model:**

1. Logistic Regression (Tuned)
   - Recall sangat tinggi (0.72) → cocok untuk deteksi dini siapa yang mungkin keluar.
   - Precision rendah (0.34) → banyak false positive (karyawan diprediksi keluar, padahal tidak).
   - ROC AUC 0.811 → cukup bagus dalam memisahkan kelas keluar vs tidak.
   - Risiko: bisa menyebabkan over-alert di sistem HR (terlalu banyak orang yang “diperingatkan”).
2. Random Forest (Tuned)
   - Accuracy & Precision tertinggi.
   - Recall hanya 0.33 → artinya hanya mendeteksi 1 dari 3 karyawan yang keluar.
   - Cocok untuk strategi HR yang ingin memastikan prediksi positif benar, tapi tidak terlalu sensitif.
3. XGBoost (Tuned + Threshold 0.35)
   - Threshold tuning berhasil: Precision & Recall lebih seimbang dibanding RF.
   - ROC AUC sangat tinggi (0.814) → prediktif kuat.
   - Solusi “tengah” antara RF (akurasi tinggi) dan LogReg (recall tinggi).
   - Bisa digunakan untuk ranking risiko keluar karyawan.
4. Stacking Ensemble
   - Recall tertinggi (0.778) → terbaik dalam mendeteksi siapa yang keluar.
   - F1 Score tertinggi → menandakan keseimbangan precision & recall terbaik.
   - ROC AUC tertinggi (0.815) → paling baik memisahkan kelas.
   - Accuracy memang tidak tertinggi (0.755), tapi itu trade-off wajar untuk meningkatkan recall.
   - Ini adalah model paling stabil dan unggul secara keseluruhan.

## Conclusion

Melalui analisis data yang telah dilakukan dalam proyek ini, ditemukan bahwa tingkat attrition di perusahaan Jaya Jaya Maju berada pada angka yang cukup tinggi, yakni 16,92% berdasarkan data historis, dan bahkan diprediksi mencapai 29,52% jika mempertimbangkan kemungkinan pengunduran diri berdasarkan model machine learning. Angka ini menandakan bahwa attrition merupakan isu serius yang harus segera ditangani oleh departemen HR.

Berdasarkan hasil eksplorasi data dan visualisasi interaktif yang tersedia dalam dashboard, berikut beberapa temuan penting yang dapat disimpulkan:

1. Faktor-Faktor Demografis dan Profesional Mempengaruhi Attrition:
   - Karyawan dari generasi Millennial (Gen Y) dan Zoomers (Gen Z) menunjukkan kecenderungan attrition yang lebih tinggi dibandingkan generasi lainnya.
   - Pendapatan bulanan rendah (< $6.000) menjadi salah satu indikator utama karyawan berisiko tinggi untuk mengundurkan diri.
   - Departemen Sales dan beberapa job role teknis seperti Sales Executive dan Laboratory Technician memiliki angka attrition yang menonjol.
   - Status pernikahan juga berpengaruh, dengan karyawan yang belum menikah (single) cenderung lebih sering melakukan resign dibandingkan yang telah menikah.
2. Jarak Tempuh dan Aksesibilitas Terbukti Relevan:

   - Faktor Distance From Home memiliki korelasi tertinggi terhadap attrition berdasarkan analisis korelasi numerik. Menariknya, data justru menunjukkan bahwa semakin jauh jarak rumah ke kantor, semakin tinggi pula rasio attrition. Berikut adalah detail distribusi dan rasio attrition berdasarkan kategori jarak:

     | Jarak dari Rumah | Attrition | Non-Attrition | Total | Rasio Attrition       |
     | ---------------- | --------- | ------------- | ----- | --------------------- |
     | 0–5 km           | 174       | 458           | 632   | 174 / 632 ≈ **27.5%** |
     | 6–10 km          | 106       | 288           | 394   | 106 / 394 ≈ **26.9%** |
     | 20+ km           | 68        | 136           | 204   | 68 / 204 ≈ **33.3%**  |
     | 16–20 km         | 43        | 82            | 125   | 43 / 125 ≈ **34.4%**  |
     | 11–15 km         | 43        | 72            | 115   | 43 / 115 ≈ **37.4%**  |

   - Dari tabel tersebut terlihat bahwa kategori jarak 11–15 km memiliki rasio attrition tertinggi (37.4%), disusul oleh kategori 16–20 km. Ini dapat mengindikasikan bahwa jarak tempuh menengah hingga jauh menjadi beban tersendiri bagi karyawan, meskipun mereka belum berada pada titik yang sangat jauh (20+ km).
   - Temuan ini menyarankan bahwa strategi seperti fleksibilitas kerja (hybrid/WFH) atau kompensasi transportasi mungkin relevan untuk menurunkan risiko attrition pada kelompok ini.

3. Prediksi Machine Learning Meningkatkan Keakuratan Deteksi Risiko:
   - Model prediktif berbasis Stacking Ensemble (Logistic Regression, Random Forest, dan XGBoost) memberikan probabilitas attrition untuk setiap karyawan.
   - Tabel prediktif menunjukkan nama-nama karyawan dengan probabilitas lebih dari 0.5 atau yang di prediksi attrition yang sangat mungkin akan mengundurkan diri.
   - Dengan adanya skor prediksi dan probabilitas, HR dapat mengambil langkah proaktif terhadap individu tertentu (misalnya menawarkan promosi, pelatihan, atau komunikasi personal) sebelum mereka benar-benar resign.
4. Dashboard Memfasilitasi Pengambilan Keputusan Berbasis Data:
   - Dashboard dua halaman yang telah dibangun mampu menyajikan gambaran menyeluruh, mulai dari deskriptif hingga prediktif, dengan visualisasi yang intuitif dan filter interaktif.
   - Tim HR kini memiliki alat bantu yang real-time, terstruktur, dan berbasis data untuk menyusun strategi retensi yang lebih efektif.

Secara keseluruhan, proyek ini berhasil menjawab tantangan utama yang dihadapi departemen HR Jaya Jaya Maju. Dengan menggabungkan analisis eksploratif dan model prediksi, perusahaan kini mampu memahami akar permasalahan attrition serta mengantisipasi potensi risiko dengan pendekatan yang lebih strategis dan efisien.

### Rekomendasi Action Items

Berdasarkan hasil analisis data historis, evaluasi visualisasi statistik, serta hasil prediksi model machine learning terhadap risiko attrition, berikut adalah rekomendasi tindakan (action items) yang dapat diambil oleh manajemen Jaya Jaya Maju untuk mengurangi tingkat pengunduran diri karyawan secara signifikan:

1. Kebijakan Fleksibilitas Kerja untuk Karyawan dengan Jarak Tempuh Jauh
   - Alasan: Korelasi tertinggi dengan attrition ditemukan pada faktor jarak dari rumah. Karyawan yang tinggal 11–20 km dari kantor memiliki rasio pengunduran diri tertinggi (hingga 37.4%).
   - Tindakan:
     - Terapkan kebijakan hybrid working atau remote work untuk posisi yang memungkinkan.
     - Berikan subsidi transportasi atau akomodasi sementara bagi karyawan yang tinggal jauh.
2. Penyesuaian dan Segmentasi Gaji Berdasarkan Jabatan dan Masa Kerja
   - Alasan: Karyawan dengan pendapatan bulanan di bawah $6.000 memiliki tingkat attrition lebih tinggi. Ini mengindikasikan ketidakpuasan kompensasi.
   - Tindakan:
     - Lakukan benchmarking gaji per job role.
     - Evaluasi ulang skema kenaikan gaji untuk memastikan kompetitivitas pasar dan penghargaan terhadap masa kerja.
3. Program Retensi Khusus untuk Generasi Z dan Millennial
   - Alasan: Generasi muda (Gen Z dan Y) menunjukkan kecenderungan keluar yang lebih tinggi.
   - Tindakan:
     - Implementasikan career development plan yang lebih dinamis dan transparan.
     - Berikan program mentoring, pelatihan skill baru, atau rotasi kerja antar departemen untuk mencegah stagnasi.
4. Intervensi Dini Berdasarkan Hasil Prediksi Machine Learning
   - Alasan: Model prediksi mampu mengidentifikasi karyawan dengan risiko tinggi attrition berdasarkan skor probabilitas.
   - Tindakan:
     - Buat daftar employee risk watchlist dari hasil model.
     - Lakukan pendekatan proaktif seperti 1-on-1 counseling, diskusi karier, atau intervensi HR terhadap individu yang menunjukkan sinyal risiko tinggi.
5. Revitalisasi Iklim Kerja pada Departemen dan Job Role dengan Risiko Tinggi
   - Alasan: Data menunjukkan attrition tinggi di departemen Sales, serta job role seperti Sales Executive dan Lab Technician.
   - Tindakan:
     - Audit beban kerja dan beban target pada role dengan attrition tinggi.
     - Sediakan reward system, penghargaan pencapaian, serta mekanisme umpan balik dua arah.

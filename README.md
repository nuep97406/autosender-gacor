# BMKGSatu Autosender --> https://bmkgsatu.bmkg.go.id/ 
Script berbasis Python untuk Send GTS/Inaswitching dari data METAR dan SYNOP yang telah disubmit pada website BMKGSatu terlebih dahulu.

Otomatisasi execute scriptnya menggunakan **Task Scheduler** (Windows), atau yang lainnya sesuai dengan OS yang digunakan.

Contoh waktu trigger: 
Synoptik 03z - Waktu trigger (Task Scheduler) 12.00 WIT jika wilayah Indonesia Timur.\
Intinya yaitu waktu trigger sesuai dengan local time dimana pengiriman data dilakukan. Scriptnya akan mengonversi ke UTC di website BMKGsatu secara otomatis.\
\
Untuk tutorial pengoperasian Task Scheduler dan semacamnya dapat dicari di Internet atau bertanya melalui AI.

## Requirements
- Windows 10 or Up
- Python 3

## Dependencies
Script ini memerlukan beberapa module/package python untuk dapat menjalankannya, diantaranya:
- Selenium
- Webdriver_Manager

### Instalasi
`pip install selenium`\
`pip install webdriver_manager`

## Developer
Script ini dikembangkan oleh Danu (nuep) dari Sta. Met. Kelas III Gamar Malamo - Halmahera Utara (97406). Jika ada pertanyaan lebih lanjut silahkan hubungi melalui email berikut:\
[danu.danardi@bmkg.go.id](mailto:danu.danardi@bmkg.go.id)

## Important Notes
Disarankan memiliki internet yang **STABIL** dan device/computer yang **MUMPUNI**. Dikarenakan timing/kecepatan sangat mempengaruhi **keberhasilan** script autosender ini.

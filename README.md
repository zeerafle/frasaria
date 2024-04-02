# Frasaria

This tool is made to facilitate the workflow of paraphrasing text which consists of, input -> translate to English -> paraphrase -> translate to the original language.

This project uses Flask as an application provider and is deployed using Docker on GCP Cloud Run.

## How to Run

1. After cloning the repo, create a file called `.env`. Put your DeepL API key with following format.
    ```
    DEEPL_API_KEY=<your api key>
    ```
2. Install the dependencies.
    ```
    pip install -r requirements.txt
    ```
3. Run the application.
    ```
    flask run
    ```
4. Open [Postman](https://www.postman.com/) or any other API testing tool and send a POST request to `http://localhost:5000/paraphrase` with the following key and value for x-www-form-urlencoded.
    ```
    key: text
    value: <your text>
    ```
5. The response will be the paraphrased text in json.
    ```json
    {
         "paraphrased": "<your paraphrased text>"
    }
    ```

## Example

Input request:

```console
curl -X POST \
	'http://127.0.0.1:5000/paraphrase/' \
	-d 'text=Pada%20beberapa%20tahun%20terakhir,%20dampak%20serangan%20hama%20dan%20serangga%20pada%20budidaya%20kelapa%20sawit%20di%20Indonesia%20semakin%20meningkat.%20Selain%20itu,%20penyakit%20dan%20hama%20dari%20tanaman%20lain%20juga%20menjadi%20masalah%20penting%20di%20perkebunan%20kelapa%20sawit%20sehingga%20dapat%20mengancam%20masa%20depan%20industri%20kelapa%20sawit%20di%20Indonesia.%20Metode%20pengawasan%20penyakit%20tradisional%20memerlukan%20kunjungan%20lapangan%20dan%20diagnostik%20laboratorium%20sehingga%20dalam%20skala%20yang%20besar%20prosedurnya%20cukup%20menantang%20dan%20memakan%20banyak%20waktu%20serta%20membutuhkan%20pemeriksaan%20yang%20terus%20berlanjut%20oleh%20para%20ahli.%20Teknologi%20computer%20vision%20dan%20machine%20learning%20telah%20banyak%20dimanfaatkan%20untuk%20menerapkan%20aplikasi%20yang%20beragam%20di%20bidang%20agrikultur%20seperti%20pemantauan%20pertumbuhan,%20pemanenan%20otomatis,%20klasifikasi%20kualitas,%20dan%20deteksi%20penyakit.%20Penelitian%20ini%20mengusulkan%20penerapan%20computer%20vision%20dan%20machine%20learning%20untuk%20melakukan%20klasifikasi%20pada%20citra%20batang%20kelapa%20sawit%20yang%20sehat%20dan%20yang%20terinfeksi.%20Fitur%20citra%20diekstraksi%20menggunakan%20Convolutional%20Neural%20Network%20(CNN)%20ResNet%20pra-latih%20dan%20menghasilkan%202.048%20fitur.'
```

Output response:

```json
{
   "paraphrased": "dampak hama dan serangga pada budidaya kelapa sawit telah meningkat dalam beberapa tahun terakhir di indonesia. penyebaran penyakit dan hama dari tanaman lain juga menjadi masalah penting di perkebunan kelapa sawit yang mengancam masa depan industri kelapa sawit di indonesia. metode pengawasan penyakit tradisional membutuhkan kunjungan lapangan dan diagnosa laboratorium yang membuat prosedur ini menjadi sulit dan memakan waktu dalam skala besar dan membutuhkan pemeriksaan berkelanjutan oleh para ahli. Teknologi visi komputer dan pembelajaran mesin telah banyak digunakan di bidang pertanian untuk mengimplementasikan berbagai aplikasi seperti pemantauan pertumbuhan, klasifikasi kualitas panen otomatis, dan deteksi penyakit. penelitian ini bertujuan untuk menerapkan pembelajaran mesin dan visi komputer untuk mengklasifikasikan citra batang kelapa sawit yang sehat dan yang terinfeksi. fitur citra diekstraksi menggunakan jaringan syaraf tiruan cnn resnet yang telah dilatih sebelumnya dan menghasilkan 2048 fitur"
}
```
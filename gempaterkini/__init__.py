import requests
from bs4 import BeautifulSoup

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
})
def ekstraksi_data():
    """
    Tanggal :17 Februari 2024
    Waktu : 23:47:28 WIB
    Magnitude :4.1
    Kedalaman: 10 km
    Lokasi :8.38 LS - 114.49 BT
    Pusat gempa : berada dilaut 12 km BaratDaya Jembrana
    Dirasakan : Dirasakan (Skala MMI): III Banyuwangi, III Jembrana
    :return:
    """
    try:

    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"}
      # Sesuaikan URL
        content = session.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span',{'class':'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        lokasi = None

        dirasakan = None
        kedalaman = None



        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i+1


    # print(response.status_code)
    # soup = BeautifulSoup(response.content, 'html.'parser')
    # print(soup.prettify())

    hasil = dict()
    hasil['tanggal'] = tanggal
    hasil ['waktu'] =  waktu


    hasil ['magnitudo'] =  magnitudo
    hasil ['kedalaman'] = kedalaman
    hasil ['lokasi'] = lokasi
    hasil ['koordinat'] = {'ls':ls, 'bt':bt}

    hasil['dirasakan'] = dirasakan

    return  hasil

def tampilkan_data(result):
    print('Gempa Terakhir bedasarkan data BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi  {result['lokasi']}")
    print(f"Koordinat: LS= {result['koordinat']['ls']}, BT={result['koordinat']['bt']}")

    print(f"Dirasakan: {result['dirasakan']}")


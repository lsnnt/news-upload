from bs4 import BeautifulSoup
import requests
import time
import os
from supload import upload_to_scribd
from lastruntoupload import lr
def upnews(nurl,nname):
    try:
        res = requests.get(nurl)
        print("Downloading",nname,"...")
        soup = BeautifulSoup(res.text,"html.parser")

        url = soup.find_all('b')[0].find('a')
        if(url is not None):
            url = url['data-id']
            driveid = str(url).split("/")[5]

            response = requests.get(f"https://drive.usercontent.google.com/download?id={driveid}&export=download&confirm=t",stream=True)
            if response.status_code == 200:
                with open(f"{nname}-{time.strftime('%d-%m-%Y')}.pdf", "wb") as f:
                    for chunk in response.iter_content(8192):
                        f.write(chunk)
            print("Downloaded",nname)
            print("Uploading",nname,"...")
            try:
                return [upload_to_scribd(f"{nname}-{time.strftime('%d-%m-%Y')}.pdf"),f"{nname}-{time.strftime('%d-%m-%Y')}.pdf"]
            except Exception as e:
                print(e)
            
            print("Uploaded",nname)
            os.remove(f"{nname}-{time.strftime('%d-%m-%Y')}.pdf")
    except Exception as e:
        print(e)

if __name__ ==  "__main__":
    urls = ['https://epaperwave.com/download-the-economic-times-pdf-newspaper-free/', 'https://epaperwave.com/business-standard-epaper-pdf-free-download/', 'https://epaperwave.com/hindustan-times-epaper-pdf-today/', 'https://epaperwave.com/the-times-of-india-epaper-pdf-download/', 'https://epaperwave.com/the-statesman-newspaper-today-pdf-download/', 'https://epaperwave.com/financial-express-epaper-today-pdf-download/', 'https://epaperwave.com/download-today-the-new-indian-express-newspaper/', 'https://epaperwave.com/the-telegraph-epaper-today-pdf-download/', 'https://epaperwave.com/download-the-mint-epaper-pdf-for-free-today/', 'https://epaperwave.com/free-press-journal-epaper/', 'https://epaperwave.com/navbharat-times-epaper-delhi-pdf-download/', 'https://epaperwave.com/free-punjab-kesari-epaper-pdf-download-now/', 'https://epaperwave.com/amar-ujala-epaper-download-link-for-free/','https://epaperwave.com/dainik-bhaskar-epaper-today-pdf/', 'https://epaperwave.com/jansatta-epaper-today-pdf-download/', 'https://epaperwave.com/ei-samay-epaper-pdf-free-download/','https://epaperwave.com/karmasangsthan-paper-pdf-download/', 'https://epaperwave.com/karmakshetra-epaper-today-pdf/', 'https://epaperwave.com/today-andhra-jyothi-epaper-pdf-download/', 'https://epaperwave.com/download-today-eenadu-epaper-pdf-in-telegu/', 'https://epaperwave.com/pudhari-epaper-today-pdf/', 'https://epaperwave.com/maharashtra-times-epaper-today-pdf-download/', 'https://epaperwave.com/loksatta-epaper-today-pdf-download-for-free/', 'https://epaperwave.com/lokmat-epaper-pdf-free-download/']
    fd = ["economic-times","business-standard","hindustan-times","times-of-india","the-statesman","financial-express","indian-express","the-telegraph","the-mint","free-press-journal","navbharat-times","punjab-kesari","amar-ujala","dainik-bhaskar","jansatta","ei-samay","karmasangsthan","karmakshetra","andhra-jyothi","eenadu","pudhari","maharashtra-times","loksatta","lokmat"]
    flist = []
    oflist = []
    for i in range(len(urls)):
        new_var = upnews(urls[i],fd[i])
        flist.append(new_var[0])
        oflist.append(new_var[1])
    lr(flist,oflist)
    print("All news papers uploaded successfully")
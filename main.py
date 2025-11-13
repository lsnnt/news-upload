from bs4 import BeautifulSoup
import requests
import time
import os
from supload import upload_to_scribd

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
            upload_to_scribd(f"{nname}-{time.strftime('%d-%m-%Y')}.pdf")
            print("Uploaded",nname)
            os.remove(f"{nname}-{time.strftime('%d-%m-%Y')}.pdf")
    except Exception as e:
        print(e)

if __name__ ==  "__main__":
    urls = ['https://epaperwave.com/download-the-economic-times-pdf-newspaper-free/', 'https://epaperwave.com/the-hindu-analysis-today-pdf-download/', 'https://epaperwave.com/business-standard-epaper-pdf-free-download/', 'https://epaperwave.com/hindustan-times-epaper-pdf-today/', 'https://epaperwave.com/the-times-of-india-epaper-pdf-download/', 'https://epaperwave.com/the-statesman-newspaper-today-pdf-download/', 'https://epaperwave.com/financial-express-epaper-today-pdf-download/', 'https://epaperwave.com/orissa-post-epaper-pdf-download/', 'https://epaperwave.com/download-today-the-new-indian-express-newspaper/', 'https://epaperwave.com/the-telegraph-epaper-today-pdf-download/', 'https://epaperwave.com/download-the-mint-epaper-pdf-for-free-today/', 'https://epaperwave.com/free-press-journal-epaper/', 'https://epaperwave.com/navbharat-times-epaper-delhi-pdf-download/', 'https://epaperwave.com/free-punjab-kesari-epaper-pdf-download-now/', 'https://epaperwave.com/amar-ujala-epaper-download-link-for-free/', 'https://epaperwave.com/dainik-bhaskar-epaper-today-pdf/', 'https://epaperwave.com/dainik-bhaskar-epaper-today-pdf/', 'https://epaperwave.com/jansatta-epaper-today-pdf-download/', 'https://epaperwave.com/haribhoomi-epaper-today-pdf/', 'https://epaperwave.com/ei-samay-epaper-pdf-free-download/', 'https://epaperwave.com/ekdin-epaper-pdf-download/', 'https://epaperwave.com/karmasangsthan-paper-pdf-download/', 'https://epaperwave.com/karmakshetra-epaper-today-pdf/', 'https://epaperwave.com/sangbad-pratidin-epaper-today-pdf-download-link/', 'https://epaperwave.com/download-aajkaal-epaper-pdf-for-free/', 'https://epaperwave.com/today-andhra-jyothi-epaper-pdf-download/', 'https://epaperwave.com/download-today-eenadu-epaper-pdf-in-telegu/', 'https://epaperwave.com/pudhari-epaper-today-pdf/', 'https://epaperwave.com/maharashtra-times-epaper-today-pdf-download/', 'https://epaperwave.com/loksatta-epaper-today-pdf-download-for-free/', 'https://epaperwave.com/lokmat-epaper-pdf-free-download/', 'https://epaperwave.com/sambad-epaper-today-pdf-download/', 'https://epaperwave.com/dharitri-epaper-today-pdf/', 'https://epaperwave.com/orissa-post-epaper-pdf-download/']
    fd = ["economic-times","the-hindu","business-standard","hindustan-times","times-of-india","the-statesman","financial-express","orissa-post","indian-express","the-telegraph","the-mint","free-press-journal","navbharat-times","punjab-kesari","amar-ujala","dainik-bhaskar","dainik-bhaskar","jansatta","haribhoomi","ei-samay","ekdin","karmasangsthan","karmakshetra","sangbad-pratidin","aajkaal","andhra-jyothi","eenadu","pudhari","maharashtra-times","loksatta","lokmat","sambad","dharitri","orissa-post"]
    for i in range(len(urls)):
         upnews(urls[i],fd[i])

import requests
import datetime
import os

url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
r = requests.get(url,stream = True)

currentDT = datetime.datetime.now()

try:
    os.makedirs("./Database/")
except FileExistsError:
    pass

with open('./Database/'+str(currentDT)+'.pdf', 'wb') as fd:
    for chunk in r.iter_content(2000):
        fd.write(chunk)
        

        
        
from zipfile import ZipFile 
import os 
  
def get_all_file_paths(directory): 
    file_paths = [] 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
    return file_paths         
  

def main(): 
    directory = './Database/'
    file_paths = get_all_file_paths(directory)  
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 
  
    with ZipFile('my_pdf_files.zip','w') as zip: 
        for file in file_paths: 
            zip.write(file) 
  
    print('All files zipped successfully!')         
  
if __name__ == "__main__": 
    main() 
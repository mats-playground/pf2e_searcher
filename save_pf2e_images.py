from bs4 import BeautifulSoup
import urllib.request
import requests
import shutil

def check_suffix(url_request):
    if url_request.status_code == 200:
        return True
    else:
        return False

def find_image(url_request):
    soup = BeautifulSoup(url_request.content, 'html5lib')
    for img in soup.findAll('img'):
        if url_request.url.split('/')[-1].split('.')[0] in img.get('src'):
            return img.get('src').split('\\')[-1]
    else:
        return None
    

def get_tokens(html_prefix, start=881, end=2000):
    no_img = []
    no_ids = []
    all_pass_no_img = []
    
    for i in range(start, end):
        html_url = html_prefix + '.aspx?ID=' + str(i)
        html = requests.get(html_url, stream = True)
        
        id_exists = check_suffix(html)
        image_name = find_image(html)
        
        if (id_exists) & (image_name == None):
            no_img.append(html_url)
            print('No image: ' + str(i))
            
        elif (id_exists == False) & (image_name == None):
            no_ids.append(html_url)
            print('No id: ' + str(i))
            
        elif (id_exists == False) & (image_name != None):
            return 'Something broke!'
        
        elif (id_exists) & (image_name != None):
            img = requests.get(html_prefix.split('/')[0] + '//' + html_prefix.split('/')[2] + '/Images/' + '/'.join(html_prefix.split('/')[3:]) + '/' + image_name, stream=True)
            
            if img.status_code == 200:
                img.raw.decode_content = True
                
                with open('bestiary/' + html_prefix.split('/')[-1] + '/' + image_name, 'wb') as f:
                    shutil.copyfileobj(img.raw, f)
                
                print('Image Successfully Downloaded: ' + image_name)
            
            else:
                print('Image Couldn\'t Be Retrieved: ' + image_name + ' with error ' + str(img.status_code))
                all_pass_no_img.append(image_name)
                
    return no_img, no_ids, all_pass_no_img

prefix = 'https://2e.aonprd.com/NPCs'

no_img, no_ids, all_pass_no_img = get_tokens(prefix)
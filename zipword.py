import zipfile
import time

folderpath = input("path of the folder: ")
folderpath = folderpath.strip()
zipf = zipfile.ZipFile(folderpath)
global result
result = 0
global tried
tried = 0
c=0

if not zipf:
    print("The File/Folder is not password protected ! You can access easily!")
else:
    starttime=time.time()
    wordListFile = open('wordlist.txt','r',errors='ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')
    for i in range(len(words)):
        word = word[i]
        password=word.encode('utf8').strip()
        c=c+1
        print('Trying to decode the password by:{}'.format(word))
        try:
            with zipfile.ZipFile(folderpath,'r') as zf:
                zf.extractall(pwd=password)
                print("success! the password is:"+word)
                endtime = time.time()
                result= 1
            break
        except:
            pass

if(result==0):
    print("Sorry password not found. A total of"+str(c)+"possible combination tried in"+str(endtime)+"seconds.")
else:
    duration=endtime - starttime
    print("Congrulation! password find after trying"+str(c)+"combination in"+str(duration)+"seconds.")
    

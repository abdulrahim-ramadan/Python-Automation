#Das Code schaut, was gibt in Data drin Mitnahme und was von Typ ist er(pdf oder TXT )
#print(filename)
#print(f"file:{filename},Extension:{file_extension}")
#print('-------')

#-----------------------------------------------------

#Bei zweite Code er schaut was vom Typ, ist er ohne Name
#print(filename)
#print(file_extension)
#print('-------')

#------------------------------------------------------

#Der Bibliothek bei Python muss immer ganz oben sein damit deine komplette code das nimmt
'''
import os
from pathlib import Path
import shutil

#normal code hard disk 

os.chdir('data')




for filename in os.listdir('.'):
    
        file_extension = os.path.splitext(filename)[1]

        

        if file_extension.lower() in ['.png','.jpg','.jpeg','.webp']:
            Path("images").mkdir(parents=True, exist_ok=True)
            shutil.move(filename,'images')
            

        elif file_extension.lower() in ['.py','.pdf','.txt','.yml','.md']:
            Path("Documents").mkdir(parents=True, exist_ok=True)
            shutil.move(filename,'Documents')


        elif file_extension.lower() in ['.rar']:
            Path("Archives").mkdir(parents=True, exist_ok=True)
            shutil.move(filename,'Archives') 
'''


#Verbesserte Code orgnize hard disk #

import os
from pathlib import Path
import shutil

os.chdir('data')




#create folders
folders =["imges","Documents","Archives"]
for f in folders :
    Path(f).mkdir(parents=True, exist_ok=True)



#organize
for filename in os.listdir('.'):
    file_extension = os.path.splitext(filename)[1]

    if file_extension.lower() in ['.png','.jpg','.jpeg','.webp']:
        shutil.move(filename,'images')
            

    elif file_extension.lower() in ['.py','.pdf','.txt','.yml','.md']:
        shutil.move(filename,'Documents')


    elif file_extension.lower() in ['.rar']:
        shutil.move(filename,'Archives') 

    



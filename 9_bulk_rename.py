import os
os.chdir('C:\\Users\\User\\Desktop\\Ai\\day 12\\Code (5)\\Code\\simple_images\\Zoro')
i=1
for file in os.listdir():
    src=file
    dst="Zoro"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1


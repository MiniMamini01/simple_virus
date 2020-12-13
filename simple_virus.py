import os 

def search(path):
    my_final_list = []
    files = os.listdir(r'C:\Users\minim\Desktop\test1')
    for element in files:
        if os.path.isdir(path + "\\" + element) == True:
            open(path+ '\\' + element + '\\'+ 'i am virus.txt' , 'x')
            wf = open(path + '\\' + element + '\\' + 'i am virus.txt' , 'w')
            wf.write('< i am a simple virus , hello > ')
            wf.close()
        elif element[-4:] == '.txt':
            rf = open(path + '\\' + element , 'r')
            tmp = rf.read()
            af = open(path + '\\' + element , 'w')
            af.write('<i am a simple virus , hello >' + tmp )
        else:
            pass  
        
search(r'C:\Users\minim\Desktop\test1')

#minimamini

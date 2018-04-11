import random
"""
We ask users how can view your password
"""

def questPassw(quess):
    if quess =='light':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))for x in range (6)]))
    elif quess=='middle':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))for x in range (9)]))
    elif quess=='strong':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))for x in range (12)]))
    else:
       print('ERROR')
       quess=input('How Secure must have light/middle/strong : ')
       password=questPassw(quess)
    return password 
       
       
    

def informationAboutPassword(a):
    countNumber=0
    countLitle=0
    countBig=0
    listBLetter=[]
    listSmallLette=[]
    listNumber=[]
    print("Size your password = {}".format(len(a)))
    print ('- - -'*5)
    print("Your password start with = {}".format(a[0]))
    print ('- - -'*5)
    print("The end your password  = {}".format(a[-1]))
    print ('- - -'*5)
    print("Your password = {} ".format(a))
    print ('- - -'*5)
    
    for j in range(0,len(a)):
        for i in ['1','2','3','4','5','6','7','8','9']:
            if(a[j]==i):
               listNumber.append(i)
               countNumber=countNumber+1
                
    print ("Number of digits in the password ={} ".format(countNumber))
    print("Your password has a digits={}".format(listNumber))
    print ('- - -'*5)

    for j in range(0,len(a)):
        for i in ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
            if(a[j]==i):
                listSmallLette.append(i)
                countLitle=countLitle+1
                
    print ("Number of little letters  in the password = {}".format(countLitle))
    print("Your password has a little letter = {}".format(listSmallLette))
    print ('- - -'*5)
    
    for j in range(0,len(a)):
        for i in ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']:
            if(a[j]==i):
                listBLetter.append(i)
                countBig=countBig+1
                
    
    print ("Number of Big letters  in the password = {}".format(countBig))
    print("Your password has a big letter ={}".format(listBLetter))
    print ('- - -'*5)
    
def funHello():
    print('Hello, friend :)')
    name=input('What is your name ? ')
    print('{} ,nice to meet you '.format(name))
    
funHello()
quess=input('How Secure must have light/middle/strong : ')
yourPassword=questPassw(quess)
question= input('Do you want show on the screen your password (yes/no)?')
if (question == 'yes'):
    informationAboutPassword(yourPassword)
else:
     print('See you late :)')
  

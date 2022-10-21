import webbrowser as we
import wikipedia
import pyttsx3
engine = pyttsx3.init()

q = 0
wikipedia.set_lang('ru')
print(''')



''')

while True:
    try:
        while True:
            s = input(">>>>>>")

            #if fuzz.WRatio('Привет наш мир',s) >= 93:
            #    print(a)

            #a = fuzz.WRatio('Привекуепкупуру',s)
            #if a >= 93:
            #    print(a)
            if q == 0: 

                df = wikipedia.search(s, results=11)

                if len(df) == 0:
                    continue
                
                print('1)',df[0])
                print('   ')
                print('2)',df[1])
                print('   ')
                print('3)',df[2])
                print('   ')
                print('4)',df[3])
                print('   ')
                print('5)',df[4])
                print('   ')
                print('6)',df[5])
                print('   ')
                print('7)',df[6])
                print('   ')
                print('8)',df[7])
                print('   ')
                print('9)',df[8])
                print('   ')
                print('10)',df[9])
                print('   ')
                print('11)',df[10])
                print('''
                
                
                ''')
                fd = input("123456>>>>>")
                if fd.find('й') != -1:
                    fd = fd.replace('й','')
                    fd = int(fd)
                    grhg = df[fd-1]
                    grhg = str(grhg)
                    grhg = grhg.replace(' ','_')
                    we.open('https://ru.wikipedia.org/wiki/{}'.format(grhg))
                    print('https://ru.wikipedia.org/wiki/{}'.format(grhg))
                if type(fd) != 'int':
                    fd = int(fd)

                gh = wikipedia.summary(df[fd -1])
                gh = str(gh)
                print(gh)
                engine.say(gh)
                engine.runAndWait()
            print('''



            ''')
    except:
        print('!!!')
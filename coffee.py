coffee = {
    'shokolad':3000,
    'shakar':3000,
    'sut':5000,
    "suv":5000,
    'qahva':4000,
    'Tangalar':{
      '100':100,
      '50':200,
      '10':500
    },
    'Qahvalar':{
      'Americano':3000,
      'Latte':4000,
      'Coppucino':4000,
      'Espresso':3000
    },
    'Americano':{
      'shokolad':30,
      'shakar':10,
      'qahva':30,
      'suv':150,
      'narxi':150
    },
    'Latte':{
      'shokolad':30,
      'shakar':10,
      'suv':100,
      'qahva':20,
      'narxi':160
    },
    'Coppucino':{
      'shokolad':50,
      'shakar':10,
      'sut':100,
      'suv':20,
      'qahva':40,
      'narxi':180
    },
    'Espresso':{
      'shokolad':50,
      'shakar':15,
      'sut':100,
      'qahva':30,
      'narxi':200
    }
}
from time import sleep
ishora=True
while ishora:
    print("Menyu: ")
    for j,i in zip(range(1,len(coffee['Qahvalar'].keys())+1),coffee['Qahvalar'].keys()):
        print(j,i," - ",coffee[i]['narxi'])
    print("Chiqish uchun 0 ni bosing!")


    t = int(input("Kerakli qahvani tanlang: "))
    if t==0:
        ishora=False
        break
    for i,j in enumerate(coffee['Qahvalar'].keys()):
        if i+1==t:
          satr=j
          break
        elif t!=1 or t!=2 or t!=3 or t!=4:
           print("Bunday raqmdagi coffee yo'q, qayta tanlang!")
           continue
    print("="*20)
    print(f'Siz {satr}ni tanladingiz! Narxi: {coffee[satr]["narxi"]}')

    shakar = int(input("Shakar kerakmi? 1-Ha|2-Yo'q:>>>"))
    dicti={};S=0
    print("="*20)
    print(f'Narxi: {coffee[satr]["narxi"]}')
    print("Tangalarni kiriting!")

    for i in coffee['Tangalar'].keys():
        dicti[i]=int(input(f"{i} - so'mlik: "))
        S+=dicti[i]*int(i)
        if S<coffee[satr]['narxi']:
          continue
    print()

    try:
        coffee['shakar']-=coffee[satr]['shakar']
    except:
        pass
    try:
        coffee['shokolad']-=coffee[satr]['shokolad']
    except:
        pass
    try:
        coffee['sut']-=coffee[satr]['sut']
    except:
        pass
    try:
        coffee['suv']-=coffee[satr]['suv']
    except:
        coffee['qahva']-=coffee[satr]['qahva']

    if S==coffee[satr]['narxi']:
        for i in coffee['Tangalar'].keys():
            coffee['Tangalar'][i]+=dicti[i]
    print(S)
    if S==int(coffee[satr]['narxi']):
        savol1=int(input(("Yana qahva ichishni hohlaysizmi?  1-Ha|2-Yo'q:>>>")))
        if savol1==1:
            continue
        else:print("Bizning cafega tashrif buyirganingizdan hursandmiz va sizni yana kutib qolamiz!")
        print("Xaridingiz uchun raxmat!")
        sleep(3)
        continue

    elif S>int(coffee[satr]['narxi']):
        print("Siz ko'p mablag' kiritdingiz!")
        savol=int(input("Qaytimingizni olasizmi?'\n'1-Ha|2-Yo'q :>>> "))
        if savol==1:
            print("Sizning qaytimingiz: ",S-int(coffee[satr]['narxi']))

            enter=int(input("Qaytimingizni olgach 1 ni bosing!: " ))
            if enter==1:
                savol2=int(input(("Yana qahva ichishni hohlaysizmi?  1-Ha|2-Yo'q:>>> ")))
                if savol2==1:continue

                else:print("Bizning cafega tashrif buyirganingizdan hursandmiz va sizni yana kutib qolamiz!")
                print("Xaridingiz uchun raxmat!")
                sleep(3)
                continue

        else:
          print("Raxmat bu pullar hayriyaga ishlatiladi! ")
          savol3=int(input(("Yana qahva ichishni hohlaysizmi?  1-Ha|2-Yo'q:>>>")))
          if savol3==1:
              continue
          else:print("Bizning cafega tashrif buyirganingizdan hursandmiz va sizni yana kutib qolamiz!")
          sleep(3)
          continue

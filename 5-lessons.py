# from random import randint,randrange,choise,sample
from random import randint 
# jeckpotInt=randint(1,10)
# jeckpotRange=randrange(2,20,3)
# print(jeckpotInt)
# print(jeckpotRange)

# ismlar=['Anna','Azizbek','Anora','Kamol','Isroil']
# print(choices(ismlar,k=3))

# ismlar=['Anna','Azizbek','Anora','Kamol','Isroil']
# shuffle(ismlar)
# print(ismlar)

# print(sample(range(2,30),k=10))

print("Kompyuter o'yiniga xush kelibsiz")
ism=input('Ismingizni kiriting\n')
print(f"{ism},O'yinni boshlashga tayyormisiz!")
kompyuterSoni=randint(1,25)
urinishlarSoni=0

while urinishlarSoni<10:
    TahminSon=int(input('Tahmin sonni kiriting:'))
    urinishlarSoni+=1
    if TahminSon>kompyuterSoni:
        print('Iltimos kichikroq son kirit.')
    elif TahminSon<kompyuterSoni:
        print('Iltimos kattaroq son kirit.')
    else:
        break
if TahminSon==kompyuterSoni:
    print(f'{ism},Siz golib boldingiz,urinishlar soni-{urinishlarSoni}')
else:
    print('Kechirasiz,keyingi safar yutishingiz mumkin')


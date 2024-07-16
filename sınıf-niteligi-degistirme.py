
#! Sınıf adı üzerinden sınıf niteliğini degistirme : 

class Ogrenciler:
    uniName="Dokuz Eylul University"

Ogrenciler.uniName="Ege University"  
# Sınıf adı üzerinden degistirme oldugunda , tüm örneklerdeki degerler de degisir


#! Ornek adı uzerinden sınıf niteligi degistirme : 
class Cars:
    horsePower=120

mercedes=Cars()
mercedes.horsePower=150
print(mercedes.horsePower)
print(Cars.horsePower)
# Ornek adı uzerinden degistirme islemi gerçekleştiğinde , sadece o ornek uzerindeki degeri degisir diger ornekler ya da orijinal sınıf üzerindeki degeri degismez.




#! INIT FONKSIYONUNU KULLANMAMIZIN ASIL NEDENI 

class Animals:
    legCount=4
    feetType='Meat'
    habitat="Afcira"    
    # Yukarıdaki degerleri defaul olarak atadım yani baslangıcta her örnek aynı degere sahip olacak.

ostrich=Animals()  
ostrich.feetType="Ot"
ostrich.habitat="Ekvador"
ostrich.legCount=2      
# Iste her degeri el ile manuel olarak degistirmemek icin __init__ fonksiyonunu ve self ön ekini kullanırız.
# Bir adet __init__ fonksiyonu tanımlarız ve ona gönderdigimiz parametre bizim o örnege ait örnek niteliklerimiz olur.

#! Ornek : 

#! Python'da init fonksiyonunu ve self ön ekini kullanmamızın amacı ; asıl class'ımızda sınıf niteliği atayıp her farklı örnek için bu nitelikleri manuel olarak el ile değiştirmektense ,
#! oluşturduğumuz init fonksiyonu ile ona gönderdiğimiz parametreler sayesine o örneğe özel olarak örnek nitelikleri oluşturup kullanmamızı sağlamak . Böylece bize kolaylık sağlar. 
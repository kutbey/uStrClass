

## Kullanım Amacı (Purpose Of Use)

Python programlama dili, farklı dillere ait harfleri, büyük veya küçük harflere dönüştürürken bazı sorunlar ortaya çıkmaktadır. Büyük harf ve küçük harf çevirmelerindeki sorunların çözmek  amacı ile ultimateStr sınıfı yazılmıştır.

Python'da **sort** işlemlerinde **str** tipi kelimeler sıralanırken bazı kelimlerin yanlış sıranlanması, büyük ve küçük  harf çevrimlerinden kaynaklanmaktadır. Bu sorun ultimateStr sınıfı kullanılarak çözülebilir.

***Some problems arise when the Python programming language converts letters from different languages to uppercase or lowercase letters. The ultimateStr class was written to solve the problems in capitalization and lowercase conversion.***

***While sorting str type words in sort operations in Python, incorrect ordering of some words is due to uppercase and lowercase letter conversions. This problem can be solved using ultimateStr class.***



## Örnekler (Examples)

Türk alfabesindeki küçük harfler(Lowercase letters of the Turkish alphabet):**abcçdefgğhıijklmnoöprsştuüvyz**

Türk alfabesindeki büyük harfler(Uppercase letters of the Turkish alphabet):**ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ**

Dönüşüm problemlerine bazı örnekler(Some examples of conversion problems:): 

| Örnek Türkçe Kelimeler(Example Turkish words) | str.upper() | str.lower() | str.title() | str.capitalize() | ***uStr.upper*()** | ***uStr.lower()*** | *uStr.title()* | *uStr.capitalize()* |
| :-------------------------------------------- | ----------- | ----------- | ----------- | ---------------- | ------------------ | ------------------ | -------------- | ------------------- |
| istanbul                                      | ISTABNUL    | istanbul    | Istanbul    | Istanbul         | İSTANBUL           | istanbul           | İstanbul       | İstanbul            |
| IŞIK                                          | IŞIK        | işik        | Işik        | Işik             | IŞIK               | ışık               | Işık           | Işık                |
| istakoz                                       | ISTAKOZ     | istakoz     | Istakoz     | Istakoz          | İSTAKOZ            | istakoz            | İstakoz        | İstakoz             |
| ispanya                                       | ISPANYA     | ispanya     | Ispanya     | Ispanya          | İSPANYA            | ispanya            | İspanya        | İspanya             |



# uStr Sınıfı (uStr Class)

#### Nasıl Çalışır ? (How does it work ?)

Bu sınıf zorunlu olarak bir kelime argümanı ve iki adet  opsiyonel argüman alır. Opsiyonel argümanlar, dönüşüm yapılamak istenen dilin büyük harfleri ve küçük harflerinden oluşur. Çevrim yapılacak dil varsayılan olarak Türk alfabesinin büyük harfleri ve küçük harfleri olarak tanımlanmıştır. Başaka bir dilde dönüşüm yapmayı düşünürseniz. Opsiyonel argümanları  kullanırken sıralı ve eşit uzunlukta olmasına dikkat ediniz. Opsiyonel argümanların birincisi küçük harflerin listesidir. Opsiyonel argümanların ikincisi büyük harflerin listesidir.  Opsiyonel argümanları liste,demet veya metin olarak gönderebilirsiniz. 

***This class necessarily takes a word argument and two optional arguments. Optional arguments consist of uppercase and lowercase letters of the language to be converted. The language to be translated is defined as uppercase and lowercase letters of the Turkish alphabet by default. If you consider converting to another language. When using optional arguments, make sure they are sequential and of equal length. The first of the optional arguments is the list of lowercase letters. The second of the optional arguments is the list of uppercase letters. You can send optional arguments as a list, tuple or str.***

#### Nasıl Kullanılır ?(How to use ?)

> **ultimate.py** dosyasını projenize dahil edin. (Include the **ultimate.py** file in your project.)

```python
from ultimate import uStr


sampleWords = "ispanya Isparta Işık IŞIK İSPANYA imleç"

# Methods of the str class
print(sampleWords.upper())  # Çıktı(Output): ISPANYA ISPARTA IŞIK IŞIK İSPANYA IMLEÇ
print(sampleWords.lower())  # Çıktı(Output): ispanya isparta işık işik i̇spanya imleç
print(sampleWords.title())  # Çıktı(Output): Ispanya Isparta Işık Işik İspanya Imleç
print(sampleWords.capitalize())  # Çıktı(Output): Ispanya isparta işık işik i̇spanya imleç

# ---------------------------------------------------------------------------------------

# Methods of the uStr class
print(uStr(sampleWords).upper()) # Çıktı(Output): İSPANYA ISPARTA IŞIK IŞIK İSPANYA İMLEÇ
print(uStr(sampleWords).lower()) # Çıktı(Output): ispanya ısparta ışık ışık ispanya imleç
print(uStr(sampleWords).title()) # Çıktı(Output): İspanya Isparta Işık Işık İspanya İmleç
print(uStr(sampleWords).capitalize()) # Çıktı(Output): İspanya ısparta ışık ışık ispanya imleç


```

#### Harf Listesi Argüman Olarak Nasıl Gönderilir ?(How to Send a List of Letters as Arguments ?)

```python
from ultimate import uStr


# Uppercase and lowercase letters of the alphabet
lowerCaseLetters = "abcçdefgğhıijklmnoöprsştuüvyz" # tuple veya list objeside olabilir (can also be a tuple or list object)
upperCaseLetters = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ" # tuple veya list objeside olabilir (can also be a tuple or list object)

# list or tuple sample Format:
# lowerCaseLetters = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
# upperCaseLetters = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']

sampleSentence = """
Merhaha istanbul. Bugün günlerden pazar! kalabalık bir şehir burası

Nerelere gitmeliyiz bu şehirde istasyon caddesine mi?yoksa başka bir yeremi ?
"""

output = uStr(sampleSentence, lowerLetters=lowerCaseLetters, upperLetters=upperCaseLetters).title()
print(repr(output))

# Çıktı(Output)
# '\nMerhaha İstanbul. Bugün Günlerden Pazar! Kalabalık Bir Şehir Burası\n\nNerelere Gitmeliyiz Bu Şehirde İstasyon Caddesine Mi?Yoksa Başka Bir Yeremi ?\n'

```



## uStr().forSorted() Method

#### Nasıl Çalışır ?  (How does it work ?)

1. Zorunlu olarak gönderilen argümanı uStr.lower() methodu ile dönüştürür.

2. Argümanın içindeki bütün boşlukları siler.

3. Argümanın bütün karakterleri döngü ile gezer. Döngü sırasında, opsiyonel olarak gönderilen küçük harf alfabesi içindeki harfler ile karşılaştırır. Harf ile karakter eşleşiyorsa onu alır ve yeni bir kelime oluşturur.

   - Örnek:  Argüman: "Fatih.!Çelik-Porselen pırasa"   Yeni Kelime: "fatihcelikporselenpırasa"

   - Noktalama işaretlerini ve boşlukları temizleyip hepsini birleştirir.

4. Küçük harf alfabesini harfin indeksine göre dict nesnesi içinde numaralandır. 

   - {'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9, 'ı': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16, 'o': 17, 'ö': 18, 'p': 19, 'r': 20, 's': 21, 'ş': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26, 'y': 27, 'z': 28}

5. Yeni Kelime: "fatihcelikporselenpırasa" örneğini alırsak bu kelimenin her karakterini dolaşır. 4. sırada oluşan dict nesnesi için de kelimenin harfine  karşılık gelen sıra numarasını yeni bir listeye gönderir. 

   - Bu şekilde eşleştirme yapılır: [(6, 'f'), (0, 'a'), (23, 't'), (11, 'i'), (9, 'h'), (3, 'ç'), (5, 'e'), (14, 'l'), (11, 'i'), (13, 'k'), (19, 'p'), (17, 'o'), (20, 'r'), (21, 's'), (5, 'e'), (14, 'l'), (5, 'e'), (16, 'n'), (19, 'p'), (10, 'ı'), (20, 'r'), (0, 'a'), (21, 's'), (0, 'a')]
   - Bu eşleştirme içinde sıra numaraları demet olarak döndürülür:(6, 0, 23, 11, 9, 3, 5, 14, 11, 13, 19, 17, 20, 21, 5, 14, 5, 16, 19, 10, 20, 0, 21, 0)

   

   1. ***Converts the required argument with the uStr.lower() method.***

   2. ***Deletes all spaces inside the argument.***

   3. ***All characters of the argument are looped through. During the loop, it compares with the letters in the optional lowercase alphabet. If the letter and character match, it takes it and creates a new word.***

      - ***Example: Argument: "Fatih.!Çelik-Porselen pırasa"  New Word: "fatihcelikporselenpırasa"***

      - ***Cleans up punctuation marks and spaces and combines them all.***

   4. ***Enumerate the lowercase alphabet in the dict object according to the index of the letter.***

      - ***{'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9, 'i': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n ': 16, 'o': 17, 'd': 18, 'p': 19, 'r': 20, 's': 21, 'h': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26, 'y': 27, 'z': 28}***

   5. ***New Word: If we take the example of "fatihcelikporselen leek", it loops through every character of this word. It sends the sequence number corresponding to the letter of the word to a new list for the dict object that occurs in the 4th row.***

      - ***This is how pairing is done: [(6, 'f'), (0, 'a'), (23, 't'), (11, 'i'), (9, 'h'), (3, 'ç'), (5, 'e'), (14, 'l'), (11, 'i'), (13, 'k'), (19, 'p'), (17, 'o') '), (20, 'r'), (21, 's'), (5, 'e'), (14, 'l'), (5, 'e'), (16, 'n') , (19, 'p'), (10, 'i'), (20, 'r'), (0, 'a'), (21, 's'), (0, 'a')]***
      - ***In this pairing, sequence numbers are returned as a bunch: (6, 0, 23, 11, 9, 3, 5, 14, 11, 13, 19, 17, 20, 21, 5, 14, 5, 16, 19, 10 , 20, 0, 21, 0)***
   
   

   

   #### Nasıl Kullanılır ? (How to use ?)

   ```python
   from ultimate import uStr
   
   
   names = ['ahmet arı', 'ahmet can ', 'iskender', 'cigdem',
            'ismet', 'ismail', 'ismit', 'çiğdem', 'ismıt',
            'ışık', 'şule', 'İSMAİL', "Arzu", "Hakan"]
   newSortedList = sorted(names, key=lambda name: uStr(name).forSorted())
   
   print(newSortedList)
   # ['ahmet arı', 'ahmet can ', 'Arzu', 'cigdem', 'çiğdem', 'Hakan', 'ışık', 'iskender', 'ismail', 'İSMAİL', 'ismet', 'ismıt', 'ismit', 'şule']
   
   ```
   
   

   

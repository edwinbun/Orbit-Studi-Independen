# -*- coding: utf-8 -*-
"""Adelita_Tianhe _KM-05: Functions, OOP, Time Complexity .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XdOH0HLDz0k0-18EPXoCV8MXjfqZx-bI

#**ADELITA PANGESTU ALLFINNI SRINA**
##Minggu ke-5 (Kamis, 23 September 2021)

# **Fungsi**
"""

#Contoh Deklarasi Fungsi
def cetak(x):
  print(x)

#Memanggil Fungsi
cetak("siap boss")

#Contoh Deklarasi Fungsi dengan Pengembalian
def tambah(k, l):
  return k + l;

#Memanggil Fungsi
print(tambah(4, 5))

"""# **Method**"""

#Contoh Deklarasi Object (Class)
class Sapi(object):
  def moo(self):
    print("moooooo")

#Memanggil Method
cow = Sapi()
cow.moo()

"""# **Lambda Expression**"""

#Contoh Lambda Expression
tambah = lambda k, l: (k + l)
print(tambah(4, 5))

"""# **Object Oriented Programming**

## **Encapsulation**
"""

class Sapi:
  def __init__(self, nama, usia, jenis_kelamin, warna, jenis):
    self.nama = nama
    self.usia = usia
    self.jenis_kelamin = jenis_kelamin
    self.warna = warna
    self.jenis = jenis

  def myfunc(self):
    print("Hello my name is " + self.nama)
  
  def moo(self):
    print("mhooooooo... ")

  def info(self):
    print(f"nama: {self.nama}, usia: {self.usia}, jenis kelamin: {self.jenis_kelamin}, warna: {self.warna}, jenis: {self.jenis}")


sapi1 = Sapi("abang", 1, "jantan", "coklat muda", "limosin")

sapi1.info()

"""## **Abstraction**"""

#Contoh Memanggil method dari objek tanpa harus mengetahui cara kerja method
sapi1.myfunc()

"""## **Inheritence**"""

class Binatang(object):
  def __init__(self, nama, usia, jenis, mamalia):
    self.nama = nama
    self.usia = usia
    self.jenis = jenis
    self.mamalia = mamalia

  def tidur(self, durasi):
    for x in range(durasi):
      print("ddrrr... ddrrr... ")

  def info(self):
    print(f"nama: {self.nama}, usia: {self.usia}, jenis: {self.jenis}, mamalia: {self.mamalia}")


animal1 = Binatang("cemong", 1, "omnivora", True)

animal1.info()


class Sapi(Binatang):
  def __init__(self,  nama, usia, jenis_kelamin, mamalia, warna, jenis_sapi):
    super().__init__(nama, usia, jenis_kelamin, mamalia)
    self.warna = warna
    self.jenis_sapi = jenis_sapi
  
  def moo(self):
    print("mhoooooo....")

  def info_sapi(self):
    print(f"warna: {self.warna}, jenis sapi: {self.jenis_sapi}")

cow1 = Sapi("mipan", 1.5, "betina", True, "putih hitam", "perah")

cow1.info()
cow1.info_sapi()

"""## **Polymorphism**"""

class Tumbuhan(object):
  def __init__(self, nama, usia, jenis_tumbuhan):
    self.nama = nama
    self.usia = usia
    self.jenis_tumbuhan = jenis_tumbuhan

  def tidur(self, durasi):
    for x in range(durasi):
      print("bbrrrr... bbrrrr... ")

  def info(self):
    print(f"nama: {self.nama}, usia: {self.usia}, jenis: {self.jenis_tumbuhan}")


plant1 = Tumbuhan("Atang", 3.5, "Umbi-umbian")

plant1.info()

class Kentang(Tumbuhan):
  def __init__(self,  nama, usia, warna, jenis_sayuran, jenis_tumbuhan):
    super().__init__(nama, usia, jenis_tumbuhan)
    self.warna = warna
    self.jenis_sayuran = jenis_sayuran

  def tumbuh(self, durasi):
    for x in range(durasi):
      print("hallo... aku adalah kentang yang sehat... ")

  def info_kentang(self):
    print(f"warna: {self.warna}, jenis kentang: {self.jenis_sayuran}")

potato1 = Kentang("Atang", 3.5 , "cokelat muda terang", "Russet", "Umbi-umbian")

potato1.tidur(3)
print()
potato1.info()
potato1.info_kentang()
potato1.tumbuh(2)

"""# **Time Complexity**
## Activity 

Hitung time complexity dengan bigO Notation pada algoritma berikut:

* Tidak perlu di run
"""

# 1
#Big O(3)= O(1)

arr = [1, 2, 3, 4, 5] #Big O(1)

print(arr[0]) #Big O(1)
print(arr[1]) #Big O(1)

# 2
#Big O(3 + n) = O(n)

print(arr[2]) #Big O(1)
for number in arr: #Big O(n)
  print(number)
print(arr[1]) #Big O(1)
print(arr[2]) #Big O(1)

# 3
#Big O(3 + n) = O(n)

arr2 = [6, 7, 8, 9, 10] #Big O(1)

for number in arr: #Big O(n)
  print(number)
for number in arr2: #Big O(n)
  print(number)
print(arr2[4]) #Big O(1)

# 4
#Big O(1 + 2n)= O(n)

print(arr2[1]) #Big O(1)
for number in arr: #Big O(n)
  print(number)
for number in arr: #Big O(n)
  print(number)

# 5
#Big O(2 + n^2)= O(n^2)

for number in arr: #Big O(n)
  for number2 in arr2: #Big O(n)
    print(number+number2)
print(arr[1]+arr2[1]) #Big O(1)
print(arr2[2]) #Big O(1)

# 6 
#Big O(1 + n^2)= O(n^2)

for number in arr: #Big O(n)
  for number2 in arr: #Big O(n)
    print(number+number2)
print(arr) #Big O(1)

# 7 
#Big O(3 + n^3)= O(n^3)

for number in arr: #Big O(n)
  for number2 in arr2: #Big O(n)
    for number3 in arr: #Big O(n)
      print(number+number2+number3)
print(arr[1]) #Big O(1)
print(arr2[2]) #Big O(1)
print(arr2[3]) #Big O(1)

# 8
#Big O(2 + n + n^2)= O(n^2)

for number in arr: #Big O(n)
  print(number)
print(arr2) #Big O(1)
for number in arr: #Big O(n)
  for number2 in arr2: #Big O(n)
    print(number+number2)
print(arr) #Big O(1)

# 9 
# algoritma bubble sort

mylist = [1,5,10,15,20,25,30,2,6,8,9]
print('daftar mylist awal :\n',mylist)
def bubbleSort(mylist):
    # outer loop
    for i in range(len(mylist)-1, 0, -1):
        # inner loop
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                # swap the value
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
                
    return mylist


firstlist = [5, 8, 3, 1]
print('daftar mylist hasil bubble sort :\n',bubbleSort(firstlist))

# 10
# algoritma linear search

myList = [1,5,10,15,20,25,30,2,6,8,9] # Example List
print('Pilihan angka : \n', myList)
cari = int(input("Masukkan mylist Yang Anda Cari : ")) # mylist yang ingin dicari

#fungsi
def searchNumber(List,search):
    counter = 0
    while counter != len(myList):
        if myList[counter] == search:
            result = counter
        counter += 1
    return result

#pemanggilan Fungsi
hasil = searchNumber(myList,cari)
if cari not in myList:
    print("Number Not Found !!!")
else:
    print('Number %s in index %s'% (cari,hasil))

# 11
# algoritma binary search

yourList = [2,4,9,8,1,3,5,6,3] # Example List
print('Pilihan angka: \n', yourList)
yourNumber = int(input('Insert Number to search ? ')) # mylist yang ingin dicari

#Fungsi
def searchNumber(Number,List):
    found = False     #Untuk memberikan kondisi adanya mylist
    List.sort() # binary search harus diurutkan
    firstIndex = 0  #index pertama
    lastIndex = len(List)-1 #index terakhir
    while firstIndex <= lastIndex and not found:
        middleIndex = (firstIndex + lastIndex) // 2     #mancari index tengah
        if List[middleIndex] == Number:
            found = True
        else:
            if Number < List[middleIndex]:
                lastIndex = middleIndex - 1
            else:
                firstIndex = middleIndex + 1
    return found
    
#Pemanggilam Fungsi ditandai dengan pemanggilan nama fungsi
result = searchNumber(yourNumber,yourList)
if result:
    print('Number %s is Found in List'% yourNumber)
else:
    print('Number %s not Found in List' % yourNumber)
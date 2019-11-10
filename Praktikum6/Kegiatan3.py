Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Septiana Nugraheny'
>>> NIM = 'L200190181'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Karena 'x' merupakan data yang bertype integer
>>> type(b)
<class 'int'>
>>> # Karena data 'Nama' memiliki instruksi 'len'
>>> a / b
65.61111111111111
>>> # Karena hasil '1185' dibagi '18' adalah 65.61111111111111
>>> a // b
65
>>> # Karena arti '//' adalah pembagian dengan pembulatan ke bawah
>>> 10 * (a - 999)
1820
>>> # Karena nilai 'a' setelah dikurangkan 999 adalah 182 dan dikalikan 10 adalah 1820
>>> b ** 2
324
>>> # Karena makna '**' adalah pangkat
>>> a % b
11
>>> # Karena makna '%' adalah sisa hasil bagi
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Karena '12.5' adalah angka desimal
>>> a / c
94.48
>>> # Karena hasil '1181' dibagi dengan '12.5' adalah 94.48
>>> a // c
94.0
>>> # Karena arti '//' adalah pembagian dengan pembulatan ke bawah
>>> a % c
6.0
>>> # Karena makna '%' adalah sisa hasil bagi
>>> c > b
False
>>> # Karena nominal 'c' adalah 12.5 dan nominal 'b' adalah 18, salah karena lebih besar bilangan 'b'
>>> type(c > b)
<class 'bool'>
>>> # Karena hasil dari 'bool' adalah TRUE dan FALSE
>>> a > b and b > c
True
>>> # Karena bilangan 'a' lebih besar dari 'b' dan bilangan 'b' lebih besar dari 'c'
>>> a > 1100 or b < 10
True
>>> # Karena bilangan 'a' lebih besar dari '1100' atau 'b' lebih besar dari '10'

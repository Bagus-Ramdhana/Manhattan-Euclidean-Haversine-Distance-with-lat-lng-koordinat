# Manhattan Distance with Lat&Long Koordinat  --- by Bagus Ramdana K.A

# Library
from scipy.spatial import distance

#------------------------------------------------
# DATA
Surabaya = (-7.250445 , 112.768845)
Jakarta = (-6.200000 , 106.816666)
Makasar = (-5.135399 , 119.42379)
Manado = (1.474830 , 124.842079)
Ponianak = (0.000000 , 109.333336)
Tangerang = (-6.178306 , 106.631889)
Semarang = (-6.966667 , 110.416664)
Batam = (1.045626 , 104.030457)
Banjarmasin = (-3.316694 , 114.590111)
Serang = (-6.120000 , 106.150276)
Samarinda = (-0.502106 , 117.153709)
Jember = (-8.184486 , 113.668076)
Denpasar = (-8.650000 , 115.216667)
Bogor = (-6.595038 , 106.816635)
Yogyakarta = (-7.797068 , 110.370529)

#------------------------------------------------

# Surabaya - Surabaya
rute = 'Surabaya - Surabaya'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Surabaya)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Jakarta
rute = 'Surabaya - Jakarta'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Jakarta)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Makasar
rute = 'Surabaya - Makasar'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Makasar)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Manado
rute = 'Surabaya - Manado'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Manado)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Pontianak
rute = 'Surabaya - Pontianak'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Ponianak)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Tangerang
rute = 'Surabaya - Tangerang'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Tangerang)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Semarang
rute = 'Surabaya - Semarang'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Semarang)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Batam
rute = 'Surabaya - Batam'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Batam)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Banjarmasin
rute = 'Surabaya - Banjarmasin'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Banjarmasin)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Serang
rute = 'Surabaya - Serang'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Serang)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Samarinda
rute = 'Surabaya - Samarinda'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Samarinda)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Jember
rute = 'Surabaya - Jember'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Jember)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Denpasar
rute = 'Surabaya - Denpasar'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Denpasar)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Bogor
rute = 'Surabaya - Bogor'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Bogor)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------

# Surabaya - Yogyakarta
rute = 'Surabaya - Yogyakarta'
# Manhattan Formula
dist = distance.cityblock(Surabaya, Yogyakarta)
# Tampilkan Hasil
print('Jarak Manhattan {} : {:.2f} Km'.format(rute,dist*100))

#------------------------------------------------
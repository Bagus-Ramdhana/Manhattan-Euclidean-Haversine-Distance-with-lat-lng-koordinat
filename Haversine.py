# Haversine Distance with Lat&Long Koordinat  --- by Bagus Ramdana K.A

# Library
import math
from math import *


#------------------------------------------------
# DATA
# Latitude
latSurabaya = -7.250445
latJakarta = -6.200000
latMakasar = -5.135399
latManado = 1.474830
latPonianak = 0.000000
latTangerang = -6.178306
latSemarang = -6.966667
latBatam = 1.045626
latBanjarmasin = -3.316694
latSerang = -6.120000
latSamarinda = -0.502106
latJember = -8.184486
latDenpasar = -8.650000
latBogor = -6.595038
latYogyakarta = -7.797068

# Longtitude
lngSurabaya = 112.768845
lngJakarta = 106.816666
lngMakasar = 119.42379
lngManado = 124.842079
lngPonianak = 109.333336
lngTangerang = 106.631889
lngSemarang = 110.416664
lngBatam = 104.030457
lngBanjarmasin = 114.590111
lngSerang = 106.150276
lngSamarinda = 117.153709
lngJember = 113.668076
lngDenpasar = 115.216667
lngBogor = 106.816635
lngYogyakarta = 110.370529

#------------------------------------------------
def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 
    return c * r
#------------------------------------------------

# Surabaya - Surabaya
rute = 'Surabaya - Surabaya'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latSurabaya
lon2 = lngSurabaya
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Jakarta
rute = 'Surabaya - Jakarta'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latJakarta
lon2 = lngJakarta
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Makasar
rute = 'Surabaya - Makasar'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latMakasar
lon2 = lngMakasar
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Manado
rute = 'Surabaya - Manado'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latManado
lon2 = lngManado
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Pontianak
rute = 'Surabaya - Pontianak'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latPonianak
lon2 = lngPonianak
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Tangerang
rute = 'Surabaya - Tangerang'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latTangerang
lon2 = lngTangerang
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Semarang
rute = 'Surabaya - Semarang'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latSemarang
lon2 = lngSemarang
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Batam
rute = 'Surabaya - Batam'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latBatam
lon2 = lngBatam
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Banjarmasin
rute = 'Surabaya - Banjarmasin'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latBanjarmasin
lon2 = lngBanjarmasin
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Serang
rute = 'Surabaya - Serang'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latSerang
lon2 = lngSerang
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Samarinda
rute = 'Surabaya - Samarinda'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latSamarinda
lon2 = lngSamarinda
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Jember
rute = 'Surabaya - Jember'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latJember
lon2 = lngJember
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Denpasar
rute = 'Surabaya - Denpasar'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latDenpasar
lon2 = lngDenpasar
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Bogor
rute = 'Surabaya - Bogor'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latBogor
lon2 = lngBogor
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------

# Surabaya - Yogyakarta
rute = 'Surabaya - Yogyakarta'
lat1 = latSurabaya
lon1 = lngSurabaya
lat2 = latYogyakarta
lon2 = lngYogyakarta
# Haversine Formula
dist = haversine(lon1, lat1, lon2, lat2)
# Tampilkan Hasil
print('Jarak Haversine {} : {:.2f} Km'.format(rute,dist))

#------------------------------------------------
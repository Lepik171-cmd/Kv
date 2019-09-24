import math

print('Sisesta odomeetri näit sõidulehe alustamisel:')
odoalgus = int(input())

print('Sisesta odomeetri näit sõidulehe lõpetamisel:')
odolopp = int(input())

print('Sisesta kütuse kulunorm:')
kulunorm = int(input())

print('Sisesta linnas sõidetud km kokku:')
linn = int(input())

print('Sisesta maastikul sõidetud km kokku:')
maastik = int(input())

print('Sisesta haagisega sõidetud km kokku:')
haagis = int(input())

kokku = odolopp-odoalgus
maanteel = kokku-linn-maastik-haagis

print('KOKKU: ' + str(odolopp) + '-' + str(odoalgus) + '=' + str(kokku))

print('MAANTEEL: ' + str(kokku) + '-' + str(linn) + '-' + str(maastik) + '-' + str(haagis) + '=' + str(maanteel))

lisanduv_linn = 110/100
lisanduv_maastik = 120/100
lisanduv_haagis = 125/100
maantee_kulu = maanteel*(kulunorm/100)
linn_kulu = linn*(kulunorm/100)*lisanduv_linn
maastik_kulu = maastik*(kulunorm/100)*lisanduv_maastik
haagis_kulu = haagis*(kulunorm/100)*lisanduv_haagis
normijargne = maastik_kulu+haagis_kulu+linn_kulu+maantee_kulu

print('KULU MAANTEEL: ' + str(maanteel) + '*' + str(kulunorm/100) + '=' + str(round(maantee_kulu, 2)))

print('KULU LINNAS: ' + str(linn) + '*' + str(kulunorm/100) + '*' + str(lisanduv_linn) + '=' + str(round(linn_kulu, 2)))

print('KULU MAASTIK ' + str(maastik) + '*' + str(kulunorm/100) + '*' + str(lisanduv_maastik) + '=' + str(round(maastik_kulu, 2)))

print('KULU LINNAS: ' + str(haagis) + '*' + str(kulunorm/100) + '*' + str(lisanduv_haagis) + '=' + str(round(haagis_kulu, 2)))

print('NORMIJÄRGNE KÜTUSEKULU: ' + str(round(maantee_kulu, 2)) + '+' + str(round(linn_kulu, 2)) + '+' + str(round(maastik_kulu, 2)) + '+' + str(round(haagis_kulu, 2)) + '=' + str(round(normijargne, 2)))
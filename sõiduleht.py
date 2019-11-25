import math

print('Sisesta odomeetri näit sõidulehe alustamisel (juhul kui puudub väärtus siis kirjuta 0):')
odoalgus = int(input())

print('Sisesta odomeetri näit sõidulehe lõpetamisel (juhul kui puudub väärtus siis kirjuta 0):')
odolopp = int(input())

print('Sisesta kütuse kulunorm (juhul kui puudub väärtus siis kirjuta 0):')
kulunorm = int(input())

print('Sisesta linnas sõidetud km kokku (juhul kui puudub väärtus siis kirjuta 0):')
linn = int(input())

print('Sisesta maastikul sõidetud km kokku (juhul kui puudub väärtus siis kirjuta 0):')
maastik = int(input())

print('Sisesta haagisega sõidetud km kokku (juhul kui puudub väärtus siis kirjuta 0):')
haagis = int(input())

print ('Sisesta mootori tööaeg kohapeal tundides (juhul kui puudub väärtus siis kirjuta 0):')
tiks = int(input())

kokku = odolopp-odoalgus
maanteel = kokku-linn-maastik

print('KOKKU: ' + str(odolopp) + '-' + str(odoalgus) + '=' + str(kokku) + ' km')

print('MAANTEEL: ' + str(kokku) + '-' + str(linn) + '-' + str(maastik) + '=' + str(maanteel) + ' km')

lisanduv_linn = 110/100
lisanduv_maastik = 120/100
lisanduv_haagis = 125/100
maantee_kulu = maanteel*(kulunorm/100)
linn_kulu = linn*(kulunorm/100)*lisanduv_linn
maastik_kulu = maastik*(kulunorm/100)*lisanduv_maastik
haagis_kulu = haagis*(kulunorm/100)*lisanduv_haagis
normijargne = maastik_kulu+haagis_kulu+linn_kulu+maantee_kulu
kohapeal = tiks * 3

print('KULU MAANTEEL: ' + str(maanteel) + '*' + str(kulunorm/100) + '=' + str(round(maantee_kulu, 2)) + ' l')

print('KULU LINNAS: ' + str(linn) + '*' + str(kulunorm/100) + '*' + str(lisanduv_linn) + '=' + str(round(linn_kulu, 2)) + ' l')

print('KULU MAASTIKUL: ' + str(maastik) + '*' + str(kulunorm/100) + '*' + str(lisanduv_maastik) + '=' + str(round(maastik_kulu, 2)) + ' l')

print('KULU HAAGISEGA: ' + str(haagis) + '*' + str(kulunorm/100) + '*' + str(lisanduv_haagis) + '=' + str(round(haagis_kulu, 2)) + ' l')

print ('KÜTTEKULU KOHAPEAL TÖÖDATES: ' + str(kohapeal) + ' l')

print('NORMIJÄRGNE KÜTUSEKULU: ' + str(round(kohapeal, 2)) + '+' + str(round(maantee_kulu, 2)) + '+' + str(round(linn_kulu, 2)) + '+' + str(round(maastik_kulu, 2)) + '+' + str(round(haagis_kulu, 2)) + '=' + str(round(normijargne, 2)) + ' l')

anggota = ((input('Masukan daftar siswa :')))
print ('daftar siswa:',anggota.title().split(','),anggota.upper())

add = ((input('masukan siswa yang ingin ditambahkan :')))
if add not in anggota :
    print('hasil penambahan pada daftar siswa :',[anggota.title(), add.upper()])

          
else :
    print('siswa atas nama', (add.upper()),'sudah berada dalam daftar siswa')

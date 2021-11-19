print('==== kalkulator akar dan pangkat ====')
print("pilihan menu:")
print('1. pangkat 2 (kuadrat)')
print('2. pangkat 3 (kubik)')
print('akar kuadrat')

angka = int(input('masukan menu yang anda ingin pilih : ',))

if angka ==1:
    a = int(input('masukan bilang yang ingi dipangkatkan :'))
    hasil = a ** 2
    print('hasil dari pemangkatan bilangan' ,a ,'dengan 2 (kuadrat) adalah',hasil)
    
elif angka ==2:
    a = int(input('masukan bilangan yang ingin dipangkatkan :',))
    hasil = a ** 3
    print('hasil dari pemangkatan bilangan' ,a ,'dengan 3 (kubik) adalah ' , hasil)
elif angka == 3:
    a = int(input('masukan bilangan yang ingin dipangkatkan :'))
    hasil = a ** (1.0/2)
    print('hasil dari akar kuadrat dari bilangan' ,a ,'adalah' ,hasil)

else :
    print('pilihan menu yang tidak dimasukan tidak sesuai!')
    
                
                


       




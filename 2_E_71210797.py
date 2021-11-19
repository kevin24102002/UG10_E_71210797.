suhu=float(input("Masukan suhu tubuh :"))
if suhu >= 50 :
    print("anda bukan manusia :)")
elif suhu <=32:
    print("Anda dianggap kedinginan! silahkan cari sesutau yang hangat")
elif(suhu>37.5) and (suhu<50):
    print("anda demam! Jangan berpergian ke tempat fasilitas umum")
elif(suhu>=32) and (suhu<=37.5):
    print ("Suhu anda normal!")

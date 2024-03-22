def mobil(tahun,versi,rakitan):
	print("tahun mobil adalah {}".format(tahun))
	print("versi mobil adalah {}".format(versi))
	print("rakitan mobil adalah {}".format(rakitan))
corola = {"tahun":"1999","versi":"cross","rakitan":"thailand"}
mobil(**corola)
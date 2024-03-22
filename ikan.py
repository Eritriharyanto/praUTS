def jaring(*args):
	print("masukan ikan dalam jaring")
	jumlah_ikan = int(input("masukan banyaknya ikan : "))

	for i in range(jumlah_ikan):
		ikan = input(f"ikan {i+1} : ")
		args += (ikan,)

		for i, ikan in enumerate (args):
			print(f"{i+1}. {ikan}")
	print("Terimakasih")
jaring()
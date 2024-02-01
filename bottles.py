def bottle_song(bottles):
	while bottles >= 0:
		if bottles == 0:
			print(f"""No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.""")
		elif bottles == 1:
			print(f"""{bottles} bottle of beer on the wall, {bottles} bottle of beer.
Take one down and pass it around {bottles - 1} bottle of beer on the wall.""")
		else:
			print(f"""{bottles} bottles of beer on the wall, {bottles} bottles of beer.
Take one down and pass it around {bottles - 1} bottles of beer on the wall.""")
		bottles = bottles - 1

	# pass

bottle_song(10)

# ####kldjsfalkfdajalskdfjdfls



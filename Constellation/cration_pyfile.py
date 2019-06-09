dict_const = {}
list_const = []
with open("Constellation.txt", "r") as f_in, open("Constal_dict.py", "w") as f_out:
	t = f_in.readline().rstrip().split(": ")
	x = t[1].split(", ")
	while t != [""]:
		x = t[1].split(", ")
		dict_const[t[0]] = x
		list_const.append(t[0])
		t = f_in.readline().rstrip().split(": ")
	print("dict_constell =", dict_const, file = f_out)
	print("list_constell =", sorted(list_const), file = f_out)
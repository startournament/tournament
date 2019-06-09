rus_lat_dict = {}
lat_rus_dict = {}
with open("translate.txt", "r") as f_in, open("translated.py", "w") as f_out:
    t = f_in.readline().rstrip().split("-")
    while t != [""]:
        rus_lat_dict[t[0]], lat_rus_dict[t[1]] = t[1], t[0]
        t = f_in.readline().rstrip().split("-")
    print("rus_lat_dict =", rus_lat_dict, file = f_out)
    print("lat_rus_dict =", lat_rus_dict, file = f_out)

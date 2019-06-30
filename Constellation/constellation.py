#!/usr/bin/env python3
from dictC import *
import random
import rulse
import subprocess
separate = "_______________________________"
const = random.choice(list_constell)
print(*rulse.text())
print(separate)
print(const)
q = 'closed'
#print(separate, "Это правила 'Игры Угольникова'", "", "1. На вход даётся созвездие.", "2. Требуется перечислить как можно больше соседних созвездий", "3. Созвездия перечисляются через запятую", "","Функции:", "","help - печатает соседние с данным созвездия", "end - заканчивает игру", "_______________________________", "", "Приятной игры!", separate, const, sep = "\n")
t = input().split(", ")
while t != ["end"]:
    if t == ["open"]:
        subprocess.call(["open", "Pictures/" + rus_lat_dict[const] + ".png"])
        q = 'opened'
    elif t != ["help"] and t != ["end"]:
        for el in t:
            if el in dict_constell[const]:
                print("YES")
            else:
                print("NO")
        print(dict_constell[const])
        print(separate)
        if q == 'opened':
            q = 'closed'
            subprocess.call(["kill", "Pictures/" + rus_lat_dict[const] + ".exe"])
        const = random.choice(list_constell)
        print(const)
    t = input().split(", ")

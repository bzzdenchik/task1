from functools import *

def moves(h):
    a,b = h
    return (a+1,b),(a+2,b),(a*2,b),(a,b+1),(a,b+2),(a,b*2)
@lru_cache(None)
def game(h):
    a,b = h
    if a+b>71 and (a+b)%3!=0:
        return "W"
    if any(game(i)=="W" for i in moves(h)): return "P1"
    if all(game(i)=="P1" for i in moves(h)): return "V1"
    if any(game(i)=="V1" for i in moves(h)): return "P2"
    if any(game(i)=="P2" for i in moves(h)): return "V2"
for s in range(1,69+1):
    if game((2,s)) == "V2":
        print(s, game((2, s)))
    

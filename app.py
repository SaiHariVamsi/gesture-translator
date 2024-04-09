#from translation import translate, voice
#from hands import hands
from math import dist
from decode import decode
from hands import hands
def dist_calc(res):
    x = [res[0][1], res[0][2]]
    y = [res[1][2], res[1][2]]
    return dist(x, y)

if __name__ == '__main__' :
    gesture = hands()
    iden = dist_calc(gesture)
    print(iden)
    alpha = decode(iden)   
    print(alpha) 
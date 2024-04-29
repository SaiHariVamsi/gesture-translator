#from translation import translate, voice
#from hands import hands
from decode import decode
from hands import hands
from dist import dist_calc

if __name__ == '__main__' :
    gesture = hands()
    print(gesture)
    iden = dist_calc(gesture)
    print(iden)
    alpha = decode(iden)   
    print(alpha)
from translation import translate, voice
from hands import res

if __name__ == '__main__' :
    # get the text from hands, after translation into "text_to_translate" variable
    #for eg, 
    '''text_to_translate = input("Enter text to translate: ")
    print("Enter language option: 1-Hindi, 2-Bengale, 3-Marathi, 4-Telugu, 5-Tamil, 6-Gujarati, 7-Urdu, 8-Kannada, 9-Odia, 10-Malayalam")
    opt = int(input())
    
    #translator and text-to-speech:
    text = translate(text_to_translate, opt)
    print(text)
    print('Do you want to listen to this? Y/N')
    choice = input()
    if choice.upper() == 'Y':
        voice(text, opt)'''
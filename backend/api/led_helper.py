MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def text_to_morse(text_string):
    morse = ''
    for letter in text_string:
        if letter != ' ':
            morse += MORSE_CODE_DICT[letter] + ' '
        else:
            morse += ' '
    
    return morse


def morse_to_flashes(morse):
    import gpiozero
    import time
    led = gpiozero.LED(17)
    for letter in morse:
        if letter == '.':
            led.on()
            time.sleep(0.1)
            led.off()
        elif letter == '-':
            led.on()
            time.sleep(0.3)
            led.off()
        else:
            time.sleep(0.3)
        time.sleep(0.1)











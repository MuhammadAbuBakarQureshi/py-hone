def cipher(message):

    encode = {

        ' ' : ' ',
        'a' : '!',
        'b' : '@',
        'c' : '#',
        'd' : '$',
        'e' : '%',
        'f' : '^',
        'g' : '&',
        'h' : '*',
        'i' : '(',
        'j' : ')',
        'k' : '_',
        'l' : ';',
        'm' : '1',
        'n' : '2',
        'o' : '3',
        'p' : '4',
        'q' : '5',
        'r' : '6',
        's' : '7',
        't' : '8',
        'u' : '#',
        'w' : '9',
        'x' : '0',
        'y' : '~',
        'z' : '`'

    }

    message = message.lower()

    for alphabet in message:

        message = message.replace(alphabet, encode[alphabet])

    return message

def decipher(message):

    decode = {

        ' ' : ' ',
        '!' : 'a',
        '@' : 'b',
        '#' : 'c',
        '$' : 'd',
        '%' : 'e',
        '^' : 'f',
        '&' : 'g',
        '*' : 'h',
        '(' : 'i',
        ')' : 'j',
        '_' : 'k',
        ';' : 'l',
        '1' : 'm',
        '2' : 'n',
        '3' : 'o',
        '4' : 'p',
        '5' : 'q',
        '6' : 'r',
        '7' : 's',
        '8' : 't',
        '#' : 'u',
        '9' : 'w',
        '0' : 'x',
        '~' : 'y',
        '`' : 'z'

    }



    for symbols in encode:

        message = message.replace(symbols, decode[symbols])

    return message

message = input("Enter a message : ")

encode = cipher(message)

print("Your message encoded into : ", encode)

decode = decipher(encode)

print("Your actual message : ", decode)
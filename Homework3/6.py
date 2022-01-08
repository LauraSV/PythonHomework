def int_func(message):
    latin_char = 'qwertyuioplkjhgfdsazxcvbnm'
    return message.title() if not set(message).difference(latin_char) else False


text = input('Your text here: ').split()
for word in text:
    result = int_func(word)
    if result:
        print(int_func(word), ' ')

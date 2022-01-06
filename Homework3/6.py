def int_func(message):
    latin = 'qwertyuiopasdfghjklzxcvbnm'
    return message.ti if not set(message).difference(latin) else False

print('text')

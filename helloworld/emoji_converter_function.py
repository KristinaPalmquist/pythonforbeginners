
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ':)': '😀', #ctrl, cmd, space
        ':(': '😔',
        ':/': '😏',
        ':D': '😂',
        'sun': '🌞',
        'sick': '🤮',
        'cold': '🥶',
        'wine': '🍷',
        'angry': '🤬'
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


phrase = input('>')
print(emoji_converter(phrase))
# dictionaries

phrase = input('>')
words = phrase.split(' ')
emojis = {
    ':)': '😀', #ctrl, cmd, space
    ':(': '😔',
    ':/': '😏',
    ':D': '😂'
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '

print(output)
def reverse_and_combine_text(text):
    text = text.split(' ')
    text = ' '.join([text[i][::-1] if i + 1 == len(text) else (text[i][::-1] + text[i + 1][::-1]) for i in range(0, len(text), 2)])
    print(text)
    return text if len(text.split(' ')) == 1 else reverse_and_combine_text(text)


print(reverse_and_combine_text("dfghrtcbafed"))
print("a")
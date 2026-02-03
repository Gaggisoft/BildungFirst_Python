def neue_woerter(text, gesammelt=[]):
    for wort in text.split():
        if wort not in gesammelt:
            gesammelt.append(wort)
    return gesammelt

print(neue_woerter('hallo nova core'))
print(neue_woerter('hallo explorer heute'))
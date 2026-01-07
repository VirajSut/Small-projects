import random 

Neighbors = {'a': "qwsz", 'b': "vngh", 'c': "xdfv", 'd': "sfec", 'e': "rwds", 'f': "drgv", 'g': "fthb", 
             'h': "gyjb", 'i': "ujko", 'j': "hukn", 'k': "jilm", 'l': "mkop", 'm': "njkl", 'n': "bhjm", 
             'o': "iklp", 'p': "olol", 'q': "aswa", 'r': "edft", 's': "awdx", 't': "rfgy", 'u': "yjki", 
             'v': "cfgb", 'w': "qsae", 'x': "zsdc", 'y': "tghu", 'z': "asxa"}

#figure out what the neighbors are  
def calc_neighbor(char):
    caps = False
    if char.isupper():
        caps = True
        
    low_char = char.lower()
    val = random.choice(Neighbors[low_char])
    
    if caps ==  True:
        return val.upper()
    else:
        return val
        
def mess_word(Word):
    chars = list(Word)
    
    # 50% chance that we mess with the word 
    if random.random() > 0.5:
        return Word
    
    #place has the char that im messing with 
    place = random.randrange(len(chars))
    
    #neig has the messed up char 
    neig = calc_neighbor(chars[place])
    
    chars[place] = neig
    out = "".join(chars)
    return out 
    
def main():
    text = input("Enter text: ").strip() 
    Words = text.split()
    
    for i in range(len(Words)): 
        new_word= mess_word(Words[i])
        Words[i] = new_word
        
    out = " ".join(Words)
    
    print(out)

if __name__ == "__main__":
    main()
    
    

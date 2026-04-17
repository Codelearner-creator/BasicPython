   def pattern_tracker(text: str) -> int:
    count = 0
    
    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i+1].isdigit():
            if int(text[i+1]) == int(text[i]) + 1:
                count += 1    
    return count

### Test ###
print(Pattern_tracker("123a345"))
print(Pattern_tracker("1a2b3c4d5"))
print(Pattern_tracker("12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"))
print(Pattern_tracker("111111"))
print(Pattern_tracker("012345"))

def get_input() -> str:
    """ Return the hex-dump input """

    no_of_lines = 33
    lines = []
    
    print("Paste your Hex dump here:")
    try:
        for i in range(no_of_lines):
            lines.append(input())
    except EOFError:
        pass

    lines = "\n".join(lines)
    lines = lines.split()
    lines = [line for line in lines
            if len(line) == 2]  # Removes all unimportant data

    return lines

def search_bad_chars() -> str:
    """ Return all bad characters in Hex dump """

    lines = get_input()
    bad_chars = "\\"+hex(0) # x00 is always a badchar
    
    for i in range(1,255,8):
        for i in range(i,i+7):
            lines[i] = int(lines[i],16)
            if(hex(i) != hex(lines[i])):
                bad_chars += "\\"+hex(i)
    
    print("Found these bad characters:",bad_chars)

    return bad_chars

if __name__ == '__main__':
    search_bad_chars()

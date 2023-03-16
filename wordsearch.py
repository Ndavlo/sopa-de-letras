import itertools

def find_words(matrix, words):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    results = set()
    for word in words:
        found = False
        for r, c, direction in itertools.product(range(rows), range(cols), directions):
            if search(matrix, r, c, direction, word):
                results.add(word)
                found = True
                break
        if not found:
            found = False
    return results

def search(matrix, r, c, direction, word):
    rows = len(matrix)
    cols = len(matrix[0])
    dir_r, dir_c = direction
    if dir_r == 0 and dir_c == 0:
        return False
    if r + (len(word)-1)*dir_r < 0 or r + (len(word)-1)*dir_r >= rows:
        return False
    if c + (len(word)-1)*dir_c < 0 or c + (len(word)-1)*dir_c >= cols:
        return False
    for i in range(len(word)):
        if word[i] != matrix[r+i*dir_r][c+i*dir_c]:
            return False
    return True
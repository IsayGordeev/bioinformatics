import re
from re import search, split, findall, match, finditer

file = '/Users/isajgordeev/Desktop/Python_Coding/just/data/rosalind_lcsq.txt'
import itertools

def read_fasta(file):
    with open(file) as fp:
        text = fp.read().split('>')
        split_text = []
        for x in text:
             split_text.append(x.split('\n'))
        for x in range(len(split_text)):
            split_text[x] = [split_text[x][0], ''.join(split_text[x][1:])]
        split_text.pop(0)
        return split_text

sorted_sequences = sorted(read_fasta(file), key=lambda x: -len(x[1]))
len_sorted_sequences = len(sorted_sequences)
iterable_sequence = sorted_sequences[len_sorted_sequences - 1][1]
sorted_sequences.pop()
# print(sorted_sequences)


# Maximum string length
N = 100
L = [[0 for i in range(N)]
     for j in range(N)]


def lcs(s1, s2):
    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

    cs = matrix[-1][-1]

    return len(cs), cs

print(lcs(sorted_sequences[0][1], iterable_sequence))






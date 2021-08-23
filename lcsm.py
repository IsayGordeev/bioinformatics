file = '/Users/isajgordeev/Desktop/Python_Coding/just/data/rosalind_lcsm.txt'


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

len_sequences = len(sorted_sequences)
len_min = len(sorted_sequences[len_sequences - 1][1])
entries = 0

# print(*range(len(sorted_sequences[len_sequences-1][1])))
# print(*range(len(sorted_sequences[len_sequences-1][1]), 0 ,-1))
# print(sorted_sequences[len_sequences-1][1])

for x in range(len(sorted_sequences[len_sequences - 1][1]), 0, -1):
    if entries > 0:
        break
    for y in range(len(sorted_sequences[len_sequences - 1][1])):
        if x != y and x + y <= len_min:
            motif = sorted_sequences[len_sequences - 1][1][y:x + y]
            number_of_motifs = 0
            for z in range(0, len_sequences - 1):
                if sorted_sequences[z][1].find(motif) != -1:
                    number_of_motifs += 1
                else:
                    break
            if number_of_motifs == len_sequences - 1:
                print(motif, '\n')
                entries += 1
                break

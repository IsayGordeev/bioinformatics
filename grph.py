file = '/data/rosalind_grph.txt'
a = open(file)

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

print(read_fasta(file))


# def overlap(file, i):
#     collision = []
#     for name, dna in read_fasta(file):
#         for next_name, next_dna in read_fasta(file):
#             if (name != next_name) and next_dna != dna and dna.endswith(next_dna[:i]):
#                     collision.append((name, next_name))
#     return collision
#
#
# for x in overlap(file, 3):
#     print(*x)

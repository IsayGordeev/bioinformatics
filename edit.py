file = '/data/rosalind_edit.txt'


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

sorted_sequences = sorted(read_fasta(file), key=lambda x: len(x[1]))

for i in range(len(sorted_sequences[0][1])):
    for j in range(1, len(sorted_sequences[0][1])):
        if (i!=j):
            motif = sorted_sequences[0][1][i:j]
            print(motif)



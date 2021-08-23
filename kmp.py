file = '/Users/isajgordeev/Desktop/Python_Coding/just/data/rosalind_kmp.txt'


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

DNA = read_fasta(file)[0][1]
# print(DNA)
P = [0 for x in range(len(DNA))]
for k in range(len(DNA)):
    temp_P = [0]
    for j in range(len(DNA)):
        if (j < k and j != 0):
            # print(DNA[j:k], DNA[0: k - j], j, k)

            if(DNA[0:k-j] == DNA[j:k]):
                temp_P.append(len(DNA[j:k]))
                # print(len(DNA[j:k]),DNA[j:k] )
        P[k-1] = max(temp_P)

print(P)
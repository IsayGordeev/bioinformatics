def read_fasta(fp):
    name = None
    seq = []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))  # interim genes
            name = line  # first name
            seq = []  # first seq
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))  # yields last gene


file = '/data/rosalind_sseq.txt'
with open(file) as fp:
    sseq = []
    for name, dna in read_fasta(fp):
        sseq.append(dna)
pos = []
start = 0
last_pos = 0
for y in sseq[1]:
    a = sseq[0].find(y,last_pos+1)
    last_pos = a
    pos.append(a+1)


print(*pos)

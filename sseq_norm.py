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
for y in sseq[1]:
    i = 0
    for x in range(start,len(sseq[0])):
        i += 1
        if sseq[0][x] == y:
            start = i
            pos.append(i)
            break


copy_pos = pos[:]
for x in range(0,len(pos)-1):
    pos[x+1] += copy_pos[x]

print(pos)

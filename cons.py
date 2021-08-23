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


DNA = {}
with open('/data/rosalind_cons.txt') as fp:
    for name, seq in read_fasta(fp):
        DNA[name] = seq
        leng = len(seq)

    a, b, c, d = [0 for x in range(leng)], [0 for x in range(leng)], [0 for x in range(leng)], [0 for x in range(leng)]
    cons = ''
    for k in DNA:
        for x in range(len(DNA[k])):
            q = DNA[k][x].count('A')
            w = DNA[k][x].count('C')
            e = DNA[k][x].count('G')
            r = DNA[k][x].count('T')

            a[x] += q
            b[x] += w
            c[x] += e
            d[x] += r

    for x in range(len(a)):
        q = a[x]
        w = b[x]
        e = c[x]
        r = d[x]
        prob = max(q, w, e, r)
        if prob == q:
            cons += 'A'
        else:
            if prob == w:
                cons += 'C'
            elif prob == e:
                cons += 'G'
            else:
                cons += 'T'



print(cons)
print(' A: ',*a, '\n',
      'C: ', *b, '\n',
      'G: ', *c, '\n',
      'T: ', *d, '\n', )

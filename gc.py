import operator

def GC(fastaName):
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

    genes = {}
    with open(fastaName) as fp:
        for name, seq in read_fasta(fp):
            genes[name] = seq
    gene_gcs = {}
    # percentage = 0
    for gene in genes:
        geneLength = len(genes[gene])
        gORc = genes[gene].count('G') + genes[gene].count('C')
        percentage = (gORc / geneLength) * 100
        # if percentage
        gene_gcs[gene] = percentage

    return (sortedByGC[0])

print(GC('rosalind_gc.txt'))
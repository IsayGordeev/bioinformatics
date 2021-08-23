
TABLE = {
'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
'TAA': 'break',  'CAA': 'Q',    'AAA': 'K',     'GAA': 'E',
'TAG': 'break',  'CAG': 'Q',    'AAG': 'K',     'GAG': 'E',
'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
'TGA': 'break',  'CGA': 'R',    'AGA': 'R',     'GGA': 'G',
'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

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


def result(file):
    result = ''
    lines = []
    with open(file) as fp:
        for name, seq in read_fasta(fp):
            lines.append(seq)

    dna = lines[0]
    introns = lines[1:]
    print(dna,introns)
    for intron in introns:
        dna = dna.replace(intron, '')

    for i in range(0, len(dna), 3):
        codon = dna[i:i + 3]

        protein = None
        if codon in TABLE:
            protein = TABLE[codon]
            print(protein)
        if protein == 'break':
            break

        if protein:
            result += protein

    return result


large_dataset = '/Users/isajgordeev/Desktop/Python_Coding/just/rosalind_splc.txt'

print(result(large_dataset))



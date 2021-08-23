
TABLE = {
'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
'UAA': 'break',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
'UAG': 'break',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
'UGA': 'break',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def protein_string(mrna):
    result = ''
    for i in range(0, len(mrna), 3):
        symbol = TABLE[mrna[i:i+3]]
        if symbol == 'break':
            break
        result += symbol
    return result


# a = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
b = open('data/rosalind_prot.txt').read()
print(protein_string(b))
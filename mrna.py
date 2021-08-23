RNA_CODON_TABLE = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def codon_frequencies():
    frequencies = {}
    for v in RNA_CODON_TABLE:
        if RNA_CODON_TABLE[v] not in frequencies:
            frequencies[RNA_CODON_TABLE[v]] = 0
        frequencies[RNA_CODON_TABLE[v]] += 1
    return frequencies


print(codon_frequencies())



def possible_rna_strings(input):
    f = codon_frequencies()
    n = f['Stop']


    for c in input:
        n *= f[c]

    return n


print(possible_rna_strings('MEPSCRHKKMKTCKLFAGDQEHAYAGKTQLVVDFYEPYQVYIVSPLNVGSALQWGAQLFYLCPINTFSVHHGFWKNHWWYRRQKELKVHTCGRRPCRDKGTPFHHDTTFNGTFEGEQVYAHSFMEAPFPQQLLKKTCYCKVFGAPERHIWFMESSDWYERMAECTDFKLNSEGQCWDDQLKPIWAVHILQDTMIMFNANVKGDSCNIAYTFVQEFHRCMYPWTLINVSQFWSHTHEVCNKFYFCDQGADDKHQMACMPADHMLMGYIVRKQNVFPQSTSWAYYHAWWKQKRYTEDGHNDHYSNFMDLVYMYCVIYRSSAWYKYVVKSTQMELSAQCGYMACAAKDPFMYYWVPQLIRPMTALLMDHECQINWKCYLCTTTCFDNVFYRVLKIINFCDPEEKEFERGKKCGLEGHNWSHHFKYPHAAVFKNAGMGQLNKLMAAKWMWLRHLCPDWHRIATQPQEKKMYAFIKRVLMRFCKAPQDDDLATGCCVYTCCSCRSDACKCERRPFLEFNTHMEWWQQMDERVDWLHSITWSDYRPELDCQVKQATYIDLRICSFRRHPTIEAGHVELGRQWDPVQKQQKVGESFKEFCMDANWDGVYTIVNMPWMCHVYDQAGRCMWIKGVGEDKRRAKTYQHTHSDQKSGDTYYEHDGSKYILTAGDSDYVWAEFSGSPINDCVKIMHNFPWSIYDLRAWETMYLMEVPLPTWQHPIIIFMPSWLWYMRGCTAFCQMHDEGMSYMSDFIRLPPPIFFKSDSAFQPYFKNAMHWPPCMNAIWIFGAQVDVEIQWIEKRDNMWWDQHSFGNYGEWIHPSHMCDCAQKLTAHSPRDNKMKSKMSCELHNHSGEFNKFRSQLILVVYFIWNRVVTWDFRQMRSPCEDTWGNTRLYRMSNWCPCNYLKFYWSHPKSRTPIDVHYFELLLYGAQLKYHPAGESFYPYYWHPNCWYADRKEVCNLMWRDQQWSKTPKDNTFKPIPQGRQQHHDDGPDVPQQGPWIKIFHC')%1000000)
lines = []
fp = open('data/rosalind_subs.txt')
for line in fp:
    lines.append(line)
fp.close()
a = 'GTACGGACATTATACGGACATTACGGACTACGGACGTCCTACGGACGGTACGGACCCAACTACGGACTGTACGGACCAGTACGGACGTCCTACGGACTCTAAATACGGACGCAATTACGGACTACGGACTTAGCTACGGACTACGGACGTACGGACTACGGACATACGGACTTACGGACTTACGGACGGTTATCGCCGTACGGACTACGGACCCTACGGACCTACGGACAACAGTTACGGACTACGGACTACGGACTTTACGGACTACGGACTACGGACCCGCACGCCATAAGGTACGGACGCTATACGGACTACGGACCTACGGACTACGGACCTACGGACTACGGACGCTACGGACTACGGACCTGGATCGTGGATACGGACTTACGGACACTGTACGGACGTACGGACGTTACGGACTATACGGACTACGGACTTACGGACCTTACGGACGAATACGGACTACGGACTTTCTTGAGTCAGGGATACGGACCAGGTACGGACAGTTACGGACCTGACTGCGATACGGACATACGGACCGTACGGACTACGGACTACGGACTACGGACTACGGACGGTACGGACCGTTACGGACTACGGACTACGGACCTACGGACCTCATACGGACCCTAATATACGGACACCTTGTAGCTTACGGACTACGGACTAGTACATACGGACATTACGGACTCCGTTACGGACTAAGTACGGACAGTACGGACTTGTCATTCTCGTACGGACGGTACGGACTTACGGACGGACTGTGACACTACGGACCAATCAATACGGACTGAATTACGGACCTACGGACTTACGGACTACGGACTACGTTACGGACATTACGGAC'
b = 'TACGGACTA'
c = []
# print(type(a))
for x in range(0,len(a)):
    if a[x:x+len(b)] == b:
        c.append(x+1)
print(c)

from Bio import Phylo
import io

f = open('/Users/isajgordeev/Desktop/Python_Coding/just/data/rosalind_nwck.txt','r')
pairs = [i.split('\n') for i in f.read().strip().split('\n\n')]

dist = []
for i, line in pairs:
    x,y = line.split()
    tree = Phylo.read(io.StringIO(i),'newick')
    clades = tree.find_clades()
    print(tree)
    for clade in clades:
        clade.branch_length = 1
    dist.append(tree.distance(x,y))

print(*dist)

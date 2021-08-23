from io import StringIO

from Bio import Phylo, AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator

treedata = "((A,B),D)"
handle = StringIO(treedata)

tree = Phylo.read(handle, "newick")
clades = tree.find_clades()

for x in clades:
    print(x)

# from urllib.request import urlopen
from urllib.request import urlopen

response = urlopen('uniprot.org/uniprot/A2Z669.fasta')
lines = response.readlines()
print(lines)
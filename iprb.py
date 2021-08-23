from itertools import product

def dom_probability(k, m, n):
    population = (['AA'] * k) + (['Aa'] * m) + (['aa'] * n)
    all_children = []

    for parent1 in population:

        chosen = population[:]
        chosen.remove(parent1)

        for parent2 in chosen:
            children = product(parent1, parent2)
            all_children.extend([''.join(c) for c in children])

    dominants = []

    for x in all_children:
        if x.count('A') > 0:
            dominants += x
    return (float(len(list(dominants))) / len(all_children)/2)
print(dom_probability(25,20,27))
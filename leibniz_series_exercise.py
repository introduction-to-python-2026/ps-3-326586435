def approximate_pi(n_terms):
    total = 0
    for i in range(n_terms):
        total += (-1)**i / (2*i + 1)
        approximate_pi = total*4
    return approximate_pi

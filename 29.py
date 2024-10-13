def count_distinct_terms():
    distinct_terms = set()
    for a in range(2, 101):
        for b in range(2, 101):
            distinct_terms.add(a**b)
    return len(distinct_terms)

print(count_distinct_terms())

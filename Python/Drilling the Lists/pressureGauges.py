def pressureGauges(morning, evening):
    return [[min(a, b) for a, b in zip(morning,evening)], [max(a, b) for a, b in zip(morning,evening)] ]

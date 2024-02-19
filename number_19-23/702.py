def f(s, m):
    if s >= 36:
        if s <= 85:
            return m % 2 == 0
        else:
            return (m-1) % 2 == 0
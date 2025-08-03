def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media']>= 7:
            r['situ'] = 'BOA!'
        elif r['media']>= 5:
            r['situ'] = 'RAZOAVEL'
        else:
            r['situ'] = 'RUIM!'
    return r

resp = notas(8, 8, 6, 9, 5, sit=True)
print(resp)
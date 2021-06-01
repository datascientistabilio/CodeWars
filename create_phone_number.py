def create_phone_number(n):
#p = primeiro, s = segundo, t = terceiro
    p = "".join(map(str, n[0:3]) )
    s = "".join(map(str, n[3:6]) )
    t = "".join(map(str, n[6:10]) )
    return '({}) {}-{}'.format(p, s, t)

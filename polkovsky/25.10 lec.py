s = '123'
l = [1, 2, 3]
m = {1, 2, 3}
m_it = iter(m)
s_it = iter(s)
l_it = iter(l)

for i in range(0, len(m)):print(next(m_it))


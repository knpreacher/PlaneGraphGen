from gen import Gen

inf = 999999
L = [
   [inf, inf, 1, 1, 1],
   [inf, inf, inf, 1, inf],
   [1, inf, inf, inf, inf],
   [1, 1, inf, inf, inf],
   [1, inf, inf, inf, inf]
   ]
# dw = DataWorker(L)
gen = Gen(6, 7, L)
n = len(L)
vers = list(range(0, n))
psps = gen.get_possible_shapes(n)
print("Возможные размеры: ", psps)
gen.find_bob(psps, True)
# tmp = gen.init_gen(psps[1])
# print(tmp)
# bst = gen.find_best(tmp)
# print(bst)

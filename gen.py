from data_worker import DataWorker


class Gen(DataWorker):
    pos_size = 0
    mut_count = 0

    def __init__(self, ps, mc, l):
        super().__init__(l)
        self.pos_size = ps
        self.mut_count = mc

    def init_gen(self, dim):
        vers = list(range(0, self.n))
        mx = self.reshape(vers, *dim)
        gt = list()
        for i in range(0, self.pos_size):
            smx = self.shuffle_matrix(mx)
            fl = self.calc_len(smx)
            gt.append((smx, fl))
        return sorted(gt, key=lambda obj: obj[1])

    def find_best(self, gt):
        keks = gt
        for g in range(0, self.mut_count):
            keks[self.pos_size-1] = self.mutate(keks[0], g)
            keks = sorted(keks, key=lambda obj: obj[1])
        return keks[0]

    def find_bob(self, sl, need_report):
        bst = list()
        for dim in sl:
            gt = self.init_gen(dim)
            b = self.find_best(gt)
            bst.append(b)
        if need_report:
            self.print_report(bst, sl)
        return bst

    def mutate(self, obj, ind):
        la, rc, cc = self.mx_to_line(obj[0])
        lal = len(la)
        for i in range(ind + 1, lal):
            tmp = la[i]
            la[i] = la[lal - 1 - i]
            la[lal - 1 - i] = tmp

        mx = self.reshape(la, rc, cc)
        fl = self.calc_len(mx)
        nobj = [mx, fl]
        return nobj

    def print_report(self, bst, dims):
        print("Результат работы:")
        star = "*********************"
        print(star)
        for i, b in enumerate(bst):
            print("Лучший вариант для размера ", dims[i], ": ")
            print(b[0])
            print("Расстояние: ", b[1])
            print(star)

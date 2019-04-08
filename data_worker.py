import numpy as np
import math

class DataWorker:
    L = list()
    n = 0
    inf = 999999

    def __init__(self, l):
        self.L = l
        self.n = len(l)

    def empty_matrix(self, val, sr, sc):
       res = np.empty((sr, sc))
       res.fill(val)
       return res

    def reshape(self, vers, sr, sc):
       res = self.empty_matrix(-1, sr, sc)
       for k in range(0, len(vers)):
          i = k // sc
          j = k % sc
          res[i][j] = vers[k]
       return res

    def ml_line_ind(self, ml):
        cc = ml.shape[1]
        rc = ml.shape[0]
        res = list()
        for i in range(0, rc):
            for j in range(0, cc):
                res.append([ml[i, j], (i, j)])
        return res

    def calc_len(self, ml):
        lml = self.ml_line_ind(ml)
        flen = 0
        s = len(lml)
        for i in range(0, s - 1):
            v1 = lml[i][0]
            iv1 = lml[i][1]
            for j in range(i + 1, s):
                v2 = lml[j][0]
                iv2 = lml[j][1]
                if v1 != -1 and v2 != -1:
                    if self.L[int(v1)][int(v2)] != self.inf:
                        flen += abs(iv1[0] - iv2[0]) + abs(iv1[1] - iv2[1])
        return flen

    def get_possible_shapes(self, count):
        ps = list()
        maxsq = (int(math.sqrt(count)) + 1) ** 2
        for k in range(count, maxsq + 1):
            ds = self.get_del(k)
            dsl = len(ds)
            if dsl != 0:
                for i in range(0, dsl // 2):
                    ps.append((ds[i], ds[dsl - 1 - i]))
                if dsl % 2 == 1:
                    ps.append((ds[dsl // 2], ds[dsl // 2]))
        return ps

    def get_del(self, n):
        ds = list()
        for i in range(2, n):
            if n % i == 0:
                ds.append(i)
        return ds

    def shuffle_matrix(self, mx):
        np.random.shuffle(mx)
        mx = np.transpose(mx)
        np.random.shuffle(mx)
        mx = np.transpose(mx)
        return mx

    def mx_to_line(self, mx):
        rc = len(mx)
        cc = len(mx[0])

        arr = list()

        for i in range(0, rc):
            for j in range(0, cc):
                arr.append(mx[i, j])

        return arr, rc, cc


class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        mat = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                mat[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))


    def __str__(self):
        return str('_'.join(['_'.join([str(j) for j in i]) for i in matr]))



my_matrix = Matrix([[17, 33, 13],
                    [4, 71, 3],
                    [90, 10, 30]],
                   [[23, 33, 43],
                    [53, 64, 75],
                    [86, 97, 108]])



print(my_matrix.__add__())



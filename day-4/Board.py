class Board():
    def __init__(self, lines):
        self.rows = []
        for line in lines:
            self.rows.append([int(n) for n in line.replace('  ',' ').split(' ')])

        self.cols = []
        for i in range(len(self.rows)):
            self.cols.append([row[i] for row in self.rows])

    def mark_number(self, number):
        self.__mark_number(self.cols, number)
        self.__mark_number(self.rows, number)

    def __mark_number(self, number_lists, number):
        for i in range(len(number_lists)):
            for j in range(len(number_lists[i])):
                if number_lists[i][j] == number:
                    number_lists[i][j] = None

    def won(self):
        return self.__won(self.cols) or self.__won(self.rows)

    def __won(self, number_lists):
        for i in range(len(number_lists)):
            if all([n == None for n in number_lists[i]]):
                return True
        return False

    def leftover_sum(self):
        sum = 0
        for i in range(len(self.cols)):
            for j in range(len(self.cols[i])):
                if self.cols[i][j] is not None:
                    sum = sum + self.cols[i][j]
        return sum
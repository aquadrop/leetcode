class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ms, places = self.r_place_queue(n - 1, n)
        solutions = []
        for place in places:
            if not place:
                continue
            solution = []
            for y in range(n):
                line = ''
                for x in range(n):
                    c = '.' if place[x][y] == 0 else 'Q'
                    line += c
                solution.append(line)
            solutions.append(solution)
        return solutions


    def r_place_queue(self, row, n):
        if row == 0:
            mappers = []
            places = []
            for col in range(n):
                m = [[0 for a in range(n)] for b in range(n)]
                place = [[0 for a in range(n)] for b in range(n)]
                mapper = self.place_queue(0, col, n, m)
                mappers.append(mapper)
                place[0][col] = 1
                places.append(place)
            return mappers, places

        mappers, places = self.r_place_queue(row - 1, n)
        new_mappers = []
        new_places = []
        duplate_set = set()
        for col in range(n):
            for index, mapper in enumerate(mappers):
                new_mapper = self.place_queue(row, col, n, mapper)
                if new_mapper:
                    place = [[0 for a in range(n)] for b in range(n)]
                    for a in range(n):
                        for b in range(n):
                            place[a][b] = places[index][a][b]
                    place[row][col] = 1
                    new_places.append(place)
                    new_mappers.append(new_mapper)

        return new_mappers, new_places

    def check_dupliate(self, n, m, dupliate_set):
        rp = ''
        for x in range(n):
            for y in range(n):
                rp += str(m[x][y])
        if rp not in dupliate_set:
            dupliate_set.add(rp)
            return True
        return False

    def place_queue(self, x, y, n, m):
        if m[x][y] == 1:
            return None
        new_m = [[0 for a in range(n)] for b in range(n)]
        for a in range(n):
            for b in range(n):
                new_m[a][b] = m[a][b]
        new_m[x][y] = 1
        for i in range(n):
            if self.check_range(x - i, y + i, n):
                new_m[x - i][y + i] = 1
            if self.check_range(x, y + i, n):
                new_m[x][y+i] = 1
            if self.check_range(x + i, y + i, n):
                new_m[x+i][y+i] = 1
            if self.check_range(x + i, y, n):
                new_m[x+i][y] = 1
            if self.check_range(x + i, y - i, n):
                new_m[x+i][y-i]=1
            if self.check_range(x, y - i, n):
                new_m[x][y-i]=1
            if self.check_range(x - i, y - i, n):
                m[x-i][y-i]=1
            if self.check_range(x - i, y, n):
                new_m[x-i][y]=1
        return new_m

    def check_range(self, x, y, n):
        if x < 0:
            return False
        if y < 0:
            return False
        if x >= n:
            return False
        if y >= n:
            return False

        return True

if __name__ == '__main__':
    S = Solution()
    print(S.solveNQueens(2))


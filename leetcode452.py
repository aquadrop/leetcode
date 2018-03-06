class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points = sorted(points)
        if len(points) == 0:
            return 0

        a = points[0][0]
        b = points[0][1]
        arrows = 1
        for point in points:
            if point[0] in range(a, b + 1):
                a = point[0]
                if point[1] <= b:
                    b = point[1]
                continue
            a = point[0]
            b = point[1]
            arrows += 1
        return arrows

if __name__ == '__main__':
    S = Solution()
    print(S.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
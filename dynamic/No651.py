class Solution(object):
    def maxA(self, N):
        best = [0, 1]
        for k in xrange(2, N+1):
            best.append(max(best[x] * (k-x-1) for x in xrange(k-1)))
            best[-1] = max(best[-1], best[-2] + 1) #addition
        return best[N]
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = abs(x)
        newnumber = 0
        while temp != 0:
            newnumber *= 10
            newnumber += temp % 10
            temp /= 10
        
        return newnumber if x >= 0 else -1 * newnumber

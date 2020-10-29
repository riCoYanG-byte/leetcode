# Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

# 模拟内存buffer读取，先从file读进buf4，再从buf4读进buf中
#Solution1
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copiedFrom = 0
        readBufFromBuf4 = 4
        buf4 = ['']*4
        while copiedFrom < n and readBufFromBuf4 == 4 :
            readBufFromBuf4 = read4(buf4)
            for in range(1,readBufFromBuf4):
                if copiedFrom == n:
                    return copiedFrom
                buf[copiedFrom] = buf4[i]
                copiedFrom += 1

        return copiedFrom
#Solution2
# 直接从内存里去读，如果文件里没有那么多，就返回copied num 否则返回的是n

# int _read(char* buf, int n) {
#     int copiedChars = 0, readChars = 4;
#
#     while (copiedChars < n && readChars == 4) {
#         readChars = read4(buf + copiedChars);
#         copiedChars += readChars;
#     }
#     return n < copiedChars ? n : copiedChars;
# }
# 如图所示每次都读4个，如果下次不是4个，说明读到文件末尾，全部读进来如果大于，返回已经读过的最小的
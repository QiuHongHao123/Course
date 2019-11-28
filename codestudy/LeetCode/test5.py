class Solution(object):
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        动态规划法 最长回文子串
        """
        strlen= len(s)
        max=0
        imax=0
        jmax=0
        if str =="" or strlen== 1:
            return s
        dp=[[0] * (strlen+1) for j in range(strlen+1)]                                             #动态规划数组i表示首字符j表示末字符
        for i in range(strlen-2,-1,-1):
            for j in range(i,strlen):
                if i == j :
                    dp[i][j]=1
                    if max<1:
                        max=1
                        imax=i
                        jmax=j

                elif j==i+1 and s[i]==s[j]:
                    dp[i][j] = 1
                    if max<2:
                        max=2
                        imax=i
                        jmax=j

                else:
                    if dp[i+1][j-1]==1 and s[j]==s[i]:
                        dp[i][j]=1
                        if j-i+1>max:
                            max=j-i+1
                            imax=i
                            jmax=j
        return s[imax:jmax+1]

    def longestPalindrome2(self, s):
        '''

        :param s: str
        :return: str
        试图使用中心扩展法
        '''
        lenth = len(s)
        imax=0
        jmax=0
        maxlen=0
        if s=="" or lenth==1:
            return s
        for k in range(0,lenth*2-1):                                                    #由于回文有2*n-1个中心所以k设置为2n-1
            max = 0
            if k%2==0:                                                                  #奇数回文
                i=int(k/2-1)
                j=int(k/2+1)
                max=1

            else:                                                                       #偶数回文
                i=int(k/2-0.5)
                j=int(k/2+0.5)
            while i >=0 and j <=lenth - 1:

                if s[i] == s[j]:
                    max = max + 2
                    if max > maxlen:
                        maxlen = max
                        imax = i
                        jmax = j
                    i=i-1
                    j=j+1
                else:
                    break

        return s[imax:jmax+1]






s=Solution()
print(s.longestPalindrome2("cbbd"))





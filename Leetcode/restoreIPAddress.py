class Solution:
    def restoreIpAddresses(self, s):
        ml = len(s) - 3
        a, b, c, d = 1, 1, 1, 1
        combinations = []
        st = 0
        
        while d <= ml:
            st = a + b + c + d
            if st == len(s):
                if a <= 3 and b <= 3 and c <= 3 and d <= 3:
                    combinations.append([a, b, c, d])
                a = ml
            if a < ml:
                a += 1
            elif b < ml:
                a = 1
                b += 1
            elif c < ml:
                a, b = 1, 1
                c += 1
            else:
                a, b, c = 1, 1, 1
                d += 1
        
        print(combinations)
        restored_ip = []

        for c in combinations:
            app = True
            ip = ""
            j = 0
            for i in c:
                cur = s[j:j+i]
                val = int(cur)
                if (cur[0] == "0" and len(cur) > 1) or val > 255:
                    app = False
                    break
                ip += cur + "."
                j = j + i
            if app:
                restored_ip.append(ip[0:-1])
        print(restored_ip)

strnums = "101023"
s = Solution()
s.restoreIpAddresses(strnums)
# 최적화

class Solution(object):
    def subdomainVisits(self, cpdomains):
        mydictionary = dict()
        for domain in cpdomains:
            mydomains = domain.split(' ')
            cnt = int(mydomains[0])
            mydomains = mydomains[1].split('.')
            for idx in range(len(mydomains)):
                temp = '.'.join(mydomains[idx:])
                if mydictionary.get(temp) == None:
                    mydictionary[temp] = cnt
                    continue
                else:
                    mydictionary[temp] += cnt
        ans = []
        for key, value in mydictionary.items():
            ans += [str(value)+' '+str(key)] # append 를 하는 과정이 Time complexity가 커진다 때문에 += 이런식으로 추가하는거 잊지말자!
        return ans


# Runtime: 40 ms, faster than 94.15% of Python online submissions for Subdomain Visit Count.
# Memory Usage: 11.8 MB, less than 47.37% of Python online submissions for Subdomain Visit Count.


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        '''
        discuss.leetcode.com
        1.
        com
        2.
        leetcode.com
        3.
        discuss.leetcode.com

        ["9001 discuss.leetcode.com"]
        ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]


        ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
        ["901 mail.com",

        "50 yahoo.com",

        "900 google.mail.com",


        "5 wiki.org","5 org",

        "1 intel.mail.com",

        "951 com"]

        들어오는 값을 다 '.'을 기준으로 잘라서 
        해시로 저장하고,
        있으면 기존값에 더하기
        없으면 새로 만드는 것임
        '''
        mydictionary = dict()
        for domain in cpdomains:
            mydomains = domain.split(' ')
            cnt = int(mydomains[0])
            mydomains = mydomains[1].split('.')
            for idx in range(len(mydomains)):
                temp = '.'.join(mydomains[idx:])
                if mydictionary.get(temp) == None:
                    mydictionary[temp] = cnt
                else:
                    mydictionary[temp] += cnt
        ans = []
        for key, value in mydictionary.items():
            ans.append(str(value) + ' ' + str(key))
        return ans

# Runtime: 48 ms, faster than 51.13% of Python online submissions for Subdomain Visit Count.
# Memory Usage: 11.7 MB, less than 73.68% of Python online submissions for Subdomain Visit Count.

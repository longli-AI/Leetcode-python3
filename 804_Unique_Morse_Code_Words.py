class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        amd = {
            'a':".-",
            'b':"-...",
            'c':"-.-.",
            'd':"-..",
            'e':".",
            'f':"..-.",
            'g':"--.",
            'h':"....",
            'i':"..",
            'j':".---",
            'k':"-.-",
            'l':".-..",
            'm':"--",
            'n':"-.",
            'o':"---",
            'p':".--.",
            'q':"--.-",
            'r':".-.",
            's':"...",
            't':"-",
            'u':"..-",
            'v':"...-",
            'w':".--",
            'x':"-..-",
            'y':"-.--",
            'z':"--.."
        }
        
        new_list = []
        for i in words:
            mors = ''
            for j in i:
                mors = mors + amd[j]
            if mors in new_list:
                pass
            else:
                new_list.append(mors)
        
        return len(new_list)
                
'''
Runtime: 44 ms, faster than 50.14% of Python3 online submissions for Unique Morse Code Words.
'''

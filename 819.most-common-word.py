import collections
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        p = re.compile(r"[!?',;.]")
        sub = p.sub('', paragraph.lower())
        tokens = sub.split(' ')
        tokens = [word for word in tokens if word not in banned]
        count = collections.Counter(tokens)
        return count.most_common(1)[0][0]
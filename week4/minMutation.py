#题目：最小基因变化

#双向bfs解法，参考单词接龙题目即可
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        front = {start}
        back = {end}
        step = 0
        while front:
            next_front = set()
            for seq in front:
                for i in range(len(seq)):
                    for new_c in ['A','C','G','T']:
                        if seq[i] != new_c:
                            new_seq = seq[:i] + new_c + seq[i+1:]
                            if new_seq in back:
                                return step + 1
                            if new_seq in bank:
                                next_front.add(new_seq)
                                bank.remove(new_seq)
            step += 1
            front = next_front
            if len(front) > len(back):
                front,back = back,front
        return -1


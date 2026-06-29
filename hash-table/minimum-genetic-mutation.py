class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        genes = ["A", "C", "G", "T"]
        queue = [(startGene, 0)]
        visited = set([startGene])

        while queue:
            current, steps = queue.pop(0)
            if current == endGene:
                return steps
            for i in range(len(current)):
                for g in genes:
                    if g == current[i]:
                        continue
                    next_gene = current[:i] + g + current[i + 1:]
                    if next_gene in bank_set and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, steps + 1))

        return -1
        
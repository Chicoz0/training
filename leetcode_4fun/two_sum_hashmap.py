# For com For (força bruta)
# - se poucos elementos (até~100), é mais rápido que hashmap pq percorrer arrays é
#   mais rápido do que criar dicionários e consultar em certo ponto
# - Complexidade de tempo: o(n²)
# - Complexidade de memória: o(1)

# Hashmap (dicionário):
# - Complexidade de tempo: o(n)
# - Complexidade de memória: o(n) - tradeoff de memória

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        hasher = dict()

        for ind, numb in enumerate(nums):
            if hasher.get(numb) is not None:
                return [hasher.get(numb), ind]
            hasher[target-numb] = ind

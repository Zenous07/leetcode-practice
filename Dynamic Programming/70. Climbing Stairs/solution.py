def climbStairs(n):
    memory={1:1,2:2}
    def stair(n):
        if n in memory:
            return memory[n]
        memory[n]= stair(n-1)+stair(n-2)
        return memory[n]
    return stair(n)

print(climbStairs(7))
def inter(intervals):
    length=len(intervals)
    if len(intervals)<=1: return intervals
    intervals.sort()
    newArr=[]
    start=intervals[0][0]
    end=intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0]<=end:
            end=max(end,intervals[i][1])
        else:
            newArr.append([start,end])
            start=intervals[i][0]
            end=intervals[i][1]
    newArr.append([start,end])
    return newArr

print(inter([[1,3],[2,6],[8,10],[15,18]]))
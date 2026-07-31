def insertInter(intervals,newInterval):
    result=[]
    i=0
    n=len(intervals)
    while i<n and newInterval[0]>intervals[i][1]:
        result.append(intervals[i])
        i+=1

    while i<n and newInterval[0] <= intervals[i][1] and newInterval[1]>= intervals[i][0]:
        newInterval[0]=min(newInterval[0],intervals[i][0])
        newInterval[1]=max(newInterval[1],intervals[i][1])
        i+=1
    result.append(newInterval)

    while i<n:
        result.append(intervals[i])
        i+=1
    return result

print(insertInter([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
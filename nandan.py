import bisect

def jobScheduling( startTime, endTime,p) -> int:
    arr = sorted(zip(startTime, endTime, p), key=lambda x: (x[1]))
    dp, res,count= [], 0,0
    for start, end, profit in arr:
        i = bisect.bisect_right(dp, (start, float('inf')))
        if i > 0 :
            res = max(res, dp[i - 1][1] + profit)
            count+=1   
        else: 
            res = max(res, profit)
        
        dp.append((end, res,count+1))
   
    return res,count
                
if __name__ == "__main__":
    
    n = int(input("Enter the number of jobs").strip())
    print('Enter the start time,end time,profit')
    starttime=[]
    endtime=[]
    profit=[]
    for i in range(n):
        starttime.append(int(input().strip()))
        endtime.append(int(input().strip()))

        profit.append( int(input().strip()))
        
    x,y=jobScheduling(starttime,endtime,profit)
    totalprofit=sum(profit)
    print("The number of tasks and earnings available for others")
    print("Task:",(n-y))
    print('Earnings:',(totalprofit-x))
    
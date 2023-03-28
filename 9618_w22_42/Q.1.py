Jobs = [[0 for i in range(2)] for i in  range(100)]
NoOfJobs = 0   # integer

def Initialize():
    global NoOfJobs
    global Jobs
    for i in range(100):
        Jobs[i][0] = -1
        Jobs[i][1] = -1
    NoOfJobs = 0

def AddJob(Jnum, Priority):
    global NoOfJobs, Jobs
    if NoOfJobs == 100:
        print("Not Added")
    else:
        for i in range(100):
            if Jobs[i][0] == -1:
                Jobs[i][0] == Jnum
                Jobs[i][1] == Priority
                print("Added")
                NoOfJobs += 1
                break
def InsertSortAlgo():
    global Jobs, NoOfJobs
    for cn in range(1, NoOfJobs):
        temp1 = Jobs[cn][1]
        temp2  = Jobs[cn][0]
        while Jobs[cn - 1][1] > temp1 and cn > 0:
            Jobs[cn ][0] = Jobs[cn - 1][0]
            Jobs[cn ][1] = Jobs[cn - 1][1]
            cn = cn - 1
        Jobs[cn ][1] = temp1
        Jobs[cn ][0] = temp2
def PrintArray():
    global Jobs, NoOfJobs
    for i in range(NoOfJobs):
        print(str(Jobs[i][0]) ,"priority ", str(Jobs[i][1]))

Initialize()
AddJob(12,10)
AddJob(526, 9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)


InsertSortAlgo()

PrintArray()
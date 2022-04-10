import heapq

class priorityQueue:
    def __init__(self):
        self.chkpt=[]
    def push(self,chkpt,cost):
        heapq.heappush(self.chkpt,(cost,chkpt))
    def pop(self):
        return heapq.heappop(self.chkpt)[1]
    def isEmpty(self):
        if(self.chkpt==[]):
            return True
        else:
            return False
    def check(self):
        print(self.chkpt)


class chkptNode:
    def __init__(self,chkpt,distance):
        self.chkpt=str(chkpt)
        self.distance=str(distance)

def makedict():
    Dict ={}
    file=open("SrcDst.txt",'r')
    for string in file:
        line=string.split(',')
        pt1=line[0]
        pt2=line[1]
        dist=int(line[2])
        Dict.setdefault(pt1,[]).append(chkptNode(pt2,dist))
        Dict.setdefault(pt2,[]).append(chkptNode(pt1,dist))
    return Dict

def makeheuristicdict():
    heur={}
    with open("SLD.txt",'r') as file:
        for l in file:
            l= l.strip().split(",")
            node =l[0].strip()
            sld=int(l[1].strip())
            heur[node]=sld
    return heur

def heuristic(node,values):
    return values[node]

def astar(start,end,h,SrcDst):
    path={} 
    distance={}
    q=priorityQueue()
    
    q.push(start,0)
    distance[start]=0
    path[start]=None 
    visitedList=[]  #contains all the points that are visited
    while(q.isEmpty()==False):
        current= q.pop()
        visitedList.append(current)
        if(current ==end):
            break
        for new in SrcDst[current]:
            g_cost=distance[current]+int(new.distance)
            if(new.chkpt not in distance or g_cost<=distance[new.chkpt]):
                distance[new.chkpt]=g_cost
                f_cost=g_cost+heuristic(new.chkpt,h)
                q.push(new.chkpt,f_cost)
                path[new.chkpt]=current

    finalpath=[]
    i=end
    while(path.get(i)!=None):
        finalpath.append(i)
        i=path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("Path => "+str(finalpath))
    print("Total checkpoints:"+str(len(finalpath)))
    print("Total Distance:"+str(distance[end]))

    
def main():
    src="Source"
    dst="Destination"
    SrcDst = makedict()
    h=makeheuristicdict()
    astar(src,dst,h,SrcDst)

if __name__=="__main__":
    main()
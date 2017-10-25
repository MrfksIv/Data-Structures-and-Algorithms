# python3

class JobQueue:

    currentJobs = []
    jobsHistory = []
    next_free_time = []


    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))

        self.num_workers = min(self.num_workers, len(self.jobs))
        self.nextJobIndex = self.num_workers
        self.heapSize = self.num_workers

        for i in range(min(self.num_workers, len(self.jobs))):
            self.currentJobs.append((i, self.jobs[i]))
            self.jobsHistory.append((i, 0))
            self.next_free_time.append(self.jobs[i])
        assert m == len(self.jobs)
        # print("afsasfasfafs: {}".format(self.next_free_time))

    def write_response(self):
        for i in range(len(self.jobsHistory)):
          print(self.jobsHistory[i][0], self.jobsHistory[i][1]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        # print("Jobs: {}, Threads: {}".format(self.jobs, self.num_workers))

        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        # self.next_free_time = [0] * self.num_workers

        # print("before: {}".format(self.currentJobs))
        self.buildHeap()
        # print("after: {}".format(self.currentJobs))
        next_free_thread = []
        jobDone = []
        
        currentTime = 0
        while self.heapSize > 0 and self.nextJobIndex < len(self.jobs):
            print("initial jobs: {}".format(self.currentJobs))
            last = self.extractMin()
            tmpHistory = []
            if last != None:
                currentTime = last[1]
                jobDone.append(last)
 
                # print("job finished: {} @ {}".format(jobDone, currentTime) )
                print("jobs remaining: {}, total: {}".format(self.currentJobs, self.heapSize))
                
                # print("next job done: {} /// heapSize: {}".format(jobDone, self.heapSize))
                tmpHistory.append(last)
                next_free_thread.append(last[0])
                prev = self.next_free_time[last[0]]
                self.next_free_time[last[0]] = last[1]
                print("thread {} finished at: {}".format(last[0], last[1]))
                print("next one is thread {} which finishes at: {}".format(self.currentJobs[0][0], self.next_free_time[self.currentJobs[0][0]] + self.currentJobs[0][0] ))
      
                j = 0
                
                while  last[1] == self.next_free_time[self.currentJobs[0][0]] + self.currentJobs[0][0] and self.heapSize > 0:
                    last2 = self.extractMin()
                    if last2 != None:
                        jobDone.append(last)
                        print("Found job that will finish concurrently: {}".format(last2))
                        # print("job finished: {}".format(jobDone[len(jobDone)-1]))
                        print("jobs remaining: {}".format(self.currentJobs))
                        # print("next job done: {} /// heapSize: {}".format(jobDone[len(jobDone)-1], self.heapSize))
                        tmpHistory.append(last2)
                        # self.jobsHistory.append(last2)
                        
                        next_free_thread.append(last2[0])
                        self.next_free_time[last2[0]] = last2[1]

                
                next_free_thread = sorted(next_free_thread);
                tmpHistory = sorted(tmpHistory, key=lambda tup: tup[0])
                print("tmpHistory: {}".format(tmpHistory))
                self.jobsHistory.extend(tmpHistory)
                
                # print("next free time: {}, free threads: {}".format(next_free_time, next_free_thread))

                
                if len(next_free_thread) > 0:
                    for i in range(len(next_free_thread)):
                        if self.nextJobIndex < len(self.jobs)-1:
                            
                            print("Adding job: {}".format((next_free_thread[i], self.jobs[self.nextJobIndex])))
                            
                            
                            # self.jobsHistory.append((next_free_thread[i], self.next_free_time[next_free_thread[i]]))
                            if (self.jobs[self.nextJobIndex] > 0):
                                self.insertJob((next_free_thread[i], self.next_free_time[next_free_thread[i]]+ self.jobs[self.nextJobIndex]))
                            self.nextJobIndex += 1
                            print("jobs remaining after add: {}".format(self.currentJobs))
                            

                        else:
                            self.heapSize = 0
                    next_free_thread = []
                    jobDone = []
            print("--------------\n")
        # for i in range(len(self.jobs)):
        #   next_worker = 0
        #   for j in range(self.num_workers):
        #     if next_free_time[j] < next_free_time[next_worker]:
        #       next_worker = j
        #   self.assigned_workers[i] = next_worker
        #   self.start_times[i] = next_free_time[next_worker]
        #   next_free_time[next_worker] += self.jobs[i]



    def siftDown(self, i):
        leftChildIndex = i * 2 + 1
        rightChildIndex = i * 2 + 2
        minIndex = i
        # print('minIndex: {}, leftIndex: {}, rightIndex: {}, currentJobsLen: {}'.format(minIndex, leftChildIndex, rightChildIndex, len(self.currentJobs)))

        if leftChildIndex < min(self.heapSize, len(self.currentJobs)) and self.currentJobs[leftChildIndex][1] <= self.currentJobs[minIndex][1]:
            if self.currentJobs[leftChildIndex][1] < self.currentJobs[minIndex][1]:
                inIndex = leftChildIndex
            if self.currentJobs[leftChildIndex][1] == self.currentJobs[minIndex][1] and self.currentJobs[leftChildIndex][0] < self.currentJobs[minIndex][0]:
                inIndex = leftChildIndex

        if rightChildIndex < min(self.heapSize, len(self.currentJobs))  and self.currentJobs[rightChildIndex][1] <= self.currentJobs[minIndex][1]:
            minIndex = rightChildIndex
            if self.currentJobs[leftChildIndex][1] < self.currentJobs[minIndex][1]:
                inIndex = leftChildIndex
            if self.currentJobs[leftChildIndex][1] == self.currentJobs[minIndex][1] and self.currentJobs[leftChildIndex][0] < self.currentJobs[minIndex][0]:
                inIndex = leftChildIndex

        # print('minIndex: {}'.format(minIndex))
        if i != minIndex and minIndex < min(self.heapSize, len(self.currentJobs)) :
            # self._swaps.append((i, minIndex))
            self.currentJobs[i], self.currentJobs[minIndex] = self.currentJobs[minIndex], self.currentJobs[i]
            self.siftDown(minIndex)


    def siftUp(self, i):
        while i > 0 and self.currentJobs[self.parent(i)][1] >= self.currentJobs[i][1]:
            self.currentJobs[self.parent(i)], self.currentJobs[i] = self.currentJobs[i], self.currentJobs[self.parent(i)]
            i = self.parent(i)
            

    def parent(self, i):
        return int((i - 1) / 2)


    def extractMin(self):
        result = self.currentJobs[0]
        self.currentJobs[0] = self.currentJobs[self.heapSize-1]
        self.heapSize = self.heapSize - 1
        # print("heap size: {}".format(self.heapSize))
        
        # print("Extracting: {}".format(result))
        # print("After extract: {}".format(self.currentJobs))
        
        self.siftDown(0)
        # print("After extractMin(): {}, pulled out: {}".format(self.currentJobs, result))
        return result

    def insertJob(self, job):
        if self.heapSize == self.num_workers:
            return
        self.heapSize += 1
        self.currentJobs[self.heapSize - 1] = job
        self.siftUp(self.heapSize - 1)

    def buildHeap(self):
        for i in range(int(len(self.currentJobs)/2), -1, -1):
            self.siftDown(i)

    def solve(self):
        self.read_data()

        # self.num_workers = 2
        # self.heapSize = self.num_workers
        # # self.jobs = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        # self.jobs = [1,2,3,4,5]
        # self.nextJobIndex = self.num_workers
        
        
        # for i in range(self.num_workers):
        #     self.currentJobs.append((i, self.jobs[i]))
        #     self.jobsHistory.append((i, 0))

        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()


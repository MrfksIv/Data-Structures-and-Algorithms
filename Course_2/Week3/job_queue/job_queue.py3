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
        for i in range(len(self.jobs)):
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
        
        currentTime = 0
        while self.heapSize > 0 and self.nextJobIndex < len(self.jobs):
            shouldbeAdded = True
            next_free_thread = []
            # print("initial jobs: {}".format(self.currentJobs))

            finishedConcurrently = True
            
            tmpHistory = []
            while finishedConcurrently:
                if self.heapSize == 0:
                    finishedConcurrently = False
                    break

                last = self.extractMin()
                # print("finished job: {}".format(last))
                if last != None:
                    currentFinishedTime = last[1]
                    if shouldbeAdded:
                        tmpHistory.append(last)
                    # if self.nextJobIndex <= len(self.jobs)-1:
                    #     shouldbeAdded = False
                    # print("jobs remaining: {}, total: {}, remaining: {}".format(self.currentJobs, self.heapSize, self.nextJobIndex))
                    self.next_free_time[last[0]] = last[1]
          
                # print("next job done: {} /// heapSize: {}".format(jobDone, self.heapSize))
                    next_free_thread.append(last[0])
                    # print("thread {} finished at: {}".format(last[0], last[1]))
                    # print("next one is thread {} which finishes at: {}".format(self.currentJobs[0][0], self.next_free_time[self.currentJobs[0][0]]))
                    
                    

                    if last[1] != self.next_free_time[self.currentJobs[0][0]]:
                        finishedConcurrently = False
                
                else:
                    finishedConcurrently = False
                # print("--")   
            next_free_thread = sorted(next_free_thread);
            tmpHistory = sorted(tmpHistory, key=lambda tup: tup[0])
            # print("----------------------------")
            # print("tmpHistory: {}".format(tmpHistory))
            # print("----------------------------")
            self.jobsHistory.extend(tmpHistory)
                
                # print("next free time: {}, free threads: {}".format(next_free_time, next_free_thread))

            if len(next_free_thread) > 0:
                for i in range(len(next_free_thread)):
                    if self.nextJobIndex <= len(self.jobs)-1:
                            
                        # print("Adding job: {}".format((next_free_thread[i], self.jobs[self.nextJobIndex])))
                            
                            
                            # self.jobsHistory.append((next_free_thread[i], self.next_free_time[next_free_thread[i]]))
                        # if (self.jobs[self.nextJobIndex] >= 0):
                        self.next_free_time[next_free_thread[i]] += self.jobs[self.nextJobIndex]
                        self.insertJob((next_free_thread[i], self.next_free_time[next_free_thread[i]]))
                        self.nextJobIndex += 1
                        # print("jobs remaining after add: {}".format(self.currentJobs))
            



    def siftDown(self, i):
        leftChildIndex = i * 2 + 1
        rightChildIndex = i * 2 + 2
        minIndex = i
        # print('minIndex: {}, leftIndex: {}, rightIndex: {}, currentJobsLen: {}'.format(minIndex, leftChildIndex, rightChildIndex, len(self.currentJobs)))

        if leftChildIndex < min(self.heapSize, len(self.currentJobs)) and self.currentJobs[leftChildIndex][1] <= self.currentJobs[minIndex][1]:
            if self.currentJobs[leftChildIndex][1] < self.currentJobs[minIndex][1]:
                minIndex = leftChildIndex
            if self.currentJobs[leftChildIndex][1] == self.currentJobs[minIndex][1] and self.currentJobs[leftChildIndex][0] < self.currentJobs[minIndex][0]:
                minIndex = leftChildIndex

        if rightChildIndex < min(self.heapSize, len(self.currentJobs))  and self.currentJobs[rightChildIndex][1] <= self.currentJobs[minIndex][1]:
            minIndex = rightChildIndex
            if self.currentJobs[leftChildIndex][1] < self.currentJobs[minIndex][1]:
                minIndex = leftChildIndex
            if self.currentJobs[leftChildIndex][1] == self.currentJobs[minIndex][1] and self.currentJobs[leftChildIndex][0] < self.currentJobs[minIndex][0]:
                minIndex = leftChildIndex

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
        # self.read_data()
        
        self.num_workers = 2
        self.jobs = [1,2,3,4,5]
        # self.jobs = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        # self.jobs = [5,9,8,4,2,7]
        # self.jobs = [3,2,3,6,2,8,3,3]
        # self.jobs = [6, 7, 8]
        # self.jobs = [3,2,9,5,8,3]
        # self.jobs = [9,3,7,8,4,4,8,9,9]
        # self.jobs = [9, 7, 9, 6]
        # self.jobs = [2,6,4,6,4,3,5,5]
        # self.jobs = [4,6,5,4,8,4]
        # self.jobs = [2,3,4]
        # self.jobs = [4,2,6,8,8,3,9,1,3]
        # self.jobs = [8,3]
        # self.jobs = [2,4,7,8,4,6]
        # self.jobs = [8,2,4,5,4,2,2]
        # self.jobs = [4,5,4,4,4,1,9,1]
        # self.jobs = [9]
        # self.jobs = [7,9,8,1]
        # self.jobs = [1,3,2,9,4,6,2,1,2]
        # self.jobs = [1]
        # self.jobs = [7,1,1,6,1,8,1,3,2]
        # self.jobs = [6,5,2,8,7,2]
        # self.jobs = [8,8,6,3,7,5,9,8,6]
        # self.jobs = [8,5,8,1,6]
        # self.jobs = [2,3,2,6]
        # self.jobs = [9,7,1,9,2]
        # self.jobs = [4,9,2,8,9,5,4,1]
        # self.jobs = [2,3,1,4,5,9,8,1,9]
        # self.jobs = [2,7,1,6,9]

        
        self.num_workers = min(self.num_workers, len(self.jobs))
        self.nextJobIndex = self.num_workers
        self.heapSize = self.num_workers

        for i in range(self.num_workers):
            self.currentJobs.append((i, self.jobs[i]))
            self.jobsHistory.append((i, 0))
            self.next_free_time.append(self.jobs[i])
        # assert m == len(self.jobs)
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()


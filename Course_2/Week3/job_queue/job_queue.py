# python3

class JobQueue:

    currentJobs = []
    jobsHistory = []


    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.nextJobIndex = self.num_workers
        self.heapSize = self.num_workers

        for i in range(self.num_workers):
            self.currentJobs.append((i, self.jobs[i]))
            self.jobsHistory.append((i, 0))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobsHistory)):
          print(self.jobsHistory[i][0], self.jobsHistory[i][1]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        # print("Jobs: {}, Threads: {}".format(self.jobs, self.num_workers))

        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers

        # print("before: {}".format(self.currentJobs))
        self.buildHeap()
        # print("after: {}".format(self.currentJobs))
        next_free_thread = []
        jobDone = []
        
        while self.heapSize != 0:
            
            jobDone.append(self.extractMin())

            # print("job finished: {}".format(jobDone))
            # print("jobs remaining: {}".format(self.currentJobs))
            # print("next job done: {} /// heapSize: {}".format(jobDone, self.heapSize))

            next_free_thread.append(jobDone[0][0])
            next_free_time[jobDone[0][0]] += jobDone[0][1]

            j = 0
            while jobDone[0][1] == self.currentJobs[j][1] and self.heapSize > 0:
                jobDone.append(self.extractMin())

                # print("job finished: {}".format(jobDone[len(jobDone)-1]))
                # print("jobs remaining: {}".format(self.currentJobs))
                # print("next job done: {} /// heapSize: {}".format(jobDone[len(jobDone)-1], self.heapSize))

                next_free_thread.append(jobDone[len(jobDone)-1][0])
                next_free_time[jobDone[len(jobDone)-1][0]] += jobDone[len(jobDone)-1][1]
                j += 1
            j = 0
         
            
            # print("next free time: {}, free threads: {}".format(next_free_time, next_free_thread))

            
            if len(next_free_thread) > 0:
                for i in range(len(next_free_thread)):
                    if self.nextJobIndex < len(self.jobs):
                        
                        # print("Adding job: {}".format((next_free_thread[i], self.jobs[self.nextJobIndex])))
                        
                        self.jobsHistory.append((next_free_thread[i], next_free_time[jobDone[i][0]]))
                        self.insertJob((next_free_thread[i], self.jobs[self.nextJobIndex]))
                        self.nextJobIndex += 1
                next_free_thread = []
                jobDone = []
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

        if leftChildIndex < self.heapSize and self.currentJobs[leftChildIndex][1] <= self.currentJobs[minIndex][1]:
            minIndex = leftChildIndex

        if rightChildIndex < self.heapSize  and self.currentJobs[rightChildIndex][1] <= self.currentJobs[minIndex][1]:
            minIndex = rightChildIndex

        # print('minIndex: {}'.format(minIndex))
        if i != minIndex and minIndex < self.heapSize:
            # self._swaps.append((i, minIndex))
            self.currentJobs[i], self.currentJobs[minIndex] = self.currentJobs[minIndex], self.currentJobs[i]
            self.siftDown(minIndex)


    def siftUp(self, i):
        while i > 0 and self.currentJobs[self.parent(i)][1] > self.currentJobs[i][1]:
            self.currentJobs[self.parent(i)], self.currentJobs[i] = self.currentJobs[i], self.currentJobs[self.parent(i)]
            i = self.parent(i)
            

    def parent(self, i):
        return int((i - 1) / 2)


    def extractMin(self):
        result = self.currentJobs[0]
        self.currentJobs[0] = self.currentJobs[-1:][0]
        self.heapSize = self.heapSize - 1
        
        # print("Extracting: {}".format(result))
        # print("After extract: {}".format(self.currentJobs))
        
        self.siftDown(0)
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


# python3

class JobQueue:

    currentJobs = []

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.nextJob = self.num_workers

        for i in range(self.num_workers):
            self.currentJobs.append((i, self.jobs[i]))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers

        print("before: {}".format(self.currentJobs))
        self.buildHeap()
        print("after: {}".format(self.currentJobs))
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
        # print('minIndex: {}'.format(minIndex))

        if leftChildIndex < self.num_workers and self.currentJobs[leftChildIndex][1] < self.currentJobs[minIndex][1]:
            minIndex = leftChildIndex

        if rightChildIndex < self.num_workers  and self.currentJobs[rightChildIndex][1] < self.currentJobs[minIndex][1]:
            minIndex = rightChildIndex

        if i != minIndex and minIndex < self.num_workers:
            # self._swaps.append((i, minIndex))
            self.currentJobs[i], self.currentJobs[minIndex] = self.currentJobs[minIndex], self.currentJobs[i]
            self.siftDown(minIndex)

    def buildHeap(self):
        for i in range(len(self.currentJobs)/2, -1, -1):
            self.siftDown(i)

    def solve(self):
        # self.read_data()

        self.num_workers = 5
        self.jobs = [1, 10, 3, 5, 3, 8, 9, 3, 5, 4]
        
        for i in range(self.num_workers):
            self.currentJobs.append((i, self.jobs[i]))

        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()


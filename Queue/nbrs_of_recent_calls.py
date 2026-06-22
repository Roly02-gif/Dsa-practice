class RecentCounter:

    def __init__(self):
        self.req_time = []

    def ping(self, t: int) -> int:
        self.req_time.append(t)
        i = 0
        while i < len(self.req_time) and self.req_time[i] < t-3000:
            i += 1
        
        self.req_time = self.req_time[i:]
        return len(self.req_time)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
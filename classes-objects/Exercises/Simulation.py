import statistics as stats

class Simulation:
    def __init__(self, fnct_to_run, iterations):
        self._fnct_to_run = fnct_to_run
        self._iterations = iterations
        self._results = []
        self.run()
        
    def run(self):
        for i in range(self._iterations):
            result = self._fnct_to_run()
            self._results.append(result)
    
    def get_mean(self):
        return stats.mean(self._results)
    
    def get_median(self):
        return stats.median(self._results)
    
    def get_mode(self):
        try:
            return stats.mode(self._results)
        except:
            return None
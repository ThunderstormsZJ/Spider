import sys, time
class ProgressBar(object):
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width

    def move(self):
        self.count += 1

    def log(self, message=None):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        if message:
            print message
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()
    
    def progress(self):
        for i in range(self.total):
            self.move()
            self.log()
            time.sleep(1)
import luigi


class TestTask(luigi.Task):
    # 任务参数
    _params = luigi.Parameters()

    def require(self):
        # 每个任务的入口
        return LastTask()

    def run(self):
        # 每个任务具体执行内容
        pass

    def output(self):
        # 每个任务的出口
        pass

class LastTask(luigi.task):
    def run(self):
        return "last"
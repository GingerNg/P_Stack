import time

from taskflow import task, retry, engines
from taskflow.patterns import linear_flow


class EchoTask(task.Task):
       def execute(self, *args, **kwargs):
           print(self.name)
           time.sleep(10)
           # print(args)
           # print(kwargs)
...
flow = linear_flow.Flow('f1').add(
       EchoTask('t1'),
       linear_flow.Flow('f2', retry=retry.ForEach(values=['a', 'b', 'c'], name='r1', provides='value')).add(
           EchoTask('t2'),
           EchoTask('t3', requires='value')),
       EchoTask('t4'))

e = engines.load(flow, executor='threaded', engine='parallel',  # 并行
                 max_workers=1)
e.run()
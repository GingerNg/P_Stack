"""
路易吉
https://bionics.it/posts/luigi-tutorial

http://luiti.github.io/chinese/The-core-concepts-of-Luigi.html

python3 helloword.py --local-scheduler NameSubstituter
python3 helloword.py --local-scheduler NameSubstituter --name samuel

Visualizing running workflows
python3 helloword.py --scheduler-host localhost NameSubstituter --name samuel
"""
import time

import luigi


class HelloWorld(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('helloworld.txt')

    def run(self):
        time.sleep(15)
        with self.output().open('w') as outfile:
            outfile.write('Hello World!\n')


class NameSubstituter(luigi.Task):
    name = luigi.Parameter()

    def requires(self):
        return HelloWorld()

    def output(self):
        return luigi.LocalTarget(self.input().path + '.name_' + self.name)

    def run(self):
        time.sleep(15*1000)
        with self.input().open() as infile, self.output().open('w') as outfile:
            text = infile.read()
            text = text.replace('World', self.name)
            outfile.write(text)
        time.sleep(15)


if __name__ == '__main__':
    luigi.run()

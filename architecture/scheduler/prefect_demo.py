from prefect import task, Flow

"""
https://github.com/PrefectHQ/prefect
"""

@task
def say_hello():
    print("Hello, world!")


with Flow("My First Flow") as flow:
    say_hello()


flow.run() # "Hello, world!"
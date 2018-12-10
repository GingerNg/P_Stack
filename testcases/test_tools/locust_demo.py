# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: locust_demo.py
@time: 2018/7/1 14:52
@description：LOCUST： An open source load testing tool.
A fundamental feature of Locust is that you describe all your test in Python code.
"""

from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
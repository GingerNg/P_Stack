# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: click_demo.py
@time: 2018/5/18 16:50
"""
import click

@click.group()
def mysteem():
        pass

@click.command()
def vote():
        pass

@click.command()
def transfer():
        pass

mysteem.add_command(vote)
mysteem.add_command(transfer)

if __name__ == '__main__':
        mysteem()
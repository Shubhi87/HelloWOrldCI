#!/usr/bin/env python
import click

# import requests

@click.command()
def hello():
    click.echo("Hello, This is shubhi")
    
if __name__ == '__main__':
    hello()
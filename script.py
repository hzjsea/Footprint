#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: main.py.py
@time: 2021/10/7 4:53 下午
"""
import click
from common import showjob,utils
import sys


@click.group()
def cli():
    # print("example record input -i switch@action@commentary")
    pass


def check_text(ctx, param, value):

    if not value or ctx.resilient_parsing:
        ctx.exit()

    l = str(value).split("@")
    if len(l) != 3:
        click.echo("please input value like this switch@action@commentary ")
        ctx.exit()

    return value

@cli.command()
@click.option("-i", "--input", "text", callback=check_text)
def input(text: str):
    # 将内容写到文件里面
    switch_name, action, commentary = tuple(text.split("@"))
    path = utils.path_of_record()
    with open(path, 'r+') as f:
        content = f.readlines()
        id = len(content) + 1
        date = utils.get_current_time()
        line = f"{id} | {date} | {switch_name} | {action} | {commentary} \n"
        f.seek(0, 0)
        f.write(line)
        f.writelines(content)
        f.close()


@cli.command()
@click.option("-a", "--all", is_flag=True, show_default="flag(标注) is true")
@click.option("-d", "--day", type=int,  default=None, show_default="根据天数输出, 1-31")
@click.option("-m", "--month", type=int, default=None, show_default="根据月份输出 1-12")
# @click.option("-k", "--key", type=(str, str, str), nargs=3, default=None, show_default="根据关键词输出 xx gg zz, limit 3")
@click.option("-k", "--key", multiple=True, show_default="-k xx -k yy -k zz")
def show(all, day, month, key):
    if all:
        click.echo(showjob.show_all_content())
        sys.exit(0)
    
    if day or month:
        res = showjob.show_content_time(day, month)
        if res:
            click.echo(res)
        else:
            click.echo("当前范围内无记录")
        sys.exit(0)
    
    if key:
        key = list(key)
        res = showjob.show_content_keywards(key)
        if res:
            click.echo(res)
        else:
            click.echo("当前关键词无记录")
        sys.exit(0)

@cli.command()
@click.option("-p")
@click.option("-o")
@click.option("-l")
def example(p: int, o: int, l: int):
    if p:
        click.echo("parames is p")
    elif o:
        click.echo("parames is o")
    elif l:
        click.echo("parames is l")
    elif l and p:
        click.echo("parames is l and p")
    else:
        click.echo("example like this")
    
def echo_p(p: int):
    if p:
        click.echo("parames is p")

def echo_o(o: int):
    if o:
        click.echo("parames is o")


def echo_l(l: int):
    if l:
        click.echo("parames is l")

def echo_p_o(p: int, o: int):
    if p and o:
       click.echo(f"{p},{o}")

@cli.command()
@click.option("-p")
@click.option("-o")
@click.option("-l")
def instance(p: int, o: int, l: int):
    echo_p(p)
    echo_o(o)
    echo_l(l)
    echo_p_o(p,o)

if __name__ == '__main__':
    cli()

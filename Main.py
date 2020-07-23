import sys

import discord
from datetime import date
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
import os
import random

load_dotenv()
DiscToken = 'NzI5NTcwNDM3NTU3NzgwNTEx.XwK9FQ.CKOtxonYN547wG_jwP48DdE_txc'

bot = commands.Bot(command_prefix='>')

@bot.command()
async def helpme(ctx):
    await ctx.send('>help: this command\n>job <job>: use to pick a job\n>work: use to work after you\'ve picked a job\n>daily: use to get you free $250/day\n>bal: use to check your balance(if you have $0 it will not work)\nif you believe you\'ve encountered a bug, send it to t8j#0613')
@bot.command()
async def daily(ctx):
    today = date.today()
    dt = open(str(ctx.message.author.id) + 'dailytime.txt', 'a+')
    if os.stat(str(ctx.message.author.id) + 'dailytime.txt').st_size == 0:
        dt.write('69')
    dt = open(str(ctx.message.author.id) + 'dailytime.txt', 'r')
    daytime = int(dt.read())
    today2 = int(today.strftime("%Y%m%d"))
    if daytime < today2:
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        balvar = b.read()
        os.remove(str(ctx.message.author.id) + 'bal.txt')
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        b.write(str(int(balvar) + 250))
        b.close()
        response = '$250 added'
        os.remove(str(ctx.message.author.id) + 'dailytime.txt')
        dt2 = open(str(ctx.message.author.id) + 'dailytime.txt', 'a+')
        dt2.write(today.strftime("%Y%m%d"))
    else:
        response = 'it appears it hasn\'t been a day. so fuck off'
    await ctx.send(response)


@bot.command()
async def bal(ctx):
    ba = open(str(ctx.message.author.id) + 'bal.txt', 'r+')
    response = '$' + ba.read()
    await ctx.send(response)


@bot.command()
async def work(ctx):
    today = datetime.today()
    today2 = int(today.strftime("%Y%m%d%H"))
    jb = open(str(ctx.message.author.id) + 'job.txt', 'a+')
    if os.stat(str(ctx.message.author.id) + 'job.txt').st_size == 0:
        jb.write('0')
        jb.close()
    jb = open(str(ctx.message.author.id) + 'job.txt', 'r')
    job = jb.read()
    ncdt = open(str(ctx.message.author.id) + 'ncdt.txt', 'a+')
    if os.stat(str(ctx.message.author.id) + 'ncdt.txt').st_size == 0:
        ncdt.write('0')
        ncdt.close()
    ncdt = open(str(ctx.message.author.id) + 'ncdt.txt', 'r')
    ncd = ncdt.read()
    if job == 'nickdonaldworker':
        if (int(ncd) + 5 < today2):
            rand = random.randrange(1, 2)
            os.remove(str(ctx.message.author.id) + 'ncdt.txt')
            nc = open(str(ctx.message.author.id) + 'ncdt.txt', 'a+')
            nc.write(today.strftime("%Y%m%d%H"))
            nc.close()
            if rand == 1:
                global ncdmech
                ncdmech = ctx.message.author.id
                response = 'is the ice cream machine broken (>y/>n)'
                await ctx.send(response)
                return
            if rand == 2:
                global ncdnug
                ncdnug = ctx.message.author.id
                response = 'what are our nuggets made of?\n>a) chicken\n>b) children who got lost in the ball pit\n>c) the mystery meat from the dumpster\n>d) the souls of the fallen'
                await ctx.send(response)
                return
        else:
            await ctx.send('it hasn\'t been 6 hours dumbass')

@bot.command()
async def y(ctx):
    global ncdmech
    if ctx.message.author.id == ncdmech:
        response = 'good job. $300 to you'
        ncdmech = 0
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        balvar = b.read()
        os.remove(str(ctx.message.author.id) + 'bal.txt')
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        b.write(str(int(balvar) + 300))
        b.close()
        await ctx.send(response)


@bot.command()
async def n(ctx):
    global ncdmech
    if ctx.message.author.id == ncdmech:
        response = 'what are you smoking lmao -$200 you pleb'
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        balvar = b.read()
        os.remove(str(ctx.message.author.id) + 'bal.txt')
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        b.write(str(int(balvar) - 200))
        b.close()
        ncdmech = 0
        await ctx.send(response)
@bot.command()
async def a(ctx):
    global ncdnug
    if ctx.message.author.id == ncdnug:
        response = 'in your dreams lmao -$200'
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        balvar = b.read()
        os.remove(str(ctx.message.author.id) + 'bal.txt')
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        b.write(str(int(balvar) - 200))
        b.close()
        ncdnug = 0
        await ctx.send(response)

@bot.command()
async def b(ctx):
    global ncdnug
    if ctx.message.author.id == ncdnug:
        rand = random.randrange(100, 300)
        response = 'good job you get $' + str(rand)
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        balvar = b.read()
        os.remove(str(ctx.message.author.id) + 'bal.txt')
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        b.write(str(int(balvar) + rand))
        b.close()
        ncdnug = 0
        await ctx.send(response)

@bot.command()
async def c(ctx):
    global ncdnug
    if ctx.message.author.id == ncdnug:
        rand = random.randrange(100, 300)
        response = 'good job you get $' + str(rand)
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        balvar = b.read()
        os.remove(str(ctx.message.author.id) + 'bal.txt')
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        b.write(str(int(balvar) + rand))
        b.close()
        ncdnug = 0
        await ctx.send(response)

@bot.command()
async def d(ctx):
    global ncdnug
    if ctx.message.author.id == ncdnug:
        rand = random.randrange(100, 300)
        response = 'good job you get $' + str(rand)
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        balvar = b.read()
        os.remove(str(ctx.message.author.id) + 'bal.txt')
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        b.write(str(int(balvar) + rand))
        b.close()
        ncdnug = 0
        await ctx.send(response)


@bot.command()
async def job(ctx, arg):
    if arg == 'NickDonaldWorker':
        send = 'you now work at NickDonald\'s use >work to work!'
        jb = open(str(ctx.message.author.id) + 'job.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'job.txt').st_size == 0:
            jb.write('0')
            jb.close()
        else:
            jb.close()
            os.remove(str(ctx.message.author.id) + 'job.txt')
            jb = open(str(ctx.message.author.id) + 'job.txt', 'a+')
            jb.write('nickdonaldworker')
            jb.close()
    else:
        send = 'you seem to be lost. or maybe I am, idk.\nvalid professions:\nNickDonaldWorker'
    await ctx.send(send)
@bot.command()
async def shop(ctx):
    sp = open('shop.txt', 'r')
    await ctx.send(sp.read())
@bot.command()
async def buy(ctx, arg):
    if arg == 'americanflag':
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        if int(b.read()) > 1999:
            b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
            balvar = b.read()
            os.remove(str(ctx.message.author.id) + 'bal.txt')
            b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
            b.write(str(int(balvar) - 2000))
            b.close()
            inv = open(str(ctx.message.author.id) + 'flag.txt', 'a+')
            if os.stat(str(ctx.message.author.id) + 'flag.txt').st_size == 0:
                inv.write('0')
            inv.close()
            inv = open(str(ctx.message.author.id) + 'flag.txt', 'r+')
            inv2 = inv.read()
            inv.close()
            inv = open(str(ctx.message.author.id) + 'flag.txt', 'w+')
            inv.write(str(int(inv2)+1))
            inv.close()
            response = 'you are now the proud owner of the american flag'
        else:
            response = 'you broke boi'
    if arg == 'pinkdildo':
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        if int(b.read()) > 49:
            b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
            balvar = b.read()
            os.remove(str(ctx.message.author.id) + 'bal.txt')
            b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
            b.write(str(int(balvar) - 50))
            b.close()
            inv = open(str(ctx.message.author.id) + 'pd.txt', 'a+')
            if os.stat(str(ctx.message.author.id) + 'pd.txt').st_size == 0:
                inv.write('0')
            inv.close()
            inv = open(str(ctx.message.author.id) + 'pd.txt', 'r+')
            inv2 = inv.read()
            inv.close()
            inv = open(str(ctx.message.author.id) + 'pd.txt', 'w+')
            inv.write(str(int(inv2)+1))
            inv.close()
            response = 'you are now the proud owner of the pink dildo'
        else:
            response = 'you broke boi'
    if arg == 'baldeagletrophy':
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        if int(b.read()) > 9999:
            b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
            balvar = b.read()
            os.remove(str(ctx.message.author.id) + 'bal.txt')
            b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
            b.write(str(int(balvar) - 10000))
            b.close()
            inv = open(str(ctx.message.author.id) + 'bet.txt', 'a+')
            if os.stat(str(ctx.message.author.id) + 'bet.txt').st_size == 0:
                inv.write('0')
            inv.close()
            inv = open(str(ctx.message.author.id) + 'bet.txt', 'r+')
            inv2 = inv.read()
            inv.close()
            inv = open(str(ctx.message.author.id) + 'bet.txt', 'w+')
            inv.write(str(int(inv2)+1))
            inv.close()
            response = 'you are now the proud owner of the bald eagle trophy'
        else:
            response = 'you broke boi'
    if arg == 'silverbaldeagletrophy':
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        if int(b.read()) > 49999:
            b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
            balvar = b.read()
            os.remove(str(ctx.message.author.id) + 'bal.txt')
            b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
            b.write(str(int(balvar) - 50000))
            b.close()
            inv = open(str(ctx.message.author.id) + 'sbet.txt', 'a+')
            if os.stat(str(ctx.message.author.id) + 'sbet.txt').st_size == 0:
                inv.write('0')
            inv.close()
            inv = open(str(ctx.message.author.id) + 'sbet.txt', 'r+')
            inv2 = inv.read()
            inv.close()
            inv = open(str(ctx.message.author.id) + 'sbet.txt', 'w+')
            inv.write(str(int(inv2)+1))
            inv.close()
            response = 'you are now the proud owner of the silver bald eagle trophy'
        else:
            response = 'you broke boi'
    if arg == 'goldbaldeagletrophy':
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        if int(b.read()) > 99999:
            b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
            balvar = b.read()
            os.remove(str(ctx.message.author.id) + 'bal.txt')
            b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
            b.write(str(int(balvar) - 100000))
            b.close()
            inv = open(str(ctx.message.author.id) + 'gbet.txt', 'a+')
            if os.stat(str(ctx.message.author.id) + 'gbet.txt').st_size == 0:
                inv.write('0')
            inv.close()
            inv = open(str(ctx.message.author.id) + 'gbet.txt', 'r+')
            inv2 = inv.read()
            inv.close()
            inv = open(str(ctx.message.author.id) + 'gbet.txt', 'w+')
            inv.write(str(int(inv2)+1))
            inv.close()
            response = 'you are now the proud owner of the gold bald eagle trophy'
        else:
            response = 'you broke boi'
    if arg == 'cherrycock':
        b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'bal.txt').st_size == 0:
            b.write('0')
        b.close()
        b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
        if int(b.read()) > 999:
            b = open(str(ctx.message.author.id) + 'bal.txt', 'r')
            balvar = b.read()
            os.remove(str(ctx.message.author.id) + 'bal.txt')
            b = open(str(ctx.message.author.id) + 'bal.txt', 'a+')
            b.write(str(int(balvar) - 1000))
            b.close()
            inv = open(str(ctx.message.author.id) + 'cc.txt', 'a+')
            if os.stat(str(ctx.message.author.id) + 'cc.txt').st_size == 0:
                inv.write('0')
            inv.close()
            inv = open(str(ctx.message.author.id) + 'cc.txt', 'r+')
            inv2 = inv.read()
            inv.close()
            inv = open(str(ctx.message.author.id) + 'cc.txt', 'w+')
            inv.write(str(int(inv2)+1))
            inv.close()
            response = 'you are now the proud owner of a cherry cock'
        else:
            response = 'you broke boi'
    await ctx.send(response)

@bot.command()
async def sell(ctx, arg):
    if arg == 'americanflag':
        b = open(str(ctx.message.author.id) + 'flag.txt', 'a+')
        if os.stat(str(ctx.message.author.id) + 'flag.txt').st_size == 0:
            b.write('0')
        b.close()
    await ctx.send(response)

@bot.command()
async def kys(ctx):
    if str(ctx.message.author.id) == '295349622765912086' or str(ctx.message.author.id) == '550416702295375882':
        await ctx.send('goodbye')
        sys.exit()

@bot.command()
async def inv(ctx):
    usf = open(str(ctx.message.author.id) + 'flag.txt', 'a+')
    if os.stat(str(ctx.message.author.id) + 'flag.txt').st_size == 0:
        usf.write('0')
    usf.close()
    usf = open(str(ctx.message.author.id) + 'flag.txt', 'r+')
    flags = usf.read()
    usf.close()

    pd = open(str(ctx.message.author.id) + 'pd.txt', 'a+')
    if os.stat(str(ctx.message.author.id) + 'pd.txt').st_size == 0:
        pd.write('0')
    pd.close()
    pd = open(str(ctx.message.author.id) + 'pd.txt', 'r+')
    dildos = pd.read()
    pd.close()

    chc = open(str(ctx.message.author.id) + 'cc.txt', 'a+')
    if os.stat(str(ctx.message.author.id) + 'cc.txt').st_size == 0:
        chc.write('0')
    chc.close()
    chc = open(str(ctx.message.author.id) + 'cc.txt', 'r+')
    cc = chc.read()
    chc.close()

    bt = open(str(ctx.message.author.id) + 'bet.txt', 'a+')
    if os.stat(str(ctx.message.author.id) + 'bet.txt').st_size == 0:
        bt.write('0')
    bt.close()
    bt = open(str(ctx.message.author.id) + 'bet.txt', 'r+')
    bet = bt.read()
    bt.close()

    sbt = open(str(ctx.message.author.id) + 'sbet.txt', 'a+')
    if os.stat(str(ctx.message.author.id) + 'sbet.txt').st_size == 0:
        sbt.write('0')
    sbt.close()
    sbt = open(str(ctx.message.author.id) + 'sbet.txt', 'r+')
    sbet = sbt.read()
    sbt.close()

    gbt = open(str(ctx.message.author.id) + 'gbet.txt', 'a+')
    if os.stat(str(ctx.message.author.id) + 'gbet.txt').st_size == 0:
        gbt.write('0')
    gbt.close()
    gbt = open(str(ctx.message.author.id) + 'gbet.txt', 'r+')
    gbet = gbt.read()
    gbt.close()

    await ctx.send('You currently have:\n'+flags+' american flag(s) :flag_us:\n'+dildos+' pink dildo(s) :eggplant:\n'+cc+' cherry cock(s) :cherries: :eggplant:\n'+bet+' bald eagle trophie(s) :eagle:\n'+sbet+' silver bald eagle trophie(s) <:eagsil:731923625472688168>\n'+gbet+' gold bald eagle trophie(s) <:eaggol:731923625007120425>\n')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=">helpme for help"))


bot.run(DiscToken)

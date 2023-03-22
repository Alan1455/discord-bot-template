# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲



# 先去microsoft store搜尋python, 找到python的最新版本(如果沒錯應該是3.11.1)
# 等安裝完去cmd輸入(cmd是按win+r之後在彈出的視窗輸入"cmd")
# "pip install discord.py" # 這串字的意義是安裝這個discord.py的模組, 這樣import才不會呼叫不到.
# 如果以上行不通請輸入
# "pip3 install discord.py" # 這串字的意義是安裝這個discord.py的模組, 這樣import才不會呼叫不到.




import discord                   # 如果這邊都是有顏色的那代表你做對了(有裝vs code插件情況下)
from discord.ext import commands # 如果沒裝插件就沒報錯就行(黃色波浪號在文字下方就是有報錯)



TOKEN = "" # 輸入你bot的token
# 如何創建去這 https://discord.com/developers/applications 登入帳號後按 New Application
# 把該填的填完去到bot頁面按 Bot -> Reset Token -> Copy , 你就成功把bot token copy下來了, 再來貼到TOKEN變數裡就好




intents = discord.Intents.all() # 它只是一個Primer to Gateway Intents
# 從discord.py更新1.5.0之後就要加了(不加你bot運作不了), .all是要求所有的權限, 它可以是.default, 也可以是.none
# https://discordpy.readthedocs.io/en/stable/api.html#intents


# !!重要!! 要去剛剛copy bot token的那個頁面把 Privileged Gateway Intents 底下的選項都打開


prefix = ("$") # 機器人的指令前墜, 可以自訂

ac = discord.Game(name="天婦羅") # discord.Game的name可自訂義

status = discord.Status.dnd
# Status可以是online(在線上), idle(閒置), dnd(請勿打擾), invisible(隱身) 


client = commands.Bot(command_prefix = commands.when_mentioned_or(prefix), activity = ac, status = status, intents = intents) # 賦值client, 方便我們後續寫commands


@client.event # 在啟動的任何時候
async def on_ready(): # on_ready 當啟動時

    print('opened')
    # 從終端告訴你好了(opened)




@client.event # 在啟動的任何時候
async def on_message(message: discord.Message): # on_message 當有訊息時

    await client.process_commands(message) # 如果是輸入指令就不計在此function裡

    if message.author.id == client.user.id: # 如果說話的人是機器人的話pass掉
        pass




@client.command() # command 一個指令
async def hello(ctx: discord.Message): # 當你輸入.hello的時候會召喚這, 每個function名字都可以自訂

    await ctx.channel.send(f"hello {ctx.author.mention}")
    # 當有人說.hello的時候會說的話
    # 在""前加f是為了格式化 {} 裡面包的東西
    # ctx是 content 你可以把它看作是.hello這句話本身
    # ctx.author.id是說這句話(.hello)的人的id

    # !!重要!! <@{ctx.author.id}> 跟 {ctx.author.mention} 是一樣的, 只有差在<@>





@client.command() # command 一個指令
async def dm(ctx: discord.Message, user: discord.User = None, value: str = None): # 這裡有2個值(.dm完要輸入的), 一個是user(tag要dm的人), 另一個value(要對dm的人講的話), 例如.dm @FM_TW#9487 Hi

    await ctx.delete() # 刪除.dm訊息

    if user == None: # 如果要dm的人找不到/沒這個人
        await ctx.channel.send(f'{ctx.author.mention} 這誰 找不到啦') # tag說這句話的人說: "這誰 找不到啦"
    

    else: # 如果有找到要dm的人

        if value == None: # 如果你只有dm人沒填要講的話
            await ctx.channel.send(f'{ctx.author.mention} 不要叫我dm人還不講話') # tag說這句話的人說: "不要叫我dm人還不講話"

        else: # 反之(懶得打字了)
            await user.send(value) # 對@FM_TW說Hi(上方例如)





client.remove_command('help') # 因為dc預設有幫bot設這個指令, 所以我們要刪掉他(不然會跟下面起衝突)

@client.command() # command 一個指令

async def help(ctx: discord.Message): # 不用我多說了吧?

    embed = discord.Embed(title = "Commands", description = "幫助你了解這些指令", color = 0x4599)
    # 建立一個embed, 標題叫 Commands, 副標題是 description, color是那一格左邊的一條顏色(不知道怎麼形容), 可以去這看看 -> https://www.htmlcsscolor.com/hex/

    embed.add_field(name = ".hello", value = "跟你say hello", inline = False) 
    embed.add_field(name = ".dm", value = "用bot dm你指定的人, .dm (想dm誰) (dm說的話)", inline = False)
    # 內容 實際運作看看就懂了(絕對不是我懶)

    await ctx.channel.send(embed = embed) # 讓bot說出這串embed




client.run(TOKEN) # 讓你的bot動起來


# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲
# 天婦羅萬歲xd

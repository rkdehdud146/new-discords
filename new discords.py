import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.id)
    print("ready")
    print('------')
    game =discord.Game("치이 아루엘")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.even
async def on_message(massage):
    if message.content.startswith("치이야 안녕"):
        await message.channel.send("안녕")
    if message.content.startswith("안녕 치이야"):
        await message.channel.send("안녕ㅎㅇㅎㅇ")
    if message.content.startswith("치이야 소울워커"):
        await message.channel.sent("망....갓겜!")
    if message.content.startswith("치이야 블리자드월드"):
        await message.channel.send("킹갓맵")
    if message.content.startswith("치이야 블리자드월드 101단계"):
        await message.channel.send("HM9EV")
    if message.content.startswith("치이야 블리자드월드 33단계"):
        await message.channel.send("16YDR")
    if message.content.startswith("치이야 발로란트"):
        await message.content.startswith("오퍼 망겜")
    if message.content.startswith("치이야 오버워치"):
        await message.channel.send("망겜")
    if message.content.startswith("치이야 개발자가 업데이드 언제 해줄까?"):
        await message.channel.send("죽기전엔 할 것 같음")


client.run('NzI3ODc4MjY1MDk1NzE2ODY1.XvyP0Q.LcHA2PsKsfxA_qP_j1_0z8rx5Ww')
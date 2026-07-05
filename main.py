import discord
from discord.ext import commands
from discord import app_commands

# বট কনফিগারেশন
TOKEN = 'YOUR_BOT_TOKEN'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# রেজিস্ট্রেশন মডাল
class RegModal(discord.ui.Modal, title='Registration Form'):
    ign = discord.ui.TextInput(label='IGN (Ingame Name)')
    region = discord.ui.TextInput(label='Region')
    launcher = discord.ui.TextInput(label='Launcher Type')

    async def on_submit(self, interaction: discord.Interaction):
        # এখানে ডেটাবেসে (MongoDB) সেভ করার কোড হবে
        await interaction.response.send_message(f"ধন্যবাদ {self.ign}! আপনি ভেরিফাইড হয়েছেন।", ephemeral=True)

# বাটন ভিউ
class MainView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Register", style=discord.ButtonStyle.green, custom_id="reg_btn")
    async def reg(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(RegModal())

    @discord.ui.button(label="Queue: Ranked", style=discord.ButtonStyle.blurple, custom_id="queue_btn")
    async def queue(self, interaction: discord.Interaction, button: discord.ui.Button):
        # এখানে ইউজারকে কিউ লিস্টে অ্যাড করার কোড হবে
        await interaction.response.send_message("আপনি কিউতে যুক্ত হয়েছেন!", ephemeral=True)

@bot.event
async def on_ready():
    print(f'{bot.user} অনলাইনে আছে!')
    bot.add_view(MainView())

@bot.command()
async def setup(ctx):
    await ctx.send("নিচের বাটনে ক্লিক করে রেজিস্টার করুন:", view=MainView())

bot.run(TOKEN)

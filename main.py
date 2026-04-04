import discord
from discord import app_commands
import aiohttp

# ──────────────────────────────────────────────
#  EvomaGPT — Discord User App Bot
#  Install scope: applications.commands (user install)
# ──────────────────────────────────────────────

TOKEN = "YOUR_BOT_TOKEN_HERE"

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# ════════════════════════════════════════════════
#  STATIC LINK COMMANDS
# ════════════════════════════════════════════════

@tree.command(name="discord", description="Get the RankedTiers Discord invite link")
async def discord_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔗 RankedTiers Discord",
        description="Join the community!\n\n**discord.gg/rankedtiers**",
        color=0xFFD700
    )
    embed.set_footer(text="EvomaGPT", icon_url="https://i.imgur.com/placeholder.png")
    await interaction.response.send_message(embed=embed, ephemeral=True)


@tree.command(name="website", description="Get the RankedTiers tier list website link")
async def website_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🌐 RankedTiers Website",
        description="Check out the official tier list!\n\n🔗 https://www.rankedtiers.net",
        color=0xFFD700
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@tree.command(name="youtube", description="Get the Evoma YouTube channel link")
async def youtube_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="▶️ Evoma on YouTube",
        description="Watch Evoma's videos!\n\n🔗 https://youtube.com/@evomamc",
        color=0xFF0000
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@tree.command(name="mod", description="Get the Ranked Tiers Tagger mod link on Modrinth")
async def mod_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🧩 Ranked Tiers Tagger Mod",
        description="Download the mod on Modrinth!\n\n🔗 https://modrinth.com/mod/ranked-tiers-tagger\n\n*Coming soon!*",
        color=0x1BD96A
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@tree.command(name="ip", description="Get the RankedTiers Minecraft server IPs")
async def ip_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🖥️ RankedTiers — Server IP",
        color=0xFFD700
    )
    embed.add_field(name="🇪🇺 EU", value="`rankedtiers.net`", inline=True)
    embed.add_field(name="🌎 NA", value="`na.rankedtiers.net`", inline=True)
    await interaction.response.send_message(embed=embed, ephemeral=True)


# ════════════════════════════════════════════════
#  DRAIN KIT RULES  (placeholder — edit below)
# ════════════════════════════════════════════════

@tree.command(name="drain_kit", description="Display Drain Kit rules")
async def drain_kit_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚗️ Drain Kit Rules",
        description=(
            "**Rules for Drain Kit:**\n\n"
            "• Rule 1 — *(to be filled)*\n"
            "• Rule 2 — *(to be filled)*\n"
            "• Rule 3 — *(to be filled)*\n\n"
            "*Contact an admin if you have questions.*"
        ),
        color=0x9B59B6
    )
    await interaction.response.send_message(embed=embed)


# ════════════════════════════════════════════════
#  SERVER AD  (placeholder — paste text below)
# ════════════════════════════════════════════════

SERVER_AD_TEXT = """
*(Server ad text — to be filled)*
"""

@tree.command(name="server_ad", description="Post the RankedTiers server advertisement")
async def server_ad_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📢 RankedTiers — Server Advertisement",
        description=SERVER_AD_TEXT,
        color=0xFFD700
    )
    embed.set_footer(text="rankedtiers.net | na.rankedtiers.net")
    await interaction.response.send_message(embed=embed)


# ════════════════════════════════════════════════
#  UUID LOOKUP
# ════════════════════════════════════════════════

@tree.command(name="uuid", description="Look up a Minecraft player's UUID by username")
@app_commands.describe(username="The Minecraft username to look up")
async def uuid_cmd(interaction: discord.Interaction, username: str):
    await interaction.response.defer(ephemeral=True)
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{username}") as resp:
            if resp.status == 200:
                data = await resp.json()
                uuid_raw = data["id"]
                # Format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
                uuid_formatted = f"{uuid_raw[:8]}-{uuid_raw[8:12]}-{uuid_raw[12:16]}-{uuid_raw[16:20]}-{uuid_raw[20:]}"
                embed = discord.Embed(
                    title=f"🔍 UUID — {data['name']}",
                    color=0xFFD700
                )
                embed.add_field(name="Username", value=f"`{data['name']}`", inline=False)
                embed.add_field(name="UUID", value=f"`{uuid_formatted}`", inline=False)
                await interaction.followup.send(embed=embed, ephemeral=True)
            elif resp.status == 404:
                await interaction.followup.send(
                    embed=discord.Embed(
                        description=f"❌ Player **{username}** not found.",
                        color=0xFF0000
                    ),
                    ephemeral=True
                )
            else:
                await interaction.followup.send(
                    embed=discord.Embed(
                        description="❌ Mojang API error. Try again later.",
                        color=0xFF0000
                    ),
                    ephemeral=True
                )


# ════════════════════════════════════════════════
#  EVAL KIT RULES  (placeholder — fill content)
# ════════════════════════════════════════════════

@tree.command(name="eval_kit_rules", description="Display Eval Kit rules")
async def eval_kit_rules_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📋 Eval Kit Rules",
        description=(
            "*(Eval Kit rules — to be filled)*"
        ),
        color=0x3498DB
    )
    await interaction.response.send_message(embed=embed)


# ════════════════════════════════════════════════
#  TIER RESULT COMMANDS  (placeholders)
#  These will be filled when you send the resources
# ════════════════════════════════════════════════

@tree.command(name="lt1", description="Generate a Low Tier 1 result message")
async def lt1_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="LT1 Result",
        description="*(LT1 format — to be filled)*",
        color=0xE74C3C
    )
    await interaction.response.send_message(embed=embed)


@tree.command(name="ht1", description="Generate a High Tier 1 result message")
async def ht1_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="HT1 Result",
        description="*(HT1 format — to be filled)*",
        color=0xF39C12
    )
    await interaction.response.send_message(embed=embed)


@tree.command(name="lt2", description="Generate a Low Tier 2 result message")
async def lt2_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="LT2 Result",
        description="*(LT2 format — to be filled)*",
        color=0x2ECC71
    )
    await interaction.response.send_message(embed=embed)


@tree.command(name="ht2", description="Generate a High Tier 2 result message")
async def ht2_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="HT2 Result",
        description="*(HT2 format — to be filled)*",
        color=0x1ABC9C
    )
    await interaction.response.send_message(embed=embed)


@tree.command(name="ht3", description="Generate a High Tier 3 result message")
async def ht3_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="HT3 Result",
        description="*(HT3 format — to be filled)*",
        color=0x9B59B6
    )
    await interaction.response.send_message(embed=embed)


@tree.command(name="restriction_format", description="Generate a restriction format message with auto UUID")
@app_commands.describe(username="The Minecraft username of the player to restrict")
async def restriction_format_cmd(interaction: discord.Interaction, username: str):
    await interaction.response.defer()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{username}") as resp:
            if resp.status == 200:
                data = await resp.json()
                uuid_raw = data["id"]
                uuid_formatted = f"{uuid_raw[:8]}-{uuid_raw[8:12]}-{uuid_raw[12:16]}-{uuid_raw[16:20]}-{uuid_raw[20:]}"
                embed = discord.Embed(
                    title="🚫 Restriction Format",
                    description=(
                        f"**Player:** `{data['name']}`\n"
                        f"**UUID:** `{uuid_formatted}`\n\n"
                        "*(Restriction format text — to be filled)*"
                    ),
                    color=0xFF0000
                )
                await interaction.followup.send(embed=embed)
            elif resp.status == 404:
                await interaction.followup.send(
                    embed=discord.Embed(
                        description=f"❌ Player **{username}** not found.",
                        color=0xFF0000
                    )
                )
            else:
                await interaction.followup.send(
                    embed=discord.Embed(
                        description="❌ Mojang API error. Try again later.",
                        color=0xFF0000
                    )
                )


# ════════════════════════════════════════════════
#  STARTUP
# ════════════════════════════════════════════════

@client.event
async def on_ready():
    # Sync as USER INSTALL app (global commands)
    await tree.sync()
    print(f"✅ EvomaGPT is online as {client.user}")
    print(f"   Commands synced globally.")


client.run(TOKEN)

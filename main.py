import discord
from discord import app_commands
import aiohttp
from flask import Flask
from threading import Thread
import os
TOKEN = os.environ.get("DISCORD_TOKEN")

# ════════════════════════════════════════════════
#  KEEP-ALIVE (for UptimeRobot)
# ════════════════════════════════════════════════

app = Flask(__name__)

@app.route('/')
def home():
    return "EvomaGPT is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()


client = discord.Client(intents=discord.Intents.none())
tree = app_commands.CommandTree(
    client,
    allowed_installs=app_commands.AppInstallationType(guild=True, user=True),
    allowed_contexts=app_commands.AppCommandContext(guild=True, dm_channel=True, private_channel=True),
)


# ════════════════════════════════════════════════
#  STATIC LINK COMMANDS
# ════════════════════════════════════════════════

@tree.command(name="discord", description="Get the RankedTiers Discord invite link")
async def discord_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Join the RankedTiers community!\n\ndiscord.gg/rankedtiers"
    )


@tree.command(name="website", description="Get the RankedTiers tier list website link")
async def website_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="RankedTiers Website",
        description="Check out the official tier list!\n\nhttps://www.rankedtiers.net",
        color=0xFFD700
    )
    await interaction.response.send_message(embed=embed)


@tree.command(name="youtube", description="Get the Evoma YouTube channel link")
async def youtube_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Evoma on YouTube",
        description="Watch Evoma's videos!\n\nhttps://youtube.com/@evomamc",
        color=0xFF0000
    )
    await interaction.response.send_message(embed=embed)


@tree.command(name="mod", description="Get the Ranked Tiers Tagger mod link on Modrinth")
async def mod_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Ranked Tiers Tagger Mod",
        description="Download the mod on Modrinth!\n\nhttps://modrinth.com/mod/ranked-tiers-tagger",
        color=0x1BD96A
    )
    await interaction.response.send_message(embed=embed)


@tree.command(name="ip", description="Get the RankedTiers Minecraft server IPs")
async def ip_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="RankedTiers Server IP",
        color=0xFFD700
    )
    embed.add_field(name="EU", value="`rankedtiers.net`", inline=True)
    embed.add_field(name="NA", value="`na.rankedtiers.net`", inline=True)
    await interaction.response.send_message(embed=embed)


# ════════════════════════════════════════════════
#  DRAIN KIT RULES
# ════════════════════════════════════════════════

DRAIN_KIT_TEXT = (
    "## <:shulkerbox:1490522294555250688> **__HT3+ Testing Limits & Rules__** <:shulkerbox:1490522294555250688>\n"
    "<:totem:1490522298460016750> - 8 Totems of Undying\n"
    "<:SpeedPotion:1490522296559997038> - You can freely store Potions, Crystals, Obsidian, Pearls, & Bottles o' Enchanting in Shulker Boxes.\n"
    "<:CheckMark:1490523064591581255> - For regulation purposes, please only have the aforementioned items in shulkers at the start of the fight.\n"
    "<:enderchest:1490522287466746026> **Ender Chests are allowed and you may store anything (within the rules) in them!**\n"
    "*(First to 3 Wins for HT3 Tests)*\n"
    "*(First to 4 Wins for T2+ Tests)*\n\n"
    "=========================================================================\n\n"
    "## <:SmoothCrystal:1490523014926958622>  **__Universal Kit Rules & Limits__** <:anchor:1490522268537847808>\n"
    "<:anvil:1490522270089875636> ** - No beacons**\n"
    "🥛 ** - No Milk** *(This item provides little to no benefit without promoting increased stalling)*\n"
    "<:enchantedgapple:1490522286363643965> ** - No Enchanted Golden Apples**  *(The rarity of this item arguably makes it too uncommon to recur in Vanilla PvP)*\n"
    "🐢 ** - No Potions or arrows of the Turtle Master**  *(This item provides little to no benefit outside of the confines of the testing system)*\n"
    "<:anchor:1490522268537847808> ** - 64 Respawn Anchors**  *(This limit is in place to reduce stalling issues with the testing system, with low impact)*\n"
    "🎆 ** - 24 Firework Rockets**  *(This limit is in place to reduce stalling issues with the testing system, with low impact)*\n"
    "<:chestplate:1490522282139975731> ** - 4 Armor Pieces**  *(This limit is in place to reduce issues with the testing system, with low impact)*\n\n"
    "=========================================================================\n\n"
    "## <:grass:1490522289450651749> ***Kit items must be obtainable in 1.21+ Vanilla Survival. This applies to all forms of testing.***"
)

@tree.command(name="drain_kit_rules", description="Display HT3+ Testing Limits & Kit rules")
async def drain_kit_rules_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(DRAIN_KIT_TEXT)


# ════════════════════════════════════════════════
#  SERVER AD
# ════════════════════════════════════════════════

SERVER_AD_TEXT = """#  <:Ranked_Tiers:1490523311082569909>  **[1.21+] RankedTiers Network | EU & NA Crystal PvP & Tier Testing** <:Ranked_Tiers:1490523311082569909>

> <:VerifiedTester:1490523036791603230> - Active Tier Testing & Support
> <:Gift:1490522959075344424> - Frequent Giveaways
> <:Promotion:1490522999177347256> - Tier Tagger Mod  <:GreenArrow:1370871862296449025> https://modrinth.com/project/ranked-tiers-tagger
> <a:fire2:1490522288767111168> - Tier List Website <:GreenArrow:1370871862296449025> [Rankedtiers.net](https://www.rankedtiers.net/)
> <:Settings:1490523010233270342> - Practice Server: `Rankedtiers.net`
> <:Ranked_Tiers:1490523311082569909> - 7 days Test cooldown

-# <:SeniorTester:1490523009390215208> <:mod:1490522982186221669> <:regulator:1490523004470431794> - Dedicated Mods, Regulators, and Testers to Assist You!

<:rule:1490523007095931030> - JOIN NOW: discord.gg/rankedtiers"""

@tree.command(name="server_ad", description="Post the RankedTiers server advertisement")
async def server_ad_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(SERVER_AD_TEXT)


# ════════════════════════════════════════════════
#  UUID LOOKUP
# ════════════════════════════════════════════════

@tree.command(name="uuid", description="Look up a Minecraft player's UUID by username")
@app_commands.describe(username="The Minecraft username to look up")
async def uuid_cmd(interaction: discord.Interaction, username: str):
    await interaction.response.defer()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{username}") as resp:
            if resp.status == 200:
                data = await resp.json()
                uuid_raw = data["id"]
                uuid_formatted = f"{uuid_raw[:8]}-{uuid_raw[8:12]}-{uuid_raw[12:16]}-{uuid_raw[16:20]}-{uuid_raw[20:]}"
                embed = discord.Embed(
                    title=f"UUID — {data['name']}",
                    color=0xFFD700
                )
                embed.add_field(name="Username", value=f"`{data['name']}`", inline=False)
                embed.add_field(name="UUID", value=f"`{uuid_formatted}`", inline=False)
                copy_text = f"{data['name']} - {uuid_formatted}"
                await interaction.followup.send(embed=embed, view=make_copy_button(copy_text))
            elif resp.status == 404:
                await interaction.followup.send(
                    embed=discord.Embed(
                        description=f"Player **{username}** not found.",
                        color=0xFF0000
                    )
                )
            else:
                await interaction.followup.send(
                    embed=discord.Embed(
                        description="Mojang API error. Try again later.",
                        color=0xFF0000
                    )
                )


# ════════════════════════════════════════════════
#  EVAL KIT RULES
# ════════════════════════════════════════════════

EVAL_KIT_TEXT = (
    "## <:VerifiedTester:1490523036791603230> **__Tester Evaluation (Below HT3) Limits & Rules__**\n"
    "<:totem:1490522298460016750> - 14 Totems of Undying\n"
    "<:arrow:1490522271717265522> - No Weakness Arrows *(Due to the absence of storage items, this rule is in place for evaluation tests)*\n"
    "<:shulkerbox:1490522294555250688> - No Storage Items *(Ender Chests, Shulker Boxes, etc.)*\n"
    "*(First to 3 Wins)*\n\n"
    "## <:SmoothCrystal:1490523014926958622>  **__Universal Kit Rules & Limits__** <:anchor:1490522268537847808>\n"
    "<:anvil:1490522270089875636> ** - No beacons**\n"
    "🥛 ** - No Milk** *(This item provides little to no benefit without promoting increased stalling)*\n"
    "<:enchantedgapple:1490522286363643965> ** - No Enchanted Golden Apples**  *(The rarity of this item arguably makes it too uncommon to recur in Vanilla PvP)*\n"
    "🐢 ** - No Potions or arrows of the Turtle Master**  *(This item provides little to no benefit outside of the confines of the testing system)*\n"
    "<:anchor:1490522268537847808> ** - 64 Respawn Anchors**  *(This limit is in place to reduce stalling issues with the testing system, with low impact)*\n"
    "🎆 ** - 24 Firework Rockets**  *(This limit is in place to reduce stalling issues with the testing system, with low impact)*\n"
    "<:chestplate:1490522282139975731> ** - 4 Armor Pieces**  *(This limit is in place to reduce issues with the testing system, with low impact)*\n\n"
    "=========================================================================\n\n"
    "## <:grass:1490522289450651749> ***Kit items must be obtainable in 1.21+ Vanilla Survival. This applies to all forms of testing.***"
)

@tree.command(name="eval_kit_rules", description="Display Eval Kit rules")
async def eval_kit_rules_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(EVAL_KIT_TEXT)


# ════════════════════════════════════════════════
#  HELPERS
# ════════════════════════════════════════════════

def win_or_loss(score: str) -> str:
    try:
        a, b = score.strip().split("-")
        if int(a) > int(b):
            return f"Won {score}"
        else:
            return f"Lost {score}"
    except Exception:
        return score


def make_copy_button(copy_text: str) -> discord.ui.View:
    view = discord.ui.View()

    class CopyButton(discord.ui.Button):
        def __init__(self):
            super().__init__(label="Copy Text", style=discord.ButtonStyle.secondary)
            self.copy_text = copy_text

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.send_message(
                f"```\n{self.copy_text}\n```",
                ephemeral=True
            )

    view.add_item(CopyButton())
    return view


def promoted_or_failed(scores: list[str], tier_name: str) -> str:
    last_score = scores[-1] if scores else ""
    try:
        a, b = last_score.strip().split("-")
        if int(a) < int(b):
            return f"**Failed {tier_name}**"
        else:
            return f"**Promoted to {tier_name}**"
    except Exception:
        return f"**Promoted to {tier_name}**"


# ════════════════════════════════════════════════
#  /HT3
# ════════════════════════════════════════════════

@tree.command(name="ht3", description="Generate a High Tier 3 result message")
@app_commands.describe(
    player="The player (Discord user)",
    ign="In-game name of the player",
    ht3opponent1="HT3 fight 1 opponent name",
    ht3score1="HT3 fight 1 score (e.g. 3-2)",
    ht3opponent2="HT3 fight 2 opponent name (optional)",
    ht3score2="HT3 fight 2 score (optional)",
)
async def ht3_cmd(
    interaction: discord.Interaction,
    player: discord.User,
    ign: str,
    ht3opponent1: str,
    ht3score1: str,
    ht3opponent2: str = None,
    ht3score2: str = None,
):
    scores = [ht3score1]
    if ht3score2:
        scores.append(ht3score2)

    result = promoted_or_failed(scores, "High Tier 3")

    lines = [
        f"{player.mention} - {ign} - {result}",
        "*Passed Evaluation*",
        "### __HT3 Fights:__",
        f"> {win_or_loss(ht3score1)} vs. {ht3opponent1}",
    ]
    if ht3opponent2 and ht3score2:
        lines.append(f"> {win_or_loss(ht3score2)} vs. {ht3opponent2}")

    msg = "\n".join(lines)
    await interaction.response.send_message(content=msg, view=make_copy_button(msg))


# ════════════════════════════════════════════════
#  RESTRICTION FORMAT
# ════════════════════════════════════════════════

@tree.command(name="restrictionformat", description="Generate a restriction format message")
@app_commands.describe(
    igns="In-game name(s) of the player(s), separated by commas",
    discord_accounts="Discord mention(s) to restrict (e.g. @user1 @user2)",
    reason="Reason for the restriction",
)
async def restriction_format_cmd(
    interaction: discord.Interaction,
    igns: str,
    discord_accounts: str,
    reason: str,
):
    await interaction.response.defer()

    import re
    mentioned_ids = re.findall(r"<@!?(\d+)>", discord_accounts)
    mentions_display_parts = []
    for uid in mentioned_ids:
        mentions_display_parts.append(f"<@{uid}>")
    mentions_display = ", ".join(mentions_display_parts) if mentions_display_parts else discord_accounts

    ign_list = [ign.strip() for ign in igns.split(",")]
    uuid_lines = []

    async with aiohttp.ClientSession() as session:
        for ign in ign_list:
            async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    uuid_raw = data["id"]
                    uuid_formatted = f"{uuid_raw[:8]}-{uuid_raw[8:12]}-{uuid_raw[12:16]}-{uuid_raw[16:20]}-{uuid_raw[20:]}"
                    uuid_lines.append(f"{ign} - `{uuid_formatted}`")
                else:
                    uuid_lines.append(f"{ign} - `UUID not found`")

    igns_display = ", ".join(ign_list)
    uuid_block = "\n".join(uuid_lines)

    msg = (
        f"{mentions_display} - {igns_display} - Restricted for **{reason}**\n\n"
        f"{uuid_block}"
    )

    await interaction.followup.send(content=msg, view=make_copy_button(msg))


# ════════════════════════════════════════════════
#  /LT2
# ════════════════════════════════════════════════

@tree.command(name="lt2", description="Generate a Low Tier 2 result message")
@app_commands.describe(
    player="The player (Discord user)",
    ign="In-game name of the player",
    ht3opponent1="HT3 fight 1 opponent name",
    ht3score1="HT3 fight 1 score (e.g. 3-2)",
    ht3opponent2="HT3 fight 2 opponent name (optional)",
    ht3score2="HT3 fight 2 score (optional)",
    lt2opponent1="LT2 fight 1 opponent name (optional)",
    lt2score1="LT2 fight 1 score (e.g. 4-3) (optional)",
    lt2opponent2="LT2 fight 2 opponent name (optional)",
    lt2score2="LT2 fight 2 score (optional)",
)
async def lt2_cmd(
    interaction: discord.Interaction,
    player: discord.User,
    ign: str,
    ht3opponent1: str,
    ht3score1: str,
    ht3opponent2: str = None,
    ht3score2: str = None,
    lt2opponent1: str = None,
    lt2score1: str = None,
    lt2opponent2: str = None,
    lt2score2: str = None,
):
    if lt2opponent1 and lt2score1:
        final_scores = [lt2score1]
        if lt2score2:
            final_scores.append(lt2score2)
        result = promoted_or_failed(final_scores, "Low Tier 2")
    else:
        final_scores = [ht3score1]
        if ht3score2:
            final_scores.append(ht3score2)
        result = promoted_or_failed(final_scores, "Low Tier 2")

    lines = [
        f"{player.mention} - {ign} - {result}",
    ]

    if lt2opponent1 and lt2score1:
        lines.append("### __LT2 Fights:__")
        lines.append(f"> {win_or_loss(lt2score1)} vs. {lt2opponent1}")
        if lt2opponent2 and lt2score2:
            lines.append(f"> {win_or_loss(lt2score2)} vs. {lt2opponent2}")

    lines.append("### __HT3 Fights:__")
    lines.append(f"> {win_or_loss(ht3score1)} vs. {ht3opponent1}")
    if ht3opponent2 and ht3score2:
        lines.append(f"> {win_or_loss(ht3score2)} vs. {ht3opponent2}")

    msg = "\n".join(lines)
    await interaction.response.send_message(content=msg, view=make_copy_button(msg))


# ════════════════════════════════════════════════
#  /HT2
# ════════════════════════════════════════════════

@tree.command(name="ht2", description="Generate a High Tier 2 result message")
@app_commands.describe(
    player="The player (Discord user)",
    ign="In-game name of the player",
    lt2opponent1="LT2 fight 1 opponent name",
    lt2score1="LT2 fight 1 score (e.g. 3-2)",
    lt2opponent2="LT2 fight 2 opponent name (optional)",
    lt2score2="LT2 fight 2 score (optional)",
    ht2opponent1="HT2 fight 1 opponent name (optional)",
    ht2score1="HT2 fight 1 score (e.g. 4-3) (optional)",
    ht2opponent2="HT2 fight 2 opponent name (optional)",
    ht2score2="HT2 fight 2 score (optional)",
)
async def ht2_cmd(
    interaction: discord.Interaction,
    player: discord.User,
    ign: str,
    lt2opponent1: str,
    lt2score1: str,
    lt2opponent2: str = None,
    lt2score2: str = None,
    ht2opponent1: str = None,
    ht2score1: str = None,
    ht2opponent2: str = None,
    ht2score2: str = None,
):
    if ht2opponent1 and ht2score1:
        final_scores = [ht2score1]
        if ht2score2:
            final_scores.append(ht2score2)
        result = promoted_or_failed(final_scores, "High Tier 2")
    else:
        final_scores = [lt2score1]
        if lt2score2:
            final_scores.append(lt2score2)
        result = promoted_or_failed(final_scores, "High Tier 2")

    lines = [
        f"{player.mention} - {ign} - {result}",
    ]

    if ht2opponent1 and ht2score1:
        lines.append("### __HT2 Fights:__")
        lines.append(f"> {win_or_loss(ht2score1)} vs. {ht2opponent1}")
        if ht2opponent2 and ht2score2:
            lines.append(f"> {win_or_loss(ht2score2)} vs. {ht2opponent2}")

    lines.append("### __LT2 Fights:__")
    lines.append(f"> {win_or_loss(lt2score1)} vs. {lt2opponent1}")
    if lt2opponent2 and lt2score2:
        lines.append(f"> {win_or_loss(lt2score2)} vs. {lt2opponent2}")

    msg = "\n".join(lines)
    await interaction.response.send_message(content=msg, view=make_copy_button(msg))


# ════════════════════════════════════════════════
#  /LT1
# ════════════════════════════════════════════════

@tree.command(name="lt1", description="Generate a Low Tier 1 result message")
@app_commands.describe(
    player="The player (Discord user)",
    ign="In-game name of the player",
    lt2opponent1="LT2 fight 1 opponent name",
    lt2score1="LT2 fight 1 score (e.g. 4-1)",
    lt2opponent2="LT2 fight 2 opponent name (optional)",
    lt2score2="LT2 fight 2 score (optional)",
    ht2opponent1="HT2 fight 1 opponent name (optional)",
    ht2score1="HT2 fight 1 score (e.g. 4-1) (optional)",
    ht2opponent2="HT2 fight 2 opponent name (optional)",
    ht2score2="HT2 fight 2 score (optional)",
    lt1opponent1="LT1 fight 1 opponent name (optional)",
    lt1score1="LT1 fight 1 score (e.g. 4-3) (optional)",
    lt1opponent2="LT1 fight 2 opponent name (optional)",
    lt1score2="LT1 fight 2 score (optional)",
)
async def lt1_cmd(
    interaction: discord.Interaction,
    player: discord.User,
    ign: str,
    lt2opponent1: str,
    lt2score1: str,
    lt2opponent2: str = None,
    lt2score2: str = None,
    ht2opponent1: str = None,
    ht2score1: str = None,
    ht2opponent2: str = None,
    ht2score2: str = None,
    lt1opponent1: str = None,
    lt1score1: str = None,
    lt1opponent2: str = None,
    lt1score2: str = None,
):
    if lt1opponent1 and lt1score1:
        final_scores = [lt1score1]
        if lt1score2:
            final_scores.append(lt1score2)
    elif ht2opponent1 and ht2score1:
        final_scores = [ht2score1]
        if ht2score2:
            final_scores.append(ht2score2)
    else:
        final_scores = [lt2score1]
        if lt2score2:
            final_scores.append(lt2score2)

    result = promoted_or_failed(final_scores, "Low Tier 1")

    lines = [
        f"{player.mention} - {ign} - {result}",
        "",
    ]

    if lt1opponent1 and lt1score1:
        lines.append("**__LT1 Fights:__**")
        lines.append(f"> {win_or_loss(lt1score1)} vs. {lt1opponent1}")
        if lt1opponent2 and lt1score2:
            lines.append(f"> {win_or_loss(lt1score2)} vs. {lt1opponent2}")
        lines.append("")

    if ht2opponent1 and ht2score1:
        lines.append("**__HT2 Fights:__**")
        lines.append(f"> {win_or_loss(ht2score1)} vs. {ht2opponent1}")
        if ht2opponent2 and ht2score2:
            lines.append(f"> {win_or_loss(ht2score2)} vs. {ht2opponent2}")
        lines.append("")

    lines.append("**__LT2 Fights:__**")
    lines.append(f"> {win_or_loss(lt2score1)} vs. {lt2opponent1}")
    if lt2opponent2 and lt2score2:
        lines.append(f"> {win_or_loss(lt2score2)} vs. {lt2opponent2}")

    msg = "\n".join(lines)
    await interaction.response.send_message(content=msg, view=make_copy_button(msg))

# ════════════════════════════════════════════════
#  /HT1
# ════════════════════════════════════════════════

@tree.command(name="ht1", description="Generate a High Tier 1 result message")
@app_commands.describe(
    player="The player (Discord user)",
    ign="In-game name of the player",
    lt2opponent1="LT2 fight 1 opponent name",
    lt2score1="LT2 fight 1 score (e.g. 4-1)",
    lt2opponent2="LT2 fight 2 opponent name (optional)",
    lt2score2="LT2 fight 2 score (optional)",
    ht2opponent1="HT2 fight 1 opponent name (optional)",
    ht2score1="HT2 fight 1 score (e.g. 4-2) (optional)",
    ht2opponent2="HT2 fight 2 opponent name (optional)",
    ht2score2="HT2 fight 2 score (optional)",
    lt1opponent1="LT1 fight 1 opponent name (optional)",
    lt1score1="LT1 fight 1 score (e.g. 4-2) (optional)",
    lt1opponent2="LT1 fight 2 opponent name (optional)",
    lt1score2="LT1 fight 2 score (optional)",
    ht1opponent1="HT1 fight 1 opponent name (optional)",
    ht1score1="HT1 fight 1 score (e.g. 4-2) (optional)",
)
async def ht1_cmd(
    interaction: discord.Interaction,
    player: discord.User,
    ign: str,
    lt2opponent1: str,
    lt2score1: str,
    lt2opponent2: str = None,
    lt2score2: str = None,
    ht2opponent1: str = None,
    ht2score1: str = None,
    ht2opponent2: str = None,
    ht2score2: str = None,
    lt1opponent1: str = None,
    lt1score1: str = None,
    lt1opponent2: str = None,
    lt1score2: str = None,
    ht1opponent1: str = None,
    ht1score1: str = None,
):
    if ht1opponent1 and ht1score1:
        final_scores = [ht1score1]
    elif lt1opponent1 and lt1score1:
        final_scores = [lt1score1]
        if lt1score2:
            final_scores.append(lt1score2)
    elif ht2opponent1 and ht2score1:
        final_scores = [ht2score1]
        if ht2score2:
            final_scores.append(ht2score2)
    else:
        final_scores = [lt2score1]
        if lt2score2:
            final_scores.append(lt2score2)

    result = promoted_or_failed(final_scores, "High Tier 1")

    lines = [
        f"{player.mention} - {ign} - {result}",
        "",
    ]

    if ht1opponent1 and ht1score1:
        lines.append("__**HT1 Fights:**__")
        lines.append(f"> {win_or_loss(ht1score1)} vs. {ht1opponent1}")
        lines.append("")

    if lt1opponent1 and lt1score1:
        lines.append("__**LT1 Fights:**__")
        lines.append(f"> {win_or_loss(lt1score1)} vs. {lt1opponent1}")
        if lt1opponent2 and lt1score2:
            lines.append(f"> {win_or_loss(lt1score2)} vs. {lt1opponent2}")
        lines.append("")

    if ht2opponent1 and ht2score1:
        lines.append("__**HT2 Fights:**__")
        lines.append(f"> {win_or_loss(ht2score1)} vs. {ht2opponent1}")
        if ht2opponent2 and ht2score2:
            lines.append(f"> {win_or_loss(ht2score2)} vs. {ht2opponent2}")
        lines.append("")

    lines.append("__**LT2 Fights:**__")
    lines.append(f"> {win_or_loss(lt2score1)} vs. {lt2opponent1}")
    if lt2opponent2 and lt2score2:
        lines.append(f"> {win_or_loss(lt2score2)} vs. {lt2opponent2}")

    msg = "\n".join(lines)
    await interaction.response.send_message(content=msg, view=make_copy_button(msg))

# ════════════════════════════════════════════════
#  STARTUP
# ════════════════════════════════════════════════

@client.event
async def on_ready():
    await tree.sync()
    TEST_GUILD = discord.Object(id=1477430339663298701)
    await tree.sync(guild=TEST_GUILD)
    print(f"EvomaGPT is online as {client.user}")
    print(f"Commands synced globally.")


keep_alive()
client.run(TOKEN)

from classes.structure import Article, Category, Links, SubOptions, Topic

links = [
    Links(
        label="GitHub",
        url="https://github.com/chamburr/modmail",
        emoji="<:GitHub_Logo:993990129867825162>",
    ),
    Links(
        label="ModMail Website",
        url="https://modmail.xyz/",
        emoji="<:modamil_logo:993989822173696050>",
    ),
    Links(
        label="ModMail Invite",
        url="https://modmail.xyz/invite",
        emoji="<:ModmailInvite:995422671762358422>",
    ),
]


initial = Category(
    [
        Topic(
            label="Common Troubleshooting for users",
            id=1.0,
            description="Solutions for issues users need to fix from their end",
            content="Select an option from the dropdown to find help for a issue you are having.",
            emoji="<:CommonTroubleshootingForUsers:995419090808229978>",
        ),
        Topic(
            label="How to setup certain aspects of ModMail",
            id=2.0,
            description="Setting the bot up, Using a different category, and more",
            content="Will include all / most setup commands + gifs on running each command (or just a simple screenshot)",
            emoji="<:HowDoISetupCertainAspectsOfMM:995419312435232920>",
        ),
        Topic(
            label="ModMail Premium",
            id=3.0,
            description="Topics related to Modmail premium",
            content=" Modmail premium is a service that allows users to purchase premium features on Modmail.",
            emoji="<:ModmailPremium:995419968986435716>",
        ),
        Topic(
            label="How do I use X command",
            id=4.0,
            description="Examples on how to use each of the configuration commands",
            content="Select a option below to find out how to use a command.",
            emoji="<:HowDoIUseXCommand:995420187379638433>",
        ),
    ]
)


trouleshooting = SubOptions(
    [
        Article(
            label="It says that my message could not be delivered! What do I do?",
            id=1.1,
            content='Check your Privacy Settings for the server you are trying to contact. Enable "allow direct messages for server members"',
            image="https://cdn.discordapp.com/attachments/972598239159283723/986749079218446377/Discord_8aN2padDIt.gif",
            emoji="<:clyde:995754294571704330>",
        ),
        Article(
            label="ModMail told me to verify",
            id=1.2,
            content="""Hi, if you can't verify try the following steps 1.Check you are logged in to the correct Discord account on your borwser. Click the link [here](<https://discord.com/login>) or the button below to check you are logged in correctly. 2. Try opening the verfication link in incognito mode, Yes this works on mobile. Copy paste the following link in your browser: <https://modmail.xyz/login?redirect=/authorized>""",
            links=[
                Links(
                    label="Discord Login",
                    url="https://discord.com/login",
                    emoji="<:discord_logo:995748547074994206>",
                ),
                Links(
                    label="ModMail Verification",
                    url="https://modmail.xyz/login?redirect=/authorized",
                    emoji="<:modamil_logo:993989822173696050>",
                ),
            ],
            emoji="<a:redsiren:853297746626609174>",
        ),
    ]
)


aspects = SubOptions(
    [
        Article(
            label=" Should I give Modmail administrator?",
            id=2.1,
            content="""
                    Providing the administrator role to Modmail would migitate any issues when it comes to permissions, however we do not encourage anyone to provide the administrator permission 
                    to ANY bots in your server (unless you have FULL control over the code and how the bot functions). 
                    Modmail does not require administrator, however it does require certain permissions to work. 
                    Check the "What permissions does ModMail need?" option for more information.
                    """,
        ),
        Article(
            label="Modmail isn't showing anonymous replies to the user",
            id=2.2,
            content="""
                    First off, make sure whether or not you have anonymous replies enabled. 
                    Run `=viewconfig`, and then check whether it says `Enabled` or `Disabled` under "Anonymous Messaging". 
                    If it's disabled, enable it via the `=anonymous` command. If anonymous messaging is enabled, 
                    then make sure you're not using the commands (or have command only mode). 
                    Anonymous messages will only apply to messages sent without commands. 
                    If you want to send an anonymous message via commands, use `=areply`.
                    """,
        ),
        Article(
            label="The bot says that a category is not found, what should I do?",
            id=2.3,
            content="""
                    If you are a server admin; this is telling you that the bot is not set up properly. If you have previously used `=setup`, you might have deleted the category. 
                    Either use `=category [name]` to create the category or `=setup` to set up everything again.
                    
                    If you a server member; This is telling you that the bot is not set up properly on the server you are trying to contact. 
                    Reach out to that servers staff team some alternative way and explain why you were unable to contact ModMail.
                    """,
        ),
        Article(
            label=" Why is the custom emote I sent not working?",
            id=2.4,
            content="Due to Discord requirements; the bot needs to be in the server where the emote is from in order to use it. Otherwise, the emote will show up as `:emote_name:` instead of the actual emote.",
            emoji="<a:community_points:857633011830226944>",
        ),
        Article(
            label=" Why is the ModMail log not working?",
            id=2.5,
            content="This is most likely due to a lack of permission. If it still does not work with full permissions, you can try deleting the channel and run `=logging` to enable it again.",
        ),
        Article(
            label="Why isn't the bot responding to my commands?",
            id=2.6,
            content="""
                    Please check the following before asking for help:
                    • The bot has Read Messages, Send Messages, and Embed Links permissions.
                    • You are using the correct prefix. Use @ModMail prefix to check the prefix.
                    • The command you are using is valid. Check using =help <command>.
                    • The bot is online. Discord might be having issues, or the bot might be restarting.
                    """,
        ),
        Article(
            label="What permissions does ModMail need?",
            id=2.7,
            content="""
                ModMail needs the following permissions:
                - `Manage Channels`
                - `Manage Messages`
                - `Manage Roles`
                - `Read Message History`
                - `Read Messages`
                - `Send Messages`
                - `Embed Links`
                - `Attach Files`
                - `Use External Emojis`
                - `Add Reactions`
            """,
            image="https://media.discordapp.net/attachments/576764854673735680/863863546915979274/unknown-4.png?",
        ),
    ]
)


premium = SubOptions(
    [
        Article(
            label="Where can I buy premium?",
            id=3.1,
            content="You can buy premium on Modmails website on the [premium page](https://modmail.xyz/premium).",
            links=[
                Links(
                    label="Buy Premium",
                    url="https://modmail.xyz/premium",
                    emoji="<:modamil_logo:993989822173696050>",
                )
            ],
        ),
        Article(
            label="What are the perks of Modmail Premium?",
            id=3.2,
            content="""
                    Depending on the tier of premium purchased users will get access to premium features on 1 server (<@&576756461267451934>), 3 servers (<@&576754574346551306>) and 5 servers (<@&576754671620980740>).
                    Users can manage their premium with the following commands:
                    - `=premiumassign <server id>`
                    - `=premiumremove <server id>`
                    - `=premiumslist`
                    
                    Users will also get access to the ticket snippet functionality. This allows staff to easily and quickly reply to users with a pre-defined response. The commands to manage snippets are:
                    - `=viewsnippet [optional snippet name]`
                    - `=snippetadd <snippet name> <snippet content>`
                    - `=snippetremove <snippet name>`
                    To use a snippet in a ticket staff can use the following commands:
                    - `=snippet <snippet name>` / `=a <snippet name>`
                    - `=asnippet <snippet name>` / `=as <snippet name>`
                    """,
            emoji="<:full_star:983027888544702464>",
        ),
        Article(
            label="What payment methods are supported?",
            id=3.3,
            content="ModMail currently only supports PayPal.",
            emoji="<:paypal:995755934737518643>",
        ),
        Article(
            label=" Issues with premium",
            id=3.4,
            content="""
            Any user who bought premium will have one of the following roles depending on the tier purchased: <@&576756461267451934>, <@&576754574346551306> and <@&576754671620980740>.
            This enables them to use the premium management commands to assign/remove premium from servers as well as check which servers they have premium on.
            These commands are found on page 7 of the `=help` command, the second to last page
            **Users must have joined this server before purchasing otherwise they will not have received the patron role and will not be able to use the premium management commands**
            *Note: We can manually assign patron roles to those who do not join before purchase however the user will need to provide proof of payment via a ModMail ticket and the process could take a few hours while we wait for an administrator to be available.*
            """,
            image="https://media.discordapp.net/attachments/576765224460353589/929004300951253012/unknown.png",
            links=[
                Links(
                    label="Premium",
                    url="https://modmail.xyz/premium",
                    emoji="<:modamil_logo:993989822173696050>",
                ),
            ],
        ),
        Article(
            label="How many servers can I use premium on?",
            id=3.5,
            content="""
                    That depends on the tier of modmail you purchased.
                    Basic: 1 server
                    Pro: 3 servers
                    Plus: 5 servers
                    """,
        ),
        Article(
            label="Can I have a personalized version of Modmail?",
            id=3.6,
            content="""
                    You can contact <@381998065327931392> (`James [a_leon]#6196`) for a custom instance. The pricing is at $10/month or $60/year.
                    These are the benefits of a custom instance:
                    - Custom username, avatar and status message.
                    - All the premium features listed here.
                    - No confirmation messages.
                    - Commands to create tickets with users.
                    - Requring a command to send messages.
                    - Optional: Custom commands by SnowyJaguar#1034, within reason.
                    """,
        ),
    ]
)


how_to_commands = SubOptions(
    [
        Article(
            label="How do I view my server configuration?",
            id=4.1,
            content="""
                    To view the server configuration, use the `=viewconfig` command. This will show you the current:
                    - Prefix
                    - Category
                    - Access Roles
                    - Ping Roles
                    - Logging Channel
                    - Status of `loggingplus` (premium)
                    - Status of `anonymous`
                    - Status of `commandonly`
                    - Greeting Message (premium)
                    - Closing Message (premium)
                    """,
        ),
        Article(
            label="Is there a video that shows me how to use Modmail?",
            id=4.2,
            content="Yes! Click the button below to watch the video.",
        ),
        Article(
            label="How do I setup ModMail?",
            id=4.3,
            content="To setup modmail all you need to use is the `=setup` command. This will create a new category at the bottom of you channel list called `ModMail` and will create a new channel in that category called `modmail-log` where the bot will log tickets being opned and closed.",
            image="https://cdn.discordapp.com/attachments/972598239159283723/986610442094936134/Discord_rJLF2pmZKQ.gif",
        ),
        Article(
            label="How do I view/change the prefix for my server.",
            id=4.4,
            content="""
                    To change the prefix for your server use the `=prefix <new prefix>` command. 
                    This will change the prefix for your server e.g. `=prefix !`.
                    To view the current prefix for your server use the `=prefix` command without any arguments.
                    If the bot is not responding to `=` you can mention the bot to use commands e.g. `@ModMail prefix`.
                    """,
            image="https://cdn.discordapp.com/attachments/972598239159283723/986611304540307456/Discord_ZpcIEWvGLQ.png",
        ),
        Article(
            label="How do I ping people when a ticket is opened?",
            id=4.5,
            content='To inform people when new tickets are opened they need to have a ping role. You can set these with the `=pingrole <role mention|role id|role name>` command. You can set up to 10 different ping roles. If a role you are adding by name has a space in the name then you need to wrap the name in `" "` e.g. `=pingrole "Staff Team"`.',
            image="https://cdn.discordapp.com/attachments/972598239159283723/986615308297043968/Discord_LRlwXEUNOB.gif",
        ),
        Article(
            label="How do I manage my logging channel?",
            id=4.6,
            content="Via the =logging command, you can recreate, change and disable the logging channel. If your logging channel was deleted, run =logging to disable it and then re-enable it, which should re-create the channel. If you want to use an existing channel, disable logging by running =logging once. Then run =logging #channel_name to re-enable logging and to send logs to an already existing channel of your choice.",
            image="https://cdn.discordapp.com/attachments/972598239159283723/986616380528930816/Discord_f4oLWVFsgz.gif",
        ),
        Article(
            label="How do I force my staff to reply via commands?",
            id=4.7,
            content="Enable command only mode. You can do so by running `=commandonly`. Once in command only mode, staff members can only send a reply to the users by using the `=reply <message>` command. If they want to reply anonymously, they will need to use `=areply <message>`.",
            image='"https://cdn.discordapp.com/attachments/972598239159283723/986617473040257045/Discord_i7mDyLIgjD.png"',
        ),
        Article(
            label="How do I re-create my ModMail category?",
            id=4.8,
            content="To re-create your ModMail category, you can use the `=category [optional name of category]` command. This will delete your current ModMail category and create a new one.",
            image="https://cdn.discordapp.com/attachments/972598239159283723/986613581900554281/Discord_LwB01WaT1c.gif",
        ),
        Article(
            label="How do I make my staff anonymous?",
            id=4.9,
            content="To make your staff members appear as anonymous, you can use the `=anonymous` toggle command. Note that this will only work on messages sent normally without the use of commands. If you want an anonymous reply via commands, use `=areply`. As for making a member's messages anonymous,  there's no way to do that as this would be too exploitable.",
        ),
        Article(
            label="How do I let people reply to tickets?",
            id=4.10,
            content='To allow people to respond to tickets they need to have a access role. You can set these with the `=accessrole <role mention|role id|role name>` command. You can set up to 10 different access roles. If a role you are adding by name has a space in the name then you need to wrap the name in `" "` e.g. `=accessrole "Staff Team"`.',
            image="https://cdn.discordapp.com/attachments/972598239159283723/986614689725288459/Discord_Pa6RN5xMTH.gif",
        ),
    ]
)

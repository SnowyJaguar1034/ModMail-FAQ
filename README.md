# FAQ
 Simple [Discord.py](https://github.com/Rapptz/discord.py) bot for the ModMail support server

## Table of Contents

- [Questions](#questions)
- [Self Hosting](#self-hosting)<br/>
&nbsp;- [Prerequisites](#prerequisites)<br/>
&nbsp;- [Installing the source](#installing-the-source)<br/>
&nbsp;- [Setup](#setup)<br/>
&nbsp;- [Setting up a virtual environment](#setting-up-a-virtual-environment)<br/>
&nbsp;- [Module Installation](#installing-the-modules)<br/>
&nbsp;- [Running the bot](#running-the-bot)<br/>

## Questions

Have a question? Please avoid opening [issues](https://github.com/SnowyJaguar1034/Zupie/issues) for general questions. Instead, it is much better to [DM me on Discord SnowyJaguar#1034](https://discord.com/users/365262543872327681)

## Self Hosting
This self-hosting guide requires you to have some basic knowledge about [command line](https://www.computerhope.com/jargon/c/commandi.htm), [Python](https://www.python.org/), and Discord bots. We do not provide any official support for self-hosting.
### Prerequisites

In order to run FAQ, you will need to install the following software.

- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/)

You may also want to [set up a virtual environment](#setting-up-a-virtual-environment) so that FAQ's requiremnts don't mess with your base enviroment. 
### Installing the source

Please fork this repository so that you can make pull requests. Then, clone your fork.

```sh
# Clone the repository
git clone https://github.com/<your-github-username>/ModMail-Bot-FAQ.git

# Sometimes you may want to merge changes from the upstream repository to your fork.
git checkout master
git pull https://github.com/SnowyJaguar/zupie.git master
```
### Setup

Configuration is done through a `.env` file. 

You should make a copy of `example.env` and rename it to `.env`. 
- `TOKEN` : Your bots token as found on the [Discord Developer Portal](https://discord.com/developers/applications)
- `GUILD` : The ID of the guild that the bot is in.
- `DESCRIPTION` : The description of your bot
- `ACTIVITY` : The activity message shown on the bot's status

### Setting up a virtual environment
This is useful if you want to run a variety of python projects on a machine but not have version conflicts. I highly recommend doing this even if you only have one project, I didn't understand the appeal when I started using python but after a while I started seeeing the benefits.

```sh
# Go to your project’s working directory
$ cd your-bot-source-directory
# In this example I am using 'env' as the name of my virtual
# environment however you can use whatever you want
$ python3 -m venv env

# Activate the virtual environment
# On Linux
$ source env/bin/activate

# On Windows
$ env\Scripts\activate.bat

# Use pip like usual
$ (env) <Your source directory>pip install -r requirements.txt
```

### Installing the Modules

FAQ utilises [discord.py](https://github.com/Rapptz/discord.py) and several other modules to function properly. The list of modules can be found in [`requirements.txt`](requirements.txt) and you can install them with the following command.

```sh
pip install -r requirements.txt
```
### Running the bot

Congratulations! You have set up everything and you can finally have the bot up and running. Use the following command to run.

```sh
<Your source directory>python main.py
```

## License

This project is licensed under the [BSD 3-Clause [License](license.md)](https://opensource.org/licenses/BSD-3-Clause)
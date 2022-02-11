## Auto clock in & clock out

This is a simple project to avoid forgetful person (like me) to forget about clock in.

> It's only for [NUEiP](https://cloud.nueip.com/).

## Requirements

[Python 3](https://www.python.org/)  
[Firefox](https://www.mozilla.org/zh-TW/firefox/new/)  
[Gecko driver](https://github.com/mozilla/geckodriver)

## How to use

Move to the clock in project and install the packages.

```shell
pip install -r requirements.txt
```

Create the config file and **fill in the setting**.  
you could use JANDI to notice the clock in status, referring to this [post](https://blog.jandi.com/tw/jandi-webhooks-incoming/) to create a JANDI bot.

```shell
cp config_example.ini config.ini
```

Edit the crontab setting.

```shell
crontab -e
```

Add this line in the crontab file.  
According your working hours, you could adjust the crontab setting.

```plaintext
31-40 9,18 * * 1-5 auto_clock_in_file_path >> /Users/username/clock_in.log
```

> If needed, you probably need to add environment variables to your crontab.

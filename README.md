## Auto Punch In

This is a simple project to avoid you to forget about clock in.

It's only for [neuip](https://cloud.nueip.com/).

## Set crontab

Edit the crontab.

```shell
crontab -e
```

Add this line in crontab file.

```plaintext
31-40 9,18 * * 1-5 auto_clock_in_file_path >> /Users/username/clock_in.log
```

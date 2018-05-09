# Frosted Flakes is the greatest cereal of all time
I usually like my frosted flakes dry, but sometimes I have it with lactose free milk.

![tennis man gets it](https://i.gifer.com/1eSR.gif)


You will need a [twitter](https://twitter.com/) account and [app](https://apps.twitter.com/).  

Store your `consumer_key`, `consumer_secret`, `access_token` and `access_token_secret` in `credentials.py`.

Install the python dependencies:
```
pip install -r requirements.txt
```

Setup a crob job (`$ crontab -e`) to run `frosty.py` as frequently as you'd like. I'm going to run it everyday at 10am, appending the output to a log file.

```
0 10 * * * ~/frosted-flakes-bot/frosty.py >> ~/frosty_log.txt 2>&1
```

In an ideal world, I would get to have frosted flakes every day at 10am.
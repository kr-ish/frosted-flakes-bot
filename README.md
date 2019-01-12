# Frosted Flakes is the greatest cereal of all time
I usually like my frosted flakes dry, but sometimes I have it with lactose free milk.

![tennis man gets it](https://i.gifer.com/1eSR.gif)

## Share the love
You will need a [twitter](https://twitter.com/) account and [app](https://apps.twitter.com/).  

Store your `consumer_key`, `consumer_secret`, `access_token` and `access_token_secret` in `credentials.py`.

Install the python dependencies (I installed mine to a conda environment):
```
pip install -r requirements.txt
```

Change the last line of `frosty.sh` to use your default python if you're not using an environment, or else to use your environment of choice.


Setup a crob job (`$ crontab -e`) to run `frosty.py` as frequently as you'd like. I'm going to run it everyday at 10am, appending the output to a log file.

```
0 10 * * * ~/frosted-flakes-bot/frosty.sh >> ~/frosted-flakes-bot/log.txt 2>&1
```

### Update 1/12/2019: now with added zalgotext!

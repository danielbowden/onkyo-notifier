# onkyo-notifier

Use a Raspberry Pi Zero to continually monitor and notify of the Zone 2 power status of my Onkyo Receiver by flashing LEDs. This helps alert the house that we have left the outdoor entertaining speakers on.

## Video
[![Raspberry Pi Onkyo Notifier](https://img.youtube.com/vi/jRVKCMuBqD0/0.jpg)](https://www.youtube.com/watch?v=jRVKCMuBqD0 "Raspberry Pi Onkyo Notifier")

## Install

* Requires installation on a Raspberry Pi due to blinkt!'s dependency on RPi.GPIO module.

```sh
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Run
```sh
$ python onkyo_zone2_status.py
```

## Scheduled task
Run regularly on the Raspberry Pi as a scheduled task in crontab
```sh
$ crontab -e # edit cron table

*/2 * * * * /home/pi/.pyenv/shims/python3 /home/pi/bin/blinkt-proj-1/onkyo_zone2_status.py > /home/pi/logs/onkyo_zone2_status.log 2>&1
```

## Author

Daniel Bowden

[github.com/danielbowden](https://github.com/danielbowden)

[twitter.com/danielgbowden](https://twitter.com/danielgbowden)

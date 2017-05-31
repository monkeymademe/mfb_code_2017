# mfb_code_2017
Code for the displays for the Raspberry Jam Berlin at Makerfaire Berlin 2017

## Setup launcher scripts

- Make launcher scripts
- 'mkdir logs' in /home/pi/
- run: sudo crontab -e
- insert this line: @reboot sh /home/pi/launcher.sh >/home/pi/logs/cronlog 2>&1

Done

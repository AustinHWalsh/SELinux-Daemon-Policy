## Setup

### Install the Daemon

```
# cp logdaemon.py /usr/local/bin
# cp logdaemon.service /usr/lib/systemd/system
```

### Starting the Daemon

Ensure `systemd` and `python3` are installed and up to date.

Enable and start the service
```
# systemctl enable logdaemon.service
# systemctl start logdaemon.service
```

To check the status of the service use
```
# systemctl status logdaemon
```


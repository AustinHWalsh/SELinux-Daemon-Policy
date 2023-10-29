## Setup

### Install the Daemon

```bash
# cp logdaemon.py /usr/local/bin
# cp logdaemon.service /usr/lib/systemd/system
```

### Starting the Daemon

Ensure `systemd` and `python3` are installed and up to date.

Enable and start the service
```bash
# systemctl enable logdaemon.service
# systemctl start logdaemon.service
```

To check the status of the service use
```bash
# systemctl status logdaemon
```


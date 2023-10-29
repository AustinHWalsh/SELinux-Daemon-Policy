## Setup

### Starting the Daemon

Ensure `systemd` and `python3` are installed and up to date.

1. Enable and start the service
```bash
sudo systemctl enable logdaemon.service
sudo systemctl start logdaemon.service
```

To check the status of the service use
```bash
sudo systemctl status logdaemon
```

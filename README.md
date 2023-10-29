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
$ systemctl status logdaemon
```
To see the SELinux label of the service use
```
$ ps -q $(systemctl show --property MainPID --value logdaemon) -o pid,label,comm
```

The Daemon will have an unconfined type \(`unconfined_service_t`\):
```bash
    PID LABEL                                     COMMAND
 136362 system_u:system_r:unconfined_service_t:s0 python3
```

## Load the SELinux Policy
TODO

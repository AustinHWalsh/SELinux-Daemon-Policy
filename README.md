## Setup

### Install the Daemon

```
sudo cp logdaemon.py /usr/local/bin
sudo cp logdaemon.service /usr/lib/systemd/system
```

### Starting the Daemon

Ensure `systemd` and `python3` are installed and up to date.

Enable and start the service
```
sudo systemctl enable logdaemon.service
sudo systemctl start logdaemon.service
```

To check the status of the service use
```
systemctl status logdaemon
```
To see the SELinux label of the service use
```
ps -q $(systemctl show --property MainPID --value logdaemon) -o pid,label,comm
```

The Daemon will have an unconfined type \(`unconfined_service_t`\):
```bash
    PID LABEL                                     COMMAND
 136362 system_u:system_r:unconfined_service_t:s0 python3
```
and log messages will be written to `/var/log/messages`

## Installing the Logdaemon SELinux Policy

### Pre-requisites
```
sudo dnf install selinux-policy-devel
```

### Create the Policy
```
cd dist
make -f /usr/share/selinux/devel/Makefile logdaemon.pp
```

### Load the policy
```
sudo semodule -i logdaemon.pp
```

### Relabel the daemon
```
sudo restorecon -v /usr/local/bin/logdaemon.py /usr/lib/systemd/system
```

## Closing

Restart the service
```
sudo systemctl start logdaemon
```
The context will now be confined:


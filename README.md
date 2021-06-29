# healthcheck

### Installation
```
$ # Clone healthcheck repository
$ cd ~
$ git clone https://github.com/wingkeet/healthcheck.git
$ cd healthcheck

$ # Create Python virtual environment and install libraries
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install requests
$ deactivate

$ # Install daemon for systemd
$ sudo cp healthcheck.service /etc/systemd/system
$ sudo systemctl daemon-reload
$ sudo systemctl start healthcheck
$ journalctl -f -u healthcheck
$ sudo systemctl stop healthcheck
```

![systemctl-status](screenshot.png)

### How it works
The information presented here was extracted from [Linux System
Programming Techniques]
(https://www.packtpub.com/product/linux-system-programming-techniques/9781789951288)
by Jack-Benny Persson and published by Packt.

We create a **new-style daemon** for systemd. The old **forking** type is
referred to as a **SysV-style daemon**.

Daemons that are handled by systemd don't need to fork or close their
file descriptors. Instead, it's advised to use standard output and standard
error to write the daemon's logs to the systemd journal.

We need to flush stdout. Normally, streams are line-buffered, meaning they
get flushed on each new line. But when stdout is redirected to something
else, like with systemd, it's instead fully buffered.

### References
- [Understanding Systemd Units and Unit Files](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files)
- [How to create systemd service unit in Linux](https://linuxconfig.org/how-to-create-systemd-service-unit-in-linux)
- [systemd service unit configuration man page](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
- [systemd/Journal](https://wiki.archlinux.org/title/Systemd/Journal)
- [Logging in New-Style Daemons with systemd](https://www.loggly.com/blog/logging-in-new-style-daemons-with-systemd/)
- [Python Logging Basics](https://www.loggly.com/ultimate-guide/python-logging-basics/)
- [New-style daemons in Python](https://www.loggly.com/blog/new-style-daemons-python/)

#!/bin/sh

# first process
python /app/app.py &

# Minimal config for the SSH server:
sed -i '/AllowTcpForwarding/d' /etc/ssh/sshd_config
sed -i '/PermitOpen/d' /etc/ssh/sshd_config
/usr/sbin/sshd -e -D &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
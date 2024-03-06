#!/bin/sh

# first process
python app.py &

# second process
/usr/sbin/sshd &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
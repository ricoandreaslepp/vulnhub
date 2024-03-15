# Use a lightweight Linux distribution as base image
FROM python:3-alpine

# Install SSH server and required packages
RUN apk update && \
    apk add --no-cache supervisor openssh-server && \
    echo 'root:'$(xxd -l 10 -p /dev/urandom) | chpasswd && \
    sed -i 's/#MaxAuthTries 6/MaxAuthTries 10/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i 's/#PubkeyAuthentication no/PubkeyAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i '/AllowTcpForwarding/d' /etc/ssh/sshd_config && \
    sed -i '/PermitOpen/d' /etc/ssh/sshd_config && \
    ssh-keygen -A

# sshd needs this directory to work
RUN mkdir /var/run/sshd/

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# install python deps
RUN pip install --no-cache-dir -r requirements.txt

# move files
COPY flag.txt /root/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# passphrase is 
COPY --chmod=644 id_rsa /root/.ssh/id_rsa
COPY --chmod=600 id_rsa.pub /root/.ssh/authorized_keys

# Expose the port that the application runs on
EXPOSE 22 8080

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

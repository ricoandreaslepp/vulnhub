# Use a lightweight Linux distribution as base image
FROM python:3-alpine

# Install SSH server and required packages
RUN apk update && \
    apk add --no-cache supervisor openssh-server && \
    echo 'root:greenday' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i '/AllowTcpForwarding/d' /etc/ssh/sshd_config && \
    sed -i '/PermitOpen/d' /etc/ssh/sshd_config && \
    ssh-keygen -A

RUN mkdir /var/run/sshd/

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# install python deps
RUN pip install --no-cache-dir -r requirements.txt

# move the relevant files
COPY flag.txt /root/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the ports that the applications run on
EXPOSE 22 80

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

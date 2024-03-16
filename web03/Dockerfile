# Use a lightweight Linux distribution as base image
FROM python:3-alpine

# Install SSH server and required packages
RUN apk update && \
    apk add --no-cache supervisor openssh-server && \
    echo 'root:'$(xxd -l 10 -p /dev/urandom) | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    ssh-keygen -A

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# install python deps
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /opt/images
COPY ./images /opt/images

# move files
COPY flag.txt /root/
# Copy supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the port that the application runs on
EXPOSE 22 443

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
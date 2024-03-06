# Use a lightweight Linux distribution as base image
FROM python:3-alpine

# Install SSH server and required packages
RUN apk update && \
    apk add --no-cache openssh-server && \
    echo 'root:Passw0rd1!' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    ssh-keygen -A

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# install python deps
RUN pip install --no-cache-dir -r requirements.txt

# move flag from current dir to root's 
COPY flag.txt /root/

# Expose the port that the application runs on
EXPOSE 22 80

# Execute wrapper script
CMD /app/entrypoint.sh

# Use a lightweight Linux distribution as base image
FROM python:3-alpine

# Install SSH server
RUN apk update && apk add openssh-server

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# install python deps
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser kasutaja
# move flag from current dir to kasutaja's home
RUN mv flag.txt /home/kasutaja
RUN echo 'kasutaja:Passw0rd1!' | chpasswd

# Expose the port that the application runs on
EXPOSE 22 80

RUN chmod 755 /app/entrypoint.sh

# Execute wrapper script
CMD /app/entrypoint.sh

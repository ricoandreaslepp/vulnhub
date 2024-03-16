ARG BASE_IMG=alpine:3.19

FROM $BASE_IMG AS pidproxy

RUN apk update \
 && apk add --no-cache alpine-sdk \
 && git clone https://github.com/ZentriaMC/pidproxy.git \
 && cd pidproxy \
 && git checkout 193e5080e3e9b733a59e25d8f7ec84aee374b9bb \
 && sed -i 's/-mtune=generic/-mtune=native/g' Makefile \
 && make \
 && mv pidproxy /usr/bin/pidproxy \
 && cd .. \
 && rm -rf pidproxy \
 && apk del alpine-sdk


FROM $BASE_IMG

COPY --from=pidproxy /usr/bin/pidproxy /usr/bin/pidproxy
RUN apk --no-cache add vsftpd tini supervisor openssh-server && \
    sed -i 's/#MaxAuthTries 6/MaxAuthTries 10/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i 's/#PubkeyAuthentication no/PubkeyAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i '/AllowTcpForwarding/d' /etc/ssh/sshd_config && \
    sed -i '/PermitOpen/d' /etc/ssh/sshd_config && \
    ssh-keygen -A

COPY start_vsftpd.sh /bin/start_vsftpd.sh
COPY vsftpd.conf /etc/vsftpd/vsftpd.conf

# Copy supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 21 21000-21010
VOLUME /ftp/ftp

#ENTRYPOINT ["/sbin/tini", "--", "/bin/start_vsftpd.sh"]
# Run supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

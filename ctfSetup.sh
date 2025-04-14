#!/bin/bash

nmcli con del ens8-static
nmcli con add con-name ens8-static ip4 10.0.0.2/24 gw4 10.0.0.1 ifname ens8 type ethernet ipv4.dns 8.8.8.8,8.8.4.4 ipv4.method manual autoconnect yes
hostnamectl set-hostname workstation.ctf.local
echo -e "127.0.0.1\t\tlocalhost localhost.localdomain localhost4 localhost4.localdomain4" > /etc/hosts
echo -e "::1\t\t\tlocalhost localhost.localdomain localhost6 localhost6.localdomain6" >> /etc/hosts
echo -e "10.0.0.2\t\thack.me" >> /etc/hosts
echo -e "10.0.0.2\t\tworkstation.ctf.local" >> /etc/hosts
dnf -y install httpd
wget https://raw.githubusercontent.com/brianf21/CTF/refs/heads/main/index.html -O /var/www/html/index.html
systemctl enable --now httpd

# Binary Blob
# Saved file as /tmp/cute_kitty.png bcCTF{y0u_f0und_th3_fl4g}
# strings /tmp/cute_kitty.png
wget https://raw.githubusercontent.com/brianf21/CTF/refs/heads/main/create_binary.py -O /tmp/create_binary.py
chmod +x /tmp/create_binary.py
python3 /tmp/create_binary.py
rm -f /tmp/create_binary.py
wget https://raw.githubusercontent.com/brianf21/CTF/refs/heads/main/binary-ascii -O /tmp/secret

# Hidden in plain site - font is the same color as background
# Tag in about.html bcCTF{pr1ntf_1s_d4ng3r0us}
wget https://raw.githubusercontent.com/brianf21/CTF/refs/heads/main/about.html -O /var/www/html/about.html

wget https://raw.githubusercontent.com/brianf21/CTF/refs/heads/main/binary-ascii -O /var/www/html/resources.html

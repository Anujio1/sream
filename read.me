# Telegram Video Streamer Deployment Guide

## Prerequisites
- Hostinger VPS (Ubuntu 20.04/22.04)
- Domain name pointed to your VPS IP
- SSH access to the server

## 1. Upload Project
Unzip the project to `/opt/tg_streamer`:
```bash
sudo mkdir -p /opt/tg_streamer
sudo chown $(whoami):$(whoami) /opt/tg_streamer
unzip tg_streamer.zip -d /opt/tg_streamer
```

## 2. Create Environment File
Inside `/opt/tg_streamer`, create a `.env` file:
```ini
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

## 3. Install Dependencies
```bash
cd /opt/tg_streamer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 4. Configure Nginx
```bash
sudo cp nginx/tg-streamer.conf /etc/nginx/sites-available/tg_streamer
sudo ln -s /etc/nginx/sites-available/tg_streamer /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 5. Setup Systemd Service
```bash
sudo cp systemd/tg-streamer.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start tg-streamer
sudo systemctl enable tg-streamer
```

## 6. Firewall & SSL
```bash
sudo ufw allow 80
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com
```

## 7. Usage
- Upload a video to your Telegram bot.
- Get the `file_id` from the bot's response.
- Navigate to `https://yourdomain.com/player?file_id=<file_id>`.

Enjoy smooth, buffer-free streaming!

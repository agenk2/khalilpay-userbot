import os
import asyncio
from flask import Flask, request, jsonify
from telethon import TelegramClient

# Ganti angka & teks di bawah sesuai kunci dari my.telegram.org Anda
API_ID = 39948698  # Masukkan API_ID Anda
API_HASH = 'fd34a411b67ab839d2f551e1b88af8eb'  # Masukkan API_HASH Anda

app = Flask(__name__)

# Fungsi penanganan pengiriman pesan via Telethon
async def send_telegram_command(command):
    async with TelegramClient('khalilpay_session', API_ID, API_HASH) as client:
        await client.send_message('centermarlindo_bot', command)

@app.route('/')
def home():
    return jsonify({"status": "running", "message": "Userbot KhalilPay Server Active"})

@app.route('/trx', methods=['POST'])
def execute_transaction():
    data = request.json or {}
    command = data.get("command")

    if not command:
        return jsonify({"status": "failed", "message": "Command required"}), 400

    try:
        # Menjalankan loop asyncio baru setiap kali ada request transaksi
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_telegram_command(command))
        loop.close()
        
        return jsonify({"status": "success", "message": f"Perintah '{command}' terkirim ke Marlindo!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

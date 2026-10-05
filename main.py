import os
import asyncio
from flask import Flask, request, jsonify
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = 39948698  # Masukkan API_ID Anda (angka)
API_HASH = 'fd34a411b67ab839d2f551e1b88af8eb'  # Masukkan API_HASH Anda

# PASTE STRING SESSION PANJANG DI DALAM TANDA PETIK DI BAWAH INI:
SESSION_STRING = '1BVtsOLwBu0wpbS1PLWw6OK9FRmS60FSNAarRr4jGDioDOEYhrsd5txkTt8CrI_2iJTZm3QASwu1DdMQZDqz2gI0gpozpBeOLh5FsuYufMJ02wYpdmfJmtjTJxOCPLyFZrdORRVwUbcWnsSTqoZnZsVgQI8hDVGARojvcIKByNL5bnPyE6W-7gCbQ3QsTunfg0G6lqHJ5x-Qu-VCKkvHREal_DeRfTOffOrTu6E25WNInQV8Piud3OJrM3vRp0UeflT7KW-NGRB4In6vTK3aEhFMXx1dDeyG-YIRti8uZs2FODQh6X6-TdHFKpPCTgQPkH4jcSSRGWub0KAluayJ5LrkY2LR_Rwk=' 

app = Flask(__name__)

async def send_telegram_command(command):
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
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
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_telegram_command(command))
        loop.close()
        
        return jsonify({"status": "success", "message": f"Perintah '{command}' terkirim ke Marlindo!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

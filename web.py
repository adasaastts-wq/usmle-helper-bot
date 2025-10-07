from flask import Flask
import threading
import bot

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ USMLE Helper Bot is running on Render!"

def start_bot():
    bot.run_bot()

if __name__ == "__main__":
    threading.Thread(target=start_bot, daemon=True).start()
    app.run(host='0.0.0.0', port=10000)
    

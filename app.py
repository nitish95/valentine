from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('valentine.html')

if __name__ == '__main__':
    print("\n" + "="*50)
    print("💕 Valentine's Day Website Server 💕")
    print("="*50)
    print("\n🌹 Server starting...")
    print("📱 Open your browser and go to: http://localhost:5001")
    print("💝 Have fun with your Valentine!\n")
    print("Press CTRL+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5001)

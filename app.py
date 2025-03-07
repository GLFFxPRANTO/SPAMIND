from flask import Flask, request
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/spamkb/<uid>', methods=['GET'])
def get_spamkb_data(uid):
    url = f"https://freefire-virusteam.vercel.app/ind/spamkb?key=7day@apivirusteam&uid={uid}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if "UID Validated - API connected" in data:
            user_info = data["UID Validated - API connected"]

            return f"""API RESULT - :
UID : {user_info["UID"]}
NAME : {user_info["Name"]}
LEVEL : {user_info["Level"]}
REGION : {user_info["Region"]}

ADMIN PRANTO
TELEGRAM @GLFFLIKE""", 200, {'Content-Type': 'text/plain; charset=utf-8'}

        else:
            return "Error: Required data not found!", 404, {'Content-Type': 'text/plain; charset=utf-8'}
    
    except Exception as e:
        return f"Error: Server Error\nMessage: {str(e)}", 500, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("SpamKB API is running 🔥")
    serve(app, host='0.0.0.0', port=8080)  # For deployment

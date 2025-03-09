from flask import Flask, jsonify
import requests
from waitress import serve

app = Flask(__name__)

def fetch_api_data(url):
    """Fetch data from the given API URL and return JSON response."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP failures
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to connect to API: {str(e)}"}

@app.route('/Pranto7days/likes/<uid>', methods=['GET'])
def get_like_info(uid):
    url = f"https://fflrepo-chx.vercel.app/like?uid={uid}&server_name=ind"
    data = fetch_api_data(url)

    if "error" in data:
        return jsonify({"error": data["error"], "POWERED": "https://t.me/GLFFLIKE"}), 500

    if all(key in data for key in ["LikesGivenByAPI", "LikesafterCommand", "LikesbeforeCommand", "PlayerNickname", "UID"]):
        return jsonify({
            "PLAYER UID": data["UID"],
            "PLAYER NICKNAME": data["PlayerNickname"],
            "LIKES GIVEN API": data["LikesGivenByAPI"],
            "LIKES AFTER COMMAND": data["LikesafterCommand"],
            "LIKES BEFORE COMMAND": data["LikesbeforeCommand"],
            "POWERED": "https://t.me/GLFFLIKE"
        }), 200

    return jsonify({
        "message": f"Account with UID {uid} has reached the maximum likes for today. Please try again tomorrow.",
        "POWERED": "https://t.me/GLFFLIKE"
    }), 404

@app.route('/Pranto7days/newlikes/<uid>', methods=['GET'])
def get_new_like_info(uid):
    url = f"https://2ndtry-azure.vercel.app/like?server_name=bd&api_key=Try&uid={uid}"
    data = fetch_api_data(url)

    if "error" in data:
        return jsonify({"error": data["error"], "POWERED": "https://t.me/GLFFLIKE"}), 500

    if all(key in data for key in ["LikesGivenByAPI", "LikesafterCommand", "LikesbeforeCommand", "PlayerNickname", "UID"]):
        return jsonify({
            "PLAYER UID": data["UID"],
            "PLAYER NICKNAME": data["PlayerNickname"],
            "LIKES GIVEN BY API": data["LikesGivenByAPI"],
            "LIKES BEFORE COMMAND": data["LikesbeforeCommand"],
            "LIKES AFTER COMMAND": data["LikesafterCommand"],
            "POWERED": "https://t.me/GLFFLIKE"
        }), 200

    return jsonify({
        "message": f"Account with UID {uid} has reached the maximum likes for today. Please try again tomorrow.",
        "POWERED": "https://t.me/GLFFLIKE"
    }), 404

if __name__ == "__main__":
    print("Like Info API is running 🔥")
    serve(app, host='0.0.0.0', port=8080)  # Use this for deployment

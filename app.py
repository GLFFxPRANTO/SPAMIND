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

@app.route('/likes/key=pranto/<uid>', methods=['GET'])
def get_like_info(uid):
    url = f"https://fflrepo-chx.vercel.app/like?uid={uid}&server_name=ind&api_key=chxfree"
    data = fetch_api_data(url)

    if "error" in data:
        return jsonify({"error": data["error"], "OWNER": "@ASIBHASANPRANTOO"}), 500

    if all(key in data for key in ["LikesGivenByAPI", "LikesafterCommand", "LikesbeforeCommand", "PlayerNickname", "UID"]):
        return jsonify({
            "Uid": data["UID"],
            "Player nickname": data["PlayerNickname"],
            "Likes after command": data["LikesafterCommand"],
            "Likes before command": data["LikesbeforeCommand"],
            "Likes given by API": data["LikesGivenByAPI"],
            "OWNER": "@Asibhasanprantoo"
        }), 200

    return jsonify({
        "message": f"Account with UID {uid} has reached the maximum likes for today. Please try again tomorrow.",
        "OWNER": "@ASIBHASANPRANTOO"
    }), 404

if __name__ == "__main__":
    print("Like Info API is running 🔥")
    serve(app, host='0.0.0.0', port=8080)  # Deployment

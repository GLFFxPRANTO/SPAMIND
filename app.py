from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Route to fetch data from your API
@app.route('/fetch', methods=['GET'])
def fetch_api():
    uid = request.args.get('uid')
    password = request.args.get('password')

    if not uid or not password:
        return jsonify({"error": "Missing uid or password parameters"}), 400

    api_url = f"https://community-ffbd.vercel.app/jwt?uid={uid}&password={password}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()  # Convert response to JSON

        return jsonify({"status": "success", "data": data})  # Return formatted JSON

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

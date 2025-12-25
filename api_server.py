from flask import Flask, request, jsonify
from flask_cors import CORS  # optional but helpful
from bot.coc_api import CoCAPI

app = Flask(__name__)
CORS(app)  # allow calls from your web page (localhost)

coc_api = CoCAPI()


@app.get("/player")
def get_player():
    tag = request.args.get("tag", "").strip()
    if not tag:
        return jsonify({"success": False, "error": "Missing tag parameter"}), 400

    result = coc_api.get_player_info(tag)

    if not result["success"]:
        # Pass error message and status 400
        return jsonify({"success": False, "error": result["error"]}), 400

    # Return only the fields you need for the website
    data = result["data"]

    response = {
        "success": True,
        "player": {
            "tag": data.get("tag"),
            "name": data.get("name"),
            "townHallLevel": data.get("townHallLevel"),
            "expLevel": data.get("expLevel"),
            "trophies": data.get("trophies"),
            "bestTrophies": data.get("bestTrophies"),
            "clan": {
                "name": data.get("clan", {}).get("name"),
                "tag": data.get("clan", {}).get("tag"),
                "level": data.get("clan", {}).get("clanLevel"),
            },
        },
    }

    return jsonify(response), 200


@app.get("/clan")
def get_clan():
    tag = request.args.get("tag", "").strip()
    if not tag:
        return jsonify({"success": False, "error": "Missing tag parameter"}), 400

    result = coc_api.get_clan_info(tag)

    if not result["success"]:
        return jsonify({"success": False, "error": result["error"]}), 400

    data = result["data"]

    response = {
        "success": True,
        "clan": {
            "tag": data.get("tag"),
            "name": data.get("name"),
            "clanLevel": data.get("clanLevel"),
            "clanPoints": data.get("clanPoints"),
            "members": data.get("members"),
            "description": data.get("description"),
        },
    }

    return jsonify(response), 200


if __name__ == "__main__":
    # Run on http://127.0.0.1:8000
    app.run(host="127.0.0.1", port=8000, debug=True)

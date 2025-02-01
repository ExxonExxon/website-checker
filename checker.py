from flask import Flask, request, jsonify
import threading
import time


app = Flask(__name__)

# List of websites
websites: list[str] = [
    "https://google.com",
]

# Lock to ensure thread safety
websites_lock = threading.Lock()

# Gets all websites
@app.route("/get_websites")
def get_websites():
    data = {"websites": websites}
    return jsonify(data)

# Delete a website based on the number in the list
@app.route("/delete_website")
def delete_website()


# Adds a website to the list
@app.route("/add_website", methods=["POST"])
def add_website():
    global websites
    
    data = request.json
    if "value" in data:
        # Lock the list to ensure thread-safe operation
        with websites_lock:
            websites.append(data["value"])  
        return {"message": "Website added successfully", "websites": websites}, 200
    return {"error": "No value provided"}, 400

def check_websites():
    """
    Checks the websites every 10 seconds in the website list.
    """
    while True:
        # Lock the list to ensure thread-safe reading
        with websites_lock:
            for website in websites:
                print(f"Checking website: {website}")
        
        time.sleep(2)

if __name__ == '__main__':
    threading.Thread(target=check_websites, daemon=True).start()
    app.run(port=5000, debug=False)

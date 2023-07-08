from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    request_data = request.get_json()
    
    intent = request_data['queryResult']['intent']['displayName']
    parameters = request_data['queryResult']['parameters']
    
    if intent == 'start':
        response = "do you have vomitting ?  "
    else:
        response = "do you have fatigue ?."
    
    webhook_response = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [response]
                }
            }
        ]
    }
    
    return jsonify(webhook_response)

if __name__ == '__main__':
    app.run(debug=True)

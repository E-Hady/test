from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    request_data = request.get_json()
    intent = request_data['queryResult']['intent']['displayName']
    parameters = request_data['queryResult']['parameters']

    # Perform your logic based on the intent and parameters
    if intent == 'start':
        # Process the intent and parameters
        response = "Do you have vomitting ?"

    else:
        response = "Sorry, I don't understand."

    # Create the webhook response
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

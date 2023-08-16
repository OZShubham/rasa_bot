from rasa import Rasa
from sanic import Sanic, response

app = Sanic(__name__)
rasa = Rasa()

@app.route("/webhooks/rest/webhook", methods=["POST"])
async def receive_message(request):
    data = request.json
    response_data = await rasa.handle_message(data)
    return response.json(response_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)


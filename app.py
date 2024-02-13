import wikipedia
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wiki/<search_term>', methods=['GET'])
def get_wikipedia_info(search_term):
    #language = request.headers.get(Accept-Language)
    language = request.args.get('Accept-Language')
    
    if language:
        wikipedia.set_lang(language)
    else:
        wikipedia.set_lang("cs")

    try:
        wikipedia_response = wikipedia.summary(search_term, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        return e.options, 303
    except wikipedia.exceptions.PageError as e:
        return "No content found", 404

    return wikipedia_response, 200


@app.errorhandler(requests.exceptions.ConnectionError)
def handle_connection_error(e):
    return jsonify({"error": "Failed to connect to the Wikipedia server"}),  500



if __name__ == '__main__':
    app.run(debug=True)
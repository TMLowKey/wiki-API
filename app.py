import wikipedia
import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wiki/<search_term>', methods=['GET'])
def get_wikipedia_info(search_term):
    # Setting up language of wikipedia quarry, default value "cs"
    language = request.args.get('Accept-Language')
    if language:
        wikipedia.set_lang(language)
    else:
        wikipedia.set_lang("cs")

    try:
        # Check if the search_term have wiki page byitself or it just appear in artle, 
        #   also check if the list is not empty otherwise method .summary return error
        if (len(wikipedia.search(search_term)) > 0) and (search_term.lower() != wikipedia.search(search_term)[0].lower()):
            wikipedia_response = {'message': "Search term is appeared in other articles", 'data':wikipedia.search(search_term), 'Code': 303}
        else:
            wikipedia_response = {'message': "Search term found", 'data':wikipedia.summary(search_term, auto_suggest = False), 'Code':200}
    except wikipedia.exceptions.DisambiguationError as e:
        # Appear when wiki API dont find term but there is suggested terms
        return json.dumps({'message': "Did you meant", 'data': e.options, 'Code': 404}, ensure_ascii=False)
    except wikipedia.exceptions.PageError as e:
        # Appear when there is no wikipedia suggested article
        return {'message': "Search term not found", 'data': None, 'Code': 404}
    
    # ensure_ascii is turn off because displaying czech unicodes
    return json.dumps(wikipedia_response, ensure_ascii=False),  200


@app.errorhandler(requests.exceptions.ConnectionError)
def handle_connection_error(e):
    return jsonify({"error": "Failed to connect to the Wikipedia server, check if you have right language code 'en' for english 'cs' for czech."}),  500


if __name__ == '__main__':
    app.run(debug=True)
import json
import os
import pprint
import time
import multiprocessing as mp
from flask import Flask, request, make_response
app = Flask(__name__)


@app.route('/', methods=['POST'])
def MainProcess():
    get_intexd_dialgflow = request.get_json(silent=True, force=True)
    # pprint.pprint(get_intexd_dialgflow)
    ans_from_user = get_intexd_dialgflow['originalDetectIntentRequest']['payload']['data']['message']['text']
    pprint.pprint(get_intexd_dialgflow)
    print(ans_from_user)
    return send_user(ans_from_user)


def require_ans(text):
    return json.dumps({"fulfillmentText": 'Nothing'}, indent=4)

def send_user(ans_from_user):
    res = make_response(require_ans(ans_from_user))
    res.headers['Content-Type'] = 'application/json'
    return res


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f'Starting app on port {port}')
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)

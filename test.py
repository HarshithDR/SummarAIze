from flask import Flask,request
from user_interest.userinterest import *
from user_feed.userfeed import *
from flask_cors import CORS
import flow

flow.load_all_the_models()

app = Flask(__name__)
CORS(app)
@app.route('/interests', methods=['POST','GET'])
def userinterest():
    data = request.json
    user_email = data.get('useremail')
    user_interest = data.get('user_interest')
    report = set_user_interests(user_email,user_interest)
    if report['success']:
        flow.start()
    print(2342342143)
    return report

@app.route('/newsfeed', methods=['GET'])
def newsfeed():
    print(request.args)
    return accessuserfeed(request.args.get('user_id'))

if __name__ == '__main__':
    # Run the app on http://localhost:5000/ by default
    app.run(debug=True,port=5001)
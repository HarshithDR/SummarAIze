from flask import Flask,request
from user_interest.userinterest import *

app = Flask(__name__)

@app.route('/interests', methods=['POST','GET'])
def userinterest():
    print(request.args)
    return set_user_interests(request.args.get('useremail'),request.args.get('user_interest'))

if __name__ == '__main__':
    # Run the app on http://localhost:5000/ by default
    app.run(debug=True,port=5001)
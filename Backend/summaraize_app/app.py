from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask,request,jsonify
from user_interest.userinterest import *
from user_feed.userfeed import *
#from chatbot.chatbot import *
from flask_cors import CORS
import flow

app = Flask(__name__)
CORS(app)

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.start()

def scheduled_task():
    flow.start()

# Schedule the task to run every hour
scheduler.add_job(scheduled_task, 'interval', hours=2)

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
    print('Im here',request.args)
    return accessuserfeed(request.args.get('user_id'))

# @app.route('/chat_query', methods=['POST'])
# def chat_query():
#     data = request.json
#     user_question=data.get('question')
#     if user_question:

#         bot_response=run_chatbot(user_question)
#         return jsonify({'Response':bot_response})
#     else:
#         return jsonify({'Error':'No Question !!'})

if __name__ == '__main__':
    # Run the app on http://localhost:5000/ by default
    app.run(debug=True,port=5001)
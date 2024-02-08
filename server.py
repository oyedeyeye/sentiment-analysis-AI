''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, requests

# Import the sentiment_analyzer function from the package created: TODO
from SentimentAnalysis.sentiment_analysis import sent_analyzer

#Initiate the flask app : TODO
app = Flask(__name__)


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO
    text_to_analyze = request.args.get('textToAnalyze')
    # Run Sentiment analysis of the input text
    result = sentiment_analyzer(text_to_analyze)

    return f"The given text has been identified as {result['label']} with a score of {result['score']}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)

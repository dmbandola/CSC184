from flask import Flask
from crawler import *
app = Flask (__name__)

CRAWLER = Singleton()

@app.route('/')
def hello_world():
    url = request.args.get('url')
    threading.Thread = CRAWLER.download_images('threading.Thread')
    return CRAWLER.run()
    
if __name__ == '__main__':
    app.run(debug=True)

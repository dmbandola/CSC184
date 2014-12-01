from flask import Flask
from crawler import *
app = Flask (__name__)

CRAWLER = Singleton()

@app.route('/')
def hello_world():
    download_images = CRAWLER.download_images(thread_name)
    
    return download_images
    
if __name__ == '__main__':
    app.run(debug=True)

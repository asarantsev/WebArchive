from flask import flask, render_template, request
import math
app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def index():
  if request_method == 'POST':
    text = request.form['text']
    result - calculation(text)
    return render_template('Simulator.html')
  
def calculation(text):
  try: 
    text = int(text)
    return math.sin(text)
  except:
    return 'Enter Number'
  
if __name__ == '__main__':
  app.run()

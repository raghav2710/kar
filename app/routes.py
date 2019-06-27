from flask import render_template
from app import app
@app.route('/')
def name():
   return '''
    <html>
     <body>
      <h2>Click here</h2><br>
      <a href= 'http://127.0.0.1:5000/index'><i><marquee behaviour ="rotate" direction = "up"><button>index</button></marquee></i></a>
      
 
      </body>
    </html> 

    '''

    
@app.route('/index')
def index():
   user = {'username': 'RAGHAV'}
   posts = [ {'author': {'username': 'Rushant'}, 'body': 'Beautiful day in patiala'}, 
             {'author': {'username': 'Rahul'}, 'body': 'The Kabir singh movie was so cool'}]
   return render_template('index.html', title = 'Home', user = user, posts = posts)

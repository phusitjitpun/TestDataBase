from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Date 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:RBBehe54965@node1441-phusit.app.ruk-com.cloud:11030/test081'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

class Comments(db.Model):
	id = Column(Integer, primary_key=True)
	name = Column(String)
	comment = Column(String)

@app.route('/')
def index():
	result = Comments.query.all()

	return render_template('index.html', result=result)

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']
	signature = Comments(name=name, comment=comment)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('index'))

@app.route('/home', methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
	return render_template('example.html', links=links)

if __name__ == '__main__':
	app.run(debug=True)
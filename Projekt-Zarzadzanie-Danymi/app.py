from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/movies.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Nazwa użytkownika już istnieje', 'danger')
            return redirect(url_for('register'))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Rejestracja zakończona sukcesem! Możesz się teraz zalogować.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash('Zalogowano pomyślnie!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Niepoprawne dane logowania.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Wylogowano pomyślnie!', 'success')
    return redirect(url_for('home'))


@app.route('/')
def home():
    genre = request.args.get('genre')
    if genre:
        movies = Movie.query.filter_by(genre=genre).all()
    else:
        movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        movies = Movie.query.filter(Movie.title.like(f'%{query}%')).all()
    else:
        movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    reviews = Review.query.filter_by(movie_id=movie_id).all()
    return render_template('movie_detail.html', movie=movie, reviews=reviews)

@app.route('/add_review/<int:movie_id>', methods=['POST'])
@login_required
def add_review(movie_id):
    content = request.form['content']
    rating = int(request.form['rating'])
    if rating < 1 or rating > 10:
        flash('Ocena musi być w skali od 1 do 10', 'danger')
        return redirect(url_for('movie_detail', movie_id=movie_id))
    
    new_review = Review(movie_id=movie_id, user_id=current_user.id, content=content, rating=rating)
    db.session.add(new_review)
    db.session.commit()
    return redirect(url_for('movie_detail', movie_id=movie_id))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

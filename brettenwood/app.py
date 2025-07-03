from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/images/portfolio'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['REVIEWS_FILE'] = 'reviews.json'

# Sample data for water backup systems
WATER_SYSTEMS = [
    {
        'id': 1,
        'name': '1000L System',
        'capacity': '1000L',
        'pump': 'JP1000 Pressure Pump',
        'includes': ['1000L JoJo Tank', 'JP1000 Pump', 'Installation kit', 'Basic plumbing'],
        'price': 'R8,499'
    },
    {
        'id': 2,
        'name': '2500L System',
        'capacity': '2500L',
        'pump': 'JP2500 Pressure Pump',
        'includes': ['2500L JoJo Tank', 'JP2500 Pump', 'Installation kit', 'Standard plumbing', 'Basic filtration'],
        'price': 'R12,999'
    },
    {
        'id': 3,
        'name': '5000L System',
        'capacity': '5000L',
        'pump': 'JP5000 Pressure Pump',
        'includes': ['5000L JoJo Tank', 'JP5000 Pump', 'Installation kit', 'Full plumbing', 'Advanced filtration', 'Overflow protection'],
        'price': 'R18,999'
    }
]

# Load reviews from JSON file
def load_reviews():
    try:
        with open(app.config['REVIEWS_FILE'], 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save reviews to JSON file
def save_reviews(reviews):
    with open(app.config['REVIEWS_FILE'], 'w') as f:
        json.dump(reviews, f)

# Routes
@app.route('/')
def home():
    reviews = load_reviews()  # Make sure this function exists
    return render_template('index.html', reviews=reviews)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    portfolio_images = [
        {
            "filename": "job1.jpg",
            "location": "Amanzimtoti.",
            "description": "20� Big Blue 3 Stage Filtration with 55w UV setup"
        },
        {
            "filename": "job2.jpg",
            "location": "Pietermaritzburg",
            "description": "5250lt JoJo tank paired with a 1.1kw ZIL VSD, set up on a buffer connection to ensure a constant flow of municipal water into the tank, which is then fed into the home via a 3 Stage Filter with UV"
        },
        {
            "filename": "job3.jpg",
            "location": "Tongaat",
            "description": "5000lt LIN Tank powered by a 0.75kw Centrifugal Pump secured with our custom fabricated Anti-Theft Cage"
        },
        
        {
            "filename": "job4.jpg",
            "location": "Pietermaritzburg.",
            "description": "5050lt jojo Tank powered by a 1.1kw Multistage Pump with 3 step filtration"
        }

        # Add more images as needed
    ]
    return render_template('portfolio.html', images=portfolio_images)


@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    reviews_list = load_reviews()
    
    if request.method == 'POST':
        name = request.form.get('name')
        rating = int(request.form.get('rating'))
        comment = request.form.get('comment')
        
        if name and rating and comment:
            new_review = {
                'name': name,
                'rating': rating,
                'comment': comment
            }
            reviews_list.append(new_review)
            save_reviews(reviews_list)
            return redirect(url_for('reviews'))
    
    return render_template('reviews.html', reviews=reviews_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)


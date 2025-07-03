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

@app.route('/systems')
def systems():
    systems_data = [
        {
            'id': 1,
            'brand': 'JoJo',
            'name': '1000L System',
            'capacity': '1000L',
            'pump': '0.35kW Centrifugal',
            'filtration': None,
            'price': 'R7,499',
            'image': 'jojo-1000.png'
        },
        {
            'id': 2,
            'brand': 'Eco',
            'name': '1000L System',
            'capacity': '1000L',
            'pump': '0.35kW Centrifugal',
            'filtration': '3-Stage',
            'price': 'R8,999',
            'image': 'eco-1000.jpg'
        },
        {
            'id': 3,
            'brand': 'JoJo',
            'name': '2500L System',
            'capacity': '2500L',
            'pump': '0.75kW Multi-Stage',
            'filtration': None,
            'price': 'R12,999',
            'image': 'jojo-2500.webp'
        },
        {
            'id': 4,
            'brand': 'Eco',
            'name': '2500L System',
            'capacity': '2500L',
            'pump': '0.75kW Multi-Stage',
            'filtration': '3-Stage',
            'price': 'R14,499',
            'image': 'eco-2500.png'
        },
        {
            'id': 5,
            'brand': 'JoJo',
            'name': '5000L System',
            'capacity': '5000L',
            'pump': '1.1kW High-Pressure',
            'filtration': None,
            'price': 'R18,999',
            'image': 'jojo-5200.webp'
        },
        {
            'id': 6,
            'brand': 'Eco',
            'name': '5000L System',
            'capacity': '5000L',
            'pump': '1.1kW High-Pressure',
            'filtration': '3-Stage',
            'price': 'R21,499',
            'image': 'eco-5000.png'
        }
    ]
    return render_template('systems.html', systems=systems_data)

@app.route('/portfolio')
def portfolio():
    portfolio_images = [
        {
            "filename": "job1.jpg",
            "location": "Umhloti Beach.",
            "description": "2x1500L system with advanced filtration"
        },
        {
            "filename": "job2.jpg",
            "location": "Kloof",
            "description": "5050lt Eco Tank powered by a 1.1kw Multistage Pump setup for full automation"
        },
        {
            "filename": "job3.jpg",
            "location": "Tongaat",
            "description": "5050lt Eco Tank"
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



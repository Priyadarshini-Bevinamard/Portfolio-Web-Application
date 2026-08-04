from flask import Blueprint, render_template, request, jsonify
from models.database import save_contact
from datetime import datetime

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    return render_template('home.html')

@main_blueprint.route('/about')
def about():
    return render_template('about.html')

@main_blueprint.route('/skills')
def skills():
    return render_template('skills.html')

@main_blueprint.route('/projects')
def projects():
    return render_template('projects.html')

@main_blueprint.route('/certifications')
def certifications():
    return render_template('certifications.html')

@main_blueprint.route('/achievements')
def achievements():
    return render_template('achievements.html')

@main_blueprint.route('/contact')
def contact():
    return render_template('contact.html')

@main_blueprint.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.get_json()
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    if not name or not email or not subject or not message:
        return jsonify({'success': False, 'message': 'All fields are required.'}), 400

    try:
        created_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        save_contact(name, email, subject, message, created_date)
        return jsonify({'success': True, 'message': 'Message submitted successfully.'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'Unable to save contact message.'}), 500

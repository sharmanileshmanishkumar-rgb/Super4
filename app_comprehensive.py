from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import hashlib
import jwt
from datetime import datetime, timedelta
import requests
import json

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edumate_comprehensive.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    standard = db.Column(db.String(50), nullable=True)  # 6-10, JEE, Engineering
    branch = db.Column(db.String(50), nullable=True)   # CS, IT for Engineering
    grade = db.Column(db.String(20), nullable=True)     # 6th, 7th, 8th, 9th, 10th
    school = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'standard': self.standard,
            'branch': self.branch,
            'grade': self.grade,
            'school': self.school,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None
        }

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    standard = db.Column(db.String(50), nullable=False)  # 6-10, JEE, Engineering
    branch = db.Column(db.String(50), nullable=True)      # CS, IT for Engineering
    description = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(50), nullable=True)
    color = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'standard': self.standard,
            'branch': self.branch,
            'description': self.description,
            'icon': self.icon,
            'color': self.color
        }

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(20), nullable=True)  # Easy, Medium, Hard
    order_index = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'subject_id': self.subject_id,
            'name': self.name,
            'description': self.description,
            'difficulty': self.difficulty,
            'order_index': self.order_index
        }

class LearningProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=True)
    progress_percentage = db.Column(db.Float, default=0.0)
    time_spent = db.Column(db.Integer, default=0)  # in minutes
    last_accessed = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    score = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'subject_id': self.subject_id,
            'topic_id': self.topic_id,
            'progress_percentage': self.progress_percentage,
            'time_spent': self.time_spent,
            'last_accessed': self.last_accessed.isoformat(),
            'completed': self.completed,
            'score': self.score
        }

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    url = db.Column(db.String(500), nullable=True)
    duration = db.Column(db.Integer, nullable=True)  # in minutes
    level = db.Column(db.String(20), nullable=True)  # Beginner, Intermediate, Advanced
    thumbnail = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'subject_id': self.subject_id,
            'topic_id': self.topic_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'duration': self.duration,
            'level': self.level,
            'thumbnail': self.thumbnail
        }

class PracticeProblem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=True)
    question = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text, nullable=True)  # JSON array of options
    correct_answer = db.Column(db.Integer, nullable=True)  # index of correct option
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(20), nullable=True)  # Easy, Medium, Hard
    points = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'subject_id': self.subject_id,
            'topic_id': self.topic_id,
            'question': self.question,
            'options': json.loads(self.options) if self.options else [],
            'correct_answer': self.correct_answer,
            'explanation': self.explanation,
            'difficulty': self.difficulty,
            'points': self.points
        }

class Animation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=True)  # Stack, Queue, Binary Search, etc.
    data = db.Column(db.Text, nullable=True)  # JSON data for animation
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'subject_id': self.subject_id,
            'topic_id': self.topic_id,
            'name': self.name,
            'type': self.type,
            'data': json.loads(self.data) if self.data else {},
            'description': self.description
        }

# Authentication endpoints
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Check if user already exists
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'User already exists'}), 400
        
        # Create new user
        user = User(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            password_hash=hashlib.sha256(data['password'].encode()).hexdigest(),
            standard=data.get('standard'),
            branch=data.get('branch'),
            grade=data.get('grade'),
            school=data.get('school')
        )
        
        db.session.add(user)
        db.session.commit()
        
        # Generate JWT token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=7)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({
            'message': 'User registered successfully',
            'token': token,
            'user': user.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        # Find user
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # Check password
        if user.password_hash != hashlib.sha256(data['password'].encode()).hexdigest():
            return jsonify({'error': 'Invalid password'}), 401
        
        # Update last login
        user.last_login = datetime.utcnow()
        db.session.commit()
        
        # Generate JWT token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=7)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Progress tracking
@app.route('/api/progress', methods=['POST'])
def save_progress():
    try:
        data = request.get_json()
        
        # Find or create progress record
        progress = LearningProgress.query.filter_by(
            user_id=data['user_id'],
            subject_id=data['subject_id'],
            topic_id=data.get('topic_id')
        ).first()
        
        if not progress:
            progress = LearningProgress(
                user_id=data['user_id'],
                subject_id=data['subject_id'],
                topic_id=data.get('topic_id'),
                progress_percentage=data.get('progress_percentage', 0.0),
                time_spent=data.get('time_spent', 0),
                completed=data.get('completed', False),
                score=data.get('score', 0)
            )
            db.session.add(progress)
        else:
            progress.progress_percentage = data.get('progress_percentage', progress.progress_percentage)
            progress.time_spent += data.get('time_spent', 0)
            progress.completed = data.get('completed', progress.completed)
            progress.score = data.get('score', progress.score)
            progress.last_accessed = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Progress saved successfully',
            'progress': progress.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Subject content endpoints
@app.route('/api/subjects/<standard>', methods=['GET'])
def get_subjects_by_standard(standard):
    try:
        subjects = Subject.query.filter_by(standard=standard).all()
        return jsonify([subject.to_dict() for subject in subjects]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/subjects/<standard>/<subject_name>', methods=['GET'])
def get_subject_details(standard, subject_name):
    try:
        subject = Subject.query.filter_by(standard=standard, name=subject_name).first()
        if not subject:
            return jsonify({'error': 'Subject not found'}), 404
        
        # Get topics for this subject
        topics = Topic.query.filter_by(subject_id=subject.id).all()
        
        # Get videos for this subject
        videos = Video.query.filter_by(subject_id=subject.id).all()
        
        # Get practice problems for this subject
        problems = PracticeProblem.query.filter_by(subject_id=subject.id).all()
        
        # Get animations for this subject
        animations = Animation.query.filter_by(subject_id=subject.id).all()
        
        return jsonify({
            'subject': subject.to_dict(),
            'topics': [topic.to_dict() for topic in topics],
            'videos': [video.to_dict() for video in videos],
            'problems': [problem.to_dict() for problem in problems],
            'animations': [animation.to_dict() for animation in animations]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Video content endpoint
@app.route('/api/videos/<subject_name>', methods=['GET'])
def get_videos(subject_name):
    try:
        subject = Subject.query.filter_by(name=subject_name).first()
        if not subject:
            return jsonify({'error': 'Subject not found'}), 404
        
        videos = Video.query.filter_by(subject_id=subject.id).all()
        return jsonify([video.to_dict() for video in videos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Practice problems endpoint
@app.route('/api/practice/<subject_name>/<difficulty>', methods=['GET'])
def get_practice_problems(subject_name, difficulty):
    try:
        subject = Subject.query.filter_by(name=subject_name).first()
        if not subject:
            return jsonify({'error': 'Subject not found'}), 404
        
        problems = PracticeProblem.query.filter_by(
            subject_id=subject.id,
            difficulty=difficulty
        ).all()
        
        return jsonify([problem.to_dict() for problem in problems]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# AI explanation endpoint
@app.route('/api/openai/explain', methods=['POST'])
def get_ai_explanation():
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        
        # Enhanced explanations for different subjects
        explanations = {
            'data_structures': 'Data structures are ways of organizing data in a computer so that it can be used efficiently. They provide a means to manage large amounts of data efficiently.',
            'algorithms': 'Algorithms are step-by-step procedures for solving problems or completing tasks. They are the building blocks of computer programming.',
            'machine_learning': 'Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed.',
            'web_development': 'Web development involves creating websites and web applications using various technologies like HTML, CSS, JavaScript, and server-side languages.',
            'physics': 'Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force.',
            'chemistry': 'Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions.',
            'biology': 'Biology is the natural science that studies life and living organisms, including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development and evolution.',
            'mathematics': 'Mathematics is the science that deals with the logic of shape, quantity and arrangement. Math is all around us, in everything we do.',
            'mechanics': 'Mechanics is the branch of physics that deals with the motion of objects and the forces that cause this motion.',
            'thermodynamics': 'Thermodynamics is the branch of physics that deals with heat and temperature and their relation to energy and work.',
            'atomic_structure': 'Atomic structure refers to the arrangement of electrons around the nucleus of an atom.',
            'chemical_bonding': 'Chemical bonding is the attraction between atoms that allows the formation of chemical substances.',
            'cell_biology': 'Cell biology is the study of cell structure and function, and it revolves around the concept that the cell is the fundamental unit of life.',
            'genetics': 'Genetics is the study of genes, genetic variation, and heredity in living organisms.',
            'algebra': 'Algebra is a branch of mathematics that uses symbols and letters to represent numbers and quantities in formulas and equations.',
            'geometry': 'Geometry is a branch of mathematics concerned with questions of shape, size, relative position of figures, and the properties of space.'
        }
        
        explanation = explanations.get(topic.lower().replace(' ', '_'), f'This is a comprehensive explanation of {topic}. It covers all the fundamental concepts and provides practical examples.')
        
        return jsonify({
            'topic': topic,
            'explanation': explanation,
            'examples': [
                f'Example 1: Basic {topic} concept',
                f'Example 2: Advanced {topic} application',
                f'Example 3: Real-world {topic} usage'
            ]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize database with sample data
def initialize_database():
    with app.app_context():
        db.create_all()
        
        # Check if data already exists
        if Subject.query.count() == 0:
            # Insert default subjects
            subjects_data = [
                # 6-10 Standards
                {'name': 'Physics', 'standard': '6-10', 'description': 'Science of matter, motion, and energy', 'icon': 'fas fa-atom', 'color': '#3b82f6'},
                {'name': 'Chemistry', 'standard': '6-10', 'description': 'Study of matter and its properties', 'icon': 'fas fa-flask', 'color': '#10b981'},
                {'name': 'Biology', 'standard': '6-10', 'description': 'Study of living organisms', 'icon': 'fas fa-dna', 'color': '#8b5cf6'},
                {'name': 'Mathematics', 'standard': '6-10', 'description': 'Numbers, shapes, and patterns', 'icon': 'fas fa-calculator', 'color': '#f59e0b'},
                
                # JEE Preparation
                {'name': 'JEE Physics', 'standard': 'JEE', 'description': 'Advanced physics for JEE preparation', 'icon': 'fas fa-atom', 'color': '#3b82f6'},
                {'name': 'JEE Chemistry', 'standard': 'JEE', 'description': 'Advanced chemistry for JEE preparation', 'icon': 'fas fa-flask', 'color': '#10b981'},
                {'name': 'JEE Mathematics', 'standard': 'JEE', 'description': 'Advanced mathematics for JEE preparation', 'icon': 'fas fa-calculator', 'color': '#f59e0b'},
                
                # Engineering
                {'name': 'Computer Science', 'standard': 'Engineering', 'branch': 'CS', 'description': 'Computer Science Engineering', 'icon': 'fas fa-laptop-code', 'color': '#3b82f6'},
                {'name': 'Information Technology', 'standard': 'Engineering', 'branch': 'IT', 'description': 'Information Technology Engineering', 'icon': 'fas fa-server', 'color': '#10b981'}
            ]
            
            for subject_data in subjects_data:
                subject = Subject(**subject_data)
                db.session.add(subject)
            
            db.session.commit()
            
            # Insert sample topics
            physics = Subject.query.filter_by(name='Physics').first()
            chemistry = Subject.query.filter_by(name='Chemistry').first()
            biology = Subject.query.filter_by(name='Biology').first()
            mathematics = Subject.query.filter_by(name='Mathematics').first()
            
            topics_data = [
                # Physics topics
                {'subject_id': physics.id, 'name': 'Mechanics', 'description': 'Motion, forces, and energy', 'difficulty': 'Medium', 'order_index': 1},
                {'subject_id': physics.id, 'name': 'Thermodynamics', 'description': 'Heat and temperature', 'difficulty': 'Hard', 'order_index': 2},
                {'subject_id': physics.id, 'name': 'Waves & Sound', 'description': 'Wave properties and sound', 'difficulty': 'Medium', 'order_index': 3},
                {'subject_id': physics.id, 'name': 'Electricity & Magnetism', 'description': 'Electric and magnetic fields', 'difficulty': 'Hard', 'order_index': 4},
                
                # Chemistry topics
                {'subject_id': chemistry.id, 'name': 'Atomic Structure', 'description': 'Atoms, electrons, and periodic table', 'difficulty': 'Medium', 'order_index': 1},
                {'subject_id': chemistry.id, 'name': 'Chemical Bonding', 'description': 'Ionic, covalent, and metallic bonds', 'difficulty': 'Hard', 'order_index': 2},
                {'subject_id': chemistry.id, 'name': 'Chemical Reactions', 'description': 'Balancing equations and stoichiometry', 'difficulty': 'Medium', 'order_index': 3},
                {'subject_id': chemistry.id, 'name': 'Acids & Bases', 'description': 'pH scale and neutralization', 'difficulty': 'Medium', 'order_index': 4},
                
                # Biology topics
                {'subject_id': biology.id, 'name': 'Cell Biology', 'description': 'Cell structure and function', 'difficulty': 'Easy', 'order_index': 1},
                {'subject_id': biology.id, 'name': 'Genetics', 'description': 'DNA, genes, and heredity', 'difficulty': 'Hard', 'order_index': 2},
                {'subject_id': biology.id, 'name': 'Ecology', 'description': 'Ecosystems and biodiversity', 'difficulty': 'Medium', 'order_index': 3},
                {'subject_id': biology.id, 'name': 'Human Body', 'description': 'Organ systems and anatomy', 'difficulty': 'Medium', 'order_index': 4},
                
                # Mathematics topics
                {'subject_id': mathematics.id, 'name': 'Algebra', 'description': 'Linear and quadratic equations', 'difficulty': 'Medium', 'order_index': 1},
                {'subject_id': mathematics.id, 'name': 'Geometry', 'description': 'Shapes, angles, and area', 'difficulty': 'Medium', 'order_index': 2},
                {'subject_id': mathematics.id, 'name': 'Trigonometry', 'description': 'Sine, cosine, and tangent', 'difficulty': 'Hard', 'order_index': 3},
                {'subject_id': mathematics.id, 'name': 'Statistics & Probability', 'description': 'Data analysis and chance', 'difficulty': 'Medium', 'order_index': 4}
            ]
            
            for topic_data in topics_data:
                topic = Topic(**topic_data)
                db.session.add(topic)
            
            db.session.commit()
            
            print("Database initialized with sample data!")

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True, port=5000)

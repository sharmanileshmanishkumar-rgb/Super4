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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edumate.db'
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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'standard': self.standard,
            'branch': self.branch,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None
        }

class LearningProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(200), nullable=False)
    progress_percentage = db.Column(db.Float, default=0.0)
    time_spent = db.Column(db.Integer, default=0)  # in minutes
    last_accessed = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'subject': self.subject,
            'topic': self.topic,
            'progress_percentage': self.progress_percentage,
            'time_spent': self.time_spent,
            'last_accessed': self.last_accessed.isoformat()
        }

# API Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({'error': 'User already exists'}), 400
        
        # Create new user
        password_hash = hashlib.sha256(data['password'].encode()).hexdigest()
        
        user = User(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', ''),
            password_hash=password_hash,
            standard=data.get('standard', ''),
            branch=data.get('branch', '')
        )
        
        db.session.add(user)
        db.session.commit()
        
        # Generate JWT token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=7)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({
            'message': 'User created successfully',
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
        password_hash = hashlib.sha256(data['password'].encode()).hexdigest()
        if user.password_hash != password_hash:
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

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({'user': user.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/progress', methods=['POST'])
def update_progress():
    try:
        data = request.get_json()
        
        # Find existing progress or create new
        progress = LearningProgress.query.filter_by(
            user_id=data['user_id'],
            subject=data['subject'],
            topic=data['topic']
        ).first()
        
        if progress:
            progress.progress_percentage = data['progress_percentage']
            progress.time_spent += data.get('time_spent', 0)
            progress.last_accessed = datetime.utcnow()
        else:
            progress = LearningProgress(
                user_id=data['user_id'],
                subject=data['subject'],
                topic=data['topic'],
                progress_percentage=data['progress_percentage'],
                time_spent=data.get('time_spent', 0)
            )
            db.session.add(progress)
        
        db.session.commit()
        
        return jsonify({'message': 'Progress updated successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/progress/<int:user_id>', methods=['GET'])
def get_progress(user_id):
    try:
        progress_list = LearningProgress.query.filter_by(user_id=user_id).all()
        return jsonify({
            'progress': [p.to_dict() for p in progress_list]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# External API Integrations
@app.route('/api/openai/explain', methods=['POST'])
def get_ai_explanation():
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        
        # Simulate OpenAI API call
        # In a real implementation, you would call OpenAI's API
        explanations = {
            'data_structures': 'Data structures are ways of organizing data in a computer so that it can be used efficiently. They provide a means to manage large amounts of data efficiently.',
            'algorithms': 'Algorithms are step-by-step procedures for solving problems or completing tasks. They are the building blocks of computer programming.',
            'machine_learning': 'Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed.',
            'web_development': 'Web development involves creating websites and web applications using various technologies like HTML, CSS, JavaScript, and server-side languages.',
            'physics': 'Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force.',
            'chemistry': 'Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions.',
            'biology': 'Biology is the natural science that studies life and living organisms, including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development and evolution.',
            'mathematics': 'Mathematics is the science that deals with the logic of shape, quantity and arrangement. Math is all around us, in everything we do.'
        }
        
        explanation = explanations.get(topic.lower(), f'This is a comprehensive explanation of {topic}. It covers all the fundamental concepts and provides practical examples.')
        
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

# Subject-specific content endpoints
@app.route('/api/content/<standard>/<subject>', methods=['GET'])
def get_subject_content(standard, subject):
    try:
        content_data = {
            '6-10': {
                'physics': {
                    'title': 'Physics - 6-10 Standards',
                    'topics': [
                        {
                            'name': 'Mechanics',
                            'subtopics': ['Motion', 'Forces', 'Energy', 'Momentum'],
                            'videos': [
                                {'title': 'Introduction to Motion', 'duration': '15 min', 'level': 'Beginner'},
                                {'title': 'Newton\'s Laws', 'duration': '20 min', 'level': 'Intermediate'},
                                {'title': 'Energy and Work', 'duration': '25 min', 'level': 'Advanced'}
                            ],
                            'simulations': [
                                {'name': 'Projectile Motion Simulator', 'description': 'Interactive projectile motion'},
                                {'name': 'Pendulum Simulator', 'description': 'Simple harmonic motion'}
                            ],
                            'problems': [
                                {'type': 'Kinematics', 'difficulty': 'Easy', 'count': 15},
                                {'type': 'Dynamics', 'difficulty': 'Medium', 'count': 20},
                                {'type': 'Energy', 'difficulty': 'Hard', 'count': 10}
                            ]
                        },
                        {
                            'name': 'Thermodynamics',
                            'subtopics': ['Heat', 'Temperature', 'Laws of Thermodynamics'],
                            'videos': [
                                {'title': 'Heat and Temperature', 'duration': '18 min', 'level': 'Beginner'},
                                {'title': 'First Law of Thermodynamics', 'duration': '22 min', 'level': 'Intermediate'}
                            ],
                            'simulations': [
                                {'name': 'Heat Transfer Simulator', 'description': 'Visualize heat flow'},
                                {'name': 'Thermodynamic Cycle', 'description': 'Interactive cycle diagrams'}
                            ],
                            'problems': [
                                {'type': 'Heat Transfer', 'difficulty': 'Easy', 'count': 12},
                                {'type': 'Thermodynamic Laws', 'difficulty': 'Medium', 'count': 18}
                            ]
                        }
                    ],
                    'resources': [
                        'Interactive simulations',
                        'Video explanations',
                        'Practice problems',
                        'Virtual labs'
                    ]
                },
                'chemistry': {
                    'title': 'Chemistry - 6-10 Standards',
                    'topics': [
                        {
                            'name': 'Atomic Structure',
                            'subtopics': ['Atoms', 'Electrons', 'Periodic Table'],
                            'videos': [
                                {'title': 'Atomic Structure Basics', 'duration': '20 min', 'level': 'Beginner'},
                                {'title': 'Electron Configuration', 'duration': '25 min', 'level': 'Intermediate'}
                            ],
                            'simulations': [
                                {'name': 'Atomic Model Builder', 'description': 'Build atoms interactively'},
                                {'name': 'Periodic Table Explorer', 'description': 'Explore element properties'}
                            ],
                            'problems': [
                                {'type': 'Atomic Structure', 'difficulty': 'Easy', 'count': 20},
                                {'type': 'Electron Configuration', 'difficulty': 'Medium', 'count': 15}
                            ]
                        }
                    ],
                    'resources': [
                        'Molecular visualizations',
                        'Chemical equation balancer',
                        'Virtual chemistry lab',
                        'Interactive periodic table'
                    ]
                }
            },
            'JEE': {
                'jee-physics': {
                    'title': 'JEE Physics Preparation',
                    'topics': [
                        {
                            'name': 'Advanced Mechanics',
                            'subtopics': ['Kinematics', 'Dynamics', 'Work & Energy', 'Rotational Motion'],
                            'difficulty': 'Advanced',
                            'videos': [
                                {'title': 'JEE Mechanics - Part 1', 'duration': '45 min', 'level': 'Advanced'},
                                {'title': 'Problem Solving Techniques', 'duration': '60 min', 'level': 'Advanced'}
                            ],
                            'papers': [
                                {'year': '2023', 'type': 'Main', 'difficulty': 'High'},
                                {'year': '2022', 'type': 'Advanced', 'difficulty': 'Very High'}
                            ],
                            'problems': [
                                {'type': 'Previous Year', 'difficulty': 'Very Hard', 'count': 50},
                                {'type': 'Mock Tests', 'difficulty': 'Hard', 'count': 30}
                            ]
                        }
                    ],
                    'resources': [
                        'Previous year papers',
                        'Mock tests',
                        'Video solutions',
                        'Conceptual animations'
                    ]
                }
            },
            'Engineering': {
                'computer-science': {
                    'title': 'Computer Science Engineering',
                    'branches': {
                        'core': {
                            'name': 'Core CS Subjects',
                            'subjects': [
                                {
                                    'name': 'Data Structures & Algorithms',
                                    'topics': ['Arrays', 'Linked Lists', 'Trees', 'Graphs', 'Sorting', 'Searching'],
                                    'videos': [
                                        {'title': 'Introduction to Data Structures', 'duration': '30 min', 'level': 'Beginner'},
                                        {'title': 'Algorithm Analysis', 'duration': '45 min', 'level': 'Intermediate'}
                                    ],
                                    'code_examples': [
                                        {'language': 'Python', 'topic': 'Stack Implementation', 'lines': 25},
                                        {'language': 'Java', 'topic': 'Binary Tree', 'lines': 40}
                                    ],
                                    'visualizations': [
                                        {'name': 'Array Operations', 'type': 'Interactive'},
                                        {'name': 'Tree Traversal', 'type': 'Animated'}
                                    ]
                                }
                            ]
                        }
                    },
                    'resources': [
                        'Visualizations',
                        'Code examples',
                        'Practice problems',
                        'Interactive tutorials'
                    ]
                }
            }
        }
        
        if standard in content_data and subject in content_data[standard]:
            return jsonify(content_data[standard][subject]), 200
        else:
            return jsonify({'error': 'Content not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Practice problems endpoint
@app.route('/api/practice/<subject>/<difficulty>', methods=['GET'])
def get_practice_problems(subject, difficulty):
    try:
        problems = {
            'physics': {
                'easy': [
                    {'id': 1, 'question': 'What is the unit of force?', 'options': ['N', 'kg', 'm/s', 'J'], 'correct': 0},
                    {'id': 2, 'question': 'What is acceleration due to gravity?', 'options': ['9.8 m/s²', '10 m/s²', '8.9 m/s²', '11 m/s²'], 'correct': 0}
                ],
                'medium': [
                    {'id': 3, 'question': 'A car accelerates from 0 to 60 km/h in 10 seconds. What is its acceleration?', 'options': ['6 m/s²', '1.67 m/s²', '60 m/s²', '10 m/s²'], 'correct': 1}
                ],
                'hard': [
                    {'id': 4, 'question': 'A projectile is launched at 30° with velocity 20 m/s. What is its range?', 'options': ['34.6 m', '20 m', '40 m', '17.3 m'], 'correct': 0}
                ]
            },
            'chemistry': {
                'easy': [
                    {'id': 1, 'question': 'What is the atomic number of Hydrogen?', 'options': ['1', '2', '0', '3'], 'correct': 0},
                    {'id': 2, 'question': 'What is the chemical formula of water?', 'options': ['H2O', 'H2O2', 'HO', 'H3O'], 'correct': 0}
                ],
                'medium': [
                    {'id': 3, 'question': 'What is the pH of a 0.1 M HCl solution?', 'options': ['1', '2', '0.1', '10'], 'correct': 0}
                ],
                'hard': [
                    {'id': 4, 'question': 'In a chemical reaction, 2A + 3B → C, if 2 moles of A react with 3 moles of B, how many moles of C are formed?', 'options': ['1', '2', '3', '5'], 'correct': 0}
                ]
            }
        }
        
        if subject in problems and difficulty in problems[subject]:
            return jsonify({
                'subject': subject,
                'difficulty': difficulty,
                'problems': problems[subject][difficulty]
            }), 200
        else:
            return jsonify({'error': 'Problems not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Video content endpoint
@app.route('/api/videos/<subject>', methods=['GET'])
def get_video_content(subject):
    try:
        videos = {
            'physics': [
                {'title': 'Introduction to Physics', 'duration': '15 min', 'level': 'Beginner', 'url': '#'},
                {'title': 'Newton\'s Laws Explained', 'duration': '25 min', 'level': 'Intermediate', 'url': '#'},
                {'title': 'Energy and Work', 'duration': '30 min', 'level': 'Advanced', 'url': '#'}
            ],
            'chemistry': [
                {'title': 'Atomic Structure Basics', 'duration': '20 min', 'level': 'Beginner', 'url': '#'},
                {'title': 'Chemical Bonding', 'duration': '35 min', 'level': 'Intermediate', 'url': '#'},
                {'title': 'Organic Chemistry Introduction', 'duration': '40 min', 'level': 'Advanced', 'url': '#'}
            ],
            'biology': [
                {'title': 'Cell Structure and Function', 'duration': '25 min', 'level': 'Beginner', 'url': '#'},
                {'title': 'DNA and Genetics', 'duration': '30 min', 'level': 'Intermediate', 'url': '#'},
                {'title': 'Evolution and Ecology', 'duration': '35 min', 'level': 'Advanced', 'url': '#'}
            ],
            'mathematics': [
                {'title': 'Algebra Fundamentals', 'duration': '20 min', 'level': 'Beginner', 'url': '#'},
                {'title': 'Calculus Introduction', 'duration': '45 min', 'level': 'Intermediate', 'url': '#'},
                {'title': 'Advanced Calculus', 'duration': '60 min', 'level': 'Advanced', 'url': '#'}
            ]
        }
        
        if subject in videos:
            return jsonify({
                'subject': subject,
                'videos': videos[subject]
            }), 200
        else:
            return jsonify({'error': 'Videos not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)

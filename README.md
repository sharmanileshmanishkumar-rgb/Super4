# EduMate - Interactive Educational Platform

EduMate is a comprehensive educational website designed for students across different academic levels, featuring interactive animations, AI-powered learning, and personalized educational content.

## 🎯 Features

### Educational Standards
- **6-10 Standards (Science)**: Physics, Chemistry, Biology, Mathematics
- **JEE Preparation**: Advanced Physics, Chemistry, Mathematics, Mock Tests
- **Engineering**: Computer Science and Information Technology courses

### Key Features
- 🎬 **Interactive Animations**: Visual learning through animated concepts
- 🤖 **AI-Powered Learning**: Personalized explanations and assistance
- 🌙 **Dark/Light Mode**: Customizable theme with system preference detection
- 📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- 👤 **User Authentication**: Secure signup/login with session management
- 📊 **Progress Tracking**: Monitor learning progress and time spent
- 🔗 **API Integration**: GeeksforGeeks, OpenAI, Khan Academy resources
- 🎭 **Animated Character**: Interactive learning assistant

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd EduMate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask backend**
   ```bash
   python app.py
   ```

4. **Open the website**
   - Navigate to `http://localhost:5000` for the backend
   - Open `home.html` in your browser for the main website

## 📁 Project Structure

```
EduMate/
├── home.html              # Main homepage
├── login.html             # User authentication
├── standards.html          # Educational standards page
├── about.html             # About us page
├── contact.html           # Contact page
├── index.html             # Animation interface
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── text_to_animation.py   # AI animation generation
└── README.md              # This file
```

## 🎨 Website Pages

### 1. Home Page (`home.html`)
- Welcome section with feature highlights
- Educational standards preview
- User navigation and theme toggle
- Animated character assistant

### 2. Login/Signup (`login.html`)
- User registration with detailed forms
- Secure authentication system
- Social login options (Google, Facebook)
- Form validation and error handling

### 3. Standards Page (`standards.html`)
- **6-10 Standards**: Science subjects for middle/high school
- **JEE Preparation**: Comprehensive exam preparation
- **Engineering**: Computer Science and IT branches
- API integration for external resources

### 4. About Page (`about.html`)
- Company information and mission
- Team member profiles
- Statistics and achievements
- Contact information

### 5. Contact Page (`contact.html`)
- Contact form with validation
- FAQ section
- Social media links
- Business information

### 6. Animation Interface (`index.html`)
- Interactive concept animations
- Subject selection and navigation
- Progress tracking
- AI-powered explanations

## 🔧 Backend API

The Flask backend (`app.py`) provides the following endpoints:

### Authentication
- `POST /api/register` - User registration
- `POST /api/login` - User login
- `GET /api/user/<id>` - Get user information

### Learning Progress
- `POST /api/progress` - Update learning progress
- `GET /api/progress/<user_id>` - Get user progress

### External APIs
- `GET /api/geeksforgeeks/<topic>` - GeeksforGeeks content
- `POST /api/openai/explain` - AI explanations
- `GET /api/khan_academy/<subject>` - Khan Academy content

## 🎭 Animated Character

The website features an interactive animated character that:
- Provides learning assistance
- Helps navigate through subjects
- Explains complex concepts
- Responds to user interactions

## 🌙 Theme System

### Dark/Light Mode Features
- Automatic system preference detection
- Manual toggle in navigation
- Persistent theme selection
- Smooth transitions between themes
- Optimized colors for accessibility

### Theme Variables
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --accent-color: #f093fb;
    --text-dark: #2d3748;
    --text-light: #718096;
    --bg-light: #f7fafc;
    --bg-dark: #1a202c;
    --card-bg: #ffffff;
    --border-color: #e2e8f0;
}
```

## 📱 Responsive Design

The website is fully responsive with:
- Mobile-first approach
- Flexible grid layouts
- Touch-friendly interactions
- Optimized images and animations
- Cross-browser compatibility

## 🔐 User Authentication

### Registration Process
1. User fills out detailed registration form
2. System validates email and phone number
3. Password is securely hashed
4. User data is stored in database
5. JWT token is generated for session management

### Login Process
1. User enters credentials
2. System validates against database
3. Session token is generated
4. User data is stored in localStorage
5. Automatic redirect to main application

## 📊 Progress Tracking

The system tracks:
- Learning progress percentage
- Time spent on each topic
- Last accessed subjects
- Overall learning statistics

## 🔗 API Integrations

### GeeksforGeeks
- Access to programming articles
- Algorithm explanations
- Code examples and tutorials

### OpenAI Integration
- AI-powered explanations
- Personalized learning assistance
- Concept clarification

### Khan Academy
- Educational video content
- Practice exercises
- Progress tracking

## 🎨 Animation System

### Supported Concepts
- **Data Structures**: Stack, Queue, Linked List
- **Algorithms**: Bubble Sort, Binary Search
- **Mathematics**: Geometric concepts, Functions
- **Science**: Physics simulations, Chemical reactions

### Animation Features
- Step-by-step explanations
- Interactive controls (Play, Pause, Restart)
- Visual progress indicators
- Real-time concept demonstration

## 🛠️ Development

### Adding New Animations
1. Add animation data to `initializeAnimationData()`
2. Create animation setup method
3. Implement step execution logic
4. Add visual styling for elements

### Adding New Subjects
1. Update standards page with new subject
2. Add subject-specific animations
3. Create API endpoints for content
4. Update navigation and routing

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set up production database
2. Configure environment variables
3. Set up web server (nginx/Apache)
4. Deploy to cloud platform (AWS, Heroku, etc.)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For support and questions:
- Email: support@edumate.com
- Phone: +1 (555) 123-4567
- Website: Contact page for form submission

## 🎯 Future Enhancements

- [ ] Real-time collaboration features
- [ ] Advanced AI tutoring
- [ ] Mobile app development
- [ ] Offline learning capabilities
- [ ] Gamification elements
- [ ] Virtual reality integration

---

**EduMate** - Transforming education through interactive learning and AI-powered personalization.

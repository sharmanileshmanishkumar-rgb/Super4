-- EduMate Database Schema
-- Comprehensive database for educational platform

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20),
    password_hash VARCHAR(128) NOT NULL,
    standard VARCHAR(50), -- 6-10, JEE, Engineering
    branch VARCHAR(50),  -- CS, IT for Engineering
    grade VARCHAR(20),   -- 6th, 7th, 8th, 9th, 10th
    school VARCHAR(200),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME,
    is_active BOOLEAN DEFAULT 1
);

-- Subjects table
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    standard VARCHAR(50) NOT NULL, -- 6-10, JEE, Engineering
    branch VARCHAR(50), -- CS, IT for Engineering
    description TEXT,
    icon VARCHAR(50),
    color VARCHAR(20),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Topics table
CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    difficulty VARCHAR(20), -- Easy, Medium, Hard
    order_index INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

-- Learning Progress table
CREATE TABLE IF NOT EXISTS learning_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    topic_id INTEGER,
    progress_percentage FLOAT DEFAULT 0.0,
    time_spent INTEGER DEFAULT 0, -- in minutes
    last_accessed DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed BOOLEAN DEFAULT 0,
    score INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- Videos table
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    topic_id INTEGER,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    url VARCHAR(500),
    duration INTEGER, -- in minutes
    level VARCHAR(20), -- Beginner, Intermediate, Advanced
    thumbnail VARCHAR(500),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- Practice Problems table
CREATE TABLE IF NOT EXISTS practice_problems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    topic_id INTEGER,
    question TEXT NOT NULL,
    options TEXT, -- JSON array of options
    correct_answer INTEGER, -- index of correct option
    explanation TEXT,
    difficulty VARCHAR(20), -- Easy, Medium, Hard
    points INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- Animations table
CREATE TABLE IF NOT EXISTS animations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    topic_id INTEGER,
    name VARCHAR(200) NOT NULL,
    type VARCHAR(50), -- Stack, Queue, Binary Search, etc.
    data TEXT, -- JSON data for animation
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- User Sessions table
CREATE TABLE IF NOT EXISTS user_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    session_token VARCHAR(255) NOT NULL,
    expires_at DATETIME NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert default subjects
INSERT INTO subjects (name, standard, description, icon, color) VALUES
-- 6-10 Standards
('Physics', '6-10', 'Science of matter, motion, and energy', 'fas fa-atom', '#3b82f6'),
('Chemistry', '6-10', 'Study of matter and its properties', 'fas fa-flask', '#10b981'),
('Biology', '6-10', 'Study of living organisms', 'fas fa-dna', '#8b5cf6'),
('Mathematics', '6-10', 'Numbers, shapes, and patterns', 'fas fa-calculator', '#f59e0b'),

-- JEE Preparation
('JEE Physics', 'JEE', 'Advanced physics for JEE preparation', 'fas fa-atom', '#3b82f6'),
('JEE Chemistry', 'JEE', 'Advanced chemistry for JEE preparation', 'fas fa-flask', '#10b981'),
('JEE Mathematics', 'JEE', 'Advanced mathematics for JEE preparation', 'fas fa-calculator', '#f59e0b'),

-- Engineering
('Computer Science', 'Engineering', 'Computer Science Engineering', 'fas fa-laptop-code', '#3b82f6'),
('Information Technology', 'Engineering', 'Information Technology Engineering', 'fas fa-server', '#10b981');

-- Insert default topics for Physics
INSERT INTO topics (subject_id, name, description, difficulty, order_index) VALUES
(1, 'Mechanics', 'Motion, forces, and energy', 'Medium', 1),
(1, 'Thermodynamics', 'Heat and temperature', 'Hard', 2),
(1, 'Waves & Sound', 'Wave properties and sound', 'Medium', 3),
(1, 'Electricity & Magnetism', 'Electric and magnetic fields', 'Hard', 4);

-- Insert default topics for Chemistry
INSERT INTO topics (subject_id, name, description, difficulty, order_index) VALUES
(2, 'Atomic Structure', 'Atoms, electrons, and periodic table', 'Medium', 1),
(2, 'Chemical Bonding', 'Ionic, covalent, and metallic bonds', 'Hard', 2),
(2, 'Chemical Reactions', 'Balancing equations and stoichiometry', 'Medium', 3),
(2, 'Acids & Bases', 'pH scale and neutralization', 'Medium', 4);

-- Insert default topics for Biology
INSERT INTO topics (subject_id, name, description, difficulty, order_index) VALUES
(3, 'Cell Biology', 'Cell structure and function', 'Easy', 1),
(3, 'Genetics', 'DNA, genes, and heredity', 'Hard', 2),
(3, 'Ecology', 'Ecosystems and biodiversity', 'Medium', 3),
(3, 'Human Body', 'Organ systems and anatomy', 'Medium', 4);

-- Insert default topics for Mathematics
INSERT INTO topics (subject_id, name, description, difficulty, order_index) VALUES
(4, 'Algebra', 'Linear and quadratic equations', 'Medium', 1),
(4, 'Geometry', 'Shapes, angles, and area', 'Medium', 2),
(4, 'Trigonometry', 'Sine, cosine, and tangent', 'Hard', 3),
(4, 'Statistics & Probability', 'Data analysis and chance', 'Medium', 4);

-- Insert default animations
INSERT INTO animations (subject_id, topic_id, name, type, data, description) VALUES
(1, 1, 'Projectile Motion', 'Physics', '{"type": "projectile", "initial_velocity": 20, "angle": 45}', 'Interactive projectile motion simulation'),
(1, 1, 'Newton''s Laws', 'Physics', '{"type": "newton_laws", "mass": 5, "force": 10}', 'Demonstration of Newton''s three laws'),
(2, 5, 'Atomic Structure', 'Chemistry', '{"type": "atomic", "element": "Hydrogen", "electrons": 1}', '3D atomic structure visualization'),
(2, 6, 'Chemical Bonding', 'Chemistry', '{"type": "bonding", "molecule": "H2O", "bonds": 2}', 'Molecular bonding animation'),
(3, 9, 'Cell Division', 'Biology', '{"type": "mitosis", "stages": 4}', 'Cell division process animation'),
(3, 10, 'DNA Structure', 'Biology', '{"type": "dna", "base_pairs": 10}', 'DNA double helix structure'),
(4, 13, 'Quadratic Functions', 'Mathematics', '{"type": "quadratic", "a": 1, "b": -3, "c": 2}', 'Graphing quadratic functions'),
(4, 14, 'Circle Properties', 'Mathematics', '{"type": "circle", "radius": 5, "center": [0,0]}', 'Circle geometry visualization');

-- Insert sample practice problems
INSERT INTO practice_problems (subject_id, topic_id, question, options, correct_answer, explanation, difficulty, points) VALUES
(1, 1, 'What is the unit of force?', '["Newton", "Joule", "Watt", "Pascal"]', 0, 'Force is measured in Newtons (N)', 'Easy', 1),
(1, 1, 'A car accelerates from 0 to 60 km/h in 10 seconds. What is its acceleration?', '["6 m/s²", "1.67 m/s²", "60 m/s²", "10 m/s²"]', 1, 'Acceleration = (60/3.6)/10 = 1.67 m/s²', 'Medium', 2),
(2, 5, 'What is the atomic number of Hydrogen?', '["1", "2", "0", "3"]', 0, 'Hydrogen has atomic number 1', 'Easy', 1),
(2, 5, 'What is the chemical formula of water?', '["H2O", "H2O2", "HO", "H3O"]', 0, 'Water is H2O - two hydrogen atoms and one oxygen atom', 'Easy', 1),
(3, 9, 'What is the powerhouse of the cell?', '["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"]', 1, 'Mitochondria produces ATP, the energy currency of the cell', 'Medium', 2),
(4, 13, 'What is the solution to x² - 5x + 6 = 0?', '["x = 2, 3", "x = 1, 6", "x = -2, -3", "x = 0, 5"]', 0, 'Factor: (x-2)(x-3) = 0, so x = 2 or x = 3', 'Medium', 2);

-- Insert sample videos
INSERT INTO videos (subject_id, topic_id, title, description, duration, level) VALUES
(1, 1, 'Introduction to Motion', 'Basic concepts of motion and velocity', 15, 'Beginner'),
(1, 1, 'Newton''s Laws Explained', 'Detailed explanation of Newton''s three laws', 25, 'Intermediate'),
(1, 1, 'Energy and Work', 'Understanding energy conservation and work', 30, 'Advanced'),
(2, 5, 'Atomic Structure Basics', 'Introduction to atomic structure', 20, 'Beginner'),
(2, 5, 'Electron Configuration', 'How electrons are arranged in atoms', 25, 'Intermediate'),
(3, 9, 'Cell Structure and Function', 'Overview of cell organelles', 25, 'Beginner'),
(3, 9, 'DNA and Genetics', 'Introduction to genetics and DNA', 30, 'Intermediate'),
(4, 13, 'Algebra Fundamentals', 'Basic algebraic concepts', 20, 'Beginner'),
(4, 13, 'Quadratic Equations', 'Solving quadratic equations', 35, 'Intermediate');

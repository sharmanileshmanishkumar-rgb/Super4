// EduMate Subject Content and API Integration
class SubjectContentManager {
    constructor() {
        this.apiBaseUrl = 'http://localhost:5000/api';
        this.externalApis = {
            khanAcademy: 'https://www.khanacademy.org/api/v1/',
            geeksForGeeks: 'https://www.geeksforgeeks.org/api/',
            openAI: 'https://api.openai.com/v1/',
            youtube: 'https://www.googleapis.com/youtube/v3/'
        };
    }

    // 6-10 Standards Content
    getStandards610Content() {
        return {
            physics: {
                title: "Physics - 6-10 Standards",
                topics: [
                    {
                        name: "Mechanics",
                        subtopics: ["Motion", "Forces", "Energy", "Momentum"],
                        apiContent: this.getPhysicsMechanicsContent()
                    },
                    {
                        name: "Thermodynamics", 
                        subtopics: ["Heat", "Temperature", "Laws of Thermodynamics"],
                        apiContent: this.getThermodynamicsContent()
                    },
                    {
                        name: "Waves & Sound",
                        subtopics: ["Wave Properties", "Sound Waves", "Light Waves"],
                        apiContent: this.getWavesContent()
                    },
                    {
                        name: "Electricity & Magnetism",
                        subtopics: ["Electric Fields", "Magnetic Fields", "Circuits"],
                        apiContent: this.getElectricityContent()
                    }
                ],
                resources: [
                    "Interactive simulations",
                    "Video explanations", 
                    "Practice problems",
                    "Virtual labs"
                ]
            },
            chemistry: {
                title: "Chemistry - 6-10 Standards",
                topics: [
                    {
                        name: "Atomic Structure",
                        subtopics: ["Atoms", "Electrons", "Periodic Table"],
                        apiContent: this.getAtomicStructureContent()
                    },
                    {
                        name: "Chemical Bonding",
                        subtopics: ["Ionic Bonds", "Covalent Bonds", "Metallic Bonds"],
                        apiContent: this.getChemicalBondingContent()
                    },
                    {
                        name: "Chemical Reactions",
                        subtopics: ["Balancing Equations", "Types of Reactions", "Stoichiometry"],
                        apiContent: this.getChemicalReactionsContent()
                    },
                    {
                        name: "Acids & Bases",
                        subtopics: ["pH Scale", "Neutralization", "Indicators"],
                        apiContent: this.getAcidsBasesContent()
                    }
                ],
                resources: [
                    "Molecular visualizations",
                    "Chemical equation balancer",
                    "Virtual chemistry lab",
                    "Interactive periodic table"
                ]
            },
            biology: {
                title: "Biology - 6-10 Standards", 
                topics: [
                    {
                        name: "Cell Biology",
                        subtopics: ["Cell Structure", "Cell Division", "Cell Transport"],
                        apiContent: this.getCellBiologyContent()
                    },
                    {
                        name: "Genetics",
                        subtopics: ["DNA", "Genes", "Heredity", "Evolution"],
                        apiContent: this.getGeneticsContent()
                    },
                    {
                        name: "Ecology",
                        subtopics: ["Ecosystems", "Food Chains", "Biodiversity"],
                        apiContent: this.getEcologyContent()
                    },
                    {
                        name: "Human Body",
                        subtopics: ["Organ Systems", "Digestion", "Respiration", "Circulation"],
                        apiContent: this.getHumanBodyContent()
                    }
                ],
                resources: [
                    "3D cell models",
                    "DNA structure viewer",
                    "Ecosystem simulations",
                    "Anatomy visualizations"
                ]
            },
            mathematics: {
                title: "Mathematics - 6-10 Standards",
                topics: [
                    {
                        name: "Algebra",
                        subtopics: ["Linear Equations", "Quadratic Equations", "Polynomials"],
                        apiContent: this.getAlgebraContent()
                    },
                    {
                        name: "Geometry",
                        subtopics: ["Shapes", "Angles", "Area & Perimeter", "Volume"],
                        apiContent: this.getGeometryContent()
                    },
                    {
                        name: "Trigonometry",
                        subtopics: ["Sine, Cosine, Tangent", "Unit Circle", "Identities"],
                        apiContent: this.getTrigonometryContent()
                    },
                    {
                        name: "Statistics & Probability",
                        subtopics: ["Mean, Median, Mode", "Probability", "Data Analysis"],
                        apiContent: this.getStatisticsContent()
                    }
                ],
                resources: [
                    "Graphing calculator",
                    "Geometric constructions",
                    "Statistical tools",
                    "Problem-solving guides"
                ]
            }
        };
    }

    // JEE Preparation Content
    getJEEContent() {
        return {
            jeePhysics: {
                title: "JEE Physics Preparation",
                topics: [
                    {
                        name: "Mechanics",
                        subtopics: ["Kinematics", "Dynamics", "Work & Energy", "Rotational Motion"],
                        difficulty: "Advanced",
                        apiContent: this.getJEEMechanicsContent()
                    },
                    {
                        name: "Thermodynamics",
                        subtopics: ["Heat Transfer", "Laws of Thermodynamics", "Kinetic Theory"],
                        difficulty: "Advanced", 
                        apiContent: this.getJEEThermodynamicsContent()
                    },
                    {
                        name: "Electromagnetism",
                        subtopics: ["Electric Fields", "Magnetic Fields", "Electromagnetic Induction"],
                        difficulty: "Advanced",
                        apiContent: this.getJEEElectromagnetismContent()
                    },
                    {
                        name: "Modern Physics",
                        subtopics: ["Quantum Mechanics", "Nuclear Physics", "Particle Physics"],
                        difficulty: "Advanced",
                        apiContent: this.getJEEModernPhysicsContent()
                    }
                ],
                resources: [
                    "Previous year papers",
                    "Mock tests",
                    "Video solutions",
                    "Conceptual animations"
                ]
            },
            jeeChemistry: {
                title: "JEE Chemistry Preparation",
                topics: [
                    {
                        name: "Physical Chemistry",
                        subtopics: ["Atomic Structure", "Chemical Bonding", "Thermodynamics"],
                        difficulty: "Advanced",
                        apiContent: this.getJEEPhysicalChemistryContent()
                    },
                    {
                        name: "Organic Chemistry",
                        subtopics: ["Reaction Mechanisms", "Functional Groups", "Stereochemistry"],
                        difficulty: "Advanced",
                        apiContent: this.getJEEOrganicChemistryContent()
                    },
                    {
                        name: "Inorganic Chemistry", 
                        subtopics: ["Periodic Properties", "Coordination Compounds", "Metallurgy"],
                        difficulty: "Advanced",
                        apiContent: this.getJEEInorganicChemistryContent()
                    }
                ],
                resources: [
                    "Reaction mechanism animations",
                    "Molecular modeling",
                    "Practice problems",
                    "Concept videos"
                ]
            },
            jeeMathematics: {
                title: "JEE Mathematics Preparation",
                topics: [
                    {
                        name: "Calculus",
                        subtopics: ["Limits", "Derivatives", "Integrals", "Differential Equations"],
                        difficulty: "Advanced",
                        apiContent: this.getJEECalculusContent()
                    },
                    {
                        name: "Algebra",
                        subtopics: ["Complex Numbers", "Matrices", "Determinants", "Sequences"],
                        difficulty: "Advanced",
                        apiContent: this.getJEEAlgebraContent()
                    },
                    {
                        name: "Coordinate Geometry",
                        subtopics: ["Straight Lines", "Circles", "Conic Sections", "3D Geometry"],
                        difficulty: "Advanced",
                        apiContent: this.getJEECoordinateGeometryContent()
                    }
                ],
                resources: [
                    "Graphing tools",
                    "Step-by-step solutions",
                    "Practice tests",
                    "Video tutorials"
                ]
            }
        };
    }

    // Engineering Content
    getEngineeringContent() {
        return {
            computerScience: {
                title: "Computer Science Engineering",
                branches: {
                    core: {
                        name: "Core CS Subjects",
                        subjects: [
                            {
                                name: "Data Structures & Algorithms",
                                topics: ["Arrays", "Linked Lists", "Trees", "Graphs", "Sorting", "Searching"],
                                apiContent: this.getDataStructuresContent(),
                                resources: ["Visualizations", "Code examples", "Practice problems"]
                            },
                            {
                                name: "Computer Networks",
                                topics: ["OSI Model", "TCP/IP", "Routing", "Security"],
                                apiContent: this.getNetworksContent(),
                                resources: ["Network simulators", "Protocol analyzers", "Security tools"]
                            },
                            {
                                name: "Database Management Systems",
                                topics: ["SQL", "Normalization", "Transactions", "Indexing"],
                                apiContent: this.getDatabaseContent(),
                                resources: ["Database design tools", "Query builders", "Performance analyzers"]
                            },
                            {
                                name: "Operating Systems",
                                topics: ["Process Management", "Memory Management", "File Systems", "Scheduling"],
                                apiContent: this.getOperatingSystemsContent(),
                                resources: ["OS simulators", "Process visualizers", "Memory management tools"]
                            }
                        ]
                    },
                    advanced: {
                        name: "Advanced CS Subjects",
                        subjects: [
                            {
                                name: "Machine Learning",
                                topics: ["Supervised Learning", "Unsupervised Learning", "Neural Networks", "Deep Learning"],
                                apiContent: this.getMachineLearningContent(),
                                resources: ["ML frameworks", "Dataset tools", "Model visualizers"]
                            },
                            {
                                name: "Artificial Intelligence",
                                topics: ["Search Algorithms", "Knowledge Representation", "Expert Systems", "Natural Language Processing"],
                                apiContent: this.getAIContent(),
                                resources: ["AI simulators", "NLP tools", "Expert system builders"]
                            },
                            {
                                name: "Web Development",
                                topics: ["HTML/CSS", "JavaScript", "React", "Node.js", "Databases"],
                                apiContent: this.getWebDevelopmentContent(),
                                resources: ["Code editors", "Frameworks", "Testing tools"]
                            },
                            {
                                name: "Software Engineering",
                                topics: ["SDLC", "Design Patterns", "Testing", "Project Management"],
                                apiContent: this.getSoftwareEngineeringContent(),
                                resources: ["Project management tools", "Version control", "Testing frameworks"]
                            }
                        ]
                    }
                }
            },
            informationTechnology: {
                title: "Information Technology",
                branches: {
                    core: {
                        name: "Core IT Subjects",
                        subjects: [
                            {
                                name: "Information Systems",
                                topics: ["System Analysis", "Database Design", "Business Processes", "ERP Systems"],
                                apiContent: this.getInformationSystemsContent(),
                                resources: ["System modeling tools", "Database designers", "Process mappers"]
                            },
                            {
                                name: "Cybersecurity",
                                topics: ["Network Security", "Cryptography", "Ethical Hacking", "Risk Management"],
                                apiContent: this.getCybersecurityContent(),
                                resources: ["Security testing tools", "Cryptography simulators", "Vulnerability scanners"]
                            },
                            {
                                name: "Cloud Computing",
                                topics: ["AWS", "Azure", "Docker", "Kubernetes", "Microservices"],
                                apiContent: this.getCloudComputingContent(),
                                resources: ["Cloud platforms", "Container tools", "Monitoring systems"]
                            },
                            {
                                name: "Data Analytics",
                                topics: ["Data Mining", "Big Data", "Business Intelligence", "Data Visualization"],
                                apiContent: this.getDataAnalyticsContent(),
                                resources: ["Analytics platforms", "Visualization tools", "Data processing frameworks"]
                            }
                        ]
                    },
                    advanced: {
                        name: "Advanced IT Subjects",
                        subjects: [
                            {
                                name: "IT Project Management",
                                topics: ["Agile", "Scrum", "Risk Management", "Quality Assurance"],
                                apiContent: this.getITProjectManagementContent(),
                                resources: ["Project management tools", "Agile frameworks", "Quality metrics"]
                            },
                            {
                                name: "System Administration",
                                topics: ["Linux", "Windows Server", "Network Administration", "Server Management"],
                                apiContent: this.getSystemAdministrationContent(),
                                resources: ["Server management tools", "Network monitors", "System utilities"]
                            },
                            {
                                name: "Mobile App Development",
                                topics: ["Android", "iOS", "React Native", "Flutter", "App Store"],
                                apiContent: this.getMobileDevelopmentContent(),
                                resources: ["Mobile IDEs", "Emulators", "Testing frameworks"]
                            },
                            {
                                name: "DevOps",
                                topics: ["CI/CD", "Jenkins", "Git", "Infrastructure as Code", "Monitoring"],
                                apiContent: this.getDevOpsContent(),
                                resources: ["CI/CD tools", "Version control", "Monitoring systems"]
                            }
                        ]
                    }
                }
            }
        };
    }

    // API Content Methods
    async getPhysicsMechanicsContent() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/content/6-10/physics`);
            const data = await response.json();
            return {
                videos: data.topics?.[0]?.videos || [],
                simulations: data.topics?.[0]?.simulations || [],
                problems: data.topics?.[0]?.problems || []
            };
        } catch (error) {
            console.error('Error fetching physics content:', error);
            return this.getDefaultPhysicsContent();
        }
    }

    async getDataStructuresContent() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/content/Engineering/computer-science`);
            const data = await response.json();
            return {
                articles: data.branches?.core?.subjects?.[0]?.code_examples || [],
                codeExamples: data.branches?.core?.subjects?.[0]?.code_examples || [],
                visualizations: data.branches?.core?.subjects?.[0]?.visualizations || []
            };
        } catch (error) {
            console.error('Error fetching data structures content:', error);
            return this.getDefaultDataStructuresContent();
        }
    }

    async getMachineLearningContent() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/openai/explain`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'machine_learning' })
            });
            const data = await response.json();
            return {
                explanation: data.explanation,
                examples: data.examples || [],
                resources: await this.getMLResources()
            };
        } catch (error) {
            return this.getDefaultMLContent();
        }
    }

    // Default content when APIs are not available
    getDefaultPhysicsContent() {
        return {
            videos: [
                { title: "Introduction to Motion", duration: "15 min", level: "Beginner" },
                { title: "Newton's Laws", duration: "20 min", level: "Intermediate" },
                { title: "Energy and Work", duration: "25 min", level: "Advanced" }
            ],
            simulations: [
                { name: "Projectile Motion Simulator", description: "Interactive projectile motion" },
                { name: "Pendulum Simulator", description: "Simple harmonic motion" }
            ],
            problems: [
                { type: "Kinematics", difficulty: "Easy", count: 15 },
                { type: "Dynamics", difficulty: "Medium", count: 20 },
                { type: "Energy", difficulty: "Hard", count: 10 }
            ]
            ]
        };
    }

    getDefaultDataStructuresContent() {
        return {
            articles: [
                { title: "Arrays - Complete Guide", readTime: "10 min", difficulty: "Beginner" },
                { title: "Linked Lists Explained", readTime: "15 min", difficulty: "Intermediate" },
                { title: "Tree Traversal Algorithms", readTime: "20 min", difficulty: "Advanced" }
            ],
            codeExamples: [
                { language: "Python", topic: "Stack Implementation", lines: 25 },
                { language: "Java", topic: "Binary Tree", lines: 40 },
                { language: "C++", topic: "Graph Algorithms", lines: 60 }
            ],
            visualizations: [
                { name: "Array Operations", type: "Interactive" },
                { name: "Tree Visualization", type: "Animated" },
                { name: "Graph Traversal", type: "Step-by-step" }
            ]
        };
    }

    getDefaultMLContent() {
        return {
            explanation: "Machine Learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed. It involves algorithms that can identify patterns in data and make predictions or classifications.",
            examples: [
                "Email spam detection using Naive Bayes",
                "Image recognition using Convolutional Neural Networks",
                "Stock price prediction using LSTM networks"
            ],
            resources: [
                "TensorFlow tutorials",
                "Scikit-learn documentation", 
                "Kaggle datasets",
                "Jupyter notebooks"
            ]
        };
    }

    // Additional helper methods for content generation
    async getPhysicsSimulations(topic) {
        return [
            { name: `${topic} Interactive Lab`, url: "#", description: "Hands-on simulation" },
            { name: `${topic} Virtual Experiment`, url: "#", description: "Virtual laboratory" }
        ];
    }

    async getPracticeProblems(subject, topic) {
        return [
            { difficulty: "Easy", count: 20, time: "30 min" },
            { difficulty: "Medium", count: 15, time: "45 min" },
            { difficulty: "Hard", count: 10, time: "60 min" }
        ];
    }

    async getCodeExamples(topic) {
        return [
            { language: "Python", complexity: "Basic" },
            { language: "Java", complexity: "Intermediate" },
            { language: "C++", complexity: "Advanced" }
        ];
    }

    async getDataStructureVisualizations() {
        return [
            { name: "Array Operations", type: "Interactive" },
            { name: "Tree Traversal", type: "Animated" },
            { name: "Graph Algorithms", type: "Step-by-step" }
        ];
    }

    async getMLResources() {
        return [
            "TensorFlow Playground",
            "Scikit-learn Tutorials",
            "Kaggle Learning",
            "Fast.ai Course"
        ];
    }

    // Content for all subjects (abbreviated for space)
    getAtomicStructureContent() { return this.getDefaultPhysicsContent(); }
    getChemicalBondingContent() { return this.getDefaultPhysicsContent(); }
    getChemicalReactionsContent() { return this.getDefaultPhysicsContent(); }
    getAcidsBasesContent() { return this.getDefaultPhysicsContent(); }
    getCellBiologyContent() { return this.getDefaultPhysicsContent(); }
    getGeneticsContent() { return this.getDefaultPhysicsContent(); }
    getEcologyContent() { return this.getDefaultPhysicsContent(); }
    getHumanBodyContent() { return this.getDefaultPhysicsContent(); }
    getAlgebraContent() { return this.getDefaultPhysicsContent(); }
    getGeometryContent() { return this.getDefaultPhysicsContent(); }
    getTrigonometryContent() { return this.getDefaultPhysicsContent(); }
    getStatisticsContent() { return this.getDefaultPhysicsContent(); }
    
    // JEE Content methods
    getJEEMechanicsContent() { return this.getDefaultPhysicsContent(); }
    getJEEThermodynamicsContent() { return this.getDefaultPhysicsContent(); }
    getJEEElectromagnetismContent() { return this.getDefaultPhysicsContent(); }
    getJEEModernPhysicsContent() { return this.getDefaultPhysicsContent(); }
    getJEEPhysicalChemistryContent() { return this.getDefaultPhysicsContent(); }
    getJEEOrganicChemistryContent() { return this.getDefaultPhysicsContent(); }
    getJEEInorganicChemistryContent() { return this.getDefaultPhysicsContent(); }
    getJEECalculusContent() { return this.getDefaultPhysicsContent(); }
    getJEEAlgebraContent() { return this.getDefaultPhysicsContent(); }
    getJEECoordinateGeometryContent() { return this.getDefaultPhysicsContent(); }
    
    // Engineering Content methods
    getNetworksContent() { return this.getDefaultDataStructuresContent(); }
    getDatabaseContent() { return this.getDefaultDataStructuresContent(); }
    getOperatingSystemsContent() { return this.getDefaultDataStructuresContent(); }
    getAIContent() { return this.getDefaultMLContent(); }
    getWebDevelopmentContent() { return this.getDefaultDataStructuresContent(); }
    getSoftwareEngineeringContent() { return this.getDefaultDataStructuresContent(); }
    getInformationSystemsContent() { return this.getDefaultDataStructuresContent(); }
    getCybersecurityContent() { return this.getDefaultDataStructuresContent(); }
    getCloudComputingContent() { return this.getDefaultDataStructuresContent(); }
    getDataAnalyticsContent() { return this.getDefaultMLContent(); }
    getITProjectManagementContent() { return this.getDefaultDataStructuresContent(); }
    getSystemAdministrationContent() { return this.getDefaultDataStructuresContent(); }
    getMobileDevelopmentContent() { return this.getDefaultDataStructuresContent(); }
    getDevOpsContent() { return this.getDefaultDataStructuresContent(); }
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SubjectContentManager;
}

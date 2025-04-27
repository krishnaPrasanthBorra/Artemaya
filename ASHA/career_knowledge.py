"""
Career Knowledge Module for ASHA AI
This module provides structured career knowledge to enhance ASHA's responses.
"""

# Career resources by stage
CAREER_RESOURCES = {
    "Starter": {
        "networking": [
            {
                "name": "LinkedIn Learning - Networking Strategies",
                "description": "Learn effective networking techniques for early-career professionals",
                "type": "course"
            },
            {
                "name": "Women in Tech Global Network",
                "description": "A global community supporting women entering technology fields",
                "type": "community"
            },
            {
                "name": "LeanIn Circles",
                "description": "Peer mentoring groups focused on supporting women in various career stages",
                "type": "community"
            }
        ],
        "skill_building": [
            {
                "name": "Coursera",
                "description": "Free and paid courses on in-demand skills across industries",
                "type": "platform"
            },
            {
                "name": "Skillshare",
                "description": "Creative and business skills with a focus on practical applications",
                "type": "platform"
            },
            {
                "name": "HackerRank",
                "description": "Technical skill practice for those pursuing tech careers",
                "type": "practice"
            }
        ],
        "job_search": [
            {
                "name": "Indeed",
                "description": "Comprehensive job search platform with entry-level options",
                "type": "platform"
            },
            {
                "name": "Glassdoor",
                "description": "Job listings with company reviews and salary information",
                "type": "platform"
            },
            {
                "name": "Handshake",
                "description": "Platform connecting students and recent graduates with employers",
                "type": "platform"
            }
        ]
    },
    "Restarter": {
        "networking": [
            {
                "name": "Women Returners Network",
                "description": "Specialized network for women returning to work after career breaks",
                "type": "community"
            },
            {
                "name": "iRelaunch",
                "description": "Resources and events specifically for career relaunchers",
                "type": "platform"
            },
            {
                "name": "Mom Project",
                "description": "Platform connecting women with flexible work opportunities after breaks",
                "type": "platform"
            }
        ],
        "skill_building": [
            {
                "name": "Google Digital Garage",
                "description": "Free digital skills courses to update tech knowledge",
                "type": "platform"
            },
            {
                "name": "LinkedIn Learning - Returning to Work",
                "description": "Courses focused on skills and confidence for career returners",
                "type": "course"
            },
            {
                "name": "Path Forward",
                "description": "Return-to-work programs and resources",
                "type": "program"
            }
        ],
        "job_search": [
            {
                "name": "FlexJobs",
                "description": "Curated flexible, remote, and part-time job opportunities",
                "type": "platform"
            },
            {
                "name": "PowerToFly",
                "description": "Job platform connecting women with companies committed to diversity",
                "type": "platform"
            },
            {
                "name": "Après",
                "description": "Job marketplace specifically for women returning to the workforce",
                "type": "platform"
            }
        ]
    },
    "Riser": {
        "networking": [
            {
                "name": "Ellevate Network",
                "description": "Professional network for women leaders at all levels",
                "type": "community"
            },
            {
                "name": "Chief",
                "description": "Private network designed for women executives",
                "type": "community"
            },
            {
                "name": "Athena Alliance",
                "description": "Community preparing women for board positions and executive leadership",
                "type": "community"
            }
        ],
        "skill_building": [
            {
                "name": "Harvard Business School Online",
                "description": "Advanced business and leadership courses from top institutions",
                "type": "platform"
            },
            {
                "name": "MasterClass",
                "description": "Leadership and business courses taught by industry leaders",
                "type": "platform"
            },
            {
                "name": "edX Executive Education",
                "description": "Executive-level courses from leading universities",
                "type": "platform"
            }
        ],
        "leadership": [
            {
                "name": "Women's Leadership Forum",
                "description": "Events and resources for women in leadership positions",
                "type": "community"
            },
            {
                "name": "Harvard Business Review",
                "description": "Research-based articles on leadership and management",
                "type": "resource"
            },
            {
                "name": "Fast Company Women's Leadership",
                "description": "Articles and insights on women's leadership challenges and opportunities",
                "type": "resource"
            }
        ]
    }
}

# Industry-specific insights
INDUSTRY_INSIGHTS = {
    "technology": {
        "trends": [
            "AI and machine learning continue to transform roles across the tech industry",
            "Remote work has become permanently established in most tech companies",
            "Increased focus on cybersecurity skills across all tech roles",
            "Growing importance of data analytics capabilities"
        ],
        "challenges_for_women": [
            "Gender gap in technical roles, particularly in engineering and leadership",
            "Work-life balance in an industry known for intense work schedules",
            "Building confidence in male-dominated environments",
            "Finding supportive mentors and sponsors"
        ],
        "opportunities": [
            "Strong demand for diverse perspectives in product development",
            "Growing number of women-focused tech communities and scholarships",
            "Flexible work arrangements becoming more common",
            "Expanding technical roles in traditionally non-technical industries"
        ]
    },
    "healthcare": {
        "trends": [
            "Telehealth expansion creating new roles and skills needs",
            "Growing intersection of healthcare and technology",
            "Increasing focus on preventative care and wellness",
            "Rising importance of data privacy and security knowledge"
        ],
        "challenges_for_women": [
            "Gender gaps in leadership despite women forming majority of workforce",
            "Managing demanding schedules with personal responsibilities",
            "Navigating specialized career paths while balancing life commitments",
            "Addressing compensation disparities in specialized roles"
        ],
        "opportunities": [
            "Expanding roles in health technology and informatics",
            "Growing demand for healthcare management and administration",
            "Increased recognition of the value of emotional intelligence in patient care",
            "New specializations emerging at the intersection of healthcare and other fields"
        ]
    },
    "finance": {
        "trends": [
            "Fintech innovation creating new career paths",
            "Increasing importance of data analysis skills",
            "Growing focus on ESG (Environmental, Social, Governance) expertise",
            "Automation changing the nature of traditional finance roles"
        ],
        "challenges_for_women": [
            "Persistent underrepresentation in senior leadership",
            "Navigating historically male-dominated culture",
            "Balancing demanding workloads with personal responsibilities",
            "Building confidence in high-pressure environments"
        ],
        "opportunities": [
            "Expanding roles in sustainable and ethical finance",
            "Growing demand for financial technology expertise",
            "Increasing focus on diverse perspectives in investment decisions",
            "Rising importance of client relationship skills as technical tasks automate"
        ]
    },
    "education": {
        "trends": [
            "Expanding EdTech sector creating new career paths",
            "Growing demand for digital teaching skills",
            "Increasing focus on personalized learning approaches",
            "Rising importance of social-emotional learning expertise"
        ],
        "challenges_for_women": [
            "Gender gaps in educational leadership despite female-dominated profession",
            "Balancing demanding workloads with personal responsibilities",
            "Addressing compensation concerns in traditionally undervalued profession",
            "Navigating complex institutional structures for career advancement"
        ],
        "opportunities": [
            "Expanding roles in educational technology and curriculum design",
            "Growing focus on specialized instructional approaches",
            "Increasing value placed on social-emotional teaching skills",
            "New career paths in corporate learning and development"
        ]
    },
    "creative": {
        "trends": [
            "Digital transformation creating new types of creative roles",
            "Growing importance of multi-platform content creation skills",
            "Increasing client demand for data-informed creative work",
            "Rising opportunities in virtual and augmented reality"
        ],
        "challenges_for_women": [
            "Navigating subjective feedback and recognition",
            "Building sustainable freelance or entrepreneurial practices",
            "Balancing creative integrity with market demands",
            "Finding mentorship in diverse creative fields"
        ],
        "opportunities": [
            "Expanding roles at the intersection of creativity and technology",
            "Growing demand for authentic, diverse perspectives",
            "Increasing options for remote and flexible creative work",
            "Rising value of creative problem-solving in non-traditional industries"
        ]
    }
}

# Career stage transition guidance
CAREER_TRANSITIONS = {
    "Starter_to_Riser": [
        "Seek opportunities to lead small projects or task forces",
        "Build expertise in a specific area to become a go-to resource",
        "Develop mentoring relationships with more senior colleagues",
        "Begin building your personal brand through thought leadership",
        "Take on stretch assignments that test your leadership capabilities"
    ],
    "Restarter_to_Riser": [
        "Leverage unique perspectives gained during your career break",
        "Connect your previous experience to current industry challenges",
        "Seek opportunities to demonstrate leadership early in your return",
        "Build a strategic network across different departments",
        "Identify and fill knowledge gaps through targeted learning"
    ]
}

# Common career challenges and solutions
CAREER_CHALLENGES = {
    "imposter_syndrome": {
        "description": "Feeling like you don't deserve your accomplishments and might be 'found out'",
        "strategies": [
            "Document your achievements and review them regularly",
            "Recognize that imposter feelings are common among high-achievers",
            "Focus on the value you provide rather than on being 'perfect'",
            "Seek feedback regularly to gain objective perspective on your work",
            "Find a supportive community where you can discuss these feelings"
        ]
    },
    "work_life_balance": {
        "description": "Struggling to maintain boundaries between professional and personal life",
        "strategies": [
            "Set clear boundaries around working hours and communication",
            "Practice prioritization based on both impact and urgency",
            "Build in regular 'recovery' time to prevent burnout",
            "Use technology tools to automate routine tasks",
            "Negotiate flexibility where possible to accommodate life needs"
        ]
    },
    "salary_negotiation": {
        "description": "Difficulty advocating for fair compensation and benefits",
        "strategies": [
            "Research industry standards for your role, experience, and location",
            "Document your contributions and their business impact",
            "Practice negotiation conversations with trusted colleagues",
            "Consider the full compensation package, not just base salary",
            "Approach as collaborative problem-solving rather than confrontation"
        ]
    },
    "career_pivot": {
        "description": "Changing to a new industry or role type while leveraging existing skills",
        "strategies": [
            "Identify transferable skills relevant to your target field",
            "Conduct informational interviews with people in your target roles",
            "Develop bridge experiences through volunteering or side projects",
            "Create a narrative that connects your past experience to future goals",
            "Consider specialized courses or certifications to build credibility"
        ]
    },
    "visibility": {
        "description": "Ensuring your contributions are recognized, especially in remote environments",
        "strategies": [
            "Document and share wins and progress with key stakeholders",
            "Seek speaking opportunities in meetings and professional events",
            "Develop thought leadership through writing or presentations",
            "Build relationships with leaders outside your immediate team",
            "Find sponsors who will advocate for you when you're not in the room"
        ]
    },
    "managing_up": {
        "description": "Effectively communicating with and supporting your manager",
        "strategies": [
            "Understand your manager's priorities, preferences and communication style",
            "Provide solutions, not just problems when raising issues",
            "Proactively share progress and ask for feedback",
            "Help your manager look good to their leadership",
            "Learn to frame requests in terms of business outcomes"
        ]
    }
}

# Resume and interview guidance
CAREER_DOCUMENTS = {
    "resume_tips": [
        "Focus on achievements and impact rather than just responsibilities",
        "Quantify results wherever possible (percentages, metrics, etc.)",
        "Tailor your resume for each significant application",
        "Use strong action verbs to begin bullet points",
        "Include relevant keywords from the job description",
        "Ensure a clean, consistent formatting throughout",
        "Keep to 1-2 pages maximum depending on experience level"
    ],
    "cover_letter_tips": [
        "Address a specific person whenever possible",
        "Show how your experience directly relates to their needs",
        "Demonstrate knowledge of the company and its challenges",
        "Tell a compelling story about why you're the right fit",
        "Keep it concise - typically under one page",
        "End with a clear call to action"
    ],
    "interview_preparation": [
        "Research the company, its products, culture, and recent news",
        "Prepare specific examples using the STAR method (Situation, Task, Action, Result)",
        "Practice answering common questions aloud",
        "Prepare thoughtful questions that demonstrate your interest",
        "Plan your interview outfit and logistics in advance",
        "Follow up with a thank-you note highlighting key discussion points"
    ],
    "salary_negotiation_tips": [
        "Research typical compensation ranges before discussions",
        "Consider the full package (benefits, flexibility, growth opportunities)",
        "Practice your negotiation language to sound confident",
        "Focus on your value to the company, not personal needs",
        "Be prepared with specific achievements that justify your ask",
        "Consider multiple negotiation scenarios and your responses"
    ]
}

# Inspiring women leaders by field
INSPIRING_LEADERS = {
    "technology": [
        {
            "name": "Reshma Saujani",
            "role": "Founder of Girls Who Code",
            "known_for": "Addressing the gender gap in technology through education and advocacy"
        },
        {
            "name": "Whitney Wolfe Herd",
            "role": "Founder and CEO of Bumble",
            "known_for": "Creating a women-centric social connection platform and becoming the youngest female CEO to take a company public"
        },
        {
            "name": "Fei-Fei Li",
            "role": "Professor and Co-Director of Stanford's Human-Centered AI Institute",
            "known_for": "Pioneering work in AI and computer vision, and advocacy for inclusive AI"
        }
    ],
    "business": [
        {
            "name": "Indra Nooyi",
            "role": "Former CEO of PepsiCo",
            "known_for": "Strategic transformation of PepsiCo and advocacy for sustainable business practices"
        },
        {
            "name": "Sara Blakely",
            "role": "Founder of Spanx",
            "known_for": "Building a billion-dollar company from scratch and her commitment to supporting women entrepreneurs"
        },
        {
            "name": "Ursula Burns",
            "role": "Former CEO of Xerox",
            "known_for": "First Black woman to serve as CEO of a Fortune 500 company and leadership in digital transformation"
        }
    ],
    "science": [
        {
            "name": "Jennifer Doudna",
            "role": "Biochemist and Nobel Prize Winner",
            "known_for": "Co-invention of CRISPR gene editing technology"
        },
        {
            "name": "Jane Goodall",
            "role": "Primatologist and Anthropologist",
            "known_for": "Groundbreaking research on chimpanzees and environmental conservation"
        },
        {
            "name": "Frances Arnold",
            "role": "Chemical Engineer and Nobel Prize Winner",
            "known_for": "Pioneering 'directed evolution' to create enzymes for environmentally-friendly chemical products"
        }
    ]
} 
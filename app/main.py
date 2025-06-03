"""
AI Engineer Portfolio - Main Application Module

This module defines the main pages and components of the AI Engineer Portfolio application.
"""
import sys
import codecs
from typing import List, Dict, Any, Optional
from nicegui import ui, app
from pathlib import Path
import asyncio

# Force UTF-8 encoding for reliability
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Import asset manager
from app.core.assets import AssetManager

# Ensure static directory exists
static_dir = Path(__file__).parent / 'static'
static_dir.mkdir(exist_ok=True)
css_dir = static_dir / 'css'
css_dir.mkdir(exist_ok=True)

# Add static files directory to NiceGUI
app.add_static_files('/static', str(static_dir))

# Portfolio data
PORTFOLIO_DATA = {
    "personal_info": {
        "name": "Alex Morgan",
        "title": "AI Engineer & Machine Learning Specialist",
        "bio": "Passionate AI Engineer with 5+ years of experience developing cutting-edge machine learning solutions. Specialized in computer vision, NLP, and reinforcement learning with a focus on production-ready AI systems.",
        "location": "San Francisco, CA",
        "email": "alex@aiportfolio.com",
        "phone": "+1 (555) 123-4567",
        "website": "www.aiportfolio.com",
        "social": {
            "github": "github.com/alexmorgan-ai",
            "linkedin": "linkedin.com/in/alexmorgan-ai",
            "twitter": "twitter.com/alexmorgan_ai",
            "medium": "medium.com/@alexmorgan-ai"
        }
    },
    "skills": [
        {"name": "Machine Learning", "level": 95, "icon": "🧠"},
        {"name": "Deep Learning", "level": 90, "icon": "🔮"},
        {"name": "Computer Vision", "level": 85, "icon": "👁️"},
        {"name": "Natural Language Processing", "level": 90, "icon": "💬"},
        {"name": "Reinforcement Learning", "level": 80, "icon": "🎮"},
        {"name": "MLOps", "level": 85, "icon": "⚙️"},
        {"name": "Python", "level": 95, "icon": "🐍"},
        {"name": "TensorFlow/PyTorch", "level": 90, "icon": "📊"},
        {"name": "Data Engineering", "level": 80, "icon": "📈"},
        {"name": "Cloud AI Services", "level": 85, "icon": "☁️"}
    ],
    "projects": [
        {
            "title": "Computer Vision for Retail Analytics",
            "description": "Developed a real-time computer vision system that analyzes in-store customer behavior to optimize product placement and store layout.",
            "image_type": "computer_vision",
            "tags": ["Computer Vision", "PyTorch", "Real-time Analytics", "Edge AI"],
            "link": "#project1"
        },
        {
            "title": "Conversational AI Assistant",
            "description": "Built an advanced NLP-powered conversational agent that handles customer service inquiries with 92% accuracy, reducing support costs by 35%.",
            "image_type": "nlp",
            "tags": ["NLP", "Transformers", "BERT", "Cloud Deployment"],
            "link": "#project2"
        },
        {
            "title": "Predictive Maintenance System",
            "description": "Created a machine learning system that predicts equipment failures 2 weeks in advance, reducing downtime by 45% for manufacturing clients.",
            "image_type": "data_science",
            "tags": ["Time Series", "Anomaly Detection", "IoT", "Predictive Analytics"],
            "link": "#project3"
        },
        {
            "title": "Generative AI for Product Design",
            "description": "Implemented a GAN-based system that generates novel product design concepts based on market trends and brand guidelines.",
            "image_type": "generative_ai",
            "tags": ["GANs", "Creative AI", "Product Design", "PyTorch"],
            "link": "#project4"
        },
        {
            "title": "Reinforcement Learning for Supply Chain",
            "description": "Developed a reinforcement learning system that optimizes inventory management and logistics, reducing costs by 18%.",
            "image_type": "reinforcement_learning",
            "tags": ["Reinforcement Learning", "Supply Chain", "Optimization", "Simulation"],
            "link": "#project5"
        },
        {
            "title": "MLOps Pipeline for Financial Services",
            "description": "Designed and implemented an end-to-end MLOps pipeline for a financial services company, enabling continuous training and deployment of fraud detection models.",
            "image_type": "mlops",
            "tags": ["MLOps", "CI/CD", "Kubernetes", "Model Monitoring"],
            "link": "#project6"
        }
    ],
    "experience": [
        {
            "title": "Senior AI Engineer",
            "company": "TechInnovate AI",
            "date": "2021 - Present",
            "description": "Lead AI engineer for computer vision and NLP projects. Designed and implemented production ML systems for Fortune 500 clients."
        },
        {
            "title": "Machine Learning Engineer",
            "company": "DataSmart Solutions",
            "date": "2018 - 2021",
            "description": "Developed predictive models for retail and healthcare clients. Implemented MLOps practices that reduced model deployment time by 70%."
        },
        {
            "title": "AI Research Intern",
            "company": "AI Research Lab",
            "date": "2017 - 2018",
            "description": "Conducted research in reinforcement learning algorithms. Published 2 papers in top-tier AI conferences."
        }
    ],
    "education": [
        {
            "degree": "M.S. in Computer Science, AI Specialization",
            "institution": "Stanford University",
            "date": "2015 - 2017"
        },
        {
            "degree": "B.S. in Computer Science",
            "institution": "University of California, Berkeley",
            "date": "2011 - 2015"
        }
    ],
    "certifications": [
        {
            "name": "Google Cloud Professional Machine Learning Engineer",
            "issuer": "Google Cloud",
            "date": "2022"
        },
        {
            "name": "AWS Certified Machine Learning - Specialty",
            "issuer": "Amazon Web Services",
            "date": "2021"
        },
        {
            "name": "Deep Learning Specialization",
            "issuer": "Coursera (Andrew Ng)",
            "date": "2020"
        }
    ]
}

# Create navigation component
def create_navigation():
    with ui.header().classes('bg-gray-900 text-white'):
        with ui.container().classes('flex justify-between items-center py-2'):
            ui.label('AI Engineer Portfolio').classes('text-xl font-bold')
            with ui.row().classes('gap-4'):
                ui.link('Home', '#').classes('text-white hover:text-blue-300')
                ui.link('Projects', '#projects').classes('text-white hover:text-blue-300')
                ui.link('Skills', '#skills').classes('text-white hover:text-blue-300')
                ui.link('Experience', '#experience').classes('text-white hover:text-blue-300')
                ui.link('Contact', '#contact').classes('text-white hover:text-blue-300')

# Create hero section
def create_hero_section():
    hero_image = AssetManager.get_hero_image()
    
    with ui.element('div').classes('hero-section'):
        ui.element('div').classes('hero-bg').style(f'background-image: url({hero_image})')
        ui.element('div').classes('hero-overlay')
        with ui.element('div').classes('hero-content text-center'):
            ui.label(PORTFOLIO_DATA["personal_info"]["name"]).classes('text-3xl md:text-4xl font-bold mb-2')
            ui.label(PORTFOLIO_DATA["personal_info"]["title"]).classes('text-xl md:text-2xl mb-6')
            ui.markdown(PORTFOLIO_DATA["personal_info"]["bio"]).classes('max-w-2xl mx-auto mb-8')
            with ui.row().classes('justify-center gap-4'):
                ui.button('View Projects', on_click=lambda: ui.navigate('#projects')).classes('btn-primary')
                ui.button('Contact Me', on_click=lambda: ui.navigate('#contact')).classes('btn-outline')

# Create projects section
def create_projects_section():
    with ui.element('section').classes('py-16').id('projects'):
        with ui.container().classes('portfolio-container'):
            ui.label('Featured Projects').classes('text-2xl md:text-3xl font-bold section-title')
            
            with ui.grid(columns=3).classes('gap-6'):
                for project in PORTFOLIO_DATA["projects"]:
                    project_image = AssetManager.get_project_image(project["image_type"])
                    
                    with ui.card().classes('project-card'):
                        ui.element('div').classes('project-image').style(f'background-image: url({project_image})')
                        with ui.card_section().classes('project-content'):
                            ui.label(project["title"]).classes('project-title')
                            ui.label(project["description"]).classes('project-description')
                            with ui.element('div').classes('project-tags'):
                                for tag in project["tags"]:
                                    ui.label(tag).classes('project-tag')
                            with ui.row().classes('justify-between items-center mt-4'):
                                ui.link('View Details', project["link"]).classes('text-blue-400 hover:text-blue-300')

# Create skills section
def create_skills_section():
    with ui.element('section').classes('py-16 bg-gray-900').id('skills'):
        with ui.container().classes('portfolio-container'):
            ui.label('Skills & Expertise').classes('text-2xl md:text-3xl font-bold section-title')
            
            with ui.grid(columns=5).classes('gap-4'):
                for skill in PORTFOLIO_DATA["skills"]:
                    with ui.card().classes('skill-card'):
                        ui.label(skill["icon"]).classes('skill-icon')
                        ui.label(skill["name"]).classes('skill-name')
                        with ui.element('div').classes('skill-level'):
                            ui.element('div').classes('skill-level-fill').style(f'width: {skill["level"]}%')

# Create experience section
def create_experience_section():
    with ui.element('section').classes('py-16').id('experience'):
        with ui.container().classes('portfolio-container'):
            ui.label('Work Experience').classes('text-2xl md:text-3xl font-bold section-title')
            
            with ui.element('div').classes('timeline'):
                for exp in PORTFOLIO_DATA["experience"]:
                    with ui.element('div').classes('timeline-item'):
                        ui.element('div').classes('timeline-dot')
                        ui.label(exp["date"]).classes('timeline-date')
                        ui.label(exp["title"]).classes('timeline-title')
                        ui.label(exp["company"]).classes('timeline-company')
                        ui.label(exp["description"]).classes('timeline-description')
            
            ui.label('Education').classes('text-2xl md:text-3xl font-bold section-title mt-12')
            
            with ui.element('div').classes('timeline'):
                for edu in PORTFOLIO_DATA["education"]:
                    with ui.element('div').classes('timeline-item'):
                        ui.element('div').classes('timeline-dot')
                        ui.label(edu["date"]).classes('timeline-date')
                        ui.label(edu["degree"]).classes('timeline-title')
                        ui.label(edu["institution"]).classes('timeline-company')
            
            ui.label('Certifications').classes('text-2xl md:text-3xl font-bold section-title mt-12')
            
            with ui.grid(columns=3).classes('gap-4'):
                for cert in PORTFOLIO_DATA["certifications"]:
                    with ui.card().classes('skill-card'):
                        ui.label('🏆').classes('skill-icon')
                        ui.label(cert["name"]).classes('skill-name')
                        ui.label(f"{cert['issuer']} • {cert['date']}").classes('text-sm text-gray-400')

# Create contact section
def create_contact_section():
    with ui.element('section').classes('py-16 bg-gray-900').id('contact'):
        with ui.container().classes('portfolio-container'):
            ui.label('Get In Touch').classes('text-2xl md:text-3xl font-bold section-title')
            
            with ui.grid(columns=2).classes('gap-8'):
                with ui.card().classes('bg-gray-800 p-6 rounded-lg'):
                    ui.label('Contact Information').classes('text-xl font-bold mb-6')
                    
                    with ui.element('div').classes('space-y-4'):
                        with ui.element('div').classes('contact-item'):
                            with ui.element('div').classes('contact-icon'):
                                ui.icon('mail')
                            with ui.element('div'):
                                ui.label('Email').classes('text-sm text-gray-400')
                                ui.label(PORTFOLIO_DATA["personal_info"]["email"]).classes('text-white')
                        
                        with ui.element('div').classes('contact-item'):
                            with ui.element('div').classes('contact-icon'):
                                ui.icon('phone')
                            with ui.element('div'):
                                ui.label('Phone').classes('text-sm text-gray-400')
                                ui.label(PORTFOLIO_DATA["personal_info"]["phone"]).classes('text-white')
                        
                        with ui.element('div').classes('contact-item'):
                            with ui.element('div').classes('contact-icon'):
                                ui.icon('map_pin')
                            with ui.element('div'):
                                ui.label('Location').classes('text-sm text-gray-400')
                                ui.label(PORTFOLIO_DATA["personal_info"]["location"]).classes('text-white')
                    
                    ui.label('Connect With Me').classes('text-xl font-bold mt-8 mb-4')
                    
                    with ui.element('div').classes('social-links'):
                        ui.link('', PORTFOLIO_DATA["personal_info"]["social"]["github"], new_tab=True).classes('social-link').style('text-decoration: none;').add(ui.icon('github'))
                        ui.link('', PORTFOLIO_DATA["personal_info"]["social"]["linkedin"], new_tab=True).classes('social-link').style('text-decoration: none;').add(ui.icon('linkedin'))
                        ui.link('', PORTFOLIO_DATA["personal_info"]["social"]["twitter"], new_tab=True).classes('social-link').style('text-decoration: none;').add(ui.icon('twitter'))
                        ui.link('', PORTFOLIO_DATA["personal_info"]["social"]["medium"], new_tab=True).classes('social-link').style('text-decoration: none;').add(ui.icon('edit'))
                
                with ui.card().classes('bg-gray-800 p-6 rounded-lg'):
                    ui.label('Send Me a Message').classes('text-xl font-bold mb-6')
                    
                    with ui.element('form').classes('space-y-4'):
                        with ui.grid(columns=2).classes('gap-4'):
                            ui.input(label='Name').props('outlined dark').classes('col-span-1')
                            ui.input(label='Email').props('outlined dark').classes('col-span-1')
                        ui.input(label='Subject').props('outlined dark')
                        ui.textarea(label='Message', rows=5).props('outlined dark')
                        ui.button('Send Message', icon='send').classes('btn-primary mt-4')

# Create footer
def create_footer():
    with ui.footer().classes('py-8 bg-gray-900 border-t border-gray-800'):
        with ui.container().classes('portfolio-container text-center'):
            ui.label(f'© {2023} {PORTFOLIO_DATA["personal_info"]["name"]} • AI Engineer Portfolio').classes('text-gray-400')
            ui.label('Built with Python and NiceGUI').classes('text-gray-500 text-sm mt-2')

# Main page
@ui.page('/')
def main_page():
    # Add CSS
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">')
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')
    ui.add_head_html(f'<link rel="stylesheet" href="/static/css/main.css">')
    
    # Create page sections
    create_navigation()
    create_hero_section()
    create_projects_section()
    create_skills_section()
    create_experience_section()
    create_contact_section()
    create_footer()
    
    # Add scroll behavior
    ui.add_head_html('''
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Smooth scroll for anchor links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    e.preventDefault();
                    const targetId = this.getAttribute('href');
                    if (targetId === '#') return;
                    
                    const targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        window.scrollTo({
                            top: targetElement.offsetTop - 80,
                            behavior: 'smooth'
                        });
                    }
                });
            });
            
            // Add animation classes on scroll
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('fade-in');
                    }
                });
            }, { threshold: 0.1 });
            
            document.querySelectorAll('section').forEach(section => {
                observer.observe(section);
            });
        });
    </script>
    ''')
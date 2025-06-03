"""
Professional visual asset management system for the AI Engineer Portfolio.

This module provides functionality for fetching and managing professional
images for the portfolio website.
"""
import requests
from typing import List, Dict, Optional
import random
import sys
import codecs
import logging

# Force UTF-8 encoding for reliability
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

class AssetManager:
    """Manages professional visual assets for the AI Engineer Portfolio"""
    
    # AI and technology focused image categories
    IMAGE_CATEGORIES = [
        "artificial intelligence", 
        "machine learning", 
        "data science", 
        "neural networks", 
        "technology", 
        "coding", 
        "algorithms",
        "robotics"
    ]
    
    @staticmethod
    def get_image(category: Optional[str] = None, width: int = 800, height: int = 600) -> str:
        """
        Fetch a professional image for the specified category.
        
        Args:
            category: Image category (defaults to random AI-related category)
            width: Desired image width
            height: Desired image height
            
        Returns:
            URL to a professional image
        """
        try:
            if not category:
                category = random.choice(AssetManager.IMAGE_CATEGORIES)
                
            # Generate unique URL to avoid caching issues
            seed = random.randint(1000, 9999)
            return f"https://source.unsplash.com/{width}x{height}/?{category}&sig={seed}"
        except Exception as e:
            logging.error(f"Error fetching image: {e}")
            # Fallback to a placeholder if image fetching fails
            return f"https://via.placeholder.com/{width}x{height}/2563eb/ffffff?text=AI+Engineer"
    
    @staticmethod
    def get_project_image(project_type: str) -> str:
        """
        Get an image appropriate for a specific AI project type.
        
        Args:
            project_type: Type of AI project (e.g., "nlp", "computer vision")
            
        Returns:
            URL to a project-appropriate image
        """
        project_categories = {
            "nlp": ["natural language processing", "text analysis", "language ai"],
            "computer_vision": ["computer vision", "image recognition", "visual ai"],
            "reinforcement_learning": ["reinforcement learning", "game ai", "robotics"],
            "generative_ai": ["generative ai", "creative ai", "ai art"],
            "data_science": ["data science", "data visualization", "big data"],
            "mlops": ["devops", "cloud computing", "software engineering"]
        }
        
        # Get appropriate categories or default to general AI
        categories = project_categories.get(project_type, ["artificial intelligence"])
        category = random.choice(categories)
        
        return AssetManager.get_image(category, 600, 400)
    
    @staticmethod
    def get_hero_image() -> str:
        """
        Get a high-quality hero image for the portfolio header.
        
        Returns:
            URL to a hero image
        """
        hero_categories = [
            "artificial intelligence workspace",
            "futuristic technology",
            "data visualization",
            "neural networks visualization"
        ]
        category = random.choice(hero_categories)
        return AssetManager.get_image(category, 1200, 600)
# AI Engineer Portfolio

A professional, interactive portfolio website for AI Engineers built with Python and NiceGUI.

![AI Engineer Portfolio](https://source.unsplash.com/800x400/?artificial%20intelligence&sig=1)

## Features

- **Modern, Responsive Design**: Professional UI that works on all devices
- **Interactive Project Showcase**: Highlight your AI and machine learning projects
- **Skills & Expertise Section**: Visualize your technical skills
- **Work Experience Timeline**: Showcase your professional journey
- **Contact Form**: Allow potential clients or employers to reach you
- **Professional Styling**: Clean, modern design with animations and transitions

## Quick Start

### Prerequisites

- Python 3.8+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-engineer-portfolio.git
   cd ai-engineer-portfolio
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Customization

### Personal Information

Edit the `PORTFOLIO_DATA` dictionary in `app/main.py` to update your personal information, skills, projects, and experience.

### Images

The portfolio automatically fetches professional images related to AI and technology. If you want to use your own images:

1. Place your images in the `app/static/images` directory
2. Update the image paths in the `PORTFOLIO_DATA` dictionary

### Styling

The styling is defined in `app/static/css/main.css`. You can modify this file to change colors, fonts, and other visual elements.

## Deployment

### Docker

A Dockerfile is included for easy deployment:

```bash
# Build the Docker image
docker build -t ai-portfolio .

# Run the container
docker run -p 8080:8080 ai-portfolio
```

### Cloud Deployment

This application is ready for deployment on platforms like:

- **Fly.io**: Use the included Dockerfile
- **Heroku**: Add a `Procfile` with `web: python main.py`
- **Vercel**: Use the Vercel Python adapter
- **AWS, GCP, Azure**: Deploy as a container or on a VM

## Technologies Used

- **NiceGUI**: Modern Python UI framework
- **Python**: Backend logic and data handling
- **HTML/CSS**: Styling and layout
- **Docker**: Containerization for deployment

## License

MIT

## Author

Your Name - [your.email@example.com](mailto:your.email@example.com)

---

Feel free to use this template for your own AI Engineer portfolio!
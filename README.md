# Wei-Han Tu's Portfolio Website

A modern, responsive portfolio website showcasing my projects and skills in AI/ML, web development, robotics, and engineering.

## 🚀 Live Demo

Visit my portfolio at: [https://weihantu.github.io/weihantu_portfolio.github.io](https://weihantu.github.io/weihantu_portfolio.github.io)

## 📋 Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with smooth animations
- **Project Showcase**: Detailed descriptions of 8 diverse projects
- **Contact Form**: Interactive contact form with CSV data storage
- **GitHub Integration**: Direct links to all project repositories
- **Flask Backend**: Python-based server for form handling

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3 (with SCSS)
- JavaScript (jQuery)
- FontAwesome Icons

### Backend
- Python 3.12
- Flask
- CSV data storage

### Design
- HTML5 UP Dimension Template
- Responsive design principles
- Modern CSS animations

## 📁 Project Structure

```
weihantu_portfolio.github.io/
├── app.py                 # Flask application
├── contacts.csv           # Contact form data storage
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── LICENSE.txt           # MIT License
├── .gitignore            # Git ignore rules
└── static/
    ├── index.html        # Main portfolio page
    ├── assets/
    │   ├── css/          # Stylesheets
    │   ├── js/           # JavaScript files
    │   ├── sass/         # SCSS source files
    │   └── webfonts/     # Font files
    └── images/           # Portfolio images
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/WeiHanTu/weihantu_portfolio.github.io.git
   cd weihantu_portfolio.github.io
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 📊 Portfolio Projects

### AI/ML Projects
1. **Generative DnD Battlemaps** - Full-stack D&D map generation with LLMs
2. **Robotic Manipulation with RL** - PPO implementation for robotics
3. **Multitask E-commerce Recommender** - CTR/CVR prediction system
4. **Automated Fact-Checking with BERT** - NLP-based claim verification
5. **LLM-Powered Q&A Application** - RAG pipeline for document querying

### Web Development & Engineering
6. **Expectimax for 2048 Game** - AI game solver with MDP
7. **Biking Website Redesign** - Route planning with 340K+ users
8. **Urban Wind Pattern Analysis** - CFD-based environmental engineering

## 🎨 Customization

### Adding New Projects
1. Edit `static/index.html`
2. Add new project section in the work article
3. Include GitHub link and project details
4. Update project numbering

### Styling Changes
- Main styles: `static/assets/css/main.css`
- SCSS source: `static/assets/sass/`
- Responsive design: `static/assets/css/noscript.css`

### Backend Modifications
- Flask routes: `app.py`
- Contact form handling: `/save_contact` route
- Data storage: `contacts.csv`

## 📧 Contact Form

The portfolio includes a functional contact form that:
- Validates input fields
- Stores submissions in CSV format
- Provides user feedback
- Redirects to thank you page

## 🔧 Development

### Local Development
```bash
# Run with debug mode
python app.py

# Or with Flask CLI
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Deployment
The site is designed to work with GitHub Pages and can be deployed to:
- GitHub Pages (static hosting)
- Heroku
- AWS
- Any Python web server

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## 🙏 Acknowledgments

- **HTML5 UP**: For the Dimension template
- **FontAwesome**: For the icon set
- **Flask**: For the web framework
- **GitHub Pages**: For hosting

## 📞 Contact

- **GitHub**: [@WeiHanTu](https://github.com/WeiHanTu)
- **LinkedIn**: [Wei-Han Tu](https://www.linkedin.com/in/weihantu)
- **Email**: weihantu1996@gmail.com

---

**Note**: This portfolio showcases my progression from engineering to AI/ML, demonstrating both technical depth and breadth across multiple domains.

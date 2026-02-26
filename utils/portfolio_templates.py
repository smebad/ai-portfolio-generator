# Portfolio HTML Templates - Designs users can choose from

# Function to generate HTML for Modern Gradient template
def get_modern_template(data):
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data.get('name', 'Portfolio')} - Portfolio</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            animation: fadeInDown 1s;
        }}
        
        .header .headline {{
            font-size: 1.3em;
            opacity: 0.95;
            font-weight: 300;
            animation: fadeInUp 1s;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section h2 {{
            color: #667eea;
            font-size: 2em;
            margin-bottom: 20px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        
        .bio {{
            font-size: 1.2em;
            color: #555;
            line-height: 1.8;
        }}
        
        .skills-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        
        .skill-card {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            border-radius: 10px;
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        
        .skill-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }}
        
        .skill-card h3 {{
            color: #667eea;
            margin-bottom: 10px;
        }}
        
        .skill-card p {{
            color: #666;
            font-size: 0.95em;
        }}
        
        .contact {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
            margin: 40px -40px -40px -40px;
        }}
        
        .contact a {{
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-size: 1.1em;
            border: 2px solid white;
            padding: 10px 20px;
            border-radius: 25px;
            display: inline-block;
            margin-top: 20px;
            transition: all 0.3s;
        }}
        
        .contact a:hover {{
            background: white;
            color: #667eea;
        }}
        
        @keyframes fadeInDown {{
            from {{
                opacity: 0;
                transform: translateY(-20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2em;
            }}
            
            .skills-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{data.get('name', 'Your Name')}</h1>
            <p class="headline">{data.get('headline', 'Your Professional Headline')}</p>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>About Me</h2>
                <p class="bio">{data.get('bio', 'Your professional bio will appear here...')}</p>
            </div>
            
            <div class="section">
                <h2>About</h2>
                <p>{data.get('about', 'Detailed about section will appear here...')}</p>
            </div>
            
            <div class="section">
                <h2>Skills & Expertise</h2>
                <div class="skills-grid">
                    {generate_skill_cards(data.get('skills_description', {}))}
                </div>
            </div>
        </div>
        
        <div class="contact">
            <h2>Let's Connect</h2>
            <p>Ready to bring your next project to life?</p>
            <div>
                <a href="mailto:{data.get('email', 'your.email@example.com')}">Email Me</a>
                <a href="{data.get('linkedin', '#')}">LinkedIn</a>
                <a href="{data.get('github', '#')}">GitHub</a>
            </div>
        </div>
    </div>
</body>
</html>
"""
    return html


# Function to generate HTML for skill cards
def generate_skill_cards(skills_dict):
    if not skills_dict:
        return "<p>No skills data available</p>"
    
    cards_html = ""
    for skill_name, skill_desc in skills_dict.items():
        cards_html += f"""
        <div class="skill-card">
            <h3>{skill_name}</h3>
            <p>{skill_desc}</p>
        </div>
        """
    
    return cards_html


# Function to generate HTML for minimalist template
def get_minimalist_template(data):
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data.get('name', 'Portfolio')} - Portfolio</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Courier New', monospace;
            line-height: 1.8;
            color: #000;
            background: #fff;
            padding: 60px 20px;
        }}
        
        .container {{
            max-width: 800px;
            margin: 0 auto;
        }}
        
        .header {{
            border-bottom: 3px solid #000;
            padding-bottom: 30px;
            margin-bottom: 40px;
        }}
        
        .header h1 {{
            font-size: 3.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .header .headline {{
            font-size: 1.2em;
            color: #666;
        }}
        
        .section {{
            margin-bottom: 50px;
        }}
        
        .section h2 {{
            font-size: 1.5em;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}
        
        .skills-list {{
            list-style: none;
        }}
        
        .skills-list li {{
            padding: 15px 0;
            border-bottom: 1px solid #ddd;
        }}
        
        .skills-list strong {{
            display: block;
            margin-bottom: 5px;
        }}
        
        .contact {{
            border-top: 3px solid #000;
            padding-top: 30px;
            margin-top: 60px;
        }}
        
        .contact a {{
            color: #000;
            text-decoration: none;
            margin-right: 20px;
            border-bottom: 2px solid #000;
        }}
        
        .contact a:hover {{
            border-bottom: 2px solid #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{data.get('name', 'Your Name')}</h1>
            <p class="headline">{data.get('headline', 'Your Professional Headline')}</p>
        </div>
        
        <div class="section">
            <h2>Bio</h2>
            <p>{data.get('bio', 'Your professional bio will appear here...')}</p>
        </div>
        
        <div class="section">
            <h2>About</h2>
            <p>{data.get('about', 'Detailed about section will appear here...')}</p>
        </div>
        
        <div class="section">
            <h2>Skills</h2>
            <ul class="skills-list">
                {generate_skill_list(data.get('skills_description', {}))}
            </ul>
        </div>
        
        <div class="contact">
            <h2>Contact</h2>
            <a href="mailto:{data.get('email', 'your.email@example.com')}">Email</a>
            <a href="{data.get('linkedin', '#')}">LinkedIn</a>
            <a href="{data.get('github', '#')}">GitHub</a>
        </div>
    </div>
</body>
</html>
"""
    return html


def generate_skill_list(skills_dict):
    if not skills_dict:
        return "<li>No skills data available</li>"
    
    list_html = ""
    for skill_name, skill_desc in skills_dict.items():
        list_html += f"""
        <li>
            <strong>{skill_name}</strong>
            {skill_desc}
        </li>
        """
    
    return list_html


# Dictionary to store all available templates
TEMPLATES = {
    "Modern Gradient": get_modern_template,
    "Minimalist B&W": get_minimalist_template,
}

# Function to get a specific template
def get_template(template_name, data):
    template_func = TEMPLATES.get(template_name, get_modern_template)
    return template_func(data)
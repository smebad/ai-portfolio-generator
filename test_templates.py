"""
Test file for portfolio templates
This generates sample HTML files you can open in your browser
"""

from utils.portfolio_templates import get_template, TEMPLATES

# Sample test data
test_data = {
    "name": "Jane Smith",
    "headline": "Innovative Full Stack Developer & AI Enthusiast",
    "bio": "Jane Smith is a passionate Full Stack Developer with 4 years of experience building scalable web applications. She specializes in Python, React, and cutting-edge AI/ML technologies, delivering solutions that make a real impact.",
    "about": "With a strong foundation in both frontend and backend development, Jane has successfully led multiple projects from conception to deployment. Her expertise spans the entire development lifecycle, and she's particularly passionate about integrating AI capabilities into web applications. Jane thrives in collaborative environments and is known for writing clean, maintainable code that stands the test of time.",
    "skills_description": {
        "Python": "Expert in Python for backend development, data analysis, and machine learning model implementation. Proficient with Django, Flask, and FastAPI frameworks.",
        "React": "Advanced React developer creating dynamic, responsive user interfaces. Experienced with hooks, context API, and modern state management solutions.",
        "AI/ML": "Hands-on experience with TensorFlow, PyTorch, and scikit-learn. Built and deployed multiple ML models for real-world applications.",
        "Cloud & DevOps": "Proficient in AWS, Docker, and CI/CD pipelines. Experienced in deploying and scaling applications in cloud environments."
    },
    "email": "jane.smith@example.com",
    "linkedin": "https://linkedin.com/in/janesmith",
    "github": "https://github.com/janesmith"
}

def test_all_templates():
    """
    Generate HTML files for all available templates
    You can open these in your browser to see how they look
    """
    
    print("🧪 Testing Portfolio Templates...\n")
    
    for template_name in TEMPLATES.keys():
        print(f"📝 Generating: {template_name}")
        
        # Generate HTML for this template
        html_content = get_template(template_name, test_data)
        
        # Create a filename (replace spaces with underscores)
        filename = f"test_{template_name.replace(' ', '_').lower()}.html"
        
        # Save to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"   ✅ Saved to: {filename}")
        print(f"   📂 Open this file in your browser to preview!\n")
    
    print("=" * 60)
    print("✨ All templates generated successfully!")
    print("=" * 60)
    print("\n📌 HOW TO VIEW:")
    print("1. Look for the .html files in your project folder")
    print("2. Right-click any file → 'Open with' → Choose your browser")
    print("3. OR drag and drop the file into your browser window")
    print("\n💡 TIP: Try both templates to see which style you prefer!")


def test_single_template(template_name="Modern Gradient"):
    """
    Test a specific template
    
    Args:
        template_name (str): Name of the template to test
    """
    
    print(f"🧪 Testing: {template_name}\n")
    
    if template_name not in TEMPLATES:
        print(f"❌ Template '{template_name}' not found!")
        print(f"Available templates: {list(TEMPLATES.keys())}")
        return
    
    html_content = get_template(template_name, test_data)
    filename = f"test_{template_name.replace(' ', '_').lower()}.html"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Generated: {filename}")
    print(f"📂 File location: {filename}")
    print(f"\n👉 Open this file in your browser to see the portfolio!")

# Function to test with custom user data
def test_with_custom_data():
    
    
    custom_data = {
        "name": "YOUR NAME HERE",
        "headline": "Your Professional Headline",
        "bio": "Your 2-3 sentence professional bio goes here. Make it compelling!",
        "about": "Your detailed about section. Talk about your journey, expertise, and what drives you. This should be 150-200 words.",
        "skills_description": {
            "Skill 1": "Description of your first skill and how you use it.",
            "Skill 2": "Description of your second skill and expertise level.",
            "Skill 3": "Description of your third skill and projects where you've used it."
        },
        "email": "your.email@example.com",
        "linkedin": "https://linkedin.com/in/yourprofile",
        "github": "https://github.com/yourprofile"
    }
    
    print("🧪 Testing with CUSTOM data...\n")
    
    for template_name in TEMPLATES.keys():
        html_content = get_template(template_name, custom_data)
        filename = f"my_{template_name.replace(' ', '_').lower()}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Created: {filename}")
    
    print("\n🎉 Your custom portfolios are ready!")
    print("Open the 'my_*.html' files in your browser!")


# Run tests when file is executed
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("   PORTFOLIO TEMPLATE TESTER")
    print("=" * 60 + "\n")
    
    # Test all templates with sample data
    test_all_templates()
    
    print("\n" + "=" * 60)
    print("\n🔍 Want to test with YOUR data?")
    print("1. Edit the 'custom_data' in the test_with_custom_data() function")
    print("2. Uncomment the line below and run again\n")
    
    # Uncomment the next line to test with your own custom data:
    # test_with_custom_data()
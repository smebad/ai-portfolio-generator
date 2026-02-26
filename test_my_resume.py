from utils.ai_helper import AIPortfolioGenerator
from utils.portfolio_templates import get_template
import json


# Your resume text
resume_text = """
Syed Ebad
Machine Learning Engineer
Email: mohammdedbad1@hotmail.com | GitHub: https://github.com/smebad
LinkedIn: https://linkedin.com/in/syed-ebad-ml | Karachi, Pakistan

About Me:
Aspiring Machine Learning Engineer with 5+ years in enterprise systems and hands-on projects in NLP, Gen AI, and healthcare. Skilled in PyTorch, Transformers, Streamlit/Flask, and deploying end-to-end AI systems.

Skills:
Python, JavaScript, SQL, PyTorch, TensorFlow, scikit-learn, Keras, Hugging Face Transformers, LangChain, Prompt Engineering, NLP, Gen AI, Streamlit, FastAPI, Docker, Git

Projects:
- DocuChat: RAG-based PDF Q&A with LangChain & FAISS
- Parkinson's Disease Detection: SVM and Random Forest classifier
- Fake News Prediction: NLP classifier with TF-IDF

Experience:
Sante Private Limited – Distribution Executive (2018-2023)
Managed SAP S4 HANA SD Module
"""

# Generate content
ai = AIPortfolioGenerator()
result = ai.generate_from_resume(resume_text)

if result["success"]:
    print("✅ SUCCESS!\n")
    print("Generated Content:")
    print(result["content"])
    print(f"\nTokens used: {result['tokens_used']}")
    
    # Parse and create portfolio
    try:
        data = json.loads(result["content"])
        
        portfolio_data = {
            "name": "Syed Ebad",
            "headline": data.get("HEADLINE", ""),
            "bio": data.get("PROFESSIONAL_BIO", ""),
            "about": data.get("ABOUT_SECTION", ""),
            "skills_description": data.get("SKILLS_DESCRIPTION", {}),
            "email": "mohammdedbad1@hotmail.com",
            "linkedin": "https://linkedin.com/in/syed-ebad-ml",
            "github": "https://github.com/smebad"
        }
        
        # Generate HTML
        html = get_template("Modern Gradient", portfolio_data)
        
        with open("my_portfolio.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        print("\n🎉 Portfolio generated: my_portfolio.html")
        print("Open this file in your browser!")
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
else:
    print(f"❌ Error: {result['error']}")
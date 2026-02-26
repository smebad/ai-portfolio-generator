import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# This class will handle all AI-related tasks for our portfolio generator
class AIPortfolioGenerator:
    
    # Constructor to set up the Groq client
    def __init__(self):
        
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file!")
        
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"
    
    # This method generates portfolio content based on user data
    def generate_portfolio_content(self, user_data):

    # A detailed prompt for the AI
        prompt = f"""
    You are an expert portfolio writer. Generate professional portfolio content for:

    Name: {user_data.get('name', 'User')}
    Role: {user_data.get('role', 'Developer')}
    Skills: {user_data.get('skills', 'Python, AI, Web Development')}
    Experience: {user_data.get('experience', '2 years')}
    Projects: {user_data.get('projects', 'Various web applications')}

    Generate a JSON object with this EXACT structure:

    {{
    "PROFESSIONAL_BIO": "A compelling 2-3 sentence professional bio (60-80 words) that highlights expertise and impact",
    "HEADLINE": "A catchy professional headline (8-12 words)",
    "ABOUT_SECTION": "Detailed about section (150-200 words) describing background, journey, expertise, achievements, and what drives this professional. Make it personal and compelling.",
    "SKILLS_DESCRIPTION": {{
        "Python & ML Frameworks": "Expertise in building production ML models with PyTorch, TensorFlow, and scikit-learn. Developed end-to-end AI systems from research to deployment.",
        "NLP & Gen AI": "Specialized in transformer models, LangChain, and prompt engineering. Built RAG systems and conversational AI applications.",
        "Full-Stack AI Development": "Creating production-ready AI applications with Streamlit and FastAPI. Experience with REST APIs and microservices architecture.",
        "Data Science & Analytics": "Expert in EDA, feature engineering, and ML pipelines. Proficient with pandas, numpy, and visualization tools.",
        "MLOps & DevOps": "Skilled in Git, Docker, and CI/CD for ML systems. Experience deploying models to cloud platforms.",
        "Domain Expertise": "Applied ML to healthcare analytics and enterprise systems. Strong background in SAP integration and business processes."
    }}
    }}

    CRITICAL RULES:
    1. Return ONLY valid JSON - no markdown code blocks, no extra text
    2. Each skill description should be 15-25 words and describe WHAT was built or achieved
    3. Use concrete examples from the projects mentioned
    4. Make it achievement-oriented and specific
    5. The SKILLS_DESCRIPTION must have exactly 6 skills with detailed descriptions
    6. Do NOT use generic terms like "Expert", "Proficient", "Skilled" - describe actual accomplishments

    Return only the JSON object.
    """
        
        try:
            # Call Groq AI
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional portfolio content writer. You create engaging, achievement-focused content. You ONLY respond with valid JSON, no markdown formatting."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1800,
            )
            
            # Extract the generated text
            generated_content = response.choices[0].message.content.strip()
            
            # Clean up markdown code blocks if present
            if generated_content.startswith('```'):
                lines = generated_content.split('\n')
                # Remove first line (```json or ```) and last line (```)
                if lines[0].strip().startswith('```'):
                    lines = lines[1:]
                if lines and lines[-1].strip() == '```':
                    lines = lines[:-1]
                generated_content = '\n'.join(lines).strip()
            
            return {
                "success": True,
                "content": generated_content,
                "tokens_used": response.usage.total_tokens
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
            

# Test function
def test_ai_helper():

    print("Testing AI Helper...")
    
    ai = AIPortfolioGenerator()
    
    test_data = {
        "name": "Syed Ebad",
        "role": "Machine Learning Engineer",
        "skills": "Python, Deep Learning, AI/ML",
        "experience": "2 years",
        "projects": "AI chatbot, Fine-tuning language models, Prediction models for stock prices"
    }
    
    result = ai.generate_portfolio_content(test_data)
    
    if result["success"]:
        print("\n✅ SUCCESS! AI is working!")
        print(f"\nGenerated Content:\n{result['content']}")
        print(f"\nTokens used: {result['tokens_used']}")
    else:
        print(f"\n❌ ERROR: {result['error']}")


# This runs only when you execute this file directly
if __name__ == "__main__":
    test_ai_helper()
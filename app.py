"""
AI Portfolio Generator - Main Application
Built with Streamlit for easy deployment
Author: Syed Ebad
GitHub: https://github.com/smebad/ai-portfolio-generator
"""

import streamlit as st
import json
from utils.ai_helper import AIPortfolioGenerator
from utils.portfolio_templates import get_template, TEMPLATES

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="AI Portfolio Generator",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #667eea;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.1rem;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        transition: transform 0.2s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .success-box {
        padding: 1rem;
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables for the app"""
    if 'generated_content' not in st.session_state:
        st.session_state.generated_content = None
    if 'html_output' not in st.session_state:
        st.session_state.html_output = None


def parse_ai_response(ai_content):
    """
    Parse the AI-generated JSON response
    
    Args:
        ai_content (str): Raw AI response text
    
    Returns:
        dict: Parsed portfolio data or raw content if parsing fails
    """
    try:
        # Try to find JSON in the response
        start = ai_content.find('{')
        end = ai_content.rfind('}') + 1
        
        if start != -1 and end > start:
            json_str = ai_content[start:end]
            data = json.loads(json_str)
            return data
        else:
            # If no JSON found, return raw content
            return {"raw_content": ai_content}
    except json.JSONDecodeError as e:
        st.warning(f"JSON parsing error: {e}")
        return {"raw_content": ai_content}


def main():
    """Main application function"""
    
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">🚀 AI Portfolio Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Create a stunning professional portfolio in minutes with AI</p>', unsafe_allow_html=True)
    
    # Sidebar for user input
    with st.sidebar:
        st.header("📝 Your Information")
        st.write("Fill in your details below")
        
        # User input form
        name = st.text_input("Full Name*", placeholder="Enter your name here")
        role = st.text_input("Professional Role*", placeholder="e.g., Data Scientist, Software Engineer")
        
        skills = st.text_area(
            "Skills (comma-separated)*",
            placeholder=" e.g., python, aws, frameworks, ml algorithms",
            height=100
        )
        
        experience = st.text_input(
            "Years of Experience",
            placeholder="e.g., 3 years, 5+ years"
        )
        
        projects = st.text_area(
            "Key Projects (brief description)*",
            placeholder=" e.g., AI chatbot for customer support, Stock price prediction model",
            height=100
        )
        
        st.markdown("---")
        
        # Contact info
        st.subheader("📧 Contact Information")
        email = st.text_input("Email", placeholder="your.email@example.com")
        linkedin = st.text_input("LinkedIn URL", placeholder="https://linkedin.com/in/yourprofile")
        github = st.text_input("GitHub URL", placeholder="https://github.com/yourprofile")
        
        st.markdown("---")
        
        # Template selection
        st.subheader("🎨 Choose Template")
        template_choice = st.selectbox(
            "Portfolio Style",
            options=list(TEMPLATES.keys())
        )
        
        st.markdown("---")
        
        # Generate button
        generate_btn = st.button("✨ Generate Portfolio", type="primary")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🤖 AI-Generated Content")
        
        if generate_btn:
            # Validation with specific error messages
            if not name or not role or not skills or not projects:
                st.error("⚠️ Please fill in all required fields (marked with *)")
                
                # Show specific missing fields
                missing_fields = []
                if not name:
                    missing_fields.append("Full Name")
                if not role:
                    missing_fields.append("Professional Role")
                if not skills:
                    missing_fields.append("Skills")
                if not projects:
                    missing_fields.append("Key Projects")
                
                for field in missing_fields:
                    st.warning(f"• Missing: {field}")
            else:
                with st.spinner("🔮 AI is crafting your portfolio..."):
                    # Prepare user data
                    user_data = {
                        "name": name,
                        "role": role,
                        "skills": skills,
                        "experience": experience,
                        "projects": projects
                    }
                    
                    try:
                        # Generate content using AI
                        ai_generator = AIPortfolioGenerator()
                        result = ai_generator.generate_portfolio_content(user_data)
                        
                        if result["success"]:
                            st.session_state.generated_content = result["content"]
                            
                            # Parse AI response
                            parsed_data = parse_ai_response(result["content"])
                            
                            # Prepare data for template
                            portfolio_data = {
                                "name": name,
                                "headline": parsed_data.get("HEADLINE", role),
                                "bio": parsed_data.get("PROFESSIONAL_BIO", ""),
                                "about": parsed_data.get("ABOUT_SECTION", ""),
                                "skills_description": parsed_data.get("SKILLS_DESCRIPTION", {}),
                                "email": email,
                                "linkedin": linkedin,
                                "github": github
                            }
                            
                            # Generate HTML
                            html = get_template(template_choice, portfolio_data)
                            st.session_state.html_output = html
                            
                            st.success(f"✅ Portfolio generated! Used {result['tokens_used']} tokens")
                        else:
                            st.error(f"❌ Error: {result['error']}")
                            st.info("💡 Tip: Check your internet connection and API key")
                    
                    except Exception as e:
                        st.error(f"❌ Unexpected error: {str(e)}")
                        st.info("💡 Try refreshing the page or checking your .env file")
        
        # Display generated content
        if st.session_state.generated_content:
            st.markdown('<div class="success-box">✨ Content generated successfully!</div>', unsafe_allow_html=True)
            with st.expander("View Raw AI Output", expanded=False):
                st.code(st.session_state.generated_content, language="json")
    
    with col2:
        st.subheader("👁️ Portfolio Preview")
        
        if st.session_state.html_output:
            # Show preview
            st.components.v1.html(st.session_state.html_output, height=600, scrolling=True)
            
            # Download button - only if we have a name
            if name:
                safe_name = name.replace(' ', '_').lower()
                st.download_button(
                    label="📥 Download Portfolio HTML",
                    data=st.session_state.html_output,
                    file_name=f"portfolio_{safe_name}.html",
                    mime="text/html",
                    help="Download your portfolio as an HTML file"
                )
            else:
                st.warning("⚠️ Please enter your name to enable download")
        else:
            st.info("👈 Fill in your details and click 'Generate Portfolio' to see the magic!")
            
            # Show example
            with st.expander("📖 See Example", expanded=False):
                st.markdown("""
                **Example Input:**
                - **Name:** Syed Ebad
                - **Role:** Machine Learning Engineer
                - **Skills:** Python, PyTorch, TensorFlow, NLP, Gen AI
                - **Experience:** 5+ years
                - **Projects:** Pregni Sense, Transformer from Scratch
                
                The AI will generate a complete portfolio with bio, headline, and detailed skill descriptions!
                """)


if __name__ == "__main__":
    main()
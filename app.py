# app.py - Complete Quantum Prompt Optimizer Application
# This is your main application file

import streamlit as st
import requests
import json
import time
import random
from datetime import datetime
from typing import List, Dict, Optional

# ============= QUANTUM RANDOM SERVICE =============
class QuantumRandomService:
    """Handles all quantum random number generation"""
    
    def __init__(self):
        self.api_calls_count = 0
        self.last_error = None
        
    def get_quantum_random(self, num_bytes: int = 10) -> Dict:
        """Get quantum random numbers with automatic fallback"""
        
        # Try ANU Quantum first
        try:
            return self._get_anu_quantum(num_bytes)
        except Exception as e:
            st.warning(f"ANU Quantum unavailable, using Random.org")
            
        # Fallback to Random.org
        try:
            return self._get_random_org(num_bytes)
        except Exception as e:
            st.error(f"All services down, using secure random")
            return self._get_secure_random(num_bytes)
    
    def _get_anu_quantum(self, num_bytes: int) -> Dict:
        """Get quantum random from ANU"""
        url = "https://qrng.anu.edu.au/API/jsonI.php"
        params = {
            "length": num_bytes,
            "type": "uint8"
        }
        
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if not data.get("success", False):
            raise Exception("ANU API returned error")
            
        self.api_calls_count += 1
        
        return {
            "random_bytes": data["data"],
            "source": "🔬 ANU Quantum Lab",
            "source_detail": "Quantum vacuum fluctuations",
            "true_quantum": True,
            "timestamp": datetime.now().isoformat()
        }
    
    def _get_random_org(self, num_bytes: int) -> Dict:
        """Get random from Random.org atmospheric noise"""
        url = "https://www.random.org/integers/"
        params = {
            "num": num_bytes,
            "min": 0,
            "max": 255,
            "col": 1,
            "base": 10,
            "format": "plain",
            "rnd": "new"
        }
        
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        
        numbers = [int(x) for x in response.text.strip().split('\n') if x]
        self.api_calls_count += 1
        
        return {
            "random_bytes": numbers,
            "source": "🌩️ Random.org",
            "source_detail": "Atmospheric noise",
            "true_quantum": False,
            "timestamp": datetime.now().isoformat()
        }
    
    def _get_secure_random(self, num_bytes: int) -> Dict:
        """Fallback to cryptographically secure random"""
        import secrets
        
        return {
            "random_bytes": [secrets.randbits(8) for _ in range(num_bytes)],
            "source": "🔒 Secure Random",
            "source_detail": "Cryptographic pseudorandom (fallback)",
            "true_quantum": False,
            "timestamp": datetime.now().isoformat()
        }

# ============= PROMPT OPTIMIZER =============
class QuantumPromptOptimizer:
    """Core prompt optimization logic"""
    
    def __init__(self):
        self.qrng = QuantumRandomService()
        
        # Optimization techniques with templates
        self.techniques = {
            "step_by_step": {
                "name": "Step-by-Step Thinking",
                "template": "Let's think through this step-by-step:\n\n{prompt}",
                "description": "Encourages systematic reasoning"
            },
            "expert_role": {
                "name": "Expert Perspective",
                "template": "As an expert in this domain, provide a comprehensive answer:\n\n{prompt}",
                "description": "Invokes domain expertise"
            },
            "examples": {
                "name": "With Examples",
                "template": "{prompt}\n\nPlease include specific examples to illustrate your points.",
                "description": "Adds concrete examples"
            },
            "structured": {
                "name": "Structured Format",
                "template": "{prompt}\n\nOrganize your response with:\n• Clear headings\n• Bullet points for key ideas\n• A summary at the end",
                "description": "Improves readability"
            },
            "reasoning": {
                "name": "Show Reasoning",
                "template": "{prompt}\n\nExplain your reasoning and thought process throughout your answer.",
                "description": "Makes logic transparent"
            },
            "pros_cons": {
                "name": "Balanced Analysis",
                "template": "{prompt}\n\nProvide a balanced view including:\n- Pros/Benefits\n- Cons/Limitations\n- Overall recommendation",
                "description": "Ensures balanced perspective"
            },
            "eli5": {
                "name": "Simple Then Deep",
                "template": "{prompt}\n\nFirst explain in simple terms (ELI5), then provide a more detailed technical explanation.",
                "description": "Accessible to all levels"
            },
            "actionable": {
                "name": "Actionable Advice",
                "template": "{prompt}\n\nFocus on practical, actionable advice with clear next steps.",
                "description": "Emphasizes practicality"
            },
            "critical": {
                "name": "Critical Analysis",
                "template": "{prompt}\n\nApply critical thinking: question assumptions, consider alternatives, and note limitations.",
                "description": "Deeper analytical thinking"
            },
            "concise": {
                "name": "Concise Response",
                "template": "{prompt}\n\nBe concise but comprehensive. Avoid unnecessary details while covering all important points.",
                "description": "Efficient communication"
            }
        }
    
    def generate_variations(self, base_prompt: str, num_variations: int = 5) -> List[Dict]:
        """Generate prompt variations using quantum randomness"""
        
        variations = []
        used_combinations = set()
        
        for i in range(num_variations):
            # Get quantum random data
            quantum_data = self.qrng.get_quantum_random(num_bytes=20)
            
            # Select techniques using quantum randomness
            selected_techniques = self._select_techniques(
                quantum_data["random_bytes"],
                used_combinations
            )
            
            # Apply techniques to create variation
            optimized_prompt = self._apply_techniques(base_prompt, selected_techniques)
            
            # Create variation object
            variation = {
                "id": i + 1,
                "prompt": optimized_prompt,
                "techniques": selected_techniques,
                "technique_names": [self.techniques[t]["name"] for t in selected_techniques],
                "quantum_source": quantum_data["source"],
                "quantum_verified": quantum_data["true_quantum"],
                "timestamp": quantum_data["timestamp"]
            }
            
            variations.append(variation)
            used_combinations.add(tuple(sorted(selected_techniques)))
        
        return variations
    
    def _select_techniques(self, quantum_bytes: List[int], used_combinations: set) -> List[str]:
        """Use quantum randomness to select optimization techniques"""
        
        max_attempts = 10
        attempt = 0
        
        while attempt < max_attempts:
            # Number of techniques to apply (1-3)
            num_techniques = (quantum_bytes[0] % 3) + 1
            
            # Select specific techniques
            available_techniques = list(self.techniques.keys())
            selected = []
            
            for i in range(num_techniques):
                if i + 1 < len(quantum_bytes) and available_techniques:
                    idx = quantum_bytes[i + 1] % len(available_techniques)
                    technique = available_techniques[idx]
                    selected.append(technique)
                    available_techniques.remove(technique)
            
            # Check if this combination was already used
            combination = tuple(sorted(selected))
            if combination not in used_combinations:
                return selected
            
            # Shift quantum bytes for next attempt
            quantum_bytes = quantum_bytes[1:] + [quantum_bytes[0]]
            attempt += 1
        
        # Fallback: return any valid combination
        return selected[:num_techniques] if selected else ["step_by_step"]
    
    def _apply_techniques(self, base_prompt: str, techniques: List[str]) -> str:
        """Apply selected techniques to create optimized prompt"""
        
        result = base_prompt
        
        # Apply techniques in order
        for technique in techniques:
            if technique in self.techniques:
                template = self.techniques[technique]["template"]
                result = template.format(prompt=result)
        
        return result

# ============= STREAMLIT UI =============
def main():
    # Page configuration
    st.set_page_config(
        page_title="Quantum Prompt Optimizer",
        page_icon="⚛️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
        .stButton > button {
            width: 100%;
            background-color: #6366f1;
            color: white;
        }
        .stButton > button:hover {
            background-color: #4f46e5;
        }
        .success-box {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #f0fdf4;
            border: 1px solid #86efac;
        }
        .warning-box {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #fef3c7;
            border: 1px solid #fbbf24;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'variations' not in st.session_state:
        st.session_state.variations = None
    if 'optimizer' not in st.session_state:
        st.session_state.optimizer = QuantumPromptOptimizer()
    if 'generation_count' not in st.session_state:
        st.session_state.generation_count = 0
    
    # Header
    st.title("⚛️ Quantum Prompt Optimizer")
    st.markdown("### Transform your prompts using TRUE quantum randomness")
    
    # Sidebar
    with st.sidebar:
        st.header("🔬 About Quantum Randomness")
        
        st.info(
            "**What makes this quantum?**\n\n"
            "We use real quantum random numbers from:\n"
            "• **ANU Quantum Lab**: Measures quantum vacuum fluctuations\n"
            "• **Random.org**: Uses atmospheric noise\n\n"
            "Unlike computer-generated 'random' numbers, these are truly unpredictable!"
        )
        
        st.header("🎯 How It Works")
        st.write(
            "1. **Quantum Selection**: Quantum randomness selects optimization techniques\n"
            "2. **Unique Combinations**: Each variation uses different technique combinations\n"
            "3. **Better Results**: Discover prompt optimizations you'd never think of!"
        )
        
        st.header("📊 Session Stats")
        st.metric("Optimizations Generated", st.session_state.generation_count)
        st.metric("API Calls Made", st.session_state.optimizer.qrng.api_calls_count)
        
        # Add a fun quantum fact
        st.header("🤓 Quantum Fact")
        facts = [
            "A quantum bit can be 0 and 1 at the same time!",
            "Quantum entanglement was called 'spooky action at a distance' by Einstein",
            "The ANU quantum RNG measures quantum vacuum fluctuations",
            "Quantum computers could break current encryption methods",
            "Schrödinger's cat is both alive and dead until observed"
        ]
        if st.button("🎲 New Fact"):
            import random
            st.info(random.choice(facts))
    
    # Main content area
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.header("📝 Input Prompt")
        
        # Prompt input
        user_prompt = st.text_area(
            "Enter your prompt to optimize:",
            height=200,
            placeholder="Example: Explain how machine learning works\n\nOr try: Write a blog post about climate change\n\nOr: Help me understand quantum computing",
            help="This is the prompt you want to optimize for better AI responses"
        )
        
        # Number of variations
        num_variations = st.slider(
            "Number of variations to generate:",
            min_value=3,
            max_value=10,
            value=5,
            help="More variations = more diverse optimization approaches"
        )
        
        # Generate button
        if st.button("⚛️ Generate Quantum Variations", type="primary", disabled=not user_prompt):
            with st.spinner("🌌 Accessing quantum random sources..."):
                # Generate variations
                variations = st.session_state.optimizer.generate_variations(
                    user_prompt,
                    num_variations
                )
                
                # Store in session state
                st.session_state.variations = variations
                st.session_state.original_prompt = user_prompt
                st.session_state.generation_count += 1
                
                # Success message
                st.success(f"✅ Generated {num_variations} quantum-optimized variations!")
                
                # Show which source was used
                sources_used = set(v["quantum_source"] for v in variations)
                for source in sources_used:
                    st.caption(f"Powered by: {source}")
    
    with col2:
        st.header("⚡ Optimized Variations")
        
        if st.session_state.variations:
            # Add download all button
            all_prompts = "\n\n---\n\n".join([
                f"Variation {v['id']} ({', '.join(v['technique_names'])}):\n{v['prompt']}"
                for v in st.session_state.variations
            ])
            
            st.download_button(
                label="📥 Download All Variations",
                data=all_prompts,
                file_name=f"quantum_prompts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
            
            # Display each variation
            for variation in st.session_state.variations:
                with st.expander(
                    f"Variation {variation['id']}: {', '.join(variation['technique_names'])}", 
                    expanded=(variation['id'] == 1)
                ):
                    # Quantum verification badge
                    if variation["quantum_verified"]:
                        st.markdown(
                            '<div class="success-box">✅ <b>TRUE Quantum Random</b> - '
                            f'Source: {variation["quantum_source"]}</div>',
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            '<div class="warning-box">⚡ <b>Physical Random</b> - '
                            f'Source: {variation["quantum_source"]}</div>',
                            unsafe_allow_html=True
                        )
                    
                    # Show the optimized prompt
                    st.code(variation["prompt"], language=None)
                    
                    # Technique descriptions
                    st.caption("**Techniques applied:**")
                    for tech in variation["techniques"]:
                        tech_info = st.session_state.optimizer.techniques[tech]
                        st.caption(f"• {tech_info['name']}: {tech_info['description']}")
                    
                    # Copy button (using columns for layout)
                    c1, c2, c3 = st.columns([1, 1, 1])
                    with c2:
                        if st.button("📋 Copy This", key=f"copy_{variation['id']}"):
                            # Note: Streamlit doesn't have clipboard access
                            # In production, you'd use JavaScript
                            st.info("Select the text above and copy it!")
        else:
            st.info("👈 Enter a prompt and click 'Generate' to see quantum-optimized variations!")
            
            # Show example
            st.markdown("### Example Results")
            st.code(
                "Original: Explain machine learning\n\n"
                "Optimized: Let's think through this step-by-step:\n\n"
                "As an expert in this domain, provide a comprehensive answer:\n\n"
                "Explain machine learning\n\n"
                "Please include specific examples to illustrate your points.",
                language=None
            )

# ============= RUN THE APP =============
if __name__ == "__main__":
    main()

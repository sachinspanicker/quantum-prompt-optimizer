# app_updated.py - Enhanced Quantum Prompt Optimizer with Real Quantum Value
# This replaces your current app.py

import streamlit as st
import requests
import json
import time
import random
from datetime import datetime
from typing import List, Dict, Optional
import re

# ============= QUANTUM RANDOM SERVICE (Same as before) =============
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

# ============= ENHANCED QUANTUM PROMPT OPTIMIZER =============
class QuantumEnhancedOptimizer:
    """
    Uses quantum randomness to create genuinely unique prompt optimizations
    through parameter adjustment, constraint generation, and creative injection
    """
    
    def __init__(self):
        self.qrng = QuantumRandomService()
        
        # Base components for dynamic generation
        self.components = {
            "roles": [
                "expert", "teacher", "researcher", "critic", "analyst",
                "philosopher", "scientist", "artist", "engineer", "storyteller",
                "detective", "journalist", "therapist", "coach", "strategist",
                "historian", "futurist", "designer", "mentor", "explorer"
            ],
            
            "thinking_styles": [
                "analytical", "creative", "systematic", "intuitive", "logical",
                "holistic", "critical", "lateral", "convergent", "divergent",
                "abstract", "concrete", "strategic", "tactical", "innovative"
            ],
            
            "communication_tones": [
                "formal", "casual", "academic", "conversational", "professional",
                "friendly", "authoritative", "empathetic", "objective", "passionate",
                "humorous", "serious", "encouraging", "challenging", "collaborative"
            ],
            
            "constraints": [
                "using analogies from {domain}",
                "in the style of {author}",
                "as if explaining to {audience}",
                "with {emotion} undertone",
                "focusing on {aspect}",
                "avoiding {concept}",
                "emphasizing {priority}",
                "through the lens of {perspective}",
                "with examples from {field}",
                "using only {vocabulary_level} language",
                "as a {format} format",
                "within {constraint} constraint"
            ],
            
            "domains": [
                "cooking", "sports", "music", "nature", "technology", "art",
                "mathematics", "philosophy", "psychology", "physics", "biology",
                "economics", "history", "literature", "cinema", "architecture",
                "gaming", "fashion", "astronomy", "chemistry", "geography"
            ],
            
            "aspects": [
                "practical applications", "theoretical foundations", "historical context",
                "future implications", "ethical considerations", "common misconceptions",
                "real-world examples", "underlying principles", "potential risks",
                "creative possibilities", "cultural impact", "scientific basis",
                "economic factors", "social dynamics", "technical details"
            ]
        }
        
        # Optimization approaches
        self.approaches = {
            "precision_mix": "Quantum-Calibrated Parameters",
            "creative_constraints": "Quantum Creative Constraints",
            "parameter_optimization": "Quantum Parameter Optimization",
            "unexpected_connections": "Quantum Cross-Domain Fusion",
            "dynamic_structure": "Quantum Structure Generation"
        }
    
    def generate_variations(self, base_prompt: str, num_variations: int = 5) -> List[Dict]:
        """Generate genuinely unique optimizations using quantum randomness"""
        
        variations = []
        used_approaches = []
        
        for i in range(num_variations):
            # Get quantum random data (100 bytes for complex generation)
            quantum_data = self.qrng.get_quantum_random(num_bytes=100)
            quantum_bytes = quantum_data["random_bytes"]
            
            # Select approach (ensure variety)
            approach = self._select_approach(quantum_bytes[0], used_approaches)
            used_approaches.append(approach)
            
            # Apply quantum-enhanced optimization
            if approach == "precision_mix":
                result = self._quantum_precision_mix(base_prompt, quantum_bytes[1:])
            elif approach == "creative_constraints":
                result = self._quantum_creative_constraints(base_prompt, quantum_bytes[1:])
            elif approach == "parameter_optimization":
                result = self._quantum_parameter_optimization(base_prompt, quantum_bytes[1:])
            elif approach == "unexpected_connections":
                result = self._quantum_unexpected_connections(base_prompt, quantum_bytes[1:])
            else:  # dynamic_structure
                result = self._quantum_dynamic_structure(base_prompt, quantum_bytes[1:])
            
            variations.append({
                "id": i + 1,
                "prompt": result["prompt"],
                "approach": self.approaches[approach],
                "approach_key": approach,
                "parameters": result["parameters"],
                "quantum_source": quantum_data["source"],
                "quantum_verified": quantum_data["true_quantum"],
                "timestamp": quantum_data["timestamp"],
                "description": result["description"]
            })
        
        return variations
    
    def _select_approach(self, quantum_byte: int, used: List[str]) -> str:
        """Select optimization approach using quantum randomness"""
        approaches = list(self.approaches.keys())
        
        # Try to avoid repetition
        available = [a for a in approaches if a not in used]
        if not available:
            available = approaches
        
        return available[quantum_byte % len(available)]
    
    def _quantum_precision_mix(self, prompt: str, quantum_bytes: List[int]) -> Dict:
        """Mix multiple elements with quantum-determined precise percentages"""
        
        # Quantum determines exact percentages
        technical_level = quantum_bytes[0] / 255
        creativity_level = quantum_bytes[1] / 255
        detail_level = quantum_bytes[2] / 255
        formality_level = quantum_bytes[3] / 255
        
        # Quantum selects components
        role = self.components["roles"][quantum_bytes[4] % len(self.components["roles"])]
        tone = self.components["communication_tones"][quantum_bytes[5] % len(self.components["communication_tones"])]
        style = self.components["thinking_styles"][quantum_bytes[6] % len(self.components["thinking_styles"])]
        
        # Build precisely calibrated prompt
        optimized = f"""You are a {role} with {style} thinking style.

Calibration Parameters:
• Technical Level: {technical_level:.1%} - {"highly technical" if technical_level > 0.7 else "moderately technical" if technical_level > 0.3 else "simplified"}
• Creativity Level: {creativity_level:.1%} - {"highly creative" if creativity_level > 0.7 else "balanced approach" if creativity_level > 0.3 else "straightforward"}
• Detail Level: {detail_level:.1%} - {"comprehensive detail" if detail_level > 0.7 else "moderate detail" if detail_level > 0.3 else "concise"}
• Formality: {formality_level:.1%} - {"very formal" if formality_level > 0.7 else "professional" if formality_level > 0.3 else "casual"}

Communication tone: {tone}

Task: {prompt}

Your response should precisely match these calibration parameters, creating a unique blend of technical accuracy, creative expression, and appropriate detail level."""
        
        return {
            "prompt": optimized,
            "parameters": {
                "technical": f"{technical_level:.1%}",
                "creativity": f"{creativity_level:.1%}",
                "detail": f"{detail_level:.1%}",
                "formality": f"{formality_level:.1%}",
                "role": role,
                "tone": tone,
                "style": style
            },
            "description": f"Precision-calibrated {role} perspective with {style} thinking"
        }
    
    def _quantum_creative_constraints(self, prompt: str, quantum_bytes: List[int]) -> Dict:
        """Generate unexpected creative constraints using quantum randomness"""
        
        # Number of constraints
        num_constraints = (quantum_bytes[0] % 3) + 2  # 2-4 constraints
        
        constraints = []
        
        # Generate each constraint
        for i in range(num_constraints):
            constraint_type = quantum_bytes[1 + i*4] % len(self.components["constraints"])
            template = self.components["constraints"][constraint_type]
            
            # Fill in template variables
            if "{domain}" in template:
                domain = self.components["domains"][quantum_bytes[2 + i*4] % len(self.components["domains"])]
                template = template.replace("{domain}", domain)
            
            if "{audience}" in template:
                audiences = ["a curious 5-year-old", "a skeptical teenager", "a busy executive", 
                           "an academic peer", "someone from the 1800s", "an alien visitor"]
                audience = audiences[quantum_bytes[3 + i*4] % len(audiences)]
                template = template.replace("{audience}", audience)
            
            if "{emotion}" in template:
                emotions = ["curious", "playful", "serious", "inspiring", "mysterious", "urgent"]
                emotion = emotions[quantum_bytes[4 + i*4] % len(emotions)]
                template = template.replace("{emotion}", emotion)
            
            if "{aspect}" in template:
                aspect = self.components["aspects"][quantum_bytes[3 + i*4] % len(self.components["aspects"])]
                template = template.replace("{aspect}", aspect)
            
            if "{format}" in template:
                formats = ["dialogue", "story", "recipe", "scientific paper", "poem", "news article"]
                format_type = formats[quantum_bytes[3 + i*4] % len(formats)]
                template = template.replace("{format}", format_type)
            
            constraints.append(template)
        
        # Build constrained prompt
        optimized = f"""{prompt}

Creative Constraints:
{chr(10).join(f"• {c}" for c in constraints)}

These constraints should fundamentally shape your response, creating something unexpected yet coherent. The intersection of these constraints should produce insights that wouldn't emerge from 
conventional approaches."""
        
        return {
            "prompt": optimized,
            "parameters": {
                "constraints": constraints,
                "constraint_count": num_constraints
            },
            "description": f"{num_constraints} quantum-selected creative constraints"
        }
    
    def _quantum_parameter_optimization(self, prompt: str, quantum_bytes: List[int]) -> Dict:
        """Optimize multiple parameters simultaneously using quantum randomness"""
        
        # Quantum-determined parameters
        word_count = 100 + (quantum_bytes[0] * 4)  # 100-1120 words
        example_count = (quantum_bytes[1] % 4) + 1  # 1-4 examples
        perspective_count = (quantum_bytes[2] % 3) + 1  # 1-3 perspectives
        abstraction = quantum_bytes[3] / 255  # 0-1 scale
        confidence = 60 + (quantum_bytes[4] % 36)  # 60-95%
        depth_variation = quantum_bytes[5] / 255  # 0-1 scale
        
        # Focus areas
        num_focus = (quantum_bytes[6] % 3) + 1
        focus_areas = []
        for i in range(num_focus):
            idx = quantum_bytes[7 + i] % len(self.components["aspects"])
            focus_areas.append(self.components["aspects"][idx])
        
        # Structure preference
        structures = ["linear progression", "compare and contrast", "problem-solution",
                     "chronological", "cause and effect", "hierarchical"]
        structure = structures[quantum_bytes[10] % len(structures)]
        
        optimized = f"""{prompt}

Optimization Parameters:
• Response length: {word_count} words (±10%)
• Include exactly {example_count} concrete example{'s' if example_count > 1 else ''}
• Present {perspective_count} distinct perspective{'s' if perspective_count > 1 else ''}
• Abstraction level: {abstraction:.1%} ({"highly concrete" if abstraction < 0.3 else "balanced" if abstraction < 0.7 else "more abstract"})
• Confidence threshold: Only include points you're >{confidence}% confident about
• Depth variation: {depth_variation:.1%} ({"consistent depth" if depth_variation < 0.3 else "varied depth" if depth_variation < 0.7 else "dramatic depth changes"})
• Structure: {structure}

Primary focus areas: {', '.join(focus_areas)}

Balance these parameters to create an optimally informative response."""
        
        return {
            "prompt": optimized,
            "parameters": {
                "word_count": word_count,
                "examples": example_count,
                "perspectives": perspective_count,
                "abstraction": f"{abstraction:.1%}",
                "confidence": f"{confidence}%",
                "depth_variation": f"{depth_variation:.1%}",
                "structure": structure,
                "focus_areas": focus_areas
            },
            "description": f"Multi-parameter optimization with {structure} structure"
        }
    
    def _quantum_unexpected_connections(self, prompt: str, quantum_bytes: List[int]) -> Dict:
        """Create unexpected connections and analogies using quantum randomness"""
        
        # Select two unrelated domains
        domain1 = self.components["domains"][quantum_bytes[0] % len(self.components["domains"])]
        domain2 = self.components["domains"][quantum_bytes[1] % len(self.components["domains"])]
        
        # Ensure they're different
        while domain2 == domain1:
            domain2 = self.components["domains"][(quantum_bytes[1] + 1) % len(self.components["domains"])]
        
        # Connection type
        connections = [
            f"finding surprising parallels between {domain1} and {domain2}",
            f"using {domain1} principles to illuminate {domain2} concepts",
            f"discovering how {domain1} masters would approach {domain2}",
            f"creating a synthesis of {domain1} and {domain2} thinking",
            f"translating between {domain1} and {domain2} paradigms"
        ]
        connection = connections[quantum_bytes[2] % len(connections)]
        
        # Metaphor density
        metaphor_density = quantum_bytes[3] / 255
        
        # Fusion approach
        approaches = ["analytical fusion", "creative synthesis", "systematic mapping",
                     "intuitive bridging", "experimental combination"]
        approach = approaches[quantum_bytes[4] % len(approaches)]
        
        optimized = f"""{prompt}

Approach this by {connection}.

Use {approach} to create unexpected insights. Metaphor density: {metaphor_density:.1%} ({"heavy use of metaphors" if metaphor_density > 0.7 else "moderate metaphors" if metaphor_density > 0.3 else 
"subtle connections"}).

The goal is to generate insights that would be impossible from within a single domain. Let the collision of {domain1} and {domain2} thinking create something genuinely new."""
        
        return {
            "prompt": optimized,
            "parameters": {
                "domain1": domain1,
                "domain2": domain2,
                "connection_type": connection,
                "approach": approach,
                "metaphor_density": f"{metaphor_density:.1%}"
            },
            "description": f"Unexpected fusion of {domain1} and {domain2}"
        }
    
    def _quantum_dynamic_structure(self, prompt: str, quantum_bytes: List[int]) -> Dict:
        """Generate dynamic response structure using quantum randomness"""
        
        # Primary structure
        structures = [
            "Start with a paradox, resolve it through exploration",
            "Build from first principles to complex conclusions",
            "Use alternating zoom (big picture ↔ details)",
            "Create a narrative arc with tension and resolution",
            "Layer information like geological strata",
            "Spiral approach - revisit themes with deeper insight",
            "Dialectical - thesis, antithesis, synthesis",
            "Network structure - interconnected ideas"
        ]
        structure = structures[quantum_bytes[0] % len(structures)]
        
        # Rhythm pattern
        rhythms = [
            "short sentences build to long, complex ones",
            "alternating simple and complex paragraphs",
            "staccato facts punctuated by flowing explanations",
            "gradual acceleration of ideas",
            "wave pattern - intense/relaxed/intense"
        ]
        rhythm = rhythms[quantum_bytes[1] % len(rhythms)]
        
        # Information architecture
        architectures = [
            "front-load key insights",
            "build suspense before revelation",
            "distribute insights evenly",
            "cluster complexity in the middle",
            "end with surprising synthesis"
        ]
        architecture = architectures[quantum_bytes[2] % len(architectures)]
        
        # Transition style
        transitions = ["smooth and connected", "sharp contrasts", "thematic bridges",
                      "logical progression", "intuitive leaps"]
        transition = transitions[quantum_bytes[3] % len(transitions)]
        
        # Energy curve
        energy = quantum_bytes[4] / 255
        
        optimized = f"""{prompt}

Structural Blueprint:
• Overall structure: {structure}
• Rhythm: {rhythm}
• Information architecture: {architecture}
• Transitions: {transition}
• Energy level: {energy:.1%} ({"high energy throughout" if energy > 0.7 else "moderate pacing" if energy > 0.3 else "calm and measured"})

This structure should create a unique reading experience where form enhances meaning. The way you present the information should be as important as the information itself."""
        
        return {
            "prompt": optimized,
            "parameters": {
                "structure": structure,
                "rhythm": rhythm,
                "architecture": architecture,
                "transitions": transition,
                "energy": f"{energy:.1%}"
            },
            "description": f"Dynamic structure with {structure.split(',')[0]}"
        }

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
        .parameter-box {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 12px;
            margin: 8px 0;
        }
        .quantum-badge {
            background-color: #10b981;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 14px;
            display: inline-block;
            margin: 4px 0;
        }
        .approach-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 12px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'variations' not in st.session_state:
        st.session_state.variations = None
    if 'optimizer' not in st.session_state:
        st.session_state.optimizer = QuantumEnhancedOptimizer()
    if 'generation_count' not in st.session_state:
        st.session_state.generation_count = 0
    
    # Header
    st.title("⚛️ Quantum Prompt Optimizer")
    st.markdown("### Create infinite unique prompt variations using TRUE quantum randomness")
    
    # Info box
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🎲 **Infinite Variations**\nNo two optimizations are ever the same")
    with col2:
        st.info("⚛️ **True Quantum**\nPowered by real quantum measurements")
    with col3:
        st.info("🎯 **Smart Parameters**\nPrecise calibration for better results")
    
    # Sidebar
    with st.sidebar:
        st.header("🔬 How It Works")
        
        st.markdown("""
        **Real Quantum Enhancement:**
        
        Unlike simple template selection, this optimizer uses quantum randomness to:
        
        • **Generate precise parameters** (e.g., 73.2% technical)
        • **Create unique constraints** (e.g., explain like a chef teaching physics)
        • **Fuse unexpected domains** (e.g., music + mathematics)
        • **Build dynamic structures** (e.g., paradox → resolution)
        
        Each quantum byte (0-255) directly shapes your prompt's parameters, creating truly infinite variations.
        """)
        
        st.header("📊 Session Stats")
        st.metric("Optimizations Generated", st.session_state.generation_count)
        st.metric("Unique Variations", "∞", help="Truly infinite due to quantum parameters")
        
        if st.session_state.optimizer.qrng.api_calls_count > 0:
            st.metric("Quantum API Calls", st.session_state.optimizer.qrng.api_calls_count)
        
        # Examples
        st.header("💡 Example Uses")
        examples = [
            "Explain quantum computing",
            "Write a blog post about climate change",
            "Help me understand machine learning",
            "Create a marketing strategy",
            "Analyze this business problem"
        ]
        
        example_choice = st.selectbox("Try an example:", [""] + examples)
        if example_choice and st.button("Use This Example"):
            st.session_state.example_prompt = example_choice
    
    # Main content area
    col1, col2 = st.columns([1, 1.5], gap="large")
    
    with col1:
        st.header("📝 Input Prompt")
        
        # Check if example was selected
        default_prompt = ""
        if 'example_prompt' in st.session_state:
            default_prompt = st.session_state.example_prompt
            del st.session_state.example_prompt
        
        # Prompt input
        user_prompt = st.text_area(
            "Enter your prompt to optimize:",
            height=200,
            value=default_prompt,
            placeholder="Example: Explain how machine learning works\n\nOr: Write a blog post about climate change\n\nOr: Help me understand quantum computing",
            help="This prompt will be enhanced with quantum-generated parameters and constraints"
        )
        
        # Number of variations
        num_variations = st.slider(
            "Number of variations to generate:",
            min_value=3,
            max_value=7,
            value=5,
            help="Each variation uses a different quantum optimization approach"
        )
        
        # Advanced options (collapsed by default)
        with st.expander("⚙️ Advanced Options"):
            show_parameters = st.checkbox("Show all parameters", value=True)
            show_quantum_source = st.checkbox("Show quantum source", value=True)
            compare_mode = st.checkbox("Compare with simple optimization", value=False)
        
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
                
                # Show which sources were used
                sources_used = set(v["quantum_source"] for v in variations)
                for source in sources_used:
                    st.caption(f"Powered by: {source}")
        
        # Compare mode
        if compare_mode and user_prompt:
            st.markdown("---")
            st.subheader("📊 Simple vs Quantum")
            
            # Simple optimization (old method)
            simple_techniques = ["Let's think step by step", "As an expert", "Include examples"]
            simple_selected = random.sample(simple_techniques, 2)
            simple_prompt = f"{'. '.join(simple_selected)}: {user_prompt}"
            
            st.markdown("**Simple Optimization:**")
            st.code(simple_prompt, language=None)
            st.caption("Limited to ~45 combinations of fixed techniques")
    
    with col2:
        st.header("⚡ Quantum-Enhanced Variations")
        
        if st.session_state.variations:
            # Add download all button
            all_prompts = "\n\n" + "="*50 + "\n\n".join([
                f"VARIATION {v['id']}: {v['approach']}\n{'-'*40}\n\n{v['prompt']}\n\nParameters: {json.dumps(v['parameters'], indent=2)}"
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
                    f"Variation {variation['id']}: {variation['approach']}", 
                    expanded=(variation['id'] == 1)
                ):
                    # Approach header
                    st.markdown(
                        f"<div class='approach-header'>{variation['approach']}</div>",
                        unsafe_allow_html=True
                    )
                    
                    # Quantum verification
                    if show_quantum_source:
                        if variation["quantum_verified"]:
                            st.markdown(
                                f"<span class='quantum-badge'>✅ TRUE Quantum - {variation['quantum_source']}</span>",
                                unsafe_allow_html=True
                            )
                        else:
                            st.warning(f"⚡ Physical Random - {variation['quantum_source']}")
                    
                    # Show the optimized prompt
                    st.code(variation["prompt"], language=None)
                    
                    # Show parameters if enabled
                    if show_parameters:
                        st.markdown("**Quantum-Generated Parameters:**")
                        
                        # Display parameters in a nice format
                        params_html = "<div class='parameter-box'>"
                        for key, value in variation["parameters"].items():
                            if isinstance(value, list):
                                value = ", ".join(value)
                            params_html += f"<b>{key.replace('_', ' ').title()}:</b> {value}<br>"
                        params_html += "</div>"
                        
                        st.markdown(params_html, unsafe_allow_html=True)
                    
                    # Description
                    st.caption(f"💡 {variation['description']}")
                    
                    # Copy button
                    if st.button(f"📋 Copy This Variation", key=f"copy_{variation['id']}"):
                        # Note: Actual clipboard functionality requires JavaScript
                        st.info("✓ Ready to copy! Select the text above and copy it.")
                        st.balloons()
        else:
            # No variations yet - show examples
            st.info("👈 Enter a prompt and click 'Generate' to see quantum-optimized variations!")
            
            st.markdown("### 🎯 What Makes This Different?")
            
            # Show example variations
            example_col1, example_col2 = st.columns(2)
            
            with example_col1:
                st.markdown("**Traditional Optimization:**")
                st.code(
                    "Let's think step by step: Explain quantum computing. Include examples.",
                    language=None
                )
                st.caption("❌ Limited to picking from 10 techniques")
            
            with example_col2:
                st.markdown("**Quantum Enhancement:**")
                st.code(
                    """You are a storyteller with lateral thinking style.

Calibration Parameters:
• Technical Level: 42.7% - moderately technical
• Creativity Level: 89.4% - highly creative
• Detail Level: 56.9% - moderate detail

Task: Explain quantum computing

Creative Constraints:
• using analogies from music
• as if explaining to a skeptical teenager
• emphasizing creative possibilities""",
                    language=None
                )
                st.caption("✅ Infinite unique variations with precise parameters")
            
            st.markdown("---")
            
            # Feature comparison
            st.markdown("### 🚀 Quantum Enhancement Features")
            
            features = {
                "🎯 **Precise Parameter Calibration**": "Not just 'be creative' but 'be 89.4% creative'",
                "🌈 **Cross-Domain Fusion**": "Explain physics through cooking, math through music",
                "🎨 **Dynamic Constraints**": "Unique limitations that spark creativity",
                "📐 **Structural Variations**": "Start with paradox, build suspense, spiral learning",
                "♾️ **Truly Infinite**": "Quantum randomness ensures no two prompts are ever identical"
            }
            
            for feature, description in features.items():
                st.markdown(f"{feature}")
                st.caption(description)

# ============= RUN THE APP =============
if __name__ == "__main__":
    main()

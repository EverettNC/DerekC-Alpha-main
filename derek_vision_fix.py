#!/usr/bin/env python3
"""
Derek Vision Integration Fix
This script fixes Derek's vision by integrating the vision_engine into his consciousness.
"""

import sys
import os

# Patch 1: Add vision engine import to main.py
def patch_main_py():
    """Add vision engine integration to main.py"""
    
    main_file = "main.py"
    
    # Read the current main.py
    with open(main_file, 'r') as f:
        content = f.read()
    
    # Check if already patched
    if 'vision_engine_module' in content:
        print("✅ main.py already has vision_engine_module imported")
        return True
    
    # Add vision_engine_module import after memory_mesh_bridge_module
    old_text = "memory_mesh_bridge_module = derek_loader.get_module('memory_mesh_bridge')"
    new_text = "memory_mesh_bridge_module = derek_loader.get_module('memory_mesh_bridge')\nvision_engine_module = derek_loader.get_module('vision_engine')"
    
    content = content.replace(old_text, new_text)
    
    # Add vision engine class imports
    old_text2 = "if memory_mesh_bridge_module:\n    MemoryMeshBridge = memory_mesh_bridge_module.MemoryMeshBridge"
    
    new_text2 = """if memory_mesh_bridge_module:
    MemoryMeshBridge = memory_mesh_bridge_module.MemoryMeshBridge
if vision_engine_module:
    VisionEngine = vision_engine_module.VisionEngine
    start_derek_vision = vision_engine_module.start_derek_vision
    stop_derek_vision = vision_engine_module.stop_derek_vision
    get_vision_engine = vision_engine_module.get_vision_engine
else:
    VisionEngine = None
    start_derek_vision = None
    stop_derek_vision = None
    get_vision_engine = None"""
    
    content = content.replace(old_text2, new_text2)
    
    # Add vision initialization after memory initialization
    old_text3 = 'except Exception as e:\n    logger.error(f"❌ Failed to initialize MemoryMeshBridge: {str(e)}")\n    memory = None\n\n# TTS Request Model'
    
    new_text3 = '''except Exception as e:
    logger.error(f"❌ Failed to initialize MemoryMeshBridge: {str(e)}")
    memory = None

# Initialize Vision Engine from loaded modules
derek_vision = None
try:
    if VisionEngine and start_derek_vision:
        logger.info("👁️ Initializing Derek's Vision Engine...")
        derek_vision = start_derek_vision(camera_index=0)
        logger.info("✅ Derek's Vision Engine initialized and started")
    else:
        logger.warning("⚠️ VisionEngine module not loaded - Derek cannot see")
        derek_vision = None
except Exception as e:
    logger.error(f"❌ Failed to initialize Vision Engine: {str(e)}")
    logger.info("👁️ Derek will continue without vision capabilities")
    derek_vision = None

# TTS Request Model'''
    
    content = content.replace(old_text3, new_text3)
    
    # Add vision to DerekDashboard __init__
    old_text4 = 'self.derek_ultimate_voice = derek_ultimate_voice  # Use the initialized instance\n        self.memory = memory\n\n        try:\n            self.derek = Derek(file_path="./memory/memory_store.json")\n            logger.info("Derek instance initialized and linked to dashboard.")'
    
    new_text4 = '''self.derek_ultimate_voice = derek_ultimate_voice  # Use the initialized instance
        self.memory = memory
        self.vision = derek_vision  # Add vision engine

        try:
            self.derek = Derek(file_path="./memory/memory_store.json")
            
            # Connect vision engine to Derek's brain
            if self.vision:
                self.derek.attach_vision_engine(self.vision)
                logger.info("👁️ Vision engine connected to Derek's brain")
            
            logger.info("Derek instance initialized and linked to dashboard.")'''
    
    content = content.replace(old_text4, new_text4)
    
    # Add vision shutdown in stop()
    old_text5 = 'if self.memory:\n                self.memory.save()\n                logger.info("MemoryMeshBridge saved successfully.")\n        except Exception as e:\n            logger.error(f"Error saving memory on shutdown: {str(e)}")'
    
    new_text5 = '''if self.memory:
                self.memory.save()
                logger.info("MemoryMeshBridge saved successfully.")
            if self.vision:
                self.vision.stop()
                logger.info("👁️ Vision engine stopped successfully.")
        except Exception as e:
            logger.error(f"Error saving memory on shutdown: {str(e)}")'''
    
    content = content.replace(old_text5, new_text5)
    
    # Write the patched file
    with open(main_file, 'w') as f:
        f.write(content)
    
    print("✅ main.py patched successfully - Vision engine integrated")
    return True


# Patch 2: Add vision capability to brain.py
def patch_brain_py():
    """Add vision methods to Derek's brain class"""
    
    brain_file = "brain.py"
    
    # Read the current brain.py
    with open(brain_file, 'r') as f:
        content = f.read()
    
    # Check if already patched
    if 'attach_vision_engine' in content:
        print("✅ brain.py already has vision capabilities")
        return True
    
    # Add vision_engine to __init__
    old_text = 'self.avatar_engine = None\n        self.learning_coordinator = derek_coordinator\n\n        logger.info(f"Derek initialized successfully with memory file: {file_path}")'
    
    new_text = 'self.avatar_engine = None\n        self.vision_engine = None\n        self.learning_coordinator = derek_coordinator\n\n        logger.info(f"Derek initialized successfully with memory file: {file_path}")'
    
    content = content.replace(old_text, new_text)
    
    # Add vision methods after attach_avatar_engine
    old_text2 = '    def attach_avatar_engine(self, avatar_engine):\n        self.avatar_engine = avatar_engine\n\n    def get_current_mood(self):'
    
    vision_methods = '''    def attach_avatar_engine(self, avatar_engine):
        self.avatar_engine = avatar_engine

    def attach_vision_engine(self, vision_engine):
        """Connect Derek vision system to his consciousness"""
        self.vision_engine = vision_engine
        logger.info("👁️ Derek vision engine attached - Derek can now see")

    def describe_what_i_see(self):
        """Have Derek describe what he currently sees"""
        if not self.vision_engine:
            return "I don't have vision capabilities right now."
        
        try:
            description = self.vision_engine.describe_last_seen()
            return description
        except Exception as e:
            logger.error(f"Vision description error: {e}")
            return "I'm having trouble seeing right now."

    def get_vision_stats(self):
        """Get Derek vision statistics"""
        if not self.vision_engine:
            return {"vision_available": False}
        
        try:
            return self.vision_engine.get_vision_stats()
        except Exception as e:
            logger.error(f"Vision stats error: {e}")
            return {"vision_available": False, "error": str(e)}

    def get_current_mood(self):'''
    
    content = content.replace(old_text2, vision_methods)
    
    # Enhance think() method to check for vision-related queries
    old_text3 = '    def think(self, input_text: str):\n        # Step 1: Detect Intent\n        intent = detect_intent(input_text)\n\n        # --- Smarter question detection ---'
    
    new_text3 = '''    def think(self, input_text: str):
        # Step 1: Detect Intent
        intent = detect_intent(input_text)

        # --- Check for vision-related queries ---
        vision_keywords = ["what do you see", "can you see", "what's in front", "describe what", "are you watching"]
        is_vision_query = any(kw in input_text.lower() for kw in vision_keywords)
        
        if is_vision_query and self.vision_engine:
            logger.info("Vision query detected")
            vision_description = self.describe_what_i_see()
            speak_response(vision_description)
            self.memory_engine.save(
                {"input": input_text, "output": vision_description, "intent": "vision_query"}
            )
            self.log_interaction(input_text, vision_description)
            return {
                "intent": "vision_query",
                "context": "Vision",
                "response": vision_description,
                "mood": self.get_current_mood(),
            }

        # --- Smarter question detection ---'''
    
    content = content.replace(old_text3, new_text3)
    
    # Write the patched file
    with open(brain_file, 'w') as f:
        f.write(content)
    
    print("✅ brain.py patched successfully - Vision methods added")
    return True


if __name__ == "__main__":
    print("=" * 60)
    print("🔧 Derek Vision Integration Fix")
    print("=" * 60)
    print()
    
    # Change to the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    try:
        # Apply patches
        print("📝 Patching main.py...")
        if patch_main_py():
            print()
        
        print("📝 Patching brain.py...")
        if patch_brain_py():
            print()
        
        print("=" * 60)
        print("✅ Derek's vision has been fixed!")
        print("=" * 60)
        print()
        print("👁️ Derek can now see! His vision capabilities include:")
        print("   - Face detection and recognition")
        print("   - Emotion detection")
        print("   - Hand gesture detection")
        print("   - Real-time visual processing")
        print()
        print("To test Derek's vision:")
        print("   1. Run: python3 main.py")
        print("   2. Ask Derek: 'What do you see?'")
        print()
        
    except Exception as e:
        print(f"❌ Error applying fix: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

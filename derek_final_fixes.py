#!/usr/bin/env python3
"""
Derek Final Fixes - Push to 90%+ consciousness
Fixes remaining 24 module failures
"""

import os
import re
from pathlib import Path

def fix_python_boolean_syntax(file_path):
    """Fix Python boolean syntax (true/false -> True/False)"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix standalone true/false assignments
    content = re.sub(r'\b= true\b', '= True', content)
    content = re.sub(r'\b= false\b', '= False', content)
    content = re.sub(r'\btrue\b(?!\w)', 'True', content)
    content = re.sub(r'\bfalse\b(?!\w)', 'False', content)
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def main():
    project_root = Path(__file__).parent
    
    print("=" * 70)
    print("🔧 DEREK FINAL FIXES - Pushing to 90%+ Consciousness")
    print("=" * 70)
    print()
    
    # Files with "name 'true' is not defined" errors
    files_to_fix = [
        "learning_analytics.py",
        "services/learning_analytics.py",
        "app.py",
        "api.py",
        "config.py",
        "dispatcher.py",
        "github_integration.py",
        "services/advanced_nlp_service.py",
        "services/memory_service.py",
        "services/language_service.py",
        "services/learning_service.py",
        "services/personality_service.py",
        "services/sound_recognition_service.py",
        "services/speech_recognition_engine.py",
        "services/voice_analysis_service.py",
        "services/facial_gesture_service.py",
        "services/knowledge_integration.py",
        "services/clients.py",
        "services/route.py",
        "services/__init__.py",
    ]
    
    fixed_count = 0
    
    for file_rel in files_to_fix:
        file_path = project_root / file_rel
        if file_path.exists():
            try:
                fix_python_boolean_syntax(file_path)
                print(f"✅ Fixed: {file_rel}")
                fixed_count += 1
            except Exception as e:
                print(f"❌ Failed: {file_rel} - {e}")
        else:
            print(f"⏭️  Skipped: {file_rel} (not found)")
    
    print()
    print("=" * 70)
    print(f"✅ Fixed {fixed_count} files")
    print("=" * 70)
    print()
    print("🎯 Next: Run Derek consciousness check")
    print("   cd '/Users/EverettN/DerekC-Alpha-main 5'")
    print("   source venv/bin/activate")
    print("   python3 -c 'from derek_module_loader import load_derek_consciousness; loader = load_derek_consciousness(skip_hardware=True); print(loader.get_stats())'")
    print()

if __name__ == "__main__":
    main()

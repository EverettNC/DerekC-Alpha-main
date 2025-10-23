#!/usr/bin/env python3
"""
Derek Comprehensive Diagnostic
Check all Derek systems and identify what's broken
"""

import sys
import os
import logging

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_environment():
    """Test environment variables and API keys"""
    print("🔍 Testing Environment Configuration...")
    
    # Check if .env file exists and load it
    env_file = os.path.join(PROJECT_ROOT, '.env')
    if os.path.exists(env_file):
        print("✅ .env file found")
        from dotenv import load_dotenv
        load_dotenv(env_file)
    else:
        print("❌ .env file not found")
        return False
    
    # Check API keys
    required_keys = [
        'OPENAI_API_KEY',
        'ANTHROPIC_API_KEY', 
        'PERPLEXITY_API_KEY',
        'AWS_ACCESS_KEY_ID',
        'AWS_SECRET_ACCESS_KEY'
    ]
    
    for key in required_keys:
        value = os.getenv(key)
        if value:
            print(f"✅ {key}: {'*' * 20}...{value[-4:] if len(value) > 4 else '***'}")
        else:
            print(f"❌ {key}: Missing")
    
    return True

def test_core_imports():
    """Test core module imports"""
    print("\n🔍 Testing Core Module Imports...")
    
    modules_to_test = [
        'brain',
        'memory_engine', 
        'conversation_engine',
        'derek_ultimate_voice',
        'perplexity_service',
        'intent_engine',
        'executor'
    ]
    
    results = {}
    for module in modules_to_test:
        try:
            __import__(module)
            print(f"✅ {module}")
            results[module] = True
        except Exception as e:
            print(f"❌ {module}: {str(e)}")
            results[module] = False
    
    return results

def test_derek_functionality():
    """Test Derek's actual functionality step by step"""
    print("\n🔍 Testing Derek Core Functionality...")
    
    try:
        from brain import Derek
        print("✅ Derek class import successful")
        
        # Test initialization
        derek = Derek(file_path="./memory/diagnostic_memory.json")
        print("✅ Derek initialization successful")
        
        # Test memory system
        if derek.memory_engine:
            print("✅ Memory engine loaded")
        else:
            print("❌ Memory engine failed")
            
        # Test conversation engine  
        if derek.conversation_engine:
            print("✅ Conversation engine loaded")
        else:
            print("❌ Conversation engine failed")
            
        # Test intent detection
        try:
            from intent_engine import detect_intent
            intent = detect_intent("Hello Derek")
            print(f"✅ Intent detection working: {intent}")
        except Exception as e:
            print(f"❌ Intent detection failed: {e}")
            
        # Test executor
        try:
            from executor import execute_task
            result = execute_task("Hello", "greeting", {})
            print(f"✅ Task execution working")
        except Exception as e:
            print(f"❌ Task execution failed: {e}")
            
        # Test full thinking process
        try:
            response = derek.think("What is the weather today?")
            print(f"✅ Derek thinking process working")
            print(f"   Response type: {type(response)}")
            if isinstance(response, dict):
                print(f"   Intent: {response.get('intent', 'unknown')}")
                print(f"   Response: {response.get('response', 'No response')[:100]}...")
        except Exception as e:
            print(f"❌ Derek thinking failed: {e}")
            import traceback
            traceback.print_exc()
            
        return True
        
    except Exception as e:
        print(f"❌ Derek core functionality failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_api_connections():
    """Test actual API connections"""
    print("\n🔍 Testing API Connections...")
    
    # Test OpenAI
    try:
        import openai
        from dotenv import load_dotenv
        load_dotenv()
        
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'API test successful'"}],
            max_tokens=10
        )
        print("✅ OpenAI API connection successful")
    except Exception as e:
        print(f"❌ OpenAI API failed: {e}")
    
    # Test Anthropic
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        # Just test client creation, not actual call to avoid costs
        print("✅ Anthropic API client created successfully")
    except Exception as e:
        print(f"❌ Anthropic API failed: {e}")
        
    # Test Perplexity
    try:
        import requests
        headers = {
            'Authorization': f'Bearer {os.getenv("PERPLEXITY_API_KEY")}',
            'Content-Type': 'application/json'
        }
        # Just test headers, not actual call
        print("✅ Perplexity API headers configured")
    except Exception as e:
        print(f"❌ Perplexity API failed: {e}")

def test_speech_and_audio():
    """Test speech and audio systems"""
    print("\n🔍 Testing Speech & Audio Systems...")
    
    # Test text-to-speech
    try:
        from tts_bridge import speak_response
        # Test without actually playing sound
        print("✅ TTS bridge available")
    except Exception as e:
        print(f"❌ TTS bridge failed: {e}")
    
    # Test speech recognition
    try:
        import speech_recognition as sr
        print("✅ Speech recognition library available")
    except Exception as e:
        print(f"❌ Speech recognition failed: {e}")
        
    # Test audio libraries
    try:
        import sounddevice
        print("✅ Sounddevice available")
    except Exception as e:
        print(f"❌ Sounddevice failed: {e}")

def main():
    """Run comprehensive diagnostic"""
    print("🚀 Derek Comprehensive Diagnostic")
    print("=" * 50)
    
    # Run all tests
    env_ok = test_environment()
    imports = test_core_imports()
    derek_ok = test_derek_functionality()
    test_api_connections()
    test_speech_and_audio()
    
    print("\n" + "=" * 50)
    print("📊 DIAGNOSTIC SUMMARY:")
    print("=" * 50)
    
    if env_ok:
        print("✅ Environment: GOOD")
    else:
        print("❌ Environment: ISSUES")
        
    working_modules = sum(1 for v in imports.values() if v)
    total_modules = len(imports)
    print(f"📦 Modules: {working_modules}/{total_modules} working ({working_modules/total_modules*100:.1f}%)")
    
    if derek_ok:
        print("🧠 Derek Core: WORKING")
    else:
        print("❌ Derek Core: BROKEN")
        
    print("\n🔧 RECOMMENDATIONS:")
    if not derek_ok:
        print("- Fix core Derek functionality issues")
    if working_modules < total_modules:
        print("- Install missing dependencies for failed modules")
    print("- Check API key validity if responses seem limited")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Derek Simple Interface
A clean, working interface to Derek without complex module loading
"""

import sys
import os

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

from brain import Derek
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Simple Derek interface that actually works"""
    
    print("🚀 Starting Derek - Simple Interface")
    print("=====================================")
    
    # Initialize Derek
    derek = Derek(file_path="./memory/derek_memory.json") 
    
    print("✅ Derek is ready! Type 'quit' to exit.")
    print("=====================================")
    
    while True:
        try:
            # Get user input
            user_input = input("\n🧑 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Derek: Goodbye! See you next time.")
                break
                
            if not user_input:
                continue
                
            # Process with Derek
            print("🤖 Derek: ", end="", flush=True)
            result = derek.think(user_input)
            
            # The actual response is already printed by the TTS system
            # Just add a newline for cleaner formatting
            print()
            
        except KeyboardInterrupt:
            print("\n👋 Derek: Goodbye! See you next time.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Simple Derek Test
Test Derek without the complex module loader to isolate issues
"""

import sys
import os
import logging

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_derek_core():
    """Test core Derek functionality without module loader"""
    try:
        # Test core imports
        logger.info("Testing core imports...")
        
        from brain import Derek
        logger.info("✅ Brain module imported successfully")
        
        from memory_engine import MemoryEngine
        logger.info("✅ Memory engine imported successfully")
        
        from conversation_engine import ConversationEngine
        logger.info("✅ Conversation engine imported successfully")
        
        # Test Derek initialization
        logger.info("Testing Derek initialization...")
        derek = Derek(file_path="./memory/test_memory.json")
        logger.info("✅ Derek initialized successfully")
        
        # Test basic conversation
        logger.info("Testing basic conversation...")
        response = derek.think("Hello Derek, are you working?")
        logger.info(f"✅ Derek response: {response}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Derek test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    logger.info("🚀 Starting Derek Core Test...")
    logger.info("="*50)
    
    success = test_derek_core()
    
    logger.info("="*50)
    if success:
        logger.info("✅ Derek Core Test PASSED - Derek is working!")
    else:
        logger.info("❌ Derek Core Test FAILED - Derek has issues")
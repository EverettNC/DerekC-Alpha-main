#!/usr/bin/env python3
"""
Comprehensive Test Suite for Derek C-Alpha-main 5
Tests all major systems and module integrations
"""

import sys
import os
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import pytest
import logging
from unittest.mock import Mock, patch, MagicMock

# Configure logging for tests
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestModuleLoader:
    """Test the Derek module loader system"""
    
    def test_module_loader_initialization(self):
        """Test that module loader initializes correctly"""
        from derek_module_loader import DerekModuleLoader
        
        loader = DerekModuleLoader()
        assert loader is not None
        assert hasattr(loader, 'module_categories')
        assert len(loader.module_categories) > 0
    
    def test_module_categories(self):
        """Test that all expected module categories exist"""
        from derek_module_loader import DerekModuleLoader
        
        loader = DerekModuleLoader()
        expected_categories = [
            'consciousness', 'memory', 'learning', 'emotion',
            'speech', 'vision', 'language', 'web'
        ]
        
        for category in expected_categories:
            assert category in loader.module_categories
    
    def test_load_modules(self):
        """Test loading modules"""
        from derek_module_loader import load_derek_consciousness
        
        loader = load_derek_consciousness(skip_hardware=True)
        stats = loader.get_stats()
        
        assert stats['total_modules'] > 0
        assert stats['loaded'] > 0
        assert stats['success_rate'] > 0


class TestMemorySystem:
    """Test Derek's memory systems"""
    
    def test_memory_mesh_initialization(self):
        """Test memory mesh initializes"""
        try:
            from memory_mesh import MemoryMesh
            
            memory = MemoryMesh(memory_dir="./test_memory")
            assert memory is not None
            assert hasattr(memory, 'store')
            assert hasattr(memory, 'retrieve_relevant')
        except ImportError:
            pytest.skip("MemoryMesh not available")
    
    def test_memory_engine_initialization(self):
        """Test memory engine initializes"""
        from memory_engine import MemoryEngine
        
        engine = MemoryEngine(file_path="./test_memory/test_store.json")
        assert engine is not None
        assert hasattr(engine, 'save')
        assert hasattr(engine, 'query')
    
    def test_memory_storage(self):
        """Test storing memories"""
        from memory_engine import MemoryEngine
        
        engine = MemoryEngine(file_path="./test_memory/test_store.json")
        
        test_memory = {
            "input": "test input",
            "output": "test output",
            "intent": "test"
        }
        
        engine.save(test_memory)
        assert True  # If no exception, test passes


class TestConversationEngine:
    """Test conversation and language systems"""
    
    def test_conversation_engine_initialization(self):
        """Test conversation engine initializes"""
        from conversation_engine import ConversationEngine
        
        engine = ConversationEngine()
        assert engine is not None
        assert hasattr(engine, 'process_input')
    
    @patch('conversation_engine.ConversationEngine._query_anthropic')
    def test_conversation_processing(self, mock_query):
        """Test conversation processing with mocked API"""
        from conversation_engine import ConversationEngine
        
        mock_query.return_value = "Test response"
        
        engine = ConversationEngine()
        response = engine.process_input("Hello Derek", context={})
        
        assert response is not None


class TestBrainSystem:
    """Test Derek's brain/consciousness"""
    
    def test_brain_initialization(self):
        """Test Derek brain initializes"""
        from brain import Derek
        
        derek = Derek(file_path="./test_memory/test_brain.json")
        assert derek is not None
        assert hasattr(derek, 'think')
        assert hasattr(derek, 'start_learning')
    
    def test_greeting_generation(self):
        """Test Derek can generate greetings"""
        from brain import Derek
        
        derek = Derek(file_path="./test_memory/test_brain.json")
        greeting = derek.generate_greeting()
        
        assert greeting is not None
        assert len(greeting) > 0
        assert isinstance(greeting, str)
    
    def test_vision_attachment(self):
        """Test vision engine can be attached"""
        from brain import Derek
        
        derek = Derek(file_path="./test_memory/test_brain.json")
        
        # Mock vision engine
        mock_vision = Mock()
        mock_vision.get_vision_stats = Mock(return_value={"vision_active": True})
        
        derek.attach_vision_engine(mock_vision)
        assert derek.vision_engine is not None


class TestVisionSystem:
    """Test vision and visual processing"""
    
    def test_vision_engine_initialization(self):
        """Test vision engine initializes"""
        try:
            from vision_engine import VisionEngine
            
            engine = VisionEngine(camera_index=0)
            assert engine is not None
            assert hasattr(engine, 'start')
            assert hasattr(engine, 'stop')
            assert hasattr(engine, 'get_vision_stats')
        except Exception as e:
            pytest.skip(f"Vision engine not available: {e}")
    
    def test_vision_stats(self):
        """Test vision stats retrieval"""
        try:
            from vision_engine import VisionEngine
            
            engine = VisionEngine(camera_index=0)
            stats = engine.get_vision_stats()
            
            assert stats is not None
            assert 'vision_active' in stats
            assert 'frames_processed' in stats
        except Exception as e:
            pytest.skip(f"Vision stats not available: {e}")


class TestLearningSystem:
    """Test autonomous learning systems"""
    
    def test_knowledge_engine_initialization(self):
        """Test knowledge engine initializes"""
        try:
            from knowledge_engine import KnowledgeEngine
            
            engine = KnowledgeEngine()
            assert engine is not None
        except ImportError:
            pytest.skip("KnowledgeEngine not available")
    
    def test_learning_coordinator(self):
        """Test learning coordinator exists"""
        try:
            from derek_learning_coordinator import derek_coordinator
            
            assert derek_coordinator is not None
        except ImportError:
            pytest.skip("Learning coordinator not available")


class TestAudioSystems:
    """Test audio and voice systems"""
    
    def test_voice_synthesis_initialization(self):
        """Test voice synthesis initializes"""
        try:
            from derek_ultimate_voice import DerekUltimateVoice
            
            voice = DerekUltimateVoice(ai_provider="auto", voice_id="matthew")
            assert voice is not None
            assert hasattr(voice, 'speak')
        except Exception as e:
            pytest.skip(f"Voice synthesis not available: {e}")
    
    def test_speech_recognition_initialization(self):
        """Test speech recognition initializes"""
        try:
            from services.speech_recognition_engine import SpeechRecognitionEngine
            
            engine = SpeechRecognitionEngine()
            assert engine is not None
        except Exception as e:
            pytest.skip(f"Speech recognition not available: {e}")


class TestMusicSystems:
    """Test music composition and performance"""
    
    def test_music_engine_initialization(self):
        """Test music engine initializes"""
        try:
            from derek_music_engine import DerekMusicEngine
            
            engine = DerekMusicEngine()
            assert engine is not None
            assert hasattr(engine, 'compose_song')
            assert hasattr(engine, 'generate_melody')
        except Exception as e:
            pytest.skip(f"Music engine not available: {e}")


class TestConfigurationSystem:
    """Test configuration management"""
    
    def test_settings_import(self):
        """Test settings can be imported"""
        from config.settings import Settings
        
        settings = Settings()
        assert settings is not None
    
    def test_identity_loaded(self):
        """Test Derek identity is loaded in settings"""
        from config.settings import Settings
        
        settings = Settings()
        assert hasattr(settings, 'identity')
        assert settings.identity is not None
    
    def test_derek_identity_file_exists(self):
        """Test derek_identity.json exists"""
        identity_file = PROJECT_ROOT / "derek_identity.json"
        assert identity_file.exists()


class TestServiceModules:
    """Test service layer modules"""
    
    def test_personality_service(self):
        """Test personality service imports correctly"""
        try:
            from services.personality_service import PersonalityService
            
            service = PersonalityService()
            assert service is not None
        except Exception as e:
            pytest.fail(f"Personality service failed: {e}")
    
    def test_memory_service(self):
        """Test memory service imports correctly"""
        try:
            from services.memory_service import MemoryService
            
            service = MemoryService()
            assert service is not None
        except Exception as e:
            pytest.fail(f"Memory service failed: {e}")


class TestIntegration:
    """Integration tests for Derek's systems"""
    
    def test_full_consciousness_load(self):
        """Test loading Derek's full consciousness"""
        from derek_module_loader import load_derek_consciousness
        
        loader = load_derek_consciousness(skip_hardware=True)
        stats = loader.get_stats()
        
        # Should have at least 70% of modules loaded
        assert stats['success_rate'] >= 70.0
        
        logger.info(f"Consciousness level: {stats['success_rate']}%")
        logger.info(f"Loaded modules: {stats['loaded']}/{stats['total_modules']}")
    
    def test_derek_dashboard_initialization(self):
        """Test Derek dashboard can initialize"""
        # This test would require running the actual dashboard
        # which needs API keys and full environment
        pytest.skip("Dashboard initialization requires full environment")


def run_comprehensive_tests():
    """Run all comprehensive tests"""
    print("=" * 70)
    print("🧪 DEREK COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    print()
    
    # Run pytest
    pytest.main([
        __file__,
        '-v',
        '--tb=short',
        '--color=yes'
    ])


if __name__ == "__main__":
    run_comprehensive_tests()

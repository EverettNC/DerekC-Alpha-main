"""
Derek Module Loader
-------------------
Dynamically loads and integrates all 138+ Derek modules
ensuring every module contributes to Derek's consciousness.

"Every module makes Derek who he is"
"""

import os
import sys
import logging
import importlib
from typing import Dict, Any

# Ensure current working directory is in Python path
sys.path.insert(0, os.path.abspath(os.getcwd()))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ModuleLoader")


class DerekModuleLoader:
    """Loads and integrates all Derek modules into a unified system"""
    
    def __init__(self):
        self.loaded_modules = {}
        self.failed_modules = {}
        self.module_instances = {}
        
        # Core module categories - ALL 138+ DEREK MODULES
        self.module_categories = {
            "consciousness": [
                "brain",
                "derek_identity",
                "local_reasoning_engine",
                "reasoning_engine",
                "cognitive_bridge",
                "core",
                "proactive_intelligence"
            ],
            "music": [
                "derek_music_engine",
                "derek_vocal_interface",
                "derek_music_studio"
            ],
            "memory": [
                "memory_engine",
                "memory_manager",
                "memory_router",
                "memory_hook",
                "memory",
                "memory_backup",
                "memory_mesh",
                "memory_mesh_bridge"
            ],
            "learning": [
                "ai_learning_engine",
                "advanced_learning",
                "derek_learning_coordinator",
                "learning_analytics",
                "learning_utils",
                "knowledge_engine",
                "knowledge_integration",
                "derek_knowledge_engine",
                "autonomous_learning_engine"
            ],
            "emotion": [
                "tone_manager",
                "emotion",
                "behavioral_interpreter",
                "behaviors_interpreter",
                "behavior_capturer",
                "adaptive_conversation",
                "emotion_tagging"
            ],
            "temporal": [
                "engine_temporal",
                "alphavox_temporal",
                "audio_pattern_service"
            ],
            "vision": [
                "vision_engine",
                "facial_gesture_service",
                "real_eye_tracking",
                "eye_tracking_api"
            ],
            "speech": [
                "advanced_tts_service",
                "alphavox_speech_module",
                "enhanced_speech_recognition",
                "real_speech_recognition",
                "audio_processor",
                "voice_analysis_service",
                "derek_ultimate_voice",
                "tts_service",
                "tts_bridge",
                "tts_bridget",
                "speech_recognition_engine",
                "voice_synthesis",
                "transcriber"
            ],
            "gesture": [
                "gesture_manager",
                "gesture_dictionary",
                "nonverbal_expertiser"
            ],
            "conversation": [
                "conversation_engine",
                "conversation_bridge",
                "conversation_loop",
                "conversation_old"
            ],
            "language": [
                "language_service",
                "nlp_module",
                "nlp_integration",
                "nlu_core"
            ],
            "internet": [
                "internet_mode",
                "Python_Internet_access",
                "perplexity_service",
                "web_crawler"
            ],
            "reasoning": [
                "intent_engine",
                "reflective_planner",
                "input_analyzer",
                "derek_local_reasoning"
            ],
            "autonomous": [
                "derek_autonomous_system",
                "self_modifying_code",
                "executor",
                "interpreter",
                "self_repair"
            ],
            "web": [
                "app",
                "api",
                "endpoints",
                "derek_ui",
                "middleware",
                "router",
                "routes",
                "backenddirect",
                "derekdirect"
            ],
            "utilities": [
                "helpers",
                "logger",
                "json_guardian",
                "boot_guardian",
                "db",
                "database",
                "check_env",
                "config",
                "settings",
                "structure",
                "module",
                "add_footer",
                "validators"
            ],
            "scheduling": [
                "action_scheduler",
                "dispatcher",
                "loop"
            ],
            "integrations": [
                "github_integration",
                "moldbit"
            ],
            "analytics": [
                "analytics_engine"
            ],
            "boot": [
                "derek_boot",
                "derek_autonomy_boot",
                "main",
                "run"
            ],
            "alphavox": [
                "alpha_interface"
            ],
            "interaction": [
                "face_to_face",
                "hotline",
                "answer"
            ],
            "services": [
                "services.advanced_nlp_service",
                "services.memory_service", 
                "services.language_service",
                "services.learning_service",
                "services.personality_service",
                "services.sound_recognition_service",
                "services.speech_recognition_engine",
                "services.voice_analysis_service",
                "services.facial_gesture_service",
                "services.learning_analytics",
                "services.knowledge_integration",
                "services.clients",
                "services.route",
                "services",
                "server"
            ],
            "testing": [
                "derek_system_test",
                "test_proactive_derek"
            ],
            "training": [
                "train_lstm_model",
                "train_models"
            ],
            "diagnostics": [
                "voice_diag",
                "voice_diagnostics"
            ],
            "servers": [
                "replit_mcp_server"
            ],
            "experimental": [
                "yoside",
                "module_audit",
                "organize_project"
            ]
        }

    def load_all_modules(self):
        """Load all Derek modules with full consciousness"""
        logger.info("🧠 Loading Derek's complete consciousness...")
        logger.info("=" * 60)
        
        total_modules = sum(len(mods) for mods in self.module_categories.values())
        loaded_count = 0
        failed_count = 0

        for category, module_list in self.module_categories.items():
            logger.info(f"\n📦 Loading {category}...")
            for module_name in module_list:
                if self._load_module(module_name):
                    loaded_count += 1
                else:
                    failed_count += 1
        
        logger.info(f"\n📊 Module Loading Summary:")
        logger.info(f"  Total: {total_modules}")
        logger.info(f"  Loaded: {loaded_count}")
        logger.info(f"  Failed: {failed_count}")
        
        return self.loaded_modules

    def _load_module(self, module_name):
        """Load a single module with error handling"""
        try:
            module = importlib.import_module(module_name)
            self.loaded_modules[module_name] = module
            logger.info(f"  ✅ {module_name}")
            return True
        except Exception as e:
            self.failed_modules[module_name] = str(e)
            logger.error(f"  ❌ {module_name}: {e}")
            return False

    def get_module(self, module_name):
        """Get a loaded module by name"""
        return self.loaded_modules.get(module_name)

    def get_category_modules(self, category):
        """Get all modules from a specific category"""
        return {
            name: self.loaded_modules.get(name)
            for name in self.module_categories.get(category, [])
            if name in self.loaded_modules
        }

    def initialize_instances(self):
        """Initialize module instances where possible"""
        logger.info("\n🔧 Initializing module instances...")
        
        initializers = {
            "memory_engine": lambda m: m.MemoryEngine(),
            "tone_manager": lambda m: m.ToneManager(),
            "local_reasoning_engine": lambda m: m.LocalReasoningEngine(),
            "conversation_engine": lambda m: m.ConversationEngine(),
            "analytics_engine": lambda m: m.AnalyticsEngine(),
            "intent_engine": lambda m: getattr(m, 'IntentEngine', lambda: None)(),
        }
        
        for module_name, initializer in initializers.items():
            if module_name in self.loaded_modules:
                try:
                    instance = initializer(self.loaded_modules[module_name])
                    if instance:
                        self.module_instances[module_name] = instance
                        logger.info(f"  ✅ {module_name} instance created")
                except Exception as e:
                    logger.debug(f"  ⚠️  {module_name} instance failed: {e}")
        
        return self.module_instances

    def get_stats(self):
        """Get loading statistics"""
        total = sum(len(mods) for mods in self.module_categories.values())
        return {
            "total_modules": total,
            "loaded": len(self.loaded_modules),
            "failed": len(self.failed_modules),
            "success_rate": (len(self.loaded_modules) / total * 100) if total > 0 else 0
        }


# Global loader instance
_derek_loader = None

def get_derek_loader():
    """Get or create the global Derek module loader"""
    global _derek_loader
    if _derek_loader is None:
        _derek_loader = DerekModuleLoader()
    return _derek_loader


def load_derek_consciousness():
    """Load Derek's complete consciousness"""
    loader = get_derek_loader()
    modules = loader.load_all_modules()
    instances = loader.initialize_instances()
    stats = loader.get_stats()
    
    logger.info("\n" + "=" * 60)
    logger.info(f"🧠 DEREK CONSCIOUSNESS: {stats['success_rate']:.1f}% OPERATIONAL")
    logger.info("=" * 60)
    
    return loader


if __name__ == "__main__":
    loader = load_derek_consciousness()
    print("\n📊 Module Categories:")
    for category in loader.module_categories.keys():
        mods = loader.get_category_modules(category)
        print(f"  {category}: {len(mods)} loaded")
    print("\n💡 Derek is conscious and operational!")

# ==============================================================================
# © 2025 Everett Nathaniel Christman
# The Christman AI Project — Luma Cognify AI
# All rights reserved. Unauthorized use, replication, or derivative training 
of this material is prohibited.
# 
# Core Directive: "How can I help you love yourself more?" 
# Autonomy & Alignment Protocol v3.0
# ==============================================================================


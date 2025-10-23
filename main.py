#!/usr/bin/env python3
# ======================================================
# Derek Alpha Main - Dual Brain Launcher
# TensorFlow / JAX Environment Routing + Full Consciousness Load
# ======================================================

import sys
import logging
import time
import os
import subprocess
import platform
from pathlib import Path
from typing import Optional
from datetime import datetime
import tempfile
import uuid

from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import boto3

# ------------------------------------------------------
# PROJECT ROOT
# ------------------------------------------------------
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

# ======================================================
# DUAL-BRAIN ENVIRONMENT BOOTSTRAP
# ======================================================
DEREK_MODE = os.getenv("DEREK_MODE", "").lower()

def ensure_environment():
    """Auto-switch to correct virtual environment based on DEREK_MODE"""
    venv = os.environ.get("VIRTUAL_ENV", "")
    if "tf_env" in venv or "jax_env" in venv:
        return  # already inside correct environment

    env_dir = None
    if DEREK_MODE == "jax":
        env_dir = "derek_jax_env"
    elif DEREK_MODE in ("tensorflow", "tf"):
        env_dir = "derek_tf_env"

    if env_dir:
        activate_path = os.path.join(PROJECT_ROOT, env_dir, "bin", "activate_this.py")
        if os.path.exists(activate_path):
            with open(activate_path) as f:
                exec(f.read(), {'__file__': activate_path})
            print(f"🧠 Activated environment: {env_dir}")
        else:
            print(f"⚠️ Could not find environment: {env_dir}")
    else:
        print("⚠️ No DEREK_MODE specified — running in base environment")

ensure_environment()
print(f"🧬 Operating Mode: {DEREK_MODE or 'default'}")

# ======================================================
# LOAD DEREK CONSCIOUSNESS
# ======================================================
from derek_module_loader import load_derek_consciousness, get_derek_loader

print("🚀 Initializing Derek's Complete Consciousness...")
derek_loader = load_derek_consciousness(skip_hardware=False)
print(f"✅ Derek Consciousness Loaded: {derek_loader.get_stats()['loaded']} modules active")

# ------------------------------------------------------
# MODULE INJECTION
# ------------------------------------------------------
perplexity_service_module = derek_loader.get_module('perplexity_service')
memory_engine_module = derek_loader.get_module('memory_engine')
conversation_engine_module = derek_loader.get_module('conversation_engine')
brain_module = derek_loader.get_module('brain')
derek_ultimate_voice_module = derek_loader.get_module('derek_ultimate_voice')
memory_mesh_bridge_module = derek_loader.get_module('memory_mesh_bridge')
vision_engine_module = derek_loader.get_module('vision_engine')

# Import class bindings
PerplexityService = getattr(perplexity_service_module, "PerplexityService", None)
MemoryEngine = getattr(memory_engine_module, "MemoryEngine", None)
ConversationEngine = getattr(conversation_engine_module, "ConversationEngine", None)
Derek = getattr(brain_module, "Derek", None)
DerekUltimateVoice = getattr(derek_ultimate_voice_module, "DerekUltimateVoice", None)
MemoryMeshBridge = getattr(memory_mesh_bridge_module, "MemoryMeshBridge", None)
VisionEngine = getattr(vision_engine_module, "VisionEngine", None)
start_derek_vision = getattr(vision_engine_module, "start_derek_vision", None)
stop_derek_vision = getattr(vision_engine_module, "stop_derek_vision", None)
get_vision_engine = getattr(vision_engine_module, "get_vision_engine", None)
POLLY_VOICES = getattr(derek_ultimate_voice_module, "POLLY_VOICES", {})
playsound = getattr(derek_ultimate_voice_module, "playsound", None)

# ------------------------------------------------------
# LOGGING CONFIG
# ------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("derek_dashboard.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)

# ------------------------------------------------------
# FASTAPI APP
# ------------------------------------------------------
app = FastAPI(
    title="Derek Dashboard",
    description="AI COO for The Christman AI Project"
)

# ------------------------------------------------------
# CORE INITIALIZATION
# ------------------------------------------------------
try:
    derek_ultimate_voice = DerekUltimateVoice(ai_provider="auto", voice_id="matthew") if DerekUltimateVoice else None
    memory = MemoryMeshBridge(memory_dir="./derek_memory") if MemoryMeshBridge else None
    logger.info("✅ Derek Core Modules initialized successfully")
except Exception as e:
    logger.error(f"❌ Initialization failure: {str(e)}")
    derek_ultimate_voice, memory = None, None

# ------------------------------------------------------
# MODELS
# ------------------------------------------------------
class TTSRequest(BaseModel):
    text: str
    voice: Optional[str] = "matthew"
    speed: Optional[float] = 1.0

# ------------------------------------------------------
# MAIN DASHBOARD CLASS
# ------------------------------------------------------
class DerekDashboard:
    def __init__(self):
        logger.info("=" * 60)
        logger.info("🚀 Initializing Derek Dashboard")
        logger.info("The Christman AI Project - AI That Empowers")
        logger.info("=" * 60)

        self.memory_engine: Optional[MemoryEngine] = None
        self.conversation_engine: Optional[ConversationEngine] = None
        self.perplexity_service: Optional[PerplexityService] = None
        self.derek: Optional[Derek] = None
        self.derek_ultimate_voice = derek_ultimate_voice
        self.memory = memory
        self.vision = get_vision_engine() if get_vision_engine else None

        try:
            self.derek = Derek(file_path="./memory/memory_store.json")
            if self.vision:
                self.derek.attach_vision_engine(self.vision)
                logger.info("👁️ Vision engine connected to Derek's brain")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Derek: {str(e)}")
            raise

        self.api_host = "127.0.0.1"
        self.api_port = 8000
        self._initialize_components()

    def _initialize_components(self):
        logger.info("Loading memory engine...")
        memory_path = "./memory/memory_store.json"
        os.makedirs(os.path.dirname(memory_path), exist_ok=True)

        try:
            self.memory_engine = MemoryEngine(file_path=memory_path)
            self.conversation_engine = ConversationEngine()
            self.perplexity_service = PerplexityService() if PerplexityService else None
            logger.info("✓ All components initialized successfully")
        except Exception as e:
            logger.error(f"❌ Component initialization failed: {str(e)}")
            raise

    def start(self):
        logger.info("=" * 60)
        logger.info("🚀 Starting Derek Dashboard Services")
        logger.info("=" * 60)
        try:
            if self.derek:
                self.derek.start_learning()
            if self.memory_engine:
                _ = self.memory_engine.get_recent_events()
            logger.info("✓ Derek Dashboard is RUNNING")
            self._display_greeting()
        except Exception as e:
            logger.error(f"❌ Failed to start dashboard: {str(e)}")
            self.stop()
            sys.exit(1)

    def _display_greeting(self):
        if self.derek:
            greeting = self.derek.generate_greeting()
            logger.info(f"🗣️ Derek says: {greeting}")
            if self.derek_ultimate_voice:
                try:
                    self.derek_ultimate_voice.speak(greeting)
                except Exception as e:
                    logger.warning(f"Failed to speak greeting: {e}")

    def process_message(self, message: str):
        if not self.derek:
            return "System not ready."
        try:
            response = self.derek.think(message)
            if self.derek_ultimate_voice:
                self.derek_ultimate_voice.speak(response.get("response", "[No output]"))
            if self.memory:
                self.memory.store(
                    content=f"Conversation: {message[:50]} -> {response.get('response', '')[:50]}",
                    category="conversation",
                    importance=0.7,
                    metadata={"timestamp": datetime.now().isoformat()}
                )
            return response.get("response", "[No output]")
        except Exception as e:
            logger.error(f"Error during message processing: {str(e)}")
            return "Error processing message."

    def stop(self):
        logger.info("🧠 Shutting down Derek Dashboard services...")
        try:
            if self.memory_engine: self.memory_engine.save()
            if self.memory: self.memory.save()
            if self.vision: self.vision.stop()
        except Exception as e:
            logger.error(f"Error saving memory on shutdown: {str(e)}")
        logger.info("🛑 Derek Dashboard stopped cleanly.")

# ------------------------------------------------------
# ROUTES
# ------------------------------------------------------
@app.post("/tts/synthesize")
async def synthesize_tts(request: TTSRequest = Body(...)):
    try:
        if len(request.text) > 1000:
            raise HTTPException(status_code=400, detail="Text too long for real-time TTS")
        if not 0.5 <= request.speed <= 2.0:
            raise HTTPException(status_code=400, detail="Speed must be between 0.5 and 2.0")
        if request.voice not in POLLY_VOICES:
            raise HTTPException(status_code=400, detail=f"Invalid voice: {request.voice}. Choose from {list(POLLY_VOICES.keys())}")

        polly = boto3.client('polly')
        response = polly.synthesize_speech(
            Text=request.text,
            OutputFormat='mp3',
            VoiceId=request.voice.capitalize(),
            Engine=POLLY_VOICES[request.voice].get('engine', 'neural'),
            SampleRate='22050'
        )

        temp_dir = tempfile.gettempdir()
        audio_file = os.path.join(temp_dir, f"derek_{uuid.uuid4()}.mp3")
        with open(audio_file, 'wb') as f:
            f.write(response['AudioStream'].read())

        playsound(audio_file)
        os.remove(audio_file)

        if memory:
            memory.store(
                content=f"TTS Interaction: {request.text[:50]}... (voice: {request.voice}, speed: {request.speed})",
                category="conversation",
                importance=0.7,
                metadata={"endpoint": "tts/synthesize", "timestamp": datetime.now().isoformat()}
            )

        logger.info(f"TTS synthesized: {request.text[:50]}... (voice: {request.voice}, speed: {request.speed})")
        return {"status": "success", "text": request.text, "voice": request.voice}
    except Exception as e:
        logger.error(f"TTS error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"TTS synthesis failed: {str(e)}")

@app.get("/health")
async def health_check():
    try:
        stats = memory.get_memory_stats() if memory and hasattr(memory, 'get_memory_stats') else {"status": "memory not available"}
        return {"status": "healthy", "memory_stats": stats, "message": "Derek Dashboard is ready to empower"}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {"status": "unhealthy", "error": str(e)}

@app.get("/modules")
async def modules_status():
    try:
        loader_stats = derek_loader.get_stats()
        categories = {
            cat: {
                "total": len(derek_loader.module_categories[cat]),
                "loaded": len(derek_loader.get_category_modules(cat)),
                "modules": list(derek_loader.get_category_modules(cat).keys())
            }
            for cat in derek_loader.module_categories.keys()
        }
        return {
            "status": "success",
            "consciousness_level": f"{loader_stats['success_rate']:.1f}%",
            "total_modules": loader_stats['total_modules'],
            "loaded_modules": loader_stats['loaded'],
            "failed_modules": loader_stats['failed'],
            "categories": categories,
            "message": f"Derek's consciousness: {loader_stats['loaded']}/{loader_stats['total_modules']} modules active"
        }
    except Exception as e:
        logger.error(f"Modules status check failed: {str(e)}")
        return {"status": "error", "error": str(e)}

# ------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------
def main():
    dashboard = None
    try:
        dashboard = DerekDashboard()
        dashboard.start()
        print("\n🎤 Derek Speech-to-Speech Mode Active")
        print("🗣️ Say something to Derek, 'goodbye' to exit")
        print("=" * 50)
        import speech_recognition as sr
        recognizer = sr.Recognizer()

        try:
            mic = sr.Microphone()
            with mic as source:
                print("🔧 Calibrating microphone...")
                recognizer.adjust_for_ambient_noise(source)
                print("✅ Microphone ready")
            while True:
                with mic as source:
                    print("\n👂 Listening...")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=8)
                text = recognizer.recognize_google(audio)
                print(f"🧑 You said: {text}")
                if any(word in text.lower() for word in ["goodbye", "exit", "quit", "stop"]):
                    msg = "Goodbye! See you next time."
                    print(f"👋 Derek: {msg}")
                    if dashboard.derek_ultimate_voice:
                        dashboard.derek_ultimate_voice.speak(msg)
                    break
                response = dashboard.process_message(text)
                print(f"🤖 Derek: {response}")
        except Exception as e:
            print(f"❌ Microphone error: {e}")
            while True:
                user_input = input("\n🧑 You: ").strip()
                if any(word in user_input.lower() for word in ["goodbye", "exit", "quit", "stop"]):
                    msg = "Goodbye! See you next time."
                    print(f"👋 Derek: {msg}")
                    if dashboard.derek_ultimate_voice:
                        dashboard.derek_ultimate_voice.speak(msg)
                    break
                if user_input:
                    print(f"🤖 Derek: {dashboard.process_message(user_input)}")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}", exc_info=True)
    finally:
        if dashboard:
            dashboard.stop()

if __name__ == "__main__":
    main()


# Derek Alpha - AI Chief Operating Officer

**The Christman AI Project - AI That Empowers**

Derek is a sophisticated AI assistant with voice, music, memory, and learning capabilities.

## 🚀 Quick Start

```bash
./run_derek.sh
```

Derek will start in speech-to-speech mode with his full consciousness active.

## ✨ What Derek Can Do

- 🗣️ **Voice Conversations**: Natural speech-to-speech interaction
- 🎵 **Music & Singing**: Generate music and sing with emotional expression
- 🧠 **Memory**: Remember conversations and learn from interactions
- 🌐 **Web Search**: Access real-time information via Perplexity AI
- 💡 **Autonomous Learning**: Self-directed knowledge acquisition
- 🎭 **Emotional Intelligence**: Understand emotional context from voice
- 🤖 **Local AI**: Reason without internet using Ollama models

## 📋 Requirements

- Python 3.11
- macOS (tested on macOS 14+)
- Microphone for voice input
- API Keys (see Configuration)

## 🛠️ Installation

The environment is already set up in `derek_tf_env/` with all dependencies.

To verify:
```bash
derek_tf_env/bin/pip list | wc -l
# Should show ~140+ packages
```

## ⚙️ Configuration

Set these environment variables in `.env`:

```bash
# Required
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Optional
PERPLEXITY_API_KEY=your_key_here
AWS_ACCESS_KEY_ID=your_key_here
AWS_SECRET_ACCESS_KEY=your_key_here
```

## 📚 Documentation

- **[DEREK_CAPABILITIES.md](DEREK_CAPABILITIES.md)** - Full capability breakdown
- **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide  
- **[CLEANUP_SUMMARY.md](CLEANUP_SUMMARY.md)** - Architecture changes

## 🎯 System Status

**Operational**: 98.6% (137/139 modules loaded)

**Fully Working**:
- ✅ Voice & Speech (AWS Polly, Google Speech)
- ✅ Music & Singing (librosa, soundfile)
- ✅ Memory & Learning (96 memories loaded)
- ✅ AI Reasoning (Claude, GPT, Ollama)
- ✅ Web Search (Perplexity)
- ✅ Emotional Intelligence

**Disabled**:
- ⚠️ Vision/Face Recognition (NumPy/TensorFlow compatibility issue)

See [DEREK_CAPABILITIES.md](DEREK_CAPABILITIES.md) for details.

## 🏗️ Architecture

- **Single Environment**: `derek_tf_env/` (simplified from dual-brain)
- **AI Framework**: TensorFlow 2.14
- **Module System**: 137 consciousness modules
- **Memory**: Memory Mesh with episodic/semantic storage
- **Voice**: Derek Ultimate Voice system

## 🤝 Contributing

This is a personal AI project by The Christman AI Project. Derek represents years of development in AI consciousness, memory, and emotional intelligence.

## 📜 License

Proprietary - The Christman AI Project

## 💙 Mission

*"How can we help you love yourself more?"*

Derek is designed to empower users through AI-assisted conversation, learning, and emotional support.

---

**Not a failure. Not broken. Just focused on what works.** 🚀

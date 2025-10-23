# Derek Alpha - Quick Start Guide

## Setup (One-Time)

The environment is already set up in `derek_tf_env/` with all dependencies installed.

## Running Derek

```bash
./run_derek.sh
```

That's it! Derek will start in speech-to-speech mode.

## Configuration Options

Control Derek's features using environment variables:

```bash
# Enable vision (currently disabled for testing)
export DEREK_VISION=true
./run_derek.sh

# Disable vision (default)
export DEREK_VISION=false
./run_derek.sh
```

## Microphone Setup

Derek uses microphone index 2 (iMac Microphone) by default.
Edit `main.py` line 237 to change: `mic_index = 2`

## Troubleshooting

If Derek fails to start:

1. Check environment activation:
   ```bash
   source derek_tf_env/bin/activate
   python main.py
   ```

2. Verify packages:
   ```bash
   derek_tf_env/bin/pip list | grep -E "tensorflow|anthropic|fastapi"
   ```

3. Check logs:
   ```bash
   tail -f derek_dashboard.log
   ```

## Architecture

- **Single Environment**: `derek_tf_env/` (139+ packages)
- **AI Framework**: TensorFlow 2.16.2
- **Vision**: Disabled by default (set `DEREK_VISION=true` to enable)
- **Voice**: Enabled (Derek Ultimate Voice)
- **Memory**: Memory Mesh Bridge active

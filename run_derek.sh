#!/bin/bash

# =====================================================
# Derek Launcher - Simplified Single Environment
# =====================================================

echo "🧠 Launching Derek Alpha..."
echo "Using TensorFlow environment (derek_tf_env)"
echo ""

# Activate the unified environment
source ./derek_tf_env/bin/activate

# Optional: Set vision mode (default is disabled)
export DEREK_VISION="${DEREK_VISION:-false}"
export DEREK_MODE="tensorflow"

# Launch Derek
python main.py

# Cleanup
deactivate

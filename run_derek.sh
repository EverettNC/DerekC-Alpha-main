#!/bin/bash

# =====================================================
# Derek Multi-Brain Launcher — TensorFlow / JAX Switcher
# =====================================================

# Detect which module is being invoked
MODULE=$1

if [[ "$MODULE" == "tf" ]]; then
    echo "🧠 Launching Derek in TensorFlow Mode..."
    source ./derek_tf_env/bin/activate
    export DEREK_MODE="tensorflow"
    python main.py
    deactivate

elif [[ "$MODULE" == "jax" ]]; then
    echo "⚡ Launching Derek in JAX Mode..."
    source ./derek_jax_env/bin/activate
    export DEREK_MODE="jax"
    python main.py
    deactivate

else
    echo "Usage: ./run_derek.sh [tf|jax]"
    echo "Example: ./run_derek.sh tf"
    exit 1
fi


#!/bin/bash

echo "🔍 VERIFYING ALL FIXES ARE SAVED TO DISK"
echo "======================================================================"
echo ""

echo "1. Checking vision integration in main.py..."
if grep -q "vision_engine_module" main.py; then
    echo "   ✅ Vision engine integration: SAVED"
else
    echo "   ❌ Vision engine integration: NOT FOUND"
fi

echo ""
echo "2. Checking vision methods in brain.py..."
if grep -q "attach_vision_engine" brain.py; then
    echo "   ✅ Vision methods in brain: SAVED"
else
    echo "   ❌ Vision methods in brain: NOT FOUND"
fi

echo ""
echo "3. Checking boolean fixes in config/settings.py..."
if grep -q '"privacy_first": True' config/settings.py; then
    echo "   ✅ Boolean syntax (config/settings.py): FIXED"
else
    echo "   ❌ Boolean syntax (config/settings.py): STILL HAS ERRORS"
fi

echo ""
echo "4. Checking identity in config/settings.py..."
if grep -q "IDENTITY = " config/settings.py; then
    echo "   ✅ Identity configuration: SAVED"
else
    echo "   ❌ Identity configuration: NOT FOUND"
fi

echo ""
echo "5. Checking service imports..."
if grep -q "sys.path.insert" services/personality_service.py; then
    echo "   ✅ Service import fixes: SAVED"
else
    echo "   ❌ Service import fixes: NOT FOUND"
fi

echo ""
echo "6. Checking audio_requirements.txt exists..."
if [ -f "audio_requirements.txt" ]; then
    echo "   ✅ audio_requirements.txt: EXISTS"
else
    echo "   ❌ audio_requirements.txt: MISSING"
fi

echo ""
echo "7. Checking missing_dependencies.txt exists..."
if [ -f "missing_dependencies.txt" ]; then
    echo "   ✅ missing_dependencies.txt: EXISTS"
else
    echo "   ❌ missing_dependencies.txt: MISSING"
fi

echo ""
echo "8. Verifying venv has all dependencies..."
source venv/bin/activate
python3 << 'ENDPY'
import sys
deps = {
    "numpy": "numpy",
    "requests": "requests", 
    "openai": "openai",
    "cryptography": "cryptography",
    "fastapi": "fastapi",
    "boto3": "boto3",
    "sounddevice": "sounddevice",
    "librosa": "librosa",
    "vosk": "vosk"
}

all_installed = True
for name, import_name in deps.items():
    try:
        __import__(import_name)
        print(f"   ✅ {name}: installed")
    except ImportError:
        print(f"   ❌ {name}: MISSING")
        all_installed = False

if all_installed:
    print("\n   ✅ All critical dependencies: INSTALLED")
else:
    print("\n   ⚠️  Some dependencies missing")
ENDPY

echo ""
echo "======================================================================"
echo "✅ VERIFICATION COMPLETE"
echo "======================================================================"

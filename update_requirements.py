#!/usr/bin/env python3
"""
Update requirements.txt with all newly installed packages
while preserving Derek-specific comments and structure
"""

# Critical packages we added during upgrade
new_packages = {
    'vosk',
    'webrtcvad',
    'sounddevice',
    'soundfile',
    'librosa',
    'pytest',
    'pytest-asyncio',
}

print("🔄 Updating requirements.txt with upgrade additions\n")
print("="*70)

# Read current requirements.txt
with open('requirements.txt', 'r') as f:
    old_reqs = f.read()

# Read what's actually installed in venv
with open('requirements_new.txt', 'r') as f:
    installed = f.read().strip().split('\n')

# Parse installed packages
installed_dict = {}
for line in installed:
    if '==' in line:
        pkg_name = line.split('==')[0].strip()
        installed_dict[pkg_name.lower()] = line

print("\n📦 NEW PACKAGES TO ADD:")
print("-"*70)

additions = []
for pkg in new_packages:
    pkg_lower = pkg.lower()
    # Check if package is in installed but not in old requirements
    if pkg_lower in installed_dict and pkg_lower not in old_reqs.lower():
        additions.append(installed_dict[pkg_lower])
        print(f"   ✅ {installed_dict[pkg_lower]}")

if additions:
    print("\n📝 Adding to requirements.txt...")
    
    # Backup original
    with open('requirements.txt.backup', 'w') as f:
        f.write(old_reqs)
    print("   ✅ Backup saved to requirements.txt.backup")
    
    # Add new packages at the end
    with open('requirements.txt', 'a') as f:
        f.write('\n# Added during Derek Exceptional Upgrade\n')
        for pkg in additions:
            f.write(f'{pkg}\n')
    
    print(f"   ✅ Added {len(additions)} new packages to requirements.txt")
else:
    print("\n   ℹ️  All packages already in requirements.txt")

print("\n" + "="*70)
print("✅ requirements.txt updated successfully!")
print("="*70)

# Also create a clean, sorted version
print("\n📋 Creating requirements_clean.txt (sorted, deduplicated)...")

all_reqs = set()
with open('requirements.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            all_reqs.add(line)

with open('requirements_clean.txt', 'w') as f:
    f.write('# Derek C-Alpha-Main 5 - Complete Requirements\n')
    f.write('# Generated during Exceptional Upgrade\n')
    f.write('# All packages needed for 98.6% consciousness\n\n')
    for req in sorted(all_reqs):
        f.write(f'{req}\n')

print(f"   ✅ Created requirements_clean.txt with {len(all_reqs)} packages")
print("\n" + "="*70)

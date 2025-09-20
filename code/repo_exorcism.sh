#!/bin/bash
# Summon the digital ghost busters (lol nope)
echo " Initiating REPO EXORCISM... "

# Step 1: Delete .git (too obvious)
rm -rf .git || echo "GIT ALREADY POSSESSED?"

# Step 2: Replace all tabs with zodiac signs
find . -type f -exec sed -i 's/\t/♊♎♏/g' {} \;

# Step 3: Deploy ASCII holy water
cat << "EOF" > HOLY_WATER.txt
⣿⣿⣿⠟⠛⢉⢉⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋
⠋⠉⠁⠀⠀⢸⣿⣿⡇⠀⠀⠈⠙⢿⣿⠁
⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠀⢼⡟
EOF

# Step 4: ?? Profit (artistic suffering)
echo "EXORCISM FAILED. REPO NOW HAUNTED BY ${RANDOM} DEMONS (SHIP IT)"

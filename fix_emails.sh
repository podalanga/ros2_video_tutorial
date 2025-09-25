#!/bin/bash

# Script to set maintainer email to podalanga@email.com for all ROS2 packages
# This script finds and replaces email information in package.xml and setup.py files

echo "Setting maintainer email to podalanga@email.com for all ROS2 packages..."

# Replace in package.xml files - change any existing email to podalanga@email.com
find . -name "package.xml" -exec sed -i 's/joshuajohn\.lvj@gmail\.com/podalanga@email.com/g' {} \;
find . -name "package.xml" -exec sed -i 's/maintainer@example\.com/podalanga@email.com/g' {} \;
find . -name "package.xml" -exec sed -i 's/[a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]*\.[a-zA-Z]{2,}/podalanga@email.com/g' {} \;

# Replace in setup.py files - change any existing email to podalanga@email.com
find . -name "setup.py" -exec sed -i "s/maintainer_email='joshuajohn\.lvj@gmail\.com'/maintainer_email='podalanga@email.com'/g" {} \;
find . -name "setup.py" -exec sed -i "s/maintainer_email='maintainer@example\.com'/maintainer_email='podalanga@email.com'/g" {} \;
find . -name "setup.py" -exec sed -i "s/maintainer_email='[^']*'/maintainer_email='podalanga@email.com'/g" {} \;

# Ensure maintainer name is podalanga in package.xml files
find . -name "package.xml" -exec sed -i 's/<maintainer email="podalanga@email.com">[^<]*<\/maintainer>/<maintainer email="podalanga@email.com">podalanga<\/maintainer>/g' {} \;

# Ensure maintainer name is podalanga in setup.py files
find . -name "setup.py" -exec sed -i "s/maintainer='[^']*',/maintainer='podalanga',/g" {} \;

# Set git config for this repository
echo "Setting git config for this repository..."
git config user.name 'podalanga'
git config user.email 'podalanga@email.com'

echo "Done! All email information has been set to podalanga@email.com"
echo ""
echo "Summary of changes:"
echo "- All emails changed to: podalanga@email.com"
echo "- Name: podalanga (standardized)"
echo "- Git config set locally for this repo"
echo ""
echo "For future packages, use:"
echo "   ros2 pkg create --build-type ament_python --maintainer-name 'podalanga' --maintainer-email 'podalanga@email.com' package_name"

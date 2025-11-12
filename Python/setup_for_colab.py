import subprocess
import os

# Clone the repository
subprocess.run(['git', 'clone', 'https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks'], check=True)

# Change to the Python directory
os.chdir('SimpleITK-Notebooks/Python')

# Install requirements
subprocess.run(['pip', 'install', '-q', '-r', 'requirements.txt'], check=True)

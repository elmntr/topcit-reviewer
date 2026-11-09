import json, re, os

# We will create js/data-modules.js
print("Generating comprehensive TOPCIT Modules Data...")

# Helper to escape backticks and interpolation in templates
def clean_str(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


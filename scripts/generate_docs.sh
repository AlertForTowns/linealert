#!/bin/bash
set -e

echo "📚 Generating documentation..."

# Replace this with your real doc generation logic
echo "LineAlert Docs - $(date)" > docs/README.md

git config user.name "LineAlert Bot"
git config user.email "bot@alertfortowns.org"
git add docs/
git commit -m "📚 Auto-generated docs update [CI]"
git push origin main

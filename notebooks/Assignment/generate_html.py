"""
Script to generate HTML version of the notebook.
Run this script to create movie_analysis.html from movie_analysis.ipynb
"""
import subprocess
import sys

try:
    subprocess.run([sys.executable, "-m", "jupyter", "nbconvert", "--to", "html", "movie_analysis.ipynb"], check=True)
    print("HTML file generated successfully: movie_analysis.html")
except subprocess.CalledProcessError as e:
    print(f"Error generating HTML: {e}")
    print("\nAlternative: Run this command manually:")
    print("jupyter nbconvert --to html movie_analysis.ipynb")
except Exception as e:
    print(f"Error: {e}")


import os, sys
import urllib.request

os.path.dirname(sys.executable)
# Output: '/usr/bin'

os.path.dirname(os.path.realpath(sys.executable))
os.path.dirname(os.path.abspath(sys.executable))


url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)
# Synchronization Script for Claude Code Docs
import urllib.request
import re
import os
import ssl

# Bypass SSL verification for local execution on macOS mostly
ssl._create_default_https_context = ssl._create_unverified_context

INDEX_URL = "https://code.claude.com/docs/llms.txt"
OUTPUT_DIR = "docs"

def main():
    print(f"Fetching {INDEX_URL}...")
    req = urllib.request.Request(INDEX_URL, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
    except Exception as e:
        print(f"Failed to fetch index: {e}")
        return

    # Extract all markdown links
    # Format typically: - [Title](https://...)
    link_pattern = re.compile(r'\[([^\]]+)\]\((https://[^\)]+\.md)\)')
    links = link_pattern.findall(content)

    print(f"Found {len(links)} documentation links.")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    # Fetch and save each document
    for title, url in links:
        filename = url.split('/')[-1]
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        print(f"Downloading {filename}...")
        try:
            doc_req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(doc_req) as doc_response:
                doc_content = doc_response.read().decode('utf-8')
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(doc_content)
                
        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    main()

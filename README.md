A lightweight plagiarism detection tool that uses Google Custom Search API to search the web and BERT-based semantic similarity to detect potential plagiarism in text input.

Web Search: Uses Google Programmable Search Engine to find similar content on the internet.

Semantic Analysis: Uses Sentence Transformers (paraphrase-MiniLM-L6-v2) to detect rephrased or semantically similar content.

Text Extraction: Extracts paragraphs from webpages using BeautifulSoup.

Similarity Scoring: Highlights content with high semantic similarity.

requirements
requests
beautifulsoup4
sentence-transformers

API Key from Google Cloud Console: https://developers.google.com/custom-search/v1/overview
Search Engine ID (cx) from your CSE settings: https://programmablesearchengine.google.com/about/


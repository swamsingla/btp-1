"""
NCERT PDF Headings/Topics Extractor
Extracts hierarchical topics from NCERT PDFs by identifying numbered, bold headings.
"""

import fitz  # PyMuPDF
import re
import json
import os
from pathlib import Path
from typing import List, Dict


class HeadingsExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.topics = []
        self.chapter_title = None
        self.chapter_number = None
        
        # Detect subject from path
        path_lower = pdf_path.lower()
        if 'maths' in path_lower or 'math' in path_lower:
            self.subject = 'maths'
        elif 'science' in path_lower:
            self.subject = 'science'
        elif 'biology' in path_lower:
            self.subject = 'biology'
        elif 'chemistry' in path_lower:
            self.subject = 'chemistry'
        elif 'physics' in path_lower:
            self.subject = 'physics'
        else:
            self.subject = 'unknown'
        
    def extract_topics(self) -> Dict:
        """
        Extract chapter info and topics from PDF.
        Returns a dict with chapter info and hierarchical topics.
        """
        # First pass: Extract chapter title and number from first 2 pages
        self._extract_chapter_info()
        
        # Second pass: Extract all numbered section headings
        all_headings = self._extract_section_headings()
        
        # Build hierarchy from flat list
        self.topics = self._build_hierarchy(all_headings)
        
        return {
            "chapter_number": self.chapter_number,
            "chapter_title": self.chapter_title,
            "topics": self.topics
        }
    
    def _extract_chapter_info(self):
        """Extract chapter number and title from first 2 pages"""
        chapter_num_candidates = []
        chapter_title_parts = []
        
        for page_num in range(min(2, len(self.doc))):
            page = self.doc[page_num]
            blocks = page.get_text("dict")["blocks"]
            
            for block in blocks:
                if "lines" not in block:
                    continue
                
                # Process lines to detect multi-line chapter titles
                i = 0
                while i < len(block["lines"]):
                    line = block["lines"][i]
                    
                    line_text = ""
                    max_size = 0
                    is_bold = False
                    
                    for span in line["spans"]:
                        line_text += span["text"]
                        max_size = max(max_size, span["size"])
                        is_bold = is_bold or bool(span["flags"] & 2**4)
                    
                    line_text = line_text.strip()
                    
                    # Look for chapter number (very large text, single digit or "Chapter X")
                    if max_size > 30 and line_text.isdigit() and len(line_text) <= 2:
                        chapter_num_candidates.append({
                            'text': line_text,
                            'size': max_size,
                            'page': page_num
                        })
                    elif re.match(r'^Chapter\s+(\d+)', line_text, re.IGNORECASE):
                        match = re.match(r'^Chapter\s+(\d+)', line_text, re.IGNORECASE)
                        chapter_num_candidates.append({
                            'text': match.group(1),
                            'size': max_size,
                            'page': page_num
                        })
                    
                    # Look for chapter title (large text, usually 20-40 size)
                    # Handle multi-line titles
                    if (max_size > 20 and max_size < 50 and 
                        len(line_text) > 2 and len(line_text) < 100 and
                        not line_text.isdigit() and
                        not re.match(r'^Chapter\s+\d+', line_text, re.IGNORECASE) and
                        not re.match(r'^\d+\.\d+', line_text)):  # Not a section number
                        
                        # Check if next line is continuation (same size, not a section number)
                        title_text = line_text
                        next_idx = i + 1
                        
                        while next_idx < len(block["lines"]):
                            next_line = block["lines"][next_idx]
                            next_text = ""
                            next_size = 0
                            
                            for span in next_line["spans"]:
                                next_text += span["text"]
                                next_size = max(next_size, span["size"])
                            
                            next_text = next_text.strip()
                            
                            # Continuation if similar size and not a section number
                            if (abs(next_size - max_size) < 3 and 
                                len(next_text) > 0 and len(next_text) < 100 and
                                not re.match(r'^\d+\.\d+', next_text) and
                                not next_text.isdigit()):
                                title_text += " " + next_text
                                next_idx += 1
                            else:
                                break
                        
                        chapter_title_parts.append({
                            'text': title_text,
                            'size': max_size,
                            'page': page_num
                        })
                        
                        # Skip continuation lines
                        i = next_idx - 1
                    
                    i += 1
        
        # Pick the best candidates
        if chapter_num_candidates:
            chapter_num_candidates.sort(key=lambda x: x['size'], reverse=True)
            self.chapter_number = chapter_num_candidates[0]['text']
        
        if chapter_title_parts:
            chapter_title_parts.sort(key=lambda x: x['size'], reverse=True)
            self.chapter_title = chapter_title_parts[0]['text']
    
    def _extract_section_headings(self) -> List[Dict]:
        """Extract numbered section headings - subject-specific logic"""
        if self.subject == 'maths':
            return self._extract_maths_headings()
        elif self.subject in ['science', 'biology', 'chemistry', 'physics']:
            return self._extract_science_headings()
        else:
            return self._extract_maths_headings()  # Default to maths logic
    
    def _extract_maths_headings(self) -> List[Dict]:
        """Extract headings for MATHS - STRICT: must be bold + proper title"""
        all_headings = []
        
        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            blocks = page.get_text("dict")["blocks"]
            
            for block in blocks:
                if "lines" not in block:
                    continue
                    
                for line in block["lines"]:
                    line_text = ""
                    max_size = 0
                    is_bold = False
                    
                    for span in line["spans"]:
                        line_text += span["text"]
                        max_size = max(max_size, span["size"])
                        is_bold = is_bold or bool(span["flags"] & 2**4)
                    
                    line_text = line_text.strip()
                    
                    # Pattern: Numbered headings (e.g., 1.1, 1.2.3)
                    # MUST be bold AND have proper title text after number
                    heading_pattern = r'^(\d+\.\d+(?:\.\d+)*)\s+([A-Za-z].{2,})$'
                    match = re.match(heading_pattern, line_text)
                    
                    if match and is_bold and max_size >= 11.5:
                        number = match.group(1)
                        title = match.group(2).strip()
                        
                        # Must start with letter and have actual words
                        has_valid_words = sum(1 for word in title.split() 
                                             if len(word) >= 3 and any(c.isalpha() for c in word)) >= 1
                        
                        # Not just numbers/symbols
                        not_equation = not re.match(r'^[\d\s\+\-\*\/=\(\)\[\]\.,]+$', title)
                        
                        if has_valid_words and not_equation and len(title) > 3:
                            all_headings.append({
                                "number": number,
                                "title": title,
                                "page": page_num + 1
                            })
        
        return all_headings
    
    def _extract_science_headings(self) -> List[Dict]:
        """Extract headings for SCIENCE - may not be bold, larger font"""
        all_headings = []
        seen_numbers = set()  # Track section numbers only
        
        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            blocks = page.get_text("dict")["blocks"]
            
            for block in blocks:
                if "lines" not in block:
                    continue
                
                i = 0
                while i < len(block["lines"]):
                    line = block["lines"][i]
                    
                    line_text = ""
                    max_size = 0
                    
                    for span in line["spans"]:
                        line_text += span["text"]
                        max_size = max(max_size, span["size"])
                    
                    line_text = line_text.strip()
                    
                    # Pattern: Numbered headings (e.g., 1.1, 1.2.3)
                    heading_pattern = r'^(\d+\.\d+(?:\.\d+)*)\s*(.*)$'
                    match = re.match(heading_pattern, line_text)
                    
                    if match and max_size >= 13:  # Science headings are 14+ usually
                        number = match.group(1)
                        title = match.group(2).strip()
                        
                        # Skip if we already got this section number
                        if number in seen_numbers:
                            i += 1
                            continue
                        
                        # Collect all continuation lines with similar size
                        continuation_lines = [title] if title else []
                        next_idx = i + 1
                        
                        # Be more aggressive - collect up to 10 lines
                        while next_idx < len(block["lines"]) and len(continuation_lines) < 10:
                            next_line = block["lines"][next_idx]
                            next_text = ""
                            next_size = 0
                            
                            for span in next_line["spans"]:
                                next_text += span["text"]
                                next_size = max(next_size, span["size"])
                            
                            next_text = next_text.strip()
                            
                            # Stop if we hit another section number
                            if re.match(r'^\d+\.\d+', next_text):
                                break
                            
                            # Stop if size drops significantly (body text)
                            if next_size < max_size - 2:
                                break
                            
                            # Stop if lowercase start AND previous line looks complete
                            if (next_text and next_text[0].islower() and 
                                continuation_lines and len(continuation_lines[-1]) > 10):
                                break
                            
                            # Add continuation if non-empty and reasonable length
                            if next_text and len(next_text) < 100:
                                continuation_lines.append(next_text)
                                next_idx += 1
                            else:
                                break
                        
                        # Combine all parts with spaces
                        full_title = " ".join(continuation_lines).strip()
                        
                        # Clean up - remove duplicate words that appear consecutively
                        words = full_title.split()
                        cleaned_words = []
                        prev_word = None
                        for word in words:
                            if word != prev_word:
                                cleaned_words.append(word)
                                prev_word = word
                        full_title = " ".join(cleaned_words)
                        
                        # Skip to after continuations
                        i = next_idx - 1
                        
                        # Validation
                        has_letters = any(c.isalpha() for c in full_title)
                        word_count = sum(1 for word in full_title.split() if len(word) >= 3 and any(c.isalpha() for c in word))
                        not_equation = not re.match(r'^[\d\s\+\-\*\/=\(\)\[\]\.,]+$', full_title)
                        
                        # Must have at least 2 meaningful words
                        if has_letters and word_count >= 2 and not_equation and len(full_title) > 5:
                            seen_numbers.add(number)
                            all_headings.append({
                                "number": number,
                                "title": full_title,
                                "page": page_num + 1
                            })
                    
                    i += 1
        
        return all_headings
    
    def _build_hierarchy(self, headings: List[Dict]) -> List[Dict]:
        """
        Convert flat list of numbered headings into hierarchical structure.
        E.g., 1.1, 1.2, 1.2.1 -> nested structure
        """
        hierarchy = []
        stack = []
        
        for heading in headings:
            number = heading["number"]
            level = len(number.split('.'))
            
            node = {
                "number": number,
                "title": heading["title"],
                "page": heading["page"],
                "subtopics": []
            }
            
            # Find parent based on number hierarchy
            while stack and self._get_level(stack[-1]["number"]) >= level:
                stack.pop()
            
            if stack:
                stack[-1]["subtopics"].append(node)
            else:
                hierarchy.append(node)
            
            stack.append(node)
        
        return hierarchy
    
    def _get_level(self, number: str) -> int:
        """Get nesting level from number (e.g., '1.2.3' -> 3)"""
        return len(number.split('.'))
    
    def save_to_json(self, output_path: str):
        """Save extracted topics to JSON file"""
        output = {
            "source_pdf": Path(self.pdf_path).name,
            "chapter_number": self.chapter_number,
            "chapter_title": self.chapter_title,
            "total_topics": self._count_topics(self.topics),
            "topics": self.topics
        }
        
        # Create directory if it doesn't exist
        os.makedirs(Path(output_path).parent, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
    
    def _count_topics(self, topics: List[Dict]) -> int:
        """Count total number of topics including subtopics"""
        count = len(topics)
        for topic in topics:
            if topic.get("subtopics"):
                count += self._count_topics(topic["subtopics"])
        return count
    
    def print_summary(self):
        """Print a summary of extracted topics"""
        def print_topic(topic, indent=0):
            print("  " * indent + f"{topic['number']} {topic['title']} (Page {topic['page']})")
            for subtopic in topic.get("subtopics", []):
                print_topic(subtopic, indent + 1)
        
        print(f"\n{'='*70}")
        print(f"PDF: {Path(self.pdf_path).name}")
        if self.chapter_number:
            print(f"Chapter: {self.chapter_number}")
        if self.chapter_title:
            print(f"Title: {self.chapter_title}")
        print(f"Total Topics Found: {self._count_topics(self.topics)}")
        print(f"{'='*70}\n")
        
        for topic in self.topics:
            print_topic(topic)


def process_all_pdfs():
    """Process all PDFs in the input directory and save to intermediate/headings"""
    base_input = Path(__file__).parent.parent / "data" / "input"
    base_output = Path(__file__).parent.parent / "data" / "intermediate" / "headings"
    
    # Find all grade folders
    grade_folders = sorted([f for f in base_input.iterdir() if f.is_dir() and f.name.startswith("grade")])
    
    total_processed = 0
    total_errors = 0
    
    for grade_folder in grade_folders:
        grade_name = grade_folder.name
        print(f"\n{'='*80}")
        print(f"Processing {grade_name.upper()}")
        print(f"{'='*80}")
        
        # Find all subject folders in this grade
        for subject_folder in grade_folder.iterdir():
            if not subject_folder.is_dir():
                continue
                
            subject_name = subject_folder.name
            print(f"\n--- {subject_name.capitalize()} ---")
            
            # Check if there are part folders or direct PDF files
            has_parts = any(p.is_dir() and p.name.startswith("part") for p in subject_folder.iterdir())
            
            if has_parts:
                # Process each part folder
                for part_folder in sorted(subject_folder.iterdir()):
                    if not part_folder.is_dir() or not part_folder.name.startswith("part"):
                        continue
                    
                    part_name = part_folder.name
                    
                    # Find all PDFs in this part
                    pdf_files = sorted(part_folder.glob("*.pdf"))
                    
                    for pdf_file in pdf_files:
                        output_dir = base_output / grade_name / subject_name / part_name
                        output_file = output_dir / f"{pdf_file.stem}.json"
                        
                        try:
                            extractor = HeadingsExtractor(str(pdf_file))
                            result = extractor.extract_topics()
                            extractor.save_to_json(str(output_file))
                            
                            print(f"\n  📄 {pdf_file.name}")
                            print(f"     Chapter: {result['chapter_number']} - {result['chapter_title']}")
                            print(f"     Headings ({len(result['topics'])}):")
                            for topic in result['topics']:
                                print(f"       • {topic['number']} {topic['title']}")
                                for sub in topic.get('subtopics', []):
                                    print(f"         - {sub['number']} {sub['title']}")
                            total_processed += 1
                        except Exception as e:
                            print(f"  ❌ {grade_name}/{subject_name}/{part_name}/{pdf_file.name}: {e}")
                            total_errors += 1
            else:
                # Process PDFs directly in subject folder
                pdf_files = sorted(subject_folder.glob("*.pdf"))
                
                for pdf_file in pdf_files:
                    output_dir = base_output / grade_name / subject_name
                    output_file = output_dir / f"{pdf_file.stem}.json"
                    
                    try:
                        extractor = HeadingsExtractor(str(pdf_file))
                        result = extractor.extract_topics()
                        extractor.save_to_json(str(output_file))
                        
                        print(f"\n  📄 {pdf_file.name}")
                        print(f"     Chapter: {result['chapter_number']} - {result['chapter_title']}")
                        print(f"     Headings ({len(result['topics'])}):")
                        for topic in result['topics']:
                            print(f"       • {topic['number']} {topic['title']}")
                            for sub in topic.get('subtopics', []):
                                print(f"         - {sub['number']} {sub['title']}")
                        total_processed += 1
                    except Exception as e:
                        print(f"  ❌ {grade_name}/{subject_name}/{pdf_file.name}: {e}")
                        total_errors += 1
    
    print(f"\n{'='*80}")
    print(f"PROCESSING COMPLETE")
    print(f"{'='*80}")
    print(f"Total PDFs processed: {total_processed}")
    print(f"Total errors: {total_errors}")


if __name__ == "__main__":
    import sys
    
    # If argument provided, test on specific file
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("="*80)
        print("TESTING MODE - Testing on sample files")
        print("="*80)
        
        base = Path(__file__).parent.parent / "data" / "input"
        test_files = [
            base / "grade10" / "maths" / "chapter1.pdf",
            base / "grade10" / "science" / "chapter1.pdf",
            base / "grade6" / "science" / "chapter1.pdf",
        ]
        
        for pdf_path in test_files:
            if not pdf_path.exists():
                continue
            
            print(f"\n{'='*70}")
            print(f"File: {pdf_path.parent.parent.name}/{pdf_path.parent.name}/{pdf_path.name}")
            print(f"{'='*70}")
            
            extractor = HeadingsExtractor(str(pdf_path))
            result = extractor.extract_topics()
            
            print(f"Chapter: {result['chapter_number']}")
            print(f"Title: {result['chapter_title']}")
            print(f"Topics: {len(result['topics'])}\n")
            
            for topic in result['topics'][:5]:  # Show first 5
                print(f"  {topic['number']} - {topic['title']}")
    else:
        process_all_pdfs()

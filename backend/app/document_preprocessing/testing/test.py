import unittest
from document_parsing import document_parsing
from clean_text import clean_text
from generate_metadata import generate_metadata
from semantic_text_chunking import semantic_text_chunking_with_spacy, semantic_text_chunking

class TestRAGComponents(unittest.TestCase):
    def setUp(self):
        # Set up sample inputs
        self.sample_text = "This is a test document. It contains multiple sentences.\nAnd paragraphs!"
        self.sample_chunk = [
            "This is a test document.",
            "It contains multiple sentences.",
            "And paragraphs!"
        ]
        self.invalid_file = "invalid_file.xyz"  # Unsupported format
        self.sample_chunks = ["Chunk one text.", "Chunk two text."]

    def test_document_parsing(self):
        parser = document_parsing()
        with self.assertRaises(ValueError):
            parser(self.invalid_file)

    def test_clean_text(self):
        cleaned = clean_text(self.sample_text)
        expected = "This is a test document. It contains multiple sentences. And paragraphs!"
        self.assertEqual(cleaned, expected)

    def test_semantic_chunking_with_spacy(self):
        chunks = semantic_text_chunking_with_spacy(self.sample_text, max_tockens=10)
        self.assertTrue(len(chunks) > 0)

    def test_generate_metadata(self):
        metadata = generate_metadata(self.sample_chunks)
        for meta in metadata:
            self.assertIn("chunk", meta)
            self.assertIn("topic", meta)
            self.assertIn("keywords", meta)

if __name__ == "__main__":
    unittest.main()

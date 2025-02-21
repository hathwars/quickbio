import unittest
from ..dna import (
    validate_dna, # validate DNA sequence
    complement_dna, # complement DNA sequence
    reverse_complement, # reverse complement DNA sequence
    gc_content, # calculate GC content
    transcribe # transcribe DNA to RNA
)

class TestDNAFunctions(unittest.TestCase):
    
    def test_validate_dna(self):
        self.assertTrue(validate_dna("ATGC"))
        self.assertTrue(validate_dna("atgc"))
        self.assertFalse(validate_dna("ATGCX"))
        self.assertFalse(validate_dna("AUGC"))
    
    def test_complement_dna(self):
        self.assertEqual(complement_dna("ATGC"), "TACG")
        self.assertEqual(complement_dna("atgc"), "TACG")
        with self.assertRaises(ValueError):
            complement_dna("ATGCX")
    
    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("ATGC"), "GCAT")
        self.assertEqual(reverse_complement("AAAACCCGGT"), "ACCGGGTTTT")
    
    def test_gc_content(self):
        self.assertEqual(gc_content("ATGC"), 0.5)
        self.assertEqual(gc_content("AAAAAA"), 0)
        self.assertEqual(gc_content("GCGCGC"), 1.0)
        self.assertEqual(gc_content(""), 0)
    
    def test_transcribe(self):
        self.assertEqual(transcribe("ATGC"), "AUGC")
        self.assertEqual(transcribe("GATTACA"), "GAUUACA")

if __name__ == "__main__":
    unittest.main()
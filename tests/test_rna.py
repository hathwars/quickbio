import unittest
from ..rna import (
    validate_rna, # validate RNA sequence
    complement_rna, # complement RNA sequence
    to_dna, # convert RNA to DNA
    translate # translate RNA to protein
)

class TestRNAFunctions(unittest.TestCase):
    
    def test_validate_rna(self):
        self.assertTrue(validate_rna("AUGC"))
        self.assertTrue(validate_rna("augc"))
        self.assertFalse(validate_rna("ATGC"))
        self.assertFalse(validate_rna("AUGCX"))
    
    def test_complement_rna(self):
        self.assertEqual(complement_rna("AUGC"), "UACG")
        self.assertEqual(complement_rna("augc"), "UACG")
        with self.assertRaises(ValueError):
            complement_rna("AUGCX")
    
    def test_to_dna(self):
        self.assertEqual(to_dna("AUGC"), "ATGC")
        self.assertEqual(to_dna("UUUAAAGGGCCC"), "TTTAAAGGGCCC")
    
    def test_translate(self):
        self.assertEqual(translate("AUGUUU"), "MF")
        self.assertEqual(translate("AUGUUUGGG"), "MFG")
        self.assertEqual(translate("AUGUUUUAA"), "MF*")
        self.assertEqual(translate("AUG"), "M")

if __name__ == "__main__":
    unittest.main()
import random
import collections

Nucleotides = ['A', 'C', 'G', 'T']
DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
TranscribedSequence = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'U'}
DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}
RNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "_", "UAG": "_", "UGA": "_"
}

def validateSequence(dna_seq):
    """Make sure that the sequence contains a only ATCG"""
    sequence = dna_seq.upper()
    for nucleotide in sequence:
        if nucleotide not in Nucleotides:
            return False
    return sequence

def transcribe(dna_seq):
    """Transcribes DNA to RNA"""
    rna_sequence = ""

    for base in dna_seq:
        if base in TranscribedSequence:
            rna_sequence += TranscribedSequence[base]
        else:
            # Handle unknown characters, like 'N'
            rna_sequence += base

    return rna_sequence

def translate(dna_seq, init_pos=0):
    """Translates RNA to Protein"""
    return [DNA_Codons[dna_seq[pos:pos + 3]] for pos in range(init_pos, len(dna_seq) - 2, 3)]

def calculateGC(dna_seq):
    """Calculates the GC content of the given sequence"""
    if not dna_seq:
        return 0
    
    gc_count = dna_seq.count('G') + dna_seq.count('C')

    if gc_count == 0:
        return 0
    else:
        return round((gc_count / len(dna_seq)) * 100, 5)

def calculateATGCratio(dna_seq):
    """Calculates the AT/GC ratio of the given sequence"""
    if not dna_seq:
        return 0

    at_count = dna_seq.count('A') + dna_seq.count('T')
    gc_count = dna_seq.count('G') + dna_seq.count('C')

    if gc_count == 0:
        return 0
    else:
        return round(at_count / gc_count, 5)

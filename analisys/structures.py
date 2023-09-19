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

rndDNAseq = ''.join([random.choice(Nucleotides)
                     for nucleotide in range(50)])

def validateSequence(dna_seq):
    """Make sure that the sequence contains a only ACGT"""
    sequence = dna_seq.upper()
    for nucleotide in sequence:
        if nucleotide not in Nucleotides:
            return False
    return sequence


def countNucleotides(dna_seq):
    """Count the number of nucleotides (ACGT) in the sequence"""
    return dict(collections.Counter(dna_seq))


def reverseComplement(dna_seq):
    """Mirrors the reverse pair DNA sequence"""
    return ''.join([DNA_ReverseComplement[nucleotide] for nucleotide in dna_seq])[::-1]


def transcribe(dna_seq):
    """Transcribes DNA to RNA"""
    return ''.join([TranscribedSequence[nucleotide] for nucleotide in dna_seq])


def translate(dna_seq, init_pos=0):
    """Translates RNA to Protein"""
    return [DNA_Codons[dna_seq[pos:pos + 3]] for pos in range(init_pos, len(dna_seq) - 2, 3)]


def calculateGC(dna_seq):
    """Calculates the GC content of the given sequence"""
    return round((dna_seq.count('G') + dna_seq.count('C')) / len(dna_seq) * 100, 5)


def codonFrequency(dna_seq, aminoacid):
    """Returns the usage frequency of the codons"""
    list = []
    for i in range(0, len(dna_seq) - 2, 3):
        if DNA_Codons[dna_seq[i:i + 3]] == aminoacid:
            list.append(dna_seq[i:i + 3])

    frequencyDictionary = dict(collections.Counter(list))
    totalWight = sum(frequencyDictionary.values())

    for sequence in frequencyDictionary:
        frequencyDictionary[sequence] = round(
            frequencyDictionary[sequence] / totalWight, 12)
    return frequencyDictionary


def readingFrames(dna_seq):
    frames = []
    frames.append(translate(dna_seq, 0))
    frames.append(translate(dna_seq, 1))
    frames.append(translate(dna_seq, 2))
    frames.append(translate(reverseComplement(dna_seq), 0))
    frames.append(translate(reverseComplement(dna_seq), 1))
    frames.append(translate(reverseComplement(dna_seq), 2))
    return frames


def proteins(aminoacid_seq):
    """Calculate posible proteins in aminoacid sequence"""
    current_protein = []
    proteins = []

    for aminoacid in aminoacid_seq:
        if aminoacid == '_':
            # Stop gathering aminoacids if _ is read from file
            if current_protein:
                for protein in current_protein:
                    proteins.append(protein)
                current_protein = []
        else:
            # Start gathering aminoacids if M is read from file
            if aminoacid == 'M':
                current_protein.append("")
            for i in range(len(current_protein)):
                current_protein[i] += aminoacid
    return proteins


def all_proteins(sequence, startReadingPosition=0, endReadingPosition=0, ordered=False):
    if endReadingPosition > startReadingPosition:
        rfs = readingFrames(sequence[startReadingPosition: endReadingPosition])
    else:
        rfs = readingFrames(sequence)
    res = []
    for readingframes in rfs:
        prots = proteins(readingframes)
        for protein in prots:
            res.append(protein)
    if ordered:
        return sorted(res, key=len, reverse=True)
    return res

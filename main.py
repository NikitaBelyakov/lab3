import sys
import random

nucleotide_to_binary: dict[str, bin] = {
    'a': 0b00,
    'c': 0b01,
    'g': 0b10,
    't': 0b11,
}

binary_to_nucleotide: dict[bin, str] = {
    0b00: 'a',
    0b01: 'c',
    0b10: 'g',
    0b11: 't',
}

class DNACompressor:

    __compressed_dna_sequence: bin

    __original_length: int

    def __init__(self, dna_sequence: str) -> None:
        self.__compressed_dna_sequence = self._compress(dna_sequence)
        self.__original_length = len(dna_sequence)

    def __str__(self) -> str:
        return str(self.__compressed_dna_sequence)

    def _compress(self, dna_sequence: str):
        compressed: bin = 0
        for nucleotide in dna_sequence:
            compressed <<= 2
            compressed |= nucleotide_to_binary[nucleotide]
        return compressed

    def _decompress(self) -> str:
        dna_sequence: list[bin] = []
        compressed: bin = self.__compressed_dna_sequence
        for _ in range(self.__original_length):
            nucleotide_bits: bin = compressed & 0b11
            dna_sequence.append(binary_to_nucleotide[nucleotide_bits])
            compressed >>= 2
        return ''.join(dna_sequence[::-1])

    def get_compressed(self) -> str:
        return self.__str__()

    def get_decompressed(self) -> str:
        return self._decompress()

dna_sequence: str = f'ataagactccccctcaagcgttcgtggggatgctctgtttactgggcagttatcctagca\
cccggggcccgaacgaagttcaacgctagctaccttccactgatgtgaaaaggatgagat\
aatccctgtcagacgcattaagtgaatgtgtgaatgacgccactacacgctggcaagcgc\
gggcgatcgcaggttcttcttgtgaggcgactacaggctcgccattcgtcgtttcttcaa\
tggttagcctatcagaaacacggctccaatacttctgacgtctcgacgggccagcggtca\
gcaccgctgtcgatattaatcgcagctgggaactaacagaaacctaaagaaaaattcgtc\
cggttctgattatataccgggagtataatcactctcacagcccgagtacatacacgcacg\
actttacaacaagcagagctcagtctgggcctcgccatttcccgttttaagcgcgggtga\
aactgggtttaaggggcggtgtacggacaattaatcgcatttttcgataggtcatgatcg\
tcaagttttgagatctcaaacctttagtaataatgttcgcctagaatctgggggctattg\
gagaacgaaccttccatcggtcgcgataccgcataccaagccgcttatctttaaagtgca\
aatctgggaatccccatgccctaagaggtcattaagagaacctatgtttagcagctactc\
tcgtagaatgcacgtttaagggacgccgtcaccacggattccggtgcatatagttgcata\
gctagatccggtctctctctatgggataaagcgtcacaagtcgcgttcatctttctacat\
tgtaacgccattcaatcaaagtgatcgggatctgctctgctcatgatacacgctgagata\
gattcggcataaggaacggcttgctcgaatcggtaatccccgaggatcatgtcgatttgc\
atcaacagtgacgcggcaggtaccatgacaaccaaatggc'

def generate_dna(dna_length: int = 1000):
    return dna_sequence \
        if dna_length == 1000 \
        else ''.join(random.choices('acgt', k=dna_length))

def test(dna_length: int = 1000) -> None:
    print(f'Длина последовательности: {dna_length}')
    dna_sequence: str = generate_dna(dna_length)
    compressed_dna_str = DNACompressor(dna_sequence)
    print(f'Исходная строка: {sys.getsizeof(dna_sequence)} байтов')
    print(f'Сжатая строка: {sys.getsizeof(compressed_dna_str.get_compressed())} байтов')



sys.set_int_max_str_digits(999999999)
test(100_000)




# class DNASequence:
#     def __init__(self, dna_sequence: str):
#
#         if not isinstance(dna_sequence, str):
#             raise ValueError("Последовательность ДНК должна быть строкой.")
#
#         self._dna_sequence = dna_sequence.replace("\n", "").replace(" ", "").upper()  # убираем пробелы и перевод строк
#         self._compressed_sequence = self._compress()  # сжимаем последовательность при инициализации
#
#     def _compress(self):  # приватный метод для сжатия ДНК
#         nucleotide_to_binary = {
#             'A': '00',
#             'C': '01',
#             'G': '10',
#             'T': '11'
#         }
#         binary_string = ''.join([nucleotide_to_binary[nuc] for nuc in self._dna_sequence])
#
#         compressed = int(binary_string)
#         return compressed
#
#     def decompress(self):  # метод для распаковки данных
#         binary_to_nucleotide = {
#             '00': 'A',
#             '01': 'C',
#             '10': 'G',
#             '11': 'T'
#         }
#         binary_string = bin(self._compressed_sequence)[2:].zfill(len(self._dna_sequence) * 2)
#
#         decompressed = ''.join(
#             [binary_to_nucleotide[binary_string[i:i + 2]]  # разбиваем бинарную строку по 2 символа и декодируем
#              for i in range(0, len(binary_string), 2)])
#         return decompressed
#
#     def __str__(self):  # представляем строкой
#         return self.decompress()
#
#
# dna_sequence = """
#
# """
#
# dna_object = DNASequence(dna_sequence)
#
# print("Распакованная последовательность:", str(dna_object))
# print("Сжатая последовательность (целое число):", dna_object._compressed_sequence)
# print("Результат распаковки:", dna_object.decompress())
# print(f'Исходная строка: {sys.getsizeof(dna_object)} байтов')
# print(f'Сжатая строка: {sys.getsizeof(dna_object._compressed_sequence)} байтов')

from collections import Counter


def test_result(name, passed):
    print(f"{name}: {'ZDANY' if passed else 'NIEZDANY'}")


def calc_sequences(bits):
    seqs_of_zero = {}
    seqs_of_one = {}
    seqs_of_zero_capped = {}
    seqs_of_one_capped = {}

    i = 0
    sl = 1
    sb = -1
    while i < len(bits):
        if bits[i] == sb:
            sl += 1
        else:
            if sb == 0:
                if not sl in seqs_of_zero:
                    seqs_of_zero[sl] = 0
                seqs_of_zero[sl] += 1
                if sl >= 6:
                    sl = 6
                if not sl in seqs_of_zero_capped:
                    seqs_of_zero_capped[sl] = 0
                seqs_of_zero_capped[sl] += 1
            elif sb == 1:
                if not sl in seqs_of_one:
                    seqs_of_one[sl] = 0
                seqs_of_one[sl] += 1
                if sl >= 6:
                    sl = 6
                if not sl in seqs_of_one_capped:
                    seqs_of_one_capped[sl] = 0
                seqs_of_one_capped[sl] += 1
            sb = bits[i]
            sl = 1
        i += 1
    return Counter(seqs_of_zero), Counter(seqs_of_one), Counter(seqs_of_zero_capped), Counter(seqs_of_one_capped)


def single_bit_test(bits: list[int]) -> bool:
    counts = Counter(bits)
    passed = 9725 < counts[1] and counts[1] < 10275
    if not passed:
        print("single_bit_test:")
        print(counts)
    return passed


def sequence_test(seq_counts: Counter) -> bool:
    passed = sum([
        2315 <= seq_counts[1] and seq_counts[1] <= 2685,
        1114 <= seq_counts[2] and seq_counts[2] <= 1386,
        527 <= seq_counts[3] and seq_counts[3] <= 723,
        240 <= seq_counts[4] and seq_counts[4] <= 384,
        103 <= seq_counts[5] and seq_counts[5] <= 209,
        103 <= seq_counts[6] and seq_counts[6] <= 209
    ]) == 6
    if not passed:
        print("sequence_test:")
        print(seq_counts)
    return passed


def long_sequence_test(zero_seq_counts: Counter, one_seq_counts: Counter) -> bool:
    passed = len([c for c in zero_seq_counts if c >= 26]) == 0 and len([c for c in one_seq_counts if c >= 26]) == 0
    if not passed:
        print("long_sequence_test:")
        print("zero counts:")
        print([c for c in zero_seq_counts if c >= 26])
        print("one counts:")
        print([c for c in one_seq_counts if c >= 26])
    return passed


def poker_test(bits: list[int]) -> bool:
    segments_counts = Counter()

    for i in range(0, len(bits), 4):
        four_bits = bits[i:i+4]
        num = ''.join(map(str, four_bits))
        segments_counts[num] += 1

    X = (16/5000) * sum([i * i for i in segments_counts.values()]) - 5000
    passed = 2.16 <= X and X <= 46.17
    
    if not passed:
        print("poker test:")
        print(f"X = {X}")
        print("segments_counts:")
        print(segments_counts)
    
    return passed
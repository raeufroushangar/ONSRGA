import random

def adding_errors(seq_read, percent_error):
    """
    Add errors to a nucleotide sequence read.

    Parameters:
        seq_read (str): Nucleic acid string.
        percent_error (int): Error rate percentage.

    Returns:
        str: Nucleic acid string with errors.
    """
    error_num = round(len(seq_read) * (percent_error / 100))
    alphabet_no_a = ['T', 'C', 'G']
    alphabet_no_t = ['A', 'C', 'G']
    alphabet_no_c = ['A', 'G', 'T']
    alphabet_no_g = ['A', 'C', 'T']

    fragments = list(seq_read)
    change_positions = random.sample(range(0, len(seq_read)), error_num)
    
    for i in change_positions:
        random_acgt = random.randint(0, 3)
        if random_acgt == 3:
            fragments[i] = ''
        else:
            if fragments[i] == 'A':
                fragments[i] = alphabet_no_a[random_acgt]
            elif fragments[i] == 'T':
                fragments[i] = alphabet_no_t[random_acgt]
            elif fragments[i] == 'C':
                fragments[i] = alphabet_no_c[random_acgt]
            elif fragments[i] == 'G':
                fragments[i] = alphabet_no_g[random_acgt]
    
    new_seq_read = "".join(fragments)
    return new_seq_read

def generate_fragments(genome, read_len_min, read_len_max, error_status, error_rate):
    """
    Generate sequence reads from a genome with optional errors.

    Parameters:
        genome (str): Reference genome string.
        read_len_min (int): Minimum read length.
        read_len_max (int): Maximum read length.
        error_status (str): 'YES' to add errors, 'NO' to keep reads error-free.
        error_rate (int): Error rate percentage.

    Returns:
        list: List of generated sequence reads.
    """
    reads = []
    
    def fragment_generator(genome, read_len_min, read_len_max, error_rate, error_status):
        read_len = random.randint(read_len_min, read_len_max)
        start_pos = random.randint(0, len(genome) - read_len)
        read1, read2, read3 = (genome[:start_pos],
                               genome[start_pos:start_pos + read_len],
                               genome[start_pos + read_len:])
        
        if len(read2) != 0 and len(read2) >= read_len_min:
            if error_status == 'YES':
                read2_with_error = adding_errors(read2, error_rate)
                reads.append(read2_with_error)
            else:
                reads.append(read2)
        
        for read in [read1, read3]:
            if len(read) != 0 and len(read) >= read_len_min:
                if len(read) > read_len_max:
                    fragment_generator(read, read_len_min, read_len_max, error_rate, error_status)
                else:
                    if error_status == 'YES':
                        read_with_error = adding_errors(read, error_rate)
                        reads.append(read_with_error)
                    else:
                        reads.append(read)
    
    fragment_generator(genome, read_len_min, read_len_max, error_rate, error_status)
    return reads

def main():
    genome = 'CAAGACCATGCAGCCTCTCTGCTTTCATGGAGTGCTGCTAAGCCAGGGATCCTTCATATTTCCTAACAGACTTT'
    read_len_min = 5
    read_len_max = 10
    error_status = 'YES'
    error_rate = 20

    result = generate_fragments(genome, read_len_min, read_len_max, error_status, error_rate)
    print(result)

if __name__ == "__main__":
    main()

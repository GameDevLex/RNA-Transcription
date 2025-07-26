if __name__ == "__main__":
    while True:
        # Input DNA sequence
        dna_sequence = input(
            "DNA Sequence:"
        )

        if dna_sequence.lower() == "cancel":
            print("closing...")
            break

        # Convert string to Uppercase
        dna_sequence = dna_sequence.upper()

        # Check user input
        is_base_valid = set('ATCG')

        if not set(dna_sequence).issubset(is_base_valid):
            print("Invalid sequence")
            continue
        # Let's convert the dna_sequence to rna_sequence
        rna_sequence = dna_sequence.replace('T', 'U')

        print(rna_sequence)
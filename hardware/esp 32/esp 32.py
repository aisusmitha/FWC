def get_mux_minterms():
    """
    Calculates the minterms (decimal values for which the output F is 1)
    for the Boolean function realized by the given 4x1 MUX circuit.

    The circuit is defined as:
    - Select inputs: A (MSB), B (LSB)
    - Data inputs:
        - I0 = C
        - I1 = D
        - I2 = NOT D
        - I3 = NOT C AND NOT D
    - Output: F(A, B, C, D)
    """

    minterms = []

    # The loop iterates through all possible 16 combinations of the 4 input variables (A, B, C, D).
    # Each 'i' from 0 to 15 represents a unique combination.
    # For example:
    # i = 0 (0000 in binary) means A=0, B=0, C=0, D=0
    # i = 15 (1111 in binary) means A=1, B=1, C=1, D=1
    for i in range(16):
        # Extract individual bit values for A, B, C, D from the current integer 'i'.
        # We use bitwise right shift (>>) and bitwise AND (& 1) to get each bit.
        # A is the Most Significant Bit (MSB), D is the Least Significant Bit (LSB).
        A = (i >> 3) & 1  # Extracts the 4th bit (index 3)
        B = (i >> 2) & 1  # Extracts the 3rd bit (index 2)
        C = (i >> 1) & 1  # Extracts the 2nd bit (index 1)
        D = i & 1         # Extracts the 1st bit (index 0)

        # Determine the values of the MUX data inputs (I0, I1, I2, I3)
        # based on the variables C and D, as specified by the circuit diagram.
        I0 = C               # Input I0 is directly connected to C
        I1 = D               # Input I1 is directly connected to D
        I2 = 1 - D           # Input I2 is connected to NOT D (D')
        I3 = (1 - C) * (1 - D) # Input I3 is connected to NOT C AND NOT D (C'D')
                               # In Python, '1 - x' simulates NOT, and '*' simulates AND.

        # Calculate the MUX output F based on the select inputs (A, B) and the
        # calculated data inputs (I0, I1, I2, I3).
        # The general Boolean expression for a 4x1 MUX is:
        # F = (A'B' * I0) + (A'B * I1) + (AB' * I2) + (AB * I3)
        # Where A' means NOT A, B' means NOT B.
        # In Python, 'or' is used for logical OR, and multiplication '*' for logical AND.

        # Term for when select inputs A B are '00' (A'B'):
        # This term is active when A=0 and B=0, and then F = I0
        term_00 = (1 - A) * (1 - B) * I0

        # Term for when select inputs A B are '01' (A'B):
        # This term is active when A=0 and B=1, and then F = I1
        term_01 = (1 - A) * B * I1

        # Term for when select inputs A B are '10' (AB'):
        # This term is active when A=1 and B=0, and then F = I2
        term_10 = A * (1 - B) * I2

        # Term for when select inputs A B are '11' (AB):
        # This term is active when A=1 and B=1, and then F = I3
        term_11 = A * B * I3

        # Combine all terms using logical OR.
        # The 'or' operator in Python evaluates to True if any operand is True (non-zero).
        # Since our terms are 0 or 1, 'or' works correctly for Boolean logic.
        F = (term_00 or term_01 or term_10 or term_11)

        # If the calculated output F for the current input combination is 1 (True),
        # then this combination is a minterm.
        if F == 1:
            minterms.append(i) # Add the decimal value 'i' to our list of minterms.

    # Return the list of minterms, sorted in ascending order for clarity.
    return sorted(minterms)

if __name__ == "__main__":
    # Call the function to get the minterms
    result_minterms = get_mux_minterms()
    # Print the resulting list of minterms.
    print(f"The minterms where F is 1 are: {result_minterms}")

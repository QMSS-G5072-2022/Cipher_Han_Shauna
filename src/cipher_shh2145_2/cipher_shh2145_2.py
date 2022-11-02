def cipher(text, shift, encrypt=True):
    
    """
    This function will encrypt or decrypt text using caesar cipher method.
    Parameters
    ----------
    text : str
     A string to encrypt or decrypt.
    shift : int
     An integer for how many digits to shift down the alphabet.
    encrypt : bool, optional
     A boolean to indicate if you want to encrypt/decrypt the text using this function.
    Returns
    -------
    new_text
      The encrypted or decrypted text.
    Examples
    --------
    >>> from cipher_shh2145_2 import cipher
    >>> cipher('shauna', 1, encrypt = True)
    'Tibvob'
    >>> cipher('Tibvob', 1, encrypt = False)
    'Shauna'
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

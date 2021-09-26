from matrixNotInvertable import MatrixNotInvertible
import numpy as np
from numpy.linalg import inv

# create a conversion dictionary
conversion_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                   'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                   'X': 23, 'Y': 24, 'Z': 25}
# create dictionary for reverse lookup from conversion_dict
key_dict = dict((v, k) for k, v in conversion_dict.items())


def determinant(matrix):
    # calculate and return determinant
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def invertible(matrix):
    # calls determinant() and return true or false
    try:
        # check if matrix is square
        if len(matrix) == len(matrix[0]):
            # ensure determinant is not 0
            if determinant(matrix) != 0:
                print('The Matrix is invertable')
                return True
            else:
                raise MatrixNotInvertible('Determinant equals 0')
        else:
            raise MatrixNotInvertible('Matrix not Square')
    except Exception as e:
        print(e)
        print('')
        return False


def mod_inverse(n, m):
    # accepts a number n(determinant) and a modulus m and returns the modular multiplicitive
    # inverse of n mod n
    for i in range(1, m):
        if ((n % m) * (i % m)) % m == 1:
            return i


def encrypt(k, p):
    # create empty list to convert char to integer
    plain_text_array_as_integers = []
    # loop plain text string and convert each char to an integer and push to list
    for char in p:
        plain_text_array_as_integers.append(str(conversion_dict.get(char)))
    # convert list to numpy array
    plain_text_matrix = np.asarray(plain_text_array_as_integers, dtype='int')
    # reshape the 1d numpy array into 2d array of 2 elements
    plain_text_matrix = plain_text_matrix.reshape(-1, 2)
    # print the original plain text column vectors and string
    print(f'Plaintext: {p}')
    print(f'Plaintext column vectors: {plain_text_matrix}')
    print('')
    # create a 2d numpy array to hold the encrypted integer values
    encrypted_matrix = np.empty((0, 2), dtype=int)
    # loop plain_text_matrix
    for vector in plain_text_matrix:
        # perform matrix multiplication on the key and specified vector
        encrypted_vector = np.matmul(k, vector)
        # take mod 26 of each value in the computed vector
        encrypted_vector = np.mod(encrypted_vector, 26)
        # append the vector to the final vector... np.atleast_2d makes the vector 2d which makes the dimensions
        # of the vector match the dimensions of the matrix its being appended to
        encrypted_matrix = np.append(encrypted_matrix, np.atleast_2d(encrypted_vector), axis=0)
    # create empty string for the ciphertext as a string
    cipher_as_string = ''
    # loop encrypted matrix and convert back to a string using key_dict
    for int_one, int_two in encrypted_matrix:
        cipher_as_string += key_dict[int_one]
        cipher_as_string += key_dict[int_two]
    # print the results
    print(f'Ciphertext: {cipher_as_string}')
    print(f'Ciphertext column vectors: {encrypted_matrix}')
    print('')
    # return the numpy array of the encrypted matrix
    return encrypted_matrix


def decrypt(k, c):
    # accepts a cipher text matrix c
    # get the determinant
    det = determinant(k)
    # get the modular multiplicative
    mod_multiplicative = mod_inverse(det, 26)

    # take inverse of the key
    aug_key = inv(k)
    # we want the key to be in the structure of ([d, -b],[-c, a]) given from the inverse formula so
    # we multiply by the determinant to undo the last operation of the inverse calculation
    aug_key = aug_key * det
    # take mod 26 of each element
    aug_key = np.mod(aug_key, 26)
    # multiply each element by the modular multiplicative inverse of ad-bc
    aug_key = aug_key * mod_multiplicative
    # mod 26 each element again
    aug_key = np.mod(aug_key, 26)

    decrypted_matrix = np.empty((0, 2), dtype=int)
    for vector in c:
        # perform matrix multiplication on the key and specified vector
        decrypted_vector = np.matmul(aug_key, vector)
        # take mod 26 of each value in the computed vector
        decrypted_vector = np.mod(decrypted_vector, 26)
        # append the vector to the final vector... np.atleast_2d makes the vector 2d which makes the dimensions
        # of the vector match the dimensions of the matrix its being appended to
        decrypted_matrix = np.append(decrypted_matrix, np.atleast_2d(decrypted_vector), axis=0)
    # create empty string for the ciphertext as a string
    plaintext_as_string = ''
    # loop decrypted matrix and convert back to a string
    for int_one, int_two in decrypted_matrix:
        plaintext_as_string += key_dict[int(round(int_one))]
        plaintext_as_string += key_dict[int(round(int_two))]
    # print the results
    print(f'Plaintext: {plaintext_as_string}')
    print(f'Plaintext column vectors: {decrypted_matrix.astype(int)}')
    print('')
    return decrypted_matrix


def main():
    # column vectors of the key
    key = np.array([[19, 3], [8, 12], [4, 7]])
    # take transpose
    key = np.transpose(key)
    # if the key is invertible
    if invertible(key):
        # set plain text
        plain_text_string = "ATTACKATDAWN"
        # encrypt the cipher
        cipher = encrypt(key, plain_text_string)
        # decrypt the cipher
        decrypt(key, cipher)
    # column vectors of the key
    key = np.array([[7, 11], [8, 11]])
    # take transpose
    key = np.transpose(key)
    # if the key is invertible
    if invertible(key):
        # set plain text
        plain_text_string = "ATTACKATDAWN"
        # encrypt the cipher
        cipher = encrypt(key, plain_text_string)
        # decrypt the cipher
        decrypt(key, cipher)
    # column vectors of the key
    key = np.array([[5, 4], [15, 12]])
    # take transpose
    key = np.transpose(key)
    # if the key is invertible
    if invertible(key):
        # set plain text
        plain_text_string = "ATTACKATDAWN"
        # encrypt the cipher
        cipher = encrypt(key, plain_text_string)
        # decrypt the cipher
        decrypt(key, cipher)


if __name__ == '__main__':
    main()

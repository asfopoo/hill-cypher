1. Author: Edward Nardo, JHED ID: C2FFF9
2. Module Info: Module 11, Frequency Analysis, due: Sunday, April 18, 2021
3. Approach:
hill.py - I start by creating a dictionary mapping all the letters of the alphabet to the numbers 0-25.  I then create the
opposite so I can find keys by value as well.  On line 13 I create the method determinant() that accepts a matrix and
returns the determinate by using the formula from the assignment description.  On line 18 I declare the invertible() method.
inside a try block I check if the matrix is square and if the determinate is not 0.  If both of those pass I return True,
otherwise I raise my custom exception and pass it the correct message.  I then catch the exception in an except block and
print the exception.  I then return False.  On line 37 I define the mod_inverse method that takes a number n and a modulus
factor m and return the modular multiplicitive by running a simple for loop.  On line 45 I then declare the encrypt method
that accepts a key (numpy matrix) and a string plaintext.  The method converts each char of the plaintext into an integer
value and places it into a list.  I then convert the list into a 1d numpy array.  I then reshape the numpy array into
a 2d array representing 2 element column vectors.  I then loop the new column vectors and multiply each with the key matrix,
then mod each element by 26.  This is our final encrypted matrix containing integers.  I then loop the matrix and convert
it to chars and concat it to a string.  I then print the encrypted string and encrypted column vectors and return the
encrypted matrix.  The decrypt method is declared on line 84.  It accepts a key and cipher(both numpy arrays).  I then get
the determinant of the key and the modular multiplicative using the mod_inverse method.  I then take the inverse of the key and
multiply it by the determinant in order to get the structure ([d, -b],[-c, a]).  I then mod each element by 26, then
multiply each element by the modular multiplicative and mod each by 26 again.  Now that our key is set up, we can multiply
the key and each column vector of our ciphertext, then mode the result by 26 giving us our our integer unencrypted plaintext.
I then convert the integers back to characters and print both the plaintext string and the column vectors.  On line 125 is
my main method.  I do the same operations 3 times in a row.  I create an individual key using a numpy array.  I then take the
transpose of that array. I then check if the matrix is valid, and if it is I create the plain text.  I then call the cipher
method then the decrypt method.  I then repeat the process again.

matrixNotInvertable.py - I created a class named MatrixNotInvertable that extends from Exception and gave it a constructor
that accepts a message and set it to self.message

4. Known bugs:  None that I know of
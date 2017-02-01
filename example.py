#!/usr/bin/env python
"""
An example that covers some of the basics of Python. Adapted from code by Max Hantke.

This is how you can run this script:

1. Encryption of a message
python miminal.py encrypt python.txt

2. Decryption of a message
python minimal.py decrypt python_encrypted.txt

3. Variables and operators
python minimal.py variables

4. Using Numpy/Scipy
python minmal.py numeric
"""
# Import Python Libraries
import sys
import numpy
import scipy

# A class for encryption/decryption of messages
class Message(object):
    def __init__(self, message=""):
        self.msg = message
    
    def encrypt(self):
        """Encrypt the message"""
        numpy.random.seed(0)
        L1 = numpy.arange(len(self.msg))
        numpy.random.shuffle(L1)
        message_encr = ""
        for i in L1:
            message_encr += self.msg[i]
        self.msg = message_encr

    def decrypt(self):
        """Decrypt the message"""
        numpy.random.seed(0)
        L0 = numpy.arange(len(self.msg))
        L1 = numpy.arange(len(self.msg))
        numpy.random.shuffle(L1)
        order = [L0[L1==i][0] for i in L0]
        message_decr = ""
        for i in order:
            message_decr += self.msg[i]
        self.msg = message_decr

    def write(self, filename):
        """Save message to file"""
        with open(filename, 'wb') as f:
            f.write(self.msg)

    def read(self, filename):
        """Read message from file"""
        with open(filename, 'rb') as f:
            self.msg = f.read()

# Read in arguments from the command line
task = str(sys.argv[1]) # Options are encrypt, decrypt, math

# 1. Encryption of a message
if task == 'encrypt':
    print "1. Encryption of a message"
    print "==========================\n"
    
    # Read in filenames from the command line
    original  = str(sys.argv[2])
    encrypted = original.split('.')[0] + '_encrypted.' + original.split('.')[1]

    # Encrypt the original message and save to file
    msg = Message()
    msg.read(original)
    msg.encrypt()
    msg.write(encrypted)

# 2. Decryption of a message
if task == "decrypt": 
    print "2. Encryption of a message"
    print "==========================\n"
    
    # Read in filenames from the command line
    encrypted = str(sys.argv[2])
    decrypted = encrypted.split('.')[0] + '_decrypted.' + encrypted.split('.')[1]

    # Encrypt the original message and save to file
    msg = Message()
    msg.read(encrypted)
    msg.decrypt()
    msg.write(decrypted)

# 3. Variables and operators
if task == 'variables':
    print "3. Variables and operators"
    print "==========================\n"
    
    # Defining boolean variables
    a = True
    b = False

    # Defining integer variables
    c = -2
    d = 24389

    # Defining float variables
    e = 3.1
    f = -2342.4324

    # Defining a string variable
    g = "Hello!"

    # Defining lists
    h = [1,5,23,-1]
    j = [a,b,c,d,e,f,g,h,"I can put anything in a list! :)"]
    k = range(10)

    # Defining a dictionary
    l = {"key1": "any content", "key2": 13, "key1000": [1,4,6]}

    # Comparisons:
    print "a and b are equal: ", a == b
    print "b is equal to False", b == False
    print "c is smaller than d", c < d

    # Calculation and concatenations
    print "e * f = ", e*f
    print "h + j = ", h+j

    # Loops
    print "\nElements of list j in reverse order: "
    for i in j[::-1]:
        print i

    print "\nFirst 4 elements of list k: "
    for index in range(4):
        print k[index]

# 4. Using Numpy/Scipy
if task == "numeric":
    print "4. Using Numpy/Scipy"
    print "====================\n"
    
    # Defining two arrays
    a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
    b = numpy.array([1,2,1])

    # Properties of arrays
    print "a: ", a.shape, a.dtype, a
    print "b: ", b.shape, b.dtype, b

    # Manipulation of arrays
    c = b*a
    d = 2*a - numpy.sqrt(a) + 0.2
    print "c: ", c.shape, c.dtype, c
    print "d: ", d.shape, d.dtype, d

    # Convert a PNG into an array
    import scipy.misc
    image = scipy.misc.imread('bird.png')
    print "Image (colored) properties: ", image.shape, image.dtype

    # Collapse RGB channels into a single channel
    image_black_white = image.sum(axis=2)
    print "Image (black/white) properties: ", image_black_white.shape, image_black_white.dtype

    # Save black/white image to PNG file
    scipy.misc.imsave('bird_black_white.png', image_black_white)

    # Blur the image (using a gaussian filter with sigma 2 px)
    import scipy.ndimage
    image_blurred = scipy.ndimage.gaussian_filter(image_black_white, 2)
    scipy.misc.imsave('bird_blurred.png', image_blurred)

    
    
    
    
    


# Let’s look at a more advanced
# and reliable type of algorithm called linear feedback shift
# registers(LFSRs), which can serve as a jumping-off point for
# the advanced study of PRNG algorithms.

# LFSRs were designed with computer architecture in mind. At
# the lowest level, data in computers is stored as a series of 0s
# and 1s called bits.



# In Python, we can implement a feedback shift register relatively
# simply:

# bits = [1,1,1]
# Since we are working with a short bitstring, we don’t sum the 4th, 6th, 8th, and 10th bits (since
# those don’t exist), but instead sum the 2nd and 3rd bits
# xor_result = (bits[1] + bits[2]) % 2

# Then, we can take out the rightmost element of the bits easily
# with Python’s handy pop() function, storing the result in a
# variable called output:
# output = bits.pop()

# We can then insert our sum with the insert() function,
# specifying position 0 since we want it to be on the left side of
# our list:
# bits.insert(0,xor_result)

def feedback_shift(bits):
    xor_result = (bits[1] + bits[2]) % 2
    output = bits.pop()
    bits.insert(0,xor_result)
    return(bits,output)

def feedback_shift_list(bits_this):
    bits_output = [bits_this.copy()]
    random_output = []
    bits_next = bits_this.copy()
    
    while(len(bits_output) < 2**len(bits_this)):
        bits_next,next = feedback_shift(bits_next)
        bits_output.append(bits_next.copy())
        random_output.append(next)

    return bits_output,random_output

bitslist = feedback_shift_list([1,1,1])
print(bitslist)

# We can see that our LFSR outputs all seven possible bit-strings
# that are not all 0s. We have a full-period LFSR, and also one
# that shows a uniform distribution of outputs.
#!/usr/bin/env python2

"""
    Convert dragon 32 Cassetts WAV files into plain text.
    =====================================================

    In current state only the bits would be decoded, yet!

    TODO:
        detect even_odd startpoint!

    Interesting links:
        http://www.onastick.clara.net/cosio.htm
        http://www.cs.unc.edu/~yakowenk/coco/text/tapeformat.html

    Many thanks to the people from:
        http://www.python-forum.de/viewtopic.php?f=1&t=32102 (de)
        http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=8&t=4231 (en)

    :copyleft: 2013 by Jens Diemer
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""


import collections
import wave
import sys
import struct


ONE_HZ = 2400 # "1" is a single cycle at 2400 Hz
NUL_HZ = 1200 # "0" is a single cycle at 1200 Hz
MIN_TOGGLE_COUNT = 3 # How many samples must be in pos/neg to count a cycle?

DISPLAY_BLOCK_COUNT = 8 # How many bit block should be printet in one line?


def iter_steps(g, steps):
    """
    >>> for v in iter_steps([1,2,3,4], steps=2): v
    [1, 2]
    [3, 4]
    >>> for v in iter_steps([1,2,3,4,5,6], steps=3): v
    [1, 2, 3]
    [4, 5, 6]

                                 12345678        12345678
                                         12345678
    >>> bits = [int(i) for i in "0101010101010101111000"]
    >>> for v in iter_steps(bits, steps=8): v
    [0, 1, 0, 1, 0, 1, 0, 1]
    [0, 1, 0, 1, 0, 1, 0, 1]
    [1, 1, 1, 0, 0, 0]
    """
    values = []
    for value in g:
        values.append(value)
        if len(values)==steps:
            yield list(values)
            values = []
    if values:
        yield list(values)


def iter_window(g, steps):
    """
    >>> for v in iter_window([1,2,3,4], steps=2): v
    [1, 2]
    [2, 3]
    [3, 4]
    >>> for v in iter_window([1,2,3,4,5], steps=3): v
    [1, 2, 3]
    [2, 3, 4]
    [3, 4, 5]

    >>> for v in iter_window([1,2,3,4], steps=2):
    ...    v
    ...    v.append(True)
    [1, 2]
    [2, 3]
    [3, 4]
    """
    values = collections.deque(maxlen=steps)
    for value in g:
        values.append(value)
        if len(values)==steps:
            yield list(values)


def count_sign(values):
    """
    >>> count_sign([3,-1,-2])
    (1, 2)
    >>> count_sign([0,-1])
    (0, 1)
    """
    positive_count = 0
    negative_count = 0
    for value in values:
        if value>0:
            positive_count += 1
        elif value<0:
            negative_count += 1
    return positive_count, negative_count


def iter_wave_values(wavefile):
    samplewidth = wavefile.getsampwidth() # i.e 1 for 8-bit samples, 2 for 16-bit samples
    print "samplewidth:", samplewidth
    nchannels = wavefile.getnchannels() # typically 1 for mono, 2 for stereo
    print "channels:", nchannels

    assert nchannels == 1, "Only MONO files are supported, yet!"

    frame_count = wavefile.getnframes() # number of audio frames

    # FIXME
    if samplewidth==1:
        struct_unpack_str = "b"
    elif samplewidth == 2:
        struct_unpack_str = "<h"
    else:
        raise NotImplementedError("Only sample width 2 or 1 are supported, yet!")
    print "struct_unpack_str:", struct_unpack_str

    for frame_no in xrange(frame_count):
        frame = wavefile.readframes(1)
        if not frame:
            break

        frame = struct.unpack(struct_unpack_str, frame)[0]

        yield frame_no, frame


def iter_bits(wavefile, even_odd):
    framerate = wavefile.getframerate() # frames / second
    print "Framerate:", framerate

    in_positive = even_odd
    in_negative = not even_odd
    toggle_count = 0 # Counter for detect a complete cycle
    previous_frame_no = 0

    window_values = collections.deque(maxlen=MIN_TOGGLE_COUNT)
    for frame_no, value in iter_wave_values(wavefile):
        #~ ms=float(frame_no)/framerate
        #~ print "%i %0.5fms %i" % (frame_no, ms, value)

        window_values.append(value)
        if len(window_values)>=MIN_TOGGLE_COUNT:
            positive_count, negative_count = count_sign(window_values)

            #~ print window_values, positive_count, negative_count
            if not in_positive and positive_count==MIN_TOGGLE_COUNT and negative_count==0:
                # go into a positive sinus area
                in_positive = True
                in_negative = False
                toggle_count += 1
            elif not in_negative and negative_count==MIN_TOGGLE_COUNT and positive_count==0:
                # go into a negative sinus area
                in_negative = True
                in_positive = False
                toggle_count += 1

            if toggle_count>=2:
                # a single sinus cycle complete
                toggle_count = 0

                frame_count = frame_no-previous_frame_no
                hz=framerate/frame_count

                dst_one = abs(ONE_HZ-hz)
                dst_nul = abs(NUL_HZ-hz)
                if dst_one<dst_nul:
                    yield 1
                else:
                    yield 0

                # ms=float(frame_no)/framerate
                # print "***", bit, hz, "Hz", "%0.5fms" % ms
                previous_frame_no = frame_no



def get_start_pos_iter_window(bits, pattern):
    """
    search 'pattern' bit by bit.

    >>> bits = [int(i) for i in "00100000001010101010101010101"]
    >>> get_start_pos_iter_window(bits, "01010101")
    9

    >>> get_start_pos_iter_window([1,2,3], "99")
    False
    """
    pattern = [int(i) for i in pattern]
    for pos, data in enumerate(iter_window(bits, len(pattern))):
        if data == pattern:
            return pos
            break
    return False


def get_start_pos_iter_steps(bits, pattern):
    """
    search 'pattern' in pattern-len-steps.

                                 01010101
                                         01010101
    >>> bits = [int(i) for i in "0000000001010101"]
    >>> get_start_pos_iter_window(bits, "01010101")
    8
    >>> get_start_pos_iter_steps(bits, "01010101")
    8

    >>> get_start_pos_iter_steps([1,2,3], "99")
    False
    """
    pattern_len = len(pattern)
    pattern = [int(i) for i in pattern]
    for pos, data in enumerate(iter_steps(bits, pattern_len)):
        if data == pattern:
            return pos*pattern_len
            break
    return False


def get_last_pos_iter_steps(bits, pattern):
    """
                                 01010101
                                         01010101
    >>> bits = [int(i) for i in "0101010101010101111000"]
    >>> get_last_pos_iter_steps(bits, "01010101")
    16

    >>> get_last_pos_iter_steps([1,2,3], "99")
    0

    >>> get_last_pos_iter_steps([0,1,0,1], "01")
    4
    """
    pattern_len = len(pattern)
    pattern = [int(i) for i in pattern]
    for pos, data in enumerate(iter_steps(bits, pattern_len),1):
        if data != pattern:
            pos -= 1
            break
    return pos*pattern_len


def print_bitlist(bit_list):
    in_line_count = 0
    for block in iter_steps(bit_list, steps=8):
        print list2str(block),
        in_line_count += 1
        if in_line_count>=DISPLAY_BLOCK_COUNT:
            in_line_count = 0
            print
    if in_line_count>0:
        print


def strip_pattern(bit_list, pattern):
    end = get_last_pos_iter_steps(bit_list, pattern)
    if end:
        return bit_list[end:], end
    return (bit_list, False)


def get_block(bit_list, pattern):
    """
    >>> bits = [int(i) for i in "0101010100110101"]
    >>> get_block(bits, "0101")
    (8, 4, [0, 0, 1, 1], [0, 1, 0, 1])

    >>> bits = [int(i) for i in "01010011"]
    >>> get_block(bits, "0101")
    (4, False, [0, 0, 1, 1], [])

    >>> bits = [int(i) for i in "00110101"]
    >>> get_block(bits, "0101")
    (False, 4, [0, 0, 1, 1], [0, 1, 0, 1])

    >>> bits = [int(i) for i in "0011"]
    >>> get_block(bits, "0101")
    (False, False, [0, 0, 1, 1], [])
    """

    bit_list, block_start = strip_pattern(bit_list, pattern)
    block_end = get_start_pos_iter_steps(bit_list, pattern)
    if not block_end:
        block_data = bit_list
        cut_bit_list = []
    else:
        block_data = bit_list[:block_end]
        cut_bit_list = bit_list[block_end:]

    return block_start, block_end, block_data, cut_bit_list

def list2str(l):
    """
    >>> list2str([0, 0, 0, 1, 0, 0, 1, 0])
    '00010010'
    """
    return "".join([str(c) for c in l])

def bits2ASCII(bits):
    """
    >>> c = bits2ASCII([0, 0, 0, 1, 0, 0, 1, 0])
    >>> c
    72
    >>> chr(c)
    'H'

    >>> bits2ASCII([0, 0, 1, 1, 0, 0, 1, 0])
    76
    """
    bits = bits[::-1]
    bits = list2str(bits)
    return int(bits,2)


def block2ascii(bit_list):
    """
    http://wiki.python.org/moin/BitwiseOperators
    """
    for block in iter_steps(bit_list, steps=8):
        byte_no = bits2ASCII(block)
        character = chr(byte_no)
        print "%s %4s %3s %s" % (
            list2str(block), hex(byte_no), byte_no, repr(character)
        )



if __name__ == "__main__":
    import doctest
    print doctest.testmod(
        verbose=False
        #~ verbose=True
    )
    #~ sys.exit()


    # created by Xroar Emulator
    FILENAME = "HelloWorld1 xroar.wav"
    even_odd = False

    # created by origin Dragon 32 machine
    #~ FILENAME = "HelloWorld1 origin.wav"
    #~ even_odd = True
    #~ FILENAME = "test.wav"
    #~ even_odd = True
    #~ even_odd = False

    print "Read '%s'..." % FILENAME
    wavefile = wave.open(FILENAME, "r")

    frame_count = wavefile.getnframes()
    print "Numer of audio frames:", frame_count

    #~ line = ""
    #~ for bit_count, bit in enumerate(iter_bits(wavefile, even_odd)):
        #~ if frame_no>100:
            #~ break
        #~ line += str(bit)
        #~ if len(line)>70:
            #~ print line
            #~ line = ""

    print "read..."
    bit_list = list(iter_bits(wavefile, even_odd))
    print "%i bits decoded." % len(bit_list)

    #~ print "-"*79
    #~ print_bitlist(bit_list)
    #~ print "-"*79
    #~ block2ascii(bit_list)
    #~ print "-"*79
    #~ sys.exit()

    #~ line = ""
    #~ for bit_count, bit in enumerate(bit_list):
        #~ line += str(bit)
        #~ if len(line)>70:
            #~ print line
            #~ line = ""
    #~ print line
    #~ print "-"*79

    START_LEADER = "10101010"


    start_leader_start = get_start_pos_iter_window(bit_list, START_LEADER)
    if not start_leader_start:
        print "ERROR: Start leader '%s' not found!" % START_LEADER
        sys.exit(-1)
    print "Start leader '%s' found at position: %i" % (START_LEADER, start_leader_start)

    # Cut bits before the first 01010101 start leader
    print "bits before header:", repr(list2str(bit_list[:start_leader_start]))
    bit_list = bit_list[start_leader_start:]


    #~ print "-"*79
    #~ print_bitlist(bit_list)
    #~ print "-"*79


    # file info block
    block_start, block_end, fileinfo_block, bit_list = get_block(bit_list, START_LEADER)
    print "Block pos: %i-%i len: %ibits rest: %ibits" % (
        block_start, block_end, len(fileinfo_block), len(bit_list)
    )

    print "-"*79
    print "  *** file info block data:"
    print_bitlist(fileinfo_block)
    print "-"*79
    block2ascii(fileinfo_block)
    print "-"*79


    # get data blocks
    block_no = 0
    while True:
        block_no += 1
        print "  *** data block %i" % block_no
        block_start, block_end, block_data, bit_list = get_block(bit_list, START_LEADER)
        print "  Block pos: %i-%i len: %ibits rest: %ibits" % (
            block_start, block_end, len(fileinfo_block), len(bit_list)
        )
        print_bitlist(block_data)
        print "-"*79
        block2ascii(block_data)
        print "-"*79

        if len(block_data) == 0 or len(bit_list)==0:
            # no data left
            if bit_list:
                print "Rest data:"
                print_bitlist(bit_list)
            break


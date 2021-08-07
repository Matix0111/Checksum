#!/bin/python3

import argparse
import os
import hashlib
from hmac import compare_digest

os.chdir(os.getcwd()) # For if script is placed in /usr/bin or something similar. That way there's no need for full paths when using

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', help='hash algorithm')
    parser.add_argument('-c', '--check', help='checksum to verify')
    parser.add_argument('-f', '--file', help='file to verify')
    parser.add_argument('-e', '--extract', action='store_true', help='display file\'s checksum')
    options = parser.parse_args()

    if options.extract:
        return options
    if not options.algorithm:
        return 0
    elif not options.check:
        return 0
    elif not options.file:
        return 0
    else:
        return options

options = getArgs()

class ComputeDigest:
    _algos = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }

    def __init__(self, algorithm, checksum, file):
        self.algorithm = algorithm
        self.checksum = checksum
        self.file = file

    def is_valid(self):
        if self.algorithm in self._algos.keys():
            return True
        else:
            return False

    def check(self):
        isValid = self.is_valid()
        if isValid:
            checksum = self._algos[self.algorithm]()
            try:
                with open(self.file, 'rb') as f:
                    # NEW CODE
                    for byte_block in iter(lambda: f.read(4096), b''):
                        checksum.update(byte_block)

                    # OLD CODE
                    # bytes = f.read()
                    # checksum = self._algos[self.algorithm](bytes).hexdigest()
            except FileNotFoundError:
                print('Sorry, that file does not exist.')
            else:
                if options.extract:
                    print(f'Checksum: {checksum.hexdigest()}')
                else:
                    if compare_digest(checksum.hexdigest(), self.checksum.lower()):
                        print('Match!')
                    else:
                        print('[!] Not a match.')

        else:
            print(f'[!] Supported algorithms: {", ".join(self._algos.keys())}')


if __name__ == '__main__':
    if options == 0:
        pass
    else:
        digest = ComputeDigest(options.algorithm, options.check, options.file)
        digest.check()

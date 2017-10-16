#! /usr/bin/env python3.
# total_size.py - count the total size of files
import os

totalSize = 0
for filename in os.listdir('/Users/anastasia/Documents'):
  totalSize = totalSize + os.path.getsize(os.path.join('/Users/anastasia/Documents', filename))

print(totalSize)
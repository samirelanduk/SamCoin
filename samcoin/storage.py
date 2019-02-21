import struct

class Blockchain:

    def __init__(self, data=b""):
        self.data = data


    def items(self):
        bytestring = self.data
        items = []
        while bytestring:
            next_block = struct.unpack("I", bytestring[:4])[0]
            if next_block == 0: next_block = len(bytestring)
            items.append(bytestring[4:next_block])
            bytestring = bytestring[next_block:]
        return items


    def append(self, data):
        data = b"\x00\x00\x00\x00" + data
        self.data += data

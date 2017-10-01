#!/usr/bin/env python

buf = ""
f = open("backup.zip", "r")
bu1 = ""
buf += f.read()
print buf

buf = buf.encode('hex')

buf += "831a34cdf478f76ad054f38c9aee6abd"
buf += "6a9dbff98ab7becca233aa7c3c9d25ef"
buf += "220beb5020d3263f57f3f6fd975ee634"
buf += "21eb266d85c0d4ae6c4f10670ea9b5f4"
buf += "3e1df9558fdc6dc3fe761e1105d7bc5b"
buf += "a0e21fe3463cf045197e44119828c8a3"
buf += "11b7ed91a12e927cf666eb0484a41a06"
buf += "6c8d975b9f2217a1afee27d98383f4fc"
buf += "6a753e86f7284c1973809cfed2fca666"
buf += "0351c7bc27eaab75d33a70995d946ffa"
buf += "be0abce545eb87b63aa687f47ca31671"
buf += "9b21a44d808ea97f9077b97e2997c403"
buf += "1d5240f5910dc6bddb785b49d07eaeb9"
buf += "456ffe0ba034c8a40d9b7a39a9e96df3"
buf += "02cd486f6d4a14d08730a74bc9149da7"
buf += "de5fadbd1cb77e0c02c0597cf3cc182e"
buf += "f2e78951003a280428c2e0ac70bbc95e"
buf += "6fa56c6bf2e0dd9313c7e97742e38ac6"
buf += "386dbc8fe48bd51bfc1f31039dbdc594"
buf += "f6316cc99935fa8c8117c1562f148d1a"
buf += "f6f7f44d4af96a51771daf842cc40c3e"
buf += "808ec1b22e186cddc8f8fe79f7a1ace0"
buf += "e79cf40886d9b55fc613948696e990b0"
buf += "eb9e996a5d82db2ea204493b89a30ee1"
buf += "ed39e79346410bf2aa0e85193af1075f"
buf += "f4dc25f74aae592408547d6c03047c03"
buf += "a0162f18132728af17249ed59e85c334"
buf += "461589865af8c3930580cee174132cfb"
buf += "02781604b68ae0b112118af9b92d063e"
buf += "00000000504e75f476f7b4eb0001be7b"
buf += "80f00100ac83112cb1c467fb02000000"
buf += "0004595a"


bu1 += "fd377a585a000004e6d6b44602002101"
bu1 += "16000000742fe5a3e077ff3da25d0039"
bu1 += "9a49fbe6f3258112f39ac0202a073855"
bu1 += "0af98257012a427133cc7d214b8429da"
bu1 += "5aa757f76ce21bb9f2f97ac72174cee4"
bu1 += "b15cf7dcd62ab56c4908c112c463d0b9"
bu1 += "f01431fc196327480ba3466a55642402"

buf = bu1 + buf
buf = buf.decode('hex')

print buf

g = open("lock.iso", "w")
g.write(buf)
g.close
f.close
import types, string
import socket

hostname = socket.gethostname()

def getHomedir():
    
    if hostname in ['cpu1','gpu1','gpu2']:
        return '/home/jinkuk/'
    else:
        return '/Users/jinkuk/'

def mean(l):
	return sum(l)/len(l)

def incHash(h,key,val=1):

	try:
		h[key] += val
	except:
		h[key] = val


def addHash(h,key,val):

	try:
		h[key].append(val)
	except:
		h[key] = [val]


def pushHash(h,key,val):

	try:
		h[key].add(val)
	except:
		h[key] = set([val])


def rev(seq):

	if not isinstance(seq,types.StringType):
		print ("error: string type required!")
		print (type(seq))
		sys.exit(1)

	seq_rev = ""

	for i in range(0,len(seq)):
		seq_rev = seq[i] + seq_rev

	return seq_rev

import sys
def compl(seq, seqType):

	if not isinstance(seq,types.StringType):
		print ("error in mybio.compl: string type required!")
		print ("you entered:%s" % (seq,))
		print (type(seq))
		sys.exit(1)

	seq_ret = seq.upper()

	if seqType == 'RNA':
		tab = string.maketrans('ATUGCRYSW-','UAACGYRSW-')
	else:
		tab = string.maketrans('ATUGCRYSW-','TAACGYRSW-')
	
	seq_ret = seq_ret.translate(tab)

	return seq_ret


def rc(seq,type='DNA'):

	if not isinstance(seq,types.StringType):
		print ("error: string type required!")
		sys.exit(1)

	seq = rev(seq)
	seq = compl(seq,type)

	return seq



#!/usr/bin/env python


"""Indicates CPU part of SAR file"""
PART_CPU = 0

"""Indicates RAM memory usage part of SAR file"""
PART_MEM = 1

"""Indicates swap memory usage part of SAR file"""
PART_SWP = 2

"""I/O usage part of SAR file"""
PART_IO = 3

"""Proc Cswitch part of SAR file"""
PART_PRCSW = 4

"""Page part of SAR file"""
PART_PAGE = 5

"""Dirent part of SAR file """
PART_DENT = 6

"""Runq part of SAR file """
PART_RUNQ = 7

"""Page Swap in and swap out part of SAR file"""
PART_PAGESWAP = 8

"""Number of RPC requests/calls made per second part of SAR file"""
PART_RPCMADE = 9

"""Number of RPC requests/calls received per second part of SAR file"""
PART_RPCRCVD = 10

""" RPC requests/calls received per second regex pattern"""
PATTERN_RPCRCVD = ".*scall\/s.*badcall\/s.*packet\/s.*udp\/s.*tcp\/s.*hit\/s.*miss\/s.*sread\/s.*swrite\/s.*saccess\/s.*sgetatt\/s.*"

"""Regex terms for finding fields in SAR parts for RPC requests/calls received per second """
FIELD_RPCRCVD = [ 
    'scall\/s', 'badcall\/s', 'packet\/s', 'udp\/s', 'tcp\/s', 'hit\/s', 'miss\/s', 'sread\/s', 'swrite\/s', 'saccess\/s', 'sgetatt\/s'
]

"""Pair regexp terms for finding fields in SAR parts for RPC requests/calls received per second """
FIELDS_PAIRS_RPCRCVD = { 
    'scall':FIELD_RPCRCVD[0], 'badcall':FIELD_RPCRCVD[1], 'packet':FIELD_RPCRCVD[2], 
    'udp':FIELD_RPCRCVD[3], 'tcp':FIELD_RPCRCVD[4], 'hit':FIELD_RPCRCVD[5],
    'miss':FIELD_RPCRCVD[6], 'sread':FIELD_RPCRCVD[7], 'swrite':FIELD_RPCRCVD[8],
    'saccess':FIELD_RPCRCVD[9], 'sgetatt':FIELD_RPCRCVD[10]
}

""" RPC requests/calls  made per second regex pattern"""
PATTERN_RPCMADE = ".*call\/s.*retrans\/s.*read\/s.*write\/s.*access\/s.*getatt\/s.*"

"""Regex terms for finding fields in SAR parts for RPC requests/calls made per second """
FIELD_RPCMADE = [ 
    'call\/s', 'retrans\/s', 'read\/s', 'write\/s', 'access\/s', 'getatt\/s'
]

"""Pair regexp terms for finding fields in SAR parts for RPC requests/calls made per second """
FIELDS_PAIRS_RPCMADE = { 
    'call':FIELD_RPCMADE[0], 'retrans':FIELD_RPCMADE[1], 'read':FIELD_RPCMADE[2], 
    'write':FIELD_RPCMADE[3], 'access':FIELD_RPCMADE[4], 'getatt':FIELD_RPCMADE[5]
}

"""Page Swap in and swap out regex pattern"""
PATTERN_PAGESWAP = ".*pswpin\/s.*pswpout\/s.*"

"""Regex terms for finding fields in SAR parts for Page Swap in and swap out"""
FIELD_PAGESWAP = [
    'pswpin\/s', 'pswpout\/s'
]

"""Pair regexp terms with field names in Page Swap in and swap out our dictionary"""
FIELDS_PAIRS_PAGESWAP = { 
    'pswpin':FIELD_PAGESWAP[0], 'pswpout':FIELD_PAGESWAP[1]
}

PATTERN_RUNQ = ".*runq\-sz.*plist\-sz.*ldavg\-1.*ldavg\-5.*ldavg\-15.*"

FIELD_RUNQ = [ 
    'runq\-sz', 'plist\-sz', 'ldavg\-1', 'ldavg\-5'
]

FIELD_PAIRS_RUNQ = {
    'runq':FIELD_RUNQ[0], 'plist':FIELD_RUNQ[1], 'ldavg1':FIELD_RUNQ[2],
    'ldavg5':FIELD_RUNQ[3]
}

PATTERN_DENT =".*dentunusd.*file\-nr.*inode-nr.* pty-nr.*" 

FIELD_DENT= [
    'dentunusd', 'file\-nr', 'inode\-nr', 'pty\-nr'
]

FIELDS_PAIRS_DENT = { 
    'dentunusd':FIELD_DENT[0], 'file':FIELD_DENT[1], 'inode':FIELD_DENT[2], 'pty':FIELD_DENT[3]
}

"""Pagging regex pattern"""
PATTERN_PAGE = ".*pgpgin\/s.*pgpgout\/s.*fault\/s.*majflt\/s.*pgfree\/s.*pgscank\/s.*pgscand\/s.*pgsteal\/s.*\%vmeff.*"

"""Regex terms for finding fields in SAR parts for Pagging"""
FIELD_PAGE = [ 
    'pgpgin\/s', 'pgpgout\/s', 'fault\/s', 'majflt\/s', 'pgfree\/s', 'pgscank\/s' ,'pgscand\/s', \
    'pgsteal\/s', '\%vmeff'
]

"""Pair regexp terms for finding fields in SAR parts for Proc Pagging"""
FIELDS_PAIRS_PAGE = { 
    'pgpgin':FIELD_PAGE[0], 'pgpgout':FIELD_PAGE[1], 'fault':FIELD_PAGE[2], 
    'majflt':FIELD_PAGE[3], 'pgfree':FIELD_PAGE[4], 'pgscank':FIELD_PAGE[5], 
    'pgscand':FIELD_PAGE[6], 'pgsteal':FIELD_PAGE[7], 'vmeff':FIELD_PAGE[8]
}

"""Proc Cswitch regex pattern"""
PATTERN_PRCSW = ".*proc\/s.*cswch\/s.*"

"""Regex terms for finding fields in SAR parts for Proc Cswitch"""
FIELD_PRCSW = [
    'proc\/s', 'cswch\/s'
]

"""Pair regexp terms with field names in Proc Cswitch our dictionary"""
FIELDS_PAIRS_PRCSW = { 
    'proc':FIELD_PRCSW[0], 'cswch':FIELD_PRCSW[1]
}

"""CPU regexp pattern for detecting SAR section header"""
PATTERN_CPU = ".*CPU.*(usr|user).*nice.*sys.*"

"""Regexp terms for finding fields in SAR parts for CPU"""
FIELDS_CPU = [
    '\%(usr|user)', '\%nice', '\%sys', '\%iowait', '\%idle'
]

"""Pair regexp terms with field names in CPU output dictionary"""
FIELD_PAIRS_CPU = {
    'usr': FIELDS_CPU[0], 'nice': FIELDS_CPU[1], 'sys': FIELDS_CPU[2],
    'iowait': FIELDS_CPU[3], 'idle': FIELDS_CPU[4]
}

"""Mem usage regexp pattern for detecting SAR section header"""
PATTERN_MEM = ".*kbmemfree.*kbmemused.*memused.*kbbuffers.*kbcached.*"

"""Regexp terms for finding fields in SAR parts for memory usage"""
FIELDS_MEM = [
    'kbmemfree', 'kbmemused', '\%memused', 'kbbuffers', 'kbcached'
]

"""Pair regexp terms with field names in memory usage output dictionary"""
FIELD_PAIRS_MEM = {
    'memfree': FIELDS_MEM[0], 'memused': FIELDS_MEM[1],
    'memusedpercent': FIELDS_MEM[2], 'membuffer': FIELDS_MEM[3],
    'memcache': FIELDS_MEM[4]
}

"""Swap usage regexp pattern for detecting SAR section header"""
PATTERN_SWP = ".*kbswpfree.*kbswpused.*swpused.*"

"""Regexp terms for finding fields in SAR parts for swap usage"""
FIELDS_SWP = [
    'kbswpfree', 'kbswpused', '\%swpused'
]

"""Pair regexp terms with field names in swap usage output dictionary"""
FIELD_PAIRS_SWP = {
    'swapfree': FIELDS_SWP[0], 'swapused': FIELDS_SWP[1],
    'swapusedpercent': FIELDS_SWP[2]
}

"""I/O usage regexp pattern for detecting SAR section header"""
PATTERN_IO = ".*tps.*rtps.*wtps.*bread\/s.*bwrtn\/s.*"

"""Regexp terms for finding fields in SAR parts for swap usage"""
FIELDS_IO = [
    '^tps', '^rtps', '^wtps', 'bread\/s', 'bwrtn\/s'
]

"""Pair regexp terms with field names in swap usage output dictionary"""
FIELD_PAIRS_IO = {
    'tps': FIELDS_IO[0], 'rtps': FIELDS_IO[1], 'wtps': FIELDS_IO[2],
    'bread': FIELDS_IO[3], 'bwrite': FIELDS_IO[4],

}

"""Restart time regexp pattern for detecting SAR restart notices"""
PATTERN_RESTART = ".*LINUX\ RESTART.*"

"""Pattern for splitting multiple combined SAR file"""
PATTERN_MULTISPLIT = "Linux"

"""Split by date in multiday SAR file"""
PATTERN_DATE = "[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]"

__all__ = [
    "PART_CPU", "PART_MEM", "PART_SWP", "PART_IO", "PART_PAGE", "PART_PRCSW", "PART_RUNQ", 
    "PART_DENT", "PART_PAGESWAP", "PART_RPCMADE", "PART_RPCRCVD","PATTERN_CPU", "PATTERN_MEM", 
    "PATTERN_SWP", "PATTERN_IO", "PATTERN_PRCSW", "PATTERN_RESTART", "PATTERN_MULTISPLIT",
    "PATTERN_DATE", "PATTERN_PAGE", "PATTERN_DENT", "PATTERN_RUNQ", "PATTERN_PAGESWAP", 
    "PATTERN_RPCMADE", "PATTERN_RPCRCVD"
]

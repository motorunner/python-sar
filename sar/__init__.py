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

"""Pagging regex pattern"""
PATTERN_PAGE = ".*pgpgin\/s.*pgpgout\/s.*fault\/s.*majflt\/s.*pgfree\/s.*pgscank\/s.*pgscand\/s.*pgsteal\/s.*\%vmeff.*"

"""Regex terms for finding fields in SAR parts for Pagging"""
FIELD_PAGE = [ 
    'pgpgin\/s', 'pgpgin\/s', 'fault\/s', 'majflt\/s', 'pgfree\/s', 'pgscank\/s' ,'pgscand\/s', \
    'pgsteal\/s', '\%vmeff'
]

"""Pair regexp terms for finding fields in SAR parts for Proc Pagging"""
FIELDS_PAIRS_PAGE = { 
    'pgpgin':FIELD_PAGE[0], 'pgpgout':FIELD_PAGE[1], 'fault':FIELD_PAGE[2], 
    'majflt':FIELD_PAGE[3], 'pgfree':FIELD_PAGE[4], 'pgscank':FIELD_PAGE[5], 
    'pgscand':FIELD_PAGE[6], 'pgsteal':FIELD_PAGE[4], 'vmeff':FIELD_PAGE[8]
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
    "PART_CPU", "PART_MEM", "PART_SWP", "PART_IO", "PART_PAGE", "PART_PRCSW", 
    "PATTERN_CPU", "PATTERN_MEM", "PATTERN_SWP", "PATTERN_IO", "PATTERN_PRCSW"
    "PATTERN_RESTART", "PATTERN_MULTISPLIT", "PATTERN_DATE", "PATTERN_PAGE"
]

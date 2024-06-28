types = ["A",
"AAAA",
"AFSDB",
"ANY",
"APL",
"ATMA",
"AVC",
"AXFR",
"CAA",
"CDNSKEY",
"CDS",
"CERT",
"CNAME",
"CSYNC",
"DHCID",
"DLV",
"DNAME",
"DNSKEY",
"DS",
"EID",
"EUI48",
"EUI64",
"GID",
"GPOS",
"HINFO",
"HIP",
"HTTPS",
"ISDN",
"IXFR",
"KEY",
"KX",
"L32",
"L64",
"LOC",
"LP",
"MAILA",
"MAILB",
"MB",
"MD",
"MF",
"MG",
"MINFO",
"MR",
"MX",
"NAPTR",
"NID",
"NIMLOC",
"NINFO",
"NS",
"NSEC",
"NSEC3",
"NSEC3PARAM",
"NULL",
"NXT",
"None",
"OPENPGPKEY",
"OPT",
"PTR",
"PX",
"RKEY",
"RP",
"RRSIG",
"RT",
"Reserved",
"SIG",
"SMIMEA",
"SOA",
"SPF",
"SRV",
"SSHFP",
"SVCB",
"TA",
"TALINK",
"TKEY",
"TLSA",
"TSIG",
"TXT",
"UID",
"UINFO",
"UNSPEC",
"URI",
"X25",
"ZONEMD",
"NSAPPTR",
]

for typ in types:
    lower = typ.lower()
    print(f"""
case dns.Type{typ}:
		var {lower} dns.{typ}
		err = json.Unmarshal([]byte(jsonString), &{lower})
		if err != nil {{
			return nil, fmt.Errorf("failed to parse json: %s", err.Error())
		}}
		return &{lower}, nil
""")
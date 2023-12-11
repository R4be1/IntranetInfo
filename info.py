import re
import json

info = dict()
unknown = list()
ip_rule = re.compile(r'\d+[\.]\d+[\.]\d+[\.]\d+')
domain_rule = re.compile(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?')

with open('inresult.txt') as result_file:
    for line in result_file:
        match = re.findall( ip_rule, line )

        if match and match[0] not in info:
            current_ip=match[0]
            info[match[0]] = [line.strip()]

        elif match and match[0] in info:
            current_ip=match[0]
            info[match[0]].append(line.strip())

        elif line[0]==' ':
            info[current_ip].append(line.strip())

        else:
            unknown.append(line)

new_info = dict()

with open('ininfo.txt','w') as result_file:
    for ip in sorted( info, key=lambda _: sum([int(s) for s in _.split('.')]) ):
        print("_"*40)
        result_file.write("_"*40+"\n")
        print(f"\033[1;31m{ip} \033[0m:")
        result_file.write(f"{ip} :\n")
        ip_info = sorted( list(set(info[ip])) )
        for _ in ip_info:
            print(f'    {_}')
            result_file.write(f'    {_}\n')

        new_info[ip] = ip_info

#print(json.dumps(new_info, indent=4))
#print("\n")
print(set(unknown))

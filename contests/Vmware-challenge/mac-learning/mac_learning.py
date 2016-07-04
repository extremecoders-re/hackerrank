N = input()
M = {}

def isMulticast(mac):
    return int(mac[0:2], 16) & 1 == 1

for i in range(0, N):
    line = raw_input()
    port_in, d_mac, s_mac = line.split()

    if isMulticast(s_mac):
        print 'drop'
    else:
        M[s_mac] = port_in

        if isMulticast(d_mac):
            print 'flood'
        else:
            if not M.has_key(d_mac):
                print 'flood'
            else:
                port_out = M[d_mac]

                if port_in == port_out:
                    print 'drop'
                else:
                    print port_out
# This Program calculates:
# Number of hosts per subnet,
# Number of mask bits,
# Wildcark Mask
# Network Address
# Broadcast Address
# Permitted range of host address
# Maximum number of subnets
# And generates a rondom IP in the host range


import random # For randint function

def subnet_calc():
    """Function to design the subnet calculator to find:
     Number of hosts per subnet,
     Number of mask bits,
     Wildcark Mask
     Network Address
     Broadcast Address
     Permitted range of host address
     Maximum number of subnets
     And generates a rondom IP in the host range"""

    try:

        while True:
            # Take IP as input
            input_ip = raw_input("\nEnter the IP address: ")

            # Validate the IP
            octet_ip = input_ip.split(".")
            #print octet_ip
            int_octet_ip = [int(i) for i in octet_ip]

            if (len(int_octet_ip) == 4) and (int_octet_ip[0] != 127) and (int_octet_ip[0] != 169) and  (0 <= int_octet_ip[1] <= 255) and (0 <= int_octet_ip[2] <=255) and (0 <= int_octet_ip[3] <= 255):
                break
            else:
                print "Invalid IP, retry \n"
                continue

        # Predefine possible subnet masks
        masks = [0, 128, 192, 224, 240, 248, 252, 254, 255]
        while True:

            # Take subnet mask as input
            input_subet = raw_input("\nEnter the Subnet Mask: ")


            # Validate the subnet mask
            octet_subnet = [int(j) for j in input_subet.split(".")]
            #print octet_subnet
            if (len(octet_subnet) == 4) and (octet_subnet[0] == 255) and (octet_subnet[1] in masks) and (octet_subnet[2] in masks) and (octet_subnet[3] in masks) and (octet_subnet[0] >= octet_subnet[1] >= octet_subnet[2] >= octet_subnet[3]):
                break
            else:
                print "Invalid subnet mask, retry\n"
                continue

########################## Converting IP and subnet to binary #####################


        ip_in_binary = []

        # Convert each IP octet to binary
        ip_in_bin_octets = [bin(i).split("b")[1] for i in int_octet_ip]

        # make each binary octet of 8 bit length by padding zeros
        for i in range(0,len(ip_in_bin_octets)):
            if len(ip_in_bin_octets[i]) < 8:
                padded_bin = ip_in_bin_octets[i].zfill(8)
                ip_in_binary.append(padded_bin)
            else:
                ip_in_binary.append(ip_in_bin_octets[i])

        # join the binary octets
        ip_bin_mask = "".join(ip_in_binary)

        #print ip_bin_mask

        sub_in_bin = []

        # convert each subnet octet to binary
        sub_bin_octet = [bin(i).split("b")[1] for i in octet_subnet]

        # make each binary octet of 8 bit length by padding zeros
        for i in sub_bin_octet:
            if len(i) < 8:
                sub_padded = i.zfill(8)
                sub_in_bin.append(sub_padded)
            else:
                sub_in_bin.append(i)

        #print sub_in_bin

        sub_bin_mask = "".join(sub_in_bin)
        #print sub_bin_mask
        #print len(sub_bin_mask)


        #calculating number of hosts

        no_zeros = sub_bin_mask.count("0")
        no_ones = 32 - no_zeros
        no_hosts = abs(2 ** no_zeros - 2)

        #print no_hosts


        # Calculating wildcard mask
        wild_mask = []
        for i in octet_subnet:
            wild_bit = 255 - i
            wild_mask.append(wild_bit)

        wildcard = ".".join([str(i) for i in wild_mask])
        #print wildcard


        # Calculatig the network and broadcast address
        network_add_bin = ip_bin_mask[:(no_ones)] + "0" * no_zeros
        broadcast_add_bin = ip_bin_mask[:(no_ones)] + "1" * no_zeros


        network_add_bin_octet = []
        broadcast_binoct = []

        [network_add_bin_octet.append(i) for i in [network_add_bin[j:j+8] for j in range(0, len(network_add_bin), 8)]]
        [broadcast_binoct.append(i) for i in [broadcast_add_bin[j:j+8] for j in range(0,len(broadcast_add_bin),8)]]

        network_add_dec_final = ".".join([str(int(i,2)) for i in network_add_bin_octet])
        broadcast_add_dec_final = ".".join([str(int(i,2)) for i in broadcast_binoct])

        #Calculate the host IP range
        first_ip_host = network_add_bin_octet[0:3] + [(bin(int(network_add_bin_octet[3],2)+1).split("b")[1].zfill(8))]
        first_ip = ".".join([str(int(i,2)) for i in first_ip_host])


        last_ip_host = broadcast_binoct[0:3] + [bin(int(broadcast_binoct[3],2) - 1).split("b")[1].zfill(8)]
        last_ip = ".".join([str(int(i,2)) for i in last_ip_host])

        # print all the computed results

        print "\nThe entered ip address is: " + input_ip + "\n"
        print "The entered subnet mask is: " + input_subet + '\n'
        print "Calculated number of hosts per subnet: {0}\n".format(str(no_hosts))
        print "Calculated number of mask bits: {0}\n".format(str(no_ones))
        print "Calculated wildcard mask is: {0}\n".format(wildcard)
        print "The Network address is: {0}\n".format(network_add_dec_final)
        print "The Broadcast address is: {0}\n".format(broadcast_add_dec_final)
        print "IP address range is: {0} - {1}\n".format(first_ip, last_ip)
        print "Maximum number of subnets is: " + str(2**abs(24 - no_ones)) + '\n'
        list_ip = []

        # ask to generate a random ip in the range
        if raw_input("Do you want to generate a random ip? [y/n]") == 'y':
            while True:
                randip = []

                # check if the octet bit is same in first and last host address. If same, append it. else generate random IP
                for i in range(0,len(first_ip_host)):
                    for j in range(0,len(last_ip_host)):
                        if i == j:
                            if first_ip_host[i] == last_ip_host[j]:
                                randip.append(int(first_ip_host[i],2))
                            else:
                                randip.append(random.randint(int(first_ip_host[i],2),int(last_ip_host[j],2)))


                random_ip_final = ".".join(str(i) for i in randip)

                # check if generated IP has already been printed. If so, compute again till unique IP is obtained
                if random_ip_final in list_ip:
                    # if all IPs in the host range are used, exit
                    if len(list_ip) == no_hosts:
                        print "All IPs in the range used up, exiting\n"
                        break
                    continue
                else:
                    print random_ip_final + '\n'

                list_ip.append(random_ip_final)
                print "List of generated IPs:" , sorted(list_ip) ,'\n'

                if raw_input("\nGenerate another random IP? [y/n]") == 'y':
                    continue
                else:
                    break

    except KeyboardInterrupt:
        print "Interrupted by the User, exiting\n"
    except ValueError:
        print "Seem to have enterred an incorrect value, exiting\n"

# Calling the above defined function
subnet_calc()
# Subnet Calculator

The program takes an IP address and a subnet mask as input and gives the following information about the inputs:
<ul>
    <li>Network Address</li>
    <li>Broadcast Address</li>
    <li>Number of valid hosts per subnet</li>
    <li>Wildcard Mask</li>
    <li>Mask Bits</li>
</ul>
The program then prompts the user if they require a random IP within the range of the given subnet mask. If yes, a unique IP is generated and the prompt pops again until the user does not requre any more IP addresses. At this point the program terminates

## Getting Started

Download the program and place it into desired folder. 

If you're using Linux/MAC OS, open terminal and browse to the downloaded folder and run ```python subnetcalc.py```.
if you're using windows, make sure you have Python2.7 set up (See [Python installation on windows](http://stackoverflow.com/a/21373411/7586417) ). Open command prompt and browse to the installed folder and run ```python subnetcalc.py```

### Prerequisites

No external libraries used. Make sure the internal libraries especially *sys* and *random* libraries are importable. These come builtin with standard Python package and there is no need to install any external libraries.

## Running the program

When the program is run, the following prompt is obtained:

```Enter an IP address:```

Type the desired IP address that you want to find information about and press Enter. The next prompt is:

```Enter a subnet mask:```

Type the subnet mask corresponding to the IP address given and press Enter. After the information is generated, the program prompts for the generation of a random IP address. It's totally upto you! type 'y' for yes or 'n' for no and press Enter.

### Example
```
Enter an IP address: 10.0.0.1
Enter a subnet mask: 255.0.0.0


Network address is: 10.0.0.0
Broadcast address is: 10.255.255.255
Number of valid hosts per subnet: 16777214
Wildcard mask: 0.255.255.255
Mask bits: 8


Generate random ip address from subnet? (y/n)y
Random IP address is: 10.182.239.24


Generate random ip address from subnet? (y/n)n
Ok, bye! 

```
## Author

* **Sumit Chachadi** *-sumitmal@buffalo.edu*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details




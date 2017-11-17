#!/usr/bin/python
from src import *

def main():
    os.system("rm -rf tmp/ geckodriver.log") # delete tmp if created from previous usage
    
    parser = argparse.ArgumentParser(description='Bruteforce framework written in Python')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--service', dest='service', help="Provide a service being attacked.\
                          The Protocols and Services supported are SSH, FTP, SMTP, XMPP, TELNET, INSTAGRAM, FACEBOOK, TWITTER, MEETME, PORNHUB, CHATURBATE, NETFLIX, YESMOVIES, HUNTEDCOW", \
                          metavar='',choices=['ssh', 'ftp', 'smtp', 'xmpp', 'telnet', 'instagram', 'facebook', 'twitter', 'meetme', 'pornhub', 'chaturbate', 'netflix', 'yesmovies', 'huntedcow'])
    required.add_argument('-u', '--username', dest='username', help='Provide a valid username for service/protocol being executed')
    required.add_argument('-w', '--wordlist', dest='password', help='Provide a wordlist or directory to a wordlist')
    parser.add_argument('-a', '--address', dest='address', help='Provide host address for specified service. Required for certain protocols')
    parser.add_argument('-p', '--port', type=int, dest='port', help='Provide port for host address for specified service. If not specified, will be automatically set')
    parser.add_argument('-d', '--delay', type=int, dest='delay', help='Provide the number of seconds the program delays as each password is tried')
    # parser.add_argument('--proxy', dest='proxy', help="Providing a proxy for anonymization and avoiding time-outs")

    args = parser.parse_args()
    
    # Specify mandatory options.
    man_options = ['username', 'password']
    for m in man_options:
        if not args.__dict__[m]:
            # Print help for convenience
            parser.print_help()
            print R + "[!] You have to specify a username AND a wordlist! [!]" + W
            exit(1)
    
    service = args.service
    username = args.username
    wordlist = args.password
    address = args.address
    port = args.port
    delay = args.delay
        
    print header
    print (G + "[*] Username: %s " % username) + W
    sleep(0.5)
    print (G + "[*] Wordlist: %s " % wordlist) + W
    sleep(0.5)
    
    if os.path.exists(wordlist) == False:
        print R + "[!] Wordlist not found! [!]" + W
        exit(1)
        
    print (C + "[*] Service: %s "  % service) + W
    if service is None:
        print R + "[!] No service provided! [!]" + W
        exit(1)

    if delay is None:
        print O + "[?] Delay not set! Default to 1 [?]" + W
        delay = 1
        
    sleep(0.5)
    
    protocols = ["ssh", "ftp", "smtp", "telnet", "xmpp"]
    web = ["instagram", "twitter", "facebook", "meetme", "pornhub", "chaturbate", "netflix", "yesmovies", "huntedcow"]
    
    if service in protocols:
        p = ProtocolBruteforce(service, address, username, wordlist, port, delay)
        p.execute()
    elif service in web:
        # Web services do not require a port
        if address or port:
            print R + "[!] NOTE: You don't need to provide an address OR port [!]" + W
            exit(1)
        w = WebBruteforce(service, username, wordlist, delay)
        w.execute()
    else:
        print R + "[!] No such service found! [!]" + W


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print R + "\n[!] Keyboard Interrupt detected! Killing program... [!]" + W
        exit(1)

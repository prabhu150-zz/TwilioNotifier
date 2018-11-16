from twilio.rest import TwilioRestClient 
import urllib2
import re
import time
 
account_sid = "################" #hidden for privacy
auth_token = "################"  #hidden for privacy  
 
client = TwilioRestClient(account_sid, auth_token)
 
while 1:
    urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({'http': 'proxy.server:3128'})))
    donors_choose_url = "http://mu.ac.in/portal/results/" # university website
    response = urllib2.urlopen(donors_choose_url) 
    json_response = json.load(response)  # loads content into JSON file
    html_content = json.dumps(json_response)
    matches = re.findall('B.E.DEGREE [(]INFORMATION TECH. ENGG.[)] [(]SEM-VIII[)][(]CBSGS[)]', html_content);
 

    if len(matches) == 0: 
       print "Results not declared!" 
       time.sleep(7200) # checks every 2 hours
 
    else:
       msg = client.messages.create(to="+1 #######", from_="+1####", body="Results Out! Good Luck! Here you go: http://mu.ac.in/portal/results/") 
       print "SMS Sent"
       quit()
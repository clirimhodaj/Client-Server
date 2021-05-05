import socket
import random
import datetime
import threading
print("*****************************************************************************************");
print("\n\n                                    FIEK-TCP Serveri                                     \n\n");  
print("*****************************************************************************************");
serverName=input("\n\nShenoni emrin e serverit (ipaddress): ");
serverPort=input("Shenoni portin e serverit: ");
if serverName == "":
    serverName = "localhost";
if serverPort == "":
    serverPort = 13000;
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((serverName,int(serverPort)))
print('Serveri eshte startuar ne '+str(serverName)+' porti:'+str(serverPort))
server.listen(5)
print('Serveri eshte i gatshem te pranoje kerkesa')

def GAME():
    array=[]
    i=0
    while i<5:
        n=random.randint(1,35)
        if n not in array:
            array.append(n)
        else:
            continue
        i+=1
    array.sort()
    return array;


def TIME():
    time=datetime.datetime.now()
    return time.strftime('%d.%m.%Y %I:%M:%S %p');

def PALINDROME(fjala):
    val = str(fjala).lower();
    if val == str(val)[::-1]:  
        return "Teksti i dhënë është palindrom";
    else:
        return "Teksti i dhënë nuk është palindrom";
    


def GCF(num1,num2):
    while num2!=0:
        tmp=num1;
        num1=num2;
        num2=tmp%num2;
    number_as_string = str(num1)
    return number_as_string;


def REVERSE(fjala):
    reverse= str(fjala[::-1]); 
    return reverse;

    
def COUNT(tekst):
    zanore=0;
    bashketingellore=0;
    tekst = tekst.lower() 
    for i in range(0,len(tekst)):  
        if tekst[i] in ("a","e","i","o","u"):  
              zanore+=1; 
        elif (tekst[i] >= 'a' and tekst[i] <= 'z'):  
              bashketingellore += 1;  
    string="Teksti i pranuar permban " + str(zanore) + " zanore dhe " + str(bashketingellore) + " bashketingellore";
    return string;
    

def CONVERT(option,num):
    result="";
    if option == 'cmToFeets':
        result += str(num*0.0328084);
    elif option == 'FeetToCm':
        result = str(num*30.48);
    elif option == 'KmToMiles':
        result = str(num*0.621371);
    elif option == 'MileToKm':
        result = str(num*1.60934);
    return result;

def LEAPYEAR(year):
    lyear="";
    if (year%100!=0 and year % 4 == 0):
        lyear+="Viti "+ str(year) + " eshte i brishte";
    else:
        lyear+="Viti "+str(year)+" nuk eshte i brishte";
    return lyear;


def RPSGAME(zgjedhja):
    string="";
    zgjedhja=zgjedhja.lower();
    lista=["scissor","rock","paper"];
    zgjedhjapc=random.choice(lista);
    if zgjedhja==zgjedhjapc:
        string="Kompjuteri eshte \""+zgjedhjapc+"\". Ju jeni gjithashtu \""+zgjedhja+"\". Barazim !";
    elif zgjedhja=="scissor" and zgjedhjapc=="rock":
        string="Kompjuteri eshte \""+zgjedhjapc+"\". Ju jeni \""+zgjedhja+"\". Ju keni humbur !";
    elif zgjedhja=="scissor" and zgjedhjapc=="paper":
        string="Kompjuteri eshte \""+zgjedhjapc+"\". Ju jeni \""+zgjedhja+"\". Ju keni fituar !";
    elif zgjedhja=="rock" and zgjedhjapc=="scissor":
        string="Kompjuteri eshte \""+zgjedhjapc+"\". Ju jeni \""+zgjedhja+"\". Ju keni fituar !";
    elif zgjedhja=="rock" and zgjedhjapc=="paper":
        string="Kompjuteri eshte \""+zgjedhjapc+"\". Ju jeni \""+zgjedhja+"\". Ju keni humbur !";
    elif zgjedhja=="paper" and zgjedhjapc=="rock":
        string="Kompjuteri eshte \""+zgjedhjapc+"\". Ju jeni \""+zgjedhja+"\". Ju keni fituar !";
    elif zgjedhja=="paper" and zgjedhjapc=="scissor":
        string="Kompjuteri eshte \""+zgjedhjapc+"\". Ju jeni \""+zgjedhja+"\". Ju keni humbur !";
    return string;



def on_new_client(client,address):

    while True:
        
        try:
            fjalia=client.recv(1024)
            print('Kerkesa e klientit:'+str(fjalia.decode("utf-8")))
            fEdekoduar=fjalia.decode("utf-8");
            
            if fEdekoduar.lower() == "quit" or fEdekoduar.lower() == "dil" or fEdekoduar.upper() == "NDRYSHOSERVERIN":
                break;
            elif fEdekoduar == "IPADDRESS":
                answer="IP Adresa e klientit eshte: " + address[0];
            elif fEdekoduar == "PORT":
                answer="Porta e klientit eshte: " + str(address[1]);
            elif fEdekoduar == "TIME":
                answer=TIME();
            elif fEdekoduar.split(" ")[0] == "GCF":
                answer=GCF(int(fEdekoduar.split(" ")[1]),int(fEdekoduar.split(" ")[2]));
            elif fEdekoduar.split(" ")[0] == "PALINDROME":
                answer=PALINDROME(fEdekoduar[11:]); 
            elif fEdekoduar.split(" ")[0] == "REVERSE":
                answer=REVERSE(fEdekoduar[8:]);
            elif fEdekoduar.split(" ")[0] == "COUNT":
                answer=COUNT(fEdekoduar[6:]);
            elif fEdekoduar.split(" ")[0] == "CONVERT":
                answer=CONVERT(fEdekoduar.split(" ")[1],int(fEdekoduar.split(" ")[2]));
            elif fEdekoduar == "GAME":
                answer=str(GAME());
            elif fEdekoduar.split(" ")[0] == "LEAPYEAR":
                answer = LEAPYEAR(int(fEdekoduar.split(" ")[1]));
            elif fEdekoduar.split(" ")[0] == "RPSGAME":
                answer = RPSGAME(fEdekoduar.split(" ")[1]);
            else:
                answer="Formati i tekstit qe duhet te shenohet eshte : [Metoda (me shkronja te medha)] [Hapesire] [Argumenti --> (nese ka)] ";
        except Exception as e:
            answer="Argumentet duhet te jene numra te thjeshte ose stringje";
        except BaseException as e:
            answer="Kerkesa e klientit nuk duhet te jete e zbrazet";

        client.send(str.encode(answer))
    print("Klienti me IP: "+address[0]+" dhe port: "+str(address[1])+ " eshte shkyqyr")
    client.close()
  
    


while True:
    try:
        client,address=server.accept();
        threading._start_new_thread(on_new_client,(client,address));
    except KeyboardInterrupt:
        print("Serveri u fik ! ");
    except Exception as e:
        print("Gabim i paparashikuar ! ");





 
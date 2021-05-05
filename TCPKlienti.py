import socket

def main():
    serverName=input("\n\nShenoni emrin e serverit (ip-address): ");
    serverPort=input("Shenoni portin e serverit: ");
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((serverName,int(serverPort)))
    except BaseException as e:
        print(f"Ju deshtuat te lidheni ne serverin me ip:{serverName} dhe port:{serverPort}");
        main();

    while True:
        var=input("\nOperacioni(IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT,LEAPYEAR,RPSGAME)?\n ")
        s.sendall(str.encode(var))
        if var=="":
            print("Kerkesa e klientit nuk duhet te jete e zbrazet");
            continue;
        elif var.lower() =="quit" or var.lower() == "dil":
             print("Jeni shkyqur nga serveri !");
             break;
        elif var.upper() == "NDRYSHOSERVERIN":
            main();
        mesazhi=''
        data=s.recv(1024)
        if len(data)<=0:
            break
        mesazhi+=data.decode("utf-8")
        print('Pergjigjja: ',mesazhi)
 
print("*****************************************************************************************");
print("\n\n                                    FIEK-TCP Klienti                                     \n\n");  
print("*****************************************************************************************");
print("\n\nMë poshtë janë paraqitur të gjitha metodat e implementuara: ");
print("IPADDRESS");
print("PORT");
print("COUNT {hapësirë} tekst");
print("REVERSE {hapësirë} tekst");
print("PALINDROME {hapësirë} tekst");
print("TIME");
print("GAME");
print("GCF {hapësirë} numri1 {hapësirë} numri2");
print("LEAPYEAR {hapësirë} viti");
print("RPSGAME {hapësirë} Përzgjedhja");
print("Opsionet e përzgjedhjes janë:");
print("                     scissor");
print("                     rock");
print("                     paper\n");
print("CONVERT {hapësirë} Opsioni {hapësirë} Numër(i plotë)");
print("Opsionet janë:");
print("                     cmToFeets");
print("                     cmToFeets");
print("                     KmToMiles");
print("                     MileToKm\n");
print("*****************************************************************************************");
print("\nPër tu shkyqyr nga serveri shtyp \"dil\" ose \"quit\"");
print("Për të ndryshuar serverin shtyp metodën \"NDRYSHOSERVERIN\"");
main(); 
from socket import *;

def main():
    try:
        serverName = input("\n\nShkruani emrin e serverit(ipaddress): ");
        serverPort = input("Shkruani portin e serverit: ");
        clientSocket = socket(AF_INET, SOCK_DGRAM)
    except BaseException as e:
        print(f"Ju deshtuat te lidheni ne serverin me ip:{serverName} dhe port:{serverPort}");
        main();
    while True:
        message = input("\nOperacioni(IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT,LEAPYEAR,RPSGAME)?\n");
        clientSocket.sendto(message.encode(),(serverName, int(serverPort)))
    
        if message=="":
            print("Kerkesa e klientit nuk duhet te jete e zbrazet");
            continue;
        elif message.lower()=="quit" or message.lower()=="dil":
            print("Jeni shkyqyr nga serveri !");
            break;
        elif message.upper() == "NDRYSHOSERVERIN":
            main();
  
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        print("Pergjigjja: "+modifiedMessage.decode())
    clientSocket.close();
print("*****************************************************************************************");
print("\n\n                                    FIEK-UDP Klienti                                     \n\n");  
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

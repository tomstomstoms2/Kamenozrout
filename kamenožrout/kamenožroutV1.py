import pyperclip;
import time;
import datetime;


top = 0;
i = 0;
blueSum = 0;
blueMax = 0;
orangeSum = 0;
orangeMax = 0;
greenSum = 0;
greenMax = 0;
redSum = 0;
redMax = 0;
htmlOld = "htmlOld";
pyperclip.copy("notHtmlOld");
html = pyperclip.paste();
alert = True;
print("ALERT is " + str(alert));
print("Copy \nSTOP to stop \nALERT for turning alert on/off\nINFO to show info about current run")



while(html != "STOP"):

    blue = html.count("blue");
    orange = html.count("orange");
    green = html.count("green");
    red = html.count("red");
    red -= 2;
    
    

    if(blue + orange + green + red == 240):
        print("OKAY")
        #print("Blue: " + str(blue));
        #print("Orange: " + str(orange));
        #print("Green: " + str(green));
        #print("Red: " + str(red));
        i+=1;
        if(blue>blueMax):
            blueMax = blue;
        if(orange>orangeMax):
            orangeMax = orange;
        if(green>greenMax):
            greenMax = green;
        if(red>redMax):
            redMax = red;
        blueSum += blue;
        orangeSum += orange;
        greenSum += green;
        redSum += red;
        if(alert == True):
            if(blue >= 80):
                print("BLUE ALERT: " + str(blue));
            if(orange >= 80):
                print("ORANGE ALERT: " + str(orange));
            if(green >= 80):
                print("GREEN ALERT: " + str(green));
            if(red >= 80):
                print("RED ALERT: " + str(red));
    
    else:
        print("NOT OKAY")
        
    if(html == "INFO" and i != 0):
        print("Iterations: " + str(i));
        print("blueAverage: " + str(blueSum/i));
        print("Blue Max: " + str(blueMax))
        print("orangeAverage: " + str(orangeSum/i));
        print("Orange Max: " + str(orangeMax))
        print("greenAverage: " + str(greenSum/i));
        print("green Max: " + str(greenMax))
        print("redAverage: " + str(redSum/i));
        print("red Max: " + str(redMax));
        
    if(html == "ALERT"):
        alert = not alert;
        print("ALERT = " + str(alert))
        
    #time.sleep(3);
    while(html == htmlOld):
        html = pyperclip.paste();
        time.sleep(0.2);
    
    htmlOld = html;
    #print("Next " + str(i));

if(i == 0):
    print("Empty run.");
else:
    print("Iterations: " + str(i));
    print("blueAverage: " + str(blueSum/i));
    print("Blue Max: " + str(blueMax));
    print("orangeAverage: " + str(orangeSum/i));
    print("Orange Max: " + str(orangeMax));
    print("greenAverage: " + str(greenSum/i));
    print("green Max: " + str(greenMax));
    print("redAverage: " + str(redSum/i));
    print("red Max: " + str(redMax));
    with open('kamenozroutV1.txt', 'a') as f:
        f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
        f.write("TIME: " + str(datetime.datetime.now()));
        f.write("\n");
        f.write("Iterations: " + str(i));
        f.write("\n");
        f.write("blueAverage: " + str(blueSum/i));
        f.write("\n");
        f.write("Blue Max: " + str(blueMax));
        f.write("\n");
        f.write("orangeAverage: " + str(orangeSum/i));
        f.write("\n");
        f.write("Orange Max: " + str(orangeMax));
        f.write("\n");
        f.write("greenAverage: " + str(greenSum/i));
        f.write("\n");
        f.write("green Max: " + str(greenMax));
        f.write("\n");
        f.write("redAverage: " + str(redSum/i));
        f.write("\n");
        f.write("red Max: " + str(redMax));
        f.write("\n");
        f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
        f.close();
    

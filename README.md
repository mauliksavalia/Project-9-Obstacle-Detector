# Project 9 : Obstcle Detector system using Motion and proximity Sensor

# Disclaimer I uploaded receiver side of project where we made application in JAVA as I worked on frontend part.

## JAVA GUI
GUI (Graphical User Interface) in Java is an easy-to-use visual experience builder for Java applications. It is mainly made of graphical components like buttons, labels, windows, etc. through which the user can interact with an application. GUI plays an important role to build easy interfaces for Java applications.

## Requirements
There are two requirements for developing with at_java on your machine.

Java with version of 8 or higher

Maven

A code editor

## AtSign 
The atPlatform's primary network protocol is the atProtocol. AtSigns—unique identifiers for individuals, entities, and things—are provided by the atPlatform. 

Each atSign generates a unique set of private and public cryptographic keys. The atProtocol makes the public keys available to the entire world while maintaining the privacy of the private keys. 

The fully qualified atSigns and the information in their secondary servers can be interacted with using verbs provided by the atProtocol.

If you’re making a Java app, you can either fork the at_java repository and run mvn install to create a JAR to use a dependency, or create a maven project and use our dependency through the pom.xml.



## Creating an instance of AtClient
To create an instance of AtClient, use one of the factory methods. Note: you must have the .atKeys file in the ~/.atsign/keys directory. You can generate a .atKeys file from using the Register CLI or Onboaring CLI if you already own the atSign.

String ATSIGN_STR = "@bob";
AtSign atSign = new AtSign(ATSIGN_STR);
AtClient atClient = null;
try {
    atClient = AtClient.withRemoteSecondary(atSign);
} catch (AtException e) {
    System.err.println(e);
    e.printStackTrace();
}

## How to run java application
1. Clone the GitHub repositery.
2. Open JAVA folder in any code editor. (Preferable editor : Visual Studio Code (VSC) 
link to Download VSC: https://code.visualstudio.com/download
3. Open the src folder.
4. In src folder, run main.java or if you are using VSC, just click right side top trinagle button and then Run JAVA button.



## Working of the project
When you run main.java file, it will open application screen in which there are two buttons for proximity and motion detection, when you press any of the button , it will open new window and it will show result in a loop in boolean according the motion and proximity. When you're close to IOT device, result will chnage for motion detection and it will show true in a loop until you're close to device.

## My Work
Basically I worked on the JAVA application and significantly I made UI.

First I worked on the Flutter app and made connection, and started coding in the dart but it got hard for me to work in dart as I have never worked on DART. Therefore, we shifted to JAVA appliation.

I had done the commenting in java application and worked on presentation slides.

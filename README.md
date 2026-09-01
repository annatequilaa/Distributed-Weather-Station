# Unit 2: A Distributed Weather Station for Survival of a Stray Cat

## Criteria A: Planning

## Problem definition
Halley, a stray cat residing near a school, faces significant challenges as seasons change. For example, the harsh winter weather, characterized by extremely cold and dry conditions, poses serious risks to Halley’s well-being. These risks include respiratory issues like asthma and bronchitis, exacerbated by low humidity (1), as well as hypothermia and frostbite due to freezing temperatures, wind, and snow (2). Another example is the summer, characterized by extremely hot conditions which are also detrimental to Halley's health. Given the concerns of the students and teachers who wish to ensure Halley’s safety, the primary problem is determining if a suitable indoor space on campus can provide appropriate environmental conditions, particularly regarding humidity and temperature, to improve Halley’s chances of survival and comfort. _*See the evidence of consultation in the appendix_
## Proposed Solution
Considering the client's requirements an adequate solution includes a low-cost sensing device for humidity and temperature and a custom data script that processes and analyzes the samples acquired. For a low-cost sensing device, an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequate precision and range for the client's requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20, or the AM2301B [^2] have higher specifications, however, the DHT11 uses a simple serial communication (SPI) rather than more elaborated protocols such as the I2C used by the alternatives. For the range, precision, and accuracy required in this application, the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often-used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In addition to the low cost of the Arduino (< 6USD), this device is programable and expandable[^1]. I considered alternatives such as different versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constraints of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability without the need for extensive redevelopment [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a high-level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is the responsibility of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition, an HLL language will allow me and future developers to extend the solution or solve issues promptly.  

## Success Criteria

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 

1. The solution provides a visual representation of the Humidity, Temperature, and atmospheric pressure (HL) values inside a dormitory (Local) and outside the house (Remote) for a period of a minimum of 48 hours.
- **Issues tackled:** This solution helps solve the shortage of insight into the environmental conditions over time, both inside and outside the dormitory, which could help in identifying patterns or irregularities.
2. ```[HL]``` The local variables will be measured using a set of sensors around the dormitory.
- **Issues tackled:** Data collection is spatially distributed to accurately reflect variations in environmental conditions across different areas of the dormitory.
3. The solution provides mathematical modeling for the Humidity, Temperature, and atmospheric pressure (HL) levels for each Local and Remote location. ```(SL: linear model)```, ```(HL: non-linear model)```
- **Issues tackled:** This solution resolves the difficulty in understanding the relationships between variables and the need for precise modeling to predict how these factors interact locally and remotely.
4. The solution provides a comparative analysis of the Humidity, Temperature, and atmospheric pressure (HL) levels for each Local and Remote location including standard deviation, minimum, maximum, and median. 
- **Issues tackled:** This solution helps assess variability and identify extreme values or trends.
5. ```(SL)```The local samples are stored in a CSV file and ```(HL)``` posted to the remote server as a backup. 
- **Issues tackled:** This solution resolves the risk of data loss and lack of organized storage and accessibility for collected data over time.
6. The solution provides a prediction for the subsequent 12 hours for Humidity, Temperature and atmospheric pressure (HL).
- **Issues tackled:** This solution offers predictive insights into upcoming environmental changes, which could help in proactive decision-making.
7. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature, and atmospheric pressure (HL).
- **Issues tackled:** This solution resolves the challenge of a consolidated summary to communicate findings, models, and recommendations effectively, preventing informed actions based on the analysis.

_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change?_

**1. How does our use of technology shape our understanding of the environment?**
  Technology uncovers patterns and trends, such as rising global temperatures and shifting weather patterns, that would be impossible to detect through observation alone. Predictive models, satellite imaging, and machine learning provide insights into the causes and impacts of climate change, guiding policy and action. This technological lens allows us to grasp the scale and complexity of environmental issues more clearly than ever before.
  
  However, the use of data science raises critical questions, such as "How do we account for biases in data collection and limitations in models that might skew findings?" "Are interpretations of data shaped by human or algorithmic assumptions, and how does this affect conclusions?" Ethical concerns occur when data is used selectively or disproportionately to influence policies, potentially marginalizing certain communities.

**2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?** 
  In the context of our project, we must ensure the privacy of individuals by anonymizing any collected data and being transparent about how it is used. Users should give informed consent for the monitoring process, knowing exactly what data is being collected and for what purpose. Security measures such as encryption and secure storage must be implemented to protect the data from unauthorized access. Additionally, we should adhere to data minimization, collecting only the environmental information necessary to improve living conditions without compromising personal privacy.

**3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus?**
  One of the key factors is the perception of comfort, which can vary depending on cultural backgrounds; for example, individuals from warmer climates may tolerate higher temperatures and humidity better than those from cooler regions. Additionally, occupancy patterns in different parts of the campus, such as dormitories versus study buildings, can create variability in readings, as higher foot traffic or different uses of space may influence temperature and humidity levels.

  Contextual elements like building design and maintenance also play a role, as older buildings may have poorer insulation or ventilation, messing up the comparison with newer or better-maintained structures. The timing of the readings is another important factor; environmental conditions may differ between daytime and nighttime due to varying activities or heating schedules. Finally, expectations and biases among users can affect interpretation, as individuals may attribute discomfort to specific factors (e.g., blaming humidity over temperature) based on personal experiences or assumptions, even if the data suggests otherwise. 
# Criteria B: Design
![System Diagrams unit 2 (1)](https://github.com/user-attachments/assets/7ec53d20-7afa-4279-8ac2-b5798e38f4db)

**Fig.1** System diagram (HL) for the proposed system to visualize and analyze temperature and humidity data on our campus. Physical variables were measured with a network of DHT11/BMP280 sensors locally. A remote server provides an API for remote monitoring and storage via the ISAK-S network. 
![System Diagrams(2)](https://github.com/user-attachments/assets/32b39860-84fc-4718-bbd3-f137cc38b8cb)
![2](https://github.com/user-attachments/assets/e66662a2-0d0d-4a31-b10e-53b7e23baec1)
![3](https://github.com/user-attachments/assets/085a9558-75a2-4d2e-9aec-8d690f5db1d9)

**Fig.2, Fig.3, Fig.4** illustrate the locations of the DHT11 and BME280 sensors, which are connected to a computer and placed around the R3-10 dormitory. The sensors are positioned at varying distances from the nearest window to compare changes in temperature, humidity, and pressure. The order of the collection locations is as follows: 

1. On the table below the TV, 5 meters from the large window in the common room (first 12 hours)
2. On the table 1 meter from the large window in the common room (next 12 hours)
3. On the center table in the kitchen, 3 meters from the kitchen window (third cycle of 12 hours)
4. On a table in a student's room, 3 meters from the large window (last 12 hours)

## Data Storage
1. Local storage (CSV):
![image](https://github.com/user-attachments/assets/b86cb439-246a-4ae5-aa2e-9ac476e39846)
**Fig.5** stored data in local csv file

2. Remote storage (API):
![image](https://github.com/user-attachments/assets/c04ba721-50f1-4968-a2ea-e9950707249d)
**Fig.6** stored data in remote network

## Flow Diagrams

![image](https://github.com/user-attachments/assets/9b4b2ce2-44f5-44e3-9704-608c87124e9c)

**Fig.5** shows the flow diagram for one of the most used functions in the graphing part of this project: ```plot_data()```. This function plots a graph from the parameters passed into the function, with spaced out xticks labels. 

![image](https://github.com/user-attachments/assets/fe43662e-accb-42ff-b3e4-0411a0c9de28)

**Fig.6** shows the flow diagram for ```upload_data_from_csv```, the function responsible for uploading the data onto the API from the csv file after saving the data entries in the csv file. 

![image](https://github.com/user-attachments/assets/0880dd32-a228-4816-9cb5-0e351a4febbb)


**Fig.7** shows the flow diagram for the algorithm responsible for retrieving the data from API and processing it to graphable data.  

## Record of Tasks
| 1  | Plan out the problem definition and consultation with the client                                            | Write down problem definition and success criteria.                                                                                                                                                        | 10 mins | Nov 23         | A |
|----|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|----------------|---|
| 2  | Answer TOK connection questions and plan the data collection process                                        | Draft and refine answers for TOK and decide the location of collection.                                                                                                                                    | 20 mins | Nov 23         | A |
| 3  | Research how to set up Arduino sensors                                                                      | Arduino set up finished with correct wiring the computer                                                                                                                                                   | 30 mins | Nov 26         | C |
| 4  | Design BME280 and DHT11 wiring to Arduino                                                                   | Research the wiring setup and connect to our convenience. Download necessary libraries downloaded and have the code ready for collecting data                                                              | 30 mins | Nov 27         | C |
| 5  | Create sensor_ids for remote storage                                                                        | Create a program that request access to local network and create 5 sensor_ids                                                                                                                              | 45 mins | Nov 28         | C |
| 6  | Develop an Adruino file that allows sensors to start collecting data                                        | Research and initialize collection process for both sensors                                                                                                                                                | 45 mins | Nov 29         | C |
| 7  | Test the Adruino program                                                                                    | Test if the Adruino board and laptop is connection and should there be any error, start debugging process before collecting offical data.                                                                  |         |                |   |
| 8  | Develop a program for plotting raw data from both sensors and non-linear mathematical models for these data | Create code (without debugging) to graph: 1. Temperature from both DHT11 and BME280 sensors 2. Humidity from both sensors 3. Pressure from both sensors 4. Non-linear models (ax^2+bx+c) for each property | 45 mins | Nov 30         | C |
| 9  | Develop a program for collecting data to local CSV file                                                     | Create code for sensors to start collecting data and save in CSV file in the order of timestamp, DHT_temperature, DHT_humidity, BME_temperature, BME_pressure, BME_humidity                                | 30 mins | Dec 1          | C |
| 10 | Collect Data                                                                                                | Make sure the sensors can be continuously record for at least 1-day sensor                                                                                                                                 | 2 day   | Nov 30 - Dec 1 | C |
| 11 | Develop a program to upload local data do remote server                                                     | Create a program validate the data and upload values to its respective sensors                                                                                                                             | 3 hours | Dec 2          | C |
| 12 | Test upload process to API with separate id                                                                 | Upload DHT value to 2 extra ids on local network to debug and have a brief overview of how data is transferred.                                                                                            | 45 mins | Dec 3          | C |
| 13 | Create scientific poster                                                                                    | Draft the layout of the poster and fill in project's basic information                                                                                                                                     | 15 mins | Dec 1          | D |
| 14 | Upload official data                                                                                        | Extract data and upload the respective sensor ids on ISAK-S API                                                                                                                                            | 30 mins | Dec 3          | C |
| 15 | Construct Local Graphs Using Pyplot (code development)                                                                        | Using the data uploaded from the API to graph the raw data + average, trendline, and statistics                                                                                                            | 180mins | Dec 5          | C |
| 16 | Draw system diagrams that visualize our process                                                             | Create diagrams of the Adruino board and collecting locations                                                                                                                                              | 30mins  | Dec 6          | B |
| 17 | Design science poster                                                                                       | Complete the poster by incorporating the created graphs and drafting a strong conclusion that effectively summarizes the investigation.                                                                    | 40mins  | Dec 7          | D |
| 18 | Film video introducing our exploration                                                                      | Finish a video that demonstrates proposed solution to clients                                                                                                                                              | 35mins  | Dec 11         | D |
| 19 | Construct Remote Graphs Using Pyplot    (code development)                                                                    | Using the data obtained from remote sensors to graph the raw data + average and trendline, and statistics                                                                                                  | 60mins  | Dec 11         | C |
| 20 | Complete science poster                                                                                     | Putting the finished graphs onto the scientific poster and elaborate and analyze them                                                                                                                      | 35mins  | Dec 11         | D |
| 21 | Create Flow Diagrams to elaborate on our methods                                                            | Draw 3 flow diagrams that demonstrate our methods                                                                                                                                                          | 75mins  | Dec 11         | B |
## Test Plan
| Success Criteria Addressed | Purpose                                                                                                                                       | Input                                                                                                                                                                                                                                                                                                                                                                      | Expected Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1                          | Check graphs for both remote and local data are printed                                                                                       | 1. Open file graphs_local.py and run it. (see expected output to know which windows to refer to) 2. After all the windows of graphs_local.py are closed, open file graphs_remote.py and run it. (see expected output to know which windows to refer to)                                                                                                                    | When graphs_local.py is ran, the first window that pops up will have 5 graphs with smoothed data and raw data as two distinct lines on it (+cubic model but that's irrelevent for this test): temperature from DHT, humidity from DHT, temperature from BME, humidity from BME, pressure from BME. When graphs_remote.py is ran, the first window that pops up would show 3 graphs with smoothed data and raw data as two distinct lines  (+cubic model but that's irrelevent for this test): temperature, humidity, and pressure                                                                                                                                                                          |
| 2                          | Check Arduino Connects to the Computer, and that the connection is fast as an indicator that it is functioning correctly                      | Identify the tester's COM port and connect Arduino's ID, use the serial.serial() function on PyCharm to establish a serial connection. Set the parameter timeout to 0.1                                                                                                                                                                                                    | Program does not timeout. A message confirming that a connection has been established is printed onto the PyCharm console.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 2,5                        | Check that Sensor Retrieves Data and Sends to the computer                                                                                    | Upload program from Arduino IDE that identifies a sensor connected to the correct pins, and reads from so.                                                                                                                                                                                                                                                                 | A serial connection should be established between the Arduino and the computer. The recorded temperature and humidity should appear in the console as follows: "DHT\ntemperature: dht_temp humidity: dht_humidity"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2                          | Check both sensors to ensure they can retrieve and send data in the same circuit                                                              | 1. Connect both DHT and BME sensors to Arduino at once 2. Upload program from Arduino IDE that a) correctly identifies the both sensors in the correct pins and b) returns readings from both sensors 3. Run program in PyCharm which reads and prints lines stored in Arduino                                                                                             | A serial connection should be established between the Arduino and the computer. When running program, a total of 5 different values (2 from DHT 3 from BME) should be printed onto the console.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 3                          | Check a non-linear mathematical model is graphed to represent the trend of the data for both remote and local                                 | 1. Open file graphs_local.py and run it. (see expected output to know which windows to refer to) 2. After all the windows of graphs_local.py are closed, open file graphs_remote.py and run it. (see expected output to know which windows to refer to)                                                                                                                    | When graphs_local.py is ran, the third window that pops up after the previous two are closed will have 3 graphs with smoothed data, raw data, and cubic model as 3 distinct lines on it : average temperature, average humidity, pressure from BME. When graphs_remote.py is ran, after closing the previous windows, the second window that pops up would show 3 graphs with 3 graphs with smoothed data, raw data, and cubic model as 3 distinct lines on it: temperature, humidity, and pressure                                                                                                                                                                                                        |
| 4                          | Check that minimum, maximum, and median for both remote and local data are plotted for analysis and standard deviation plotted for local data | 1. Open file graphs_local.py and run it. (see expected output to know which windows to refer to) 2. After all the windows of graphs_local.py are closed, open file graphs_remote.py and run it. (see expected output to know which windows to refer to)                                                                                                                    | When graphs_local.py is ran, the fourth window that pops up after the previous three are closed will have 3 graphs with smoothed data and raw data as 2 distinct lines on it with 3 dotted lines (median, minimum, maximum) : average temperature, average humidity, pressure from BME. Close the current window, then the next window that pop up would show 3 graphs with smoothed and raw data and shaded area that is standard deviation. When graphs_remote.py is ran, the third window that pops up after the previous two  are closed will have 3 graphs with smoothed data and raw data as 2 distinct lines on it with 3 dotted lines (median, minimum, maximum) : temperature, humidity, pressure |
| 5                          | Check that reading can be saved into a csv file per certain amount of time                                                                    | Run program in PyCharm which reads the data from the Arduino each second for 10 minutes, and then saves the data into a csv file once per minute.                                                                                                                                                                                                                          | A new csv file called "testcase.csv" should be created. Within it, there should be 10 lines, each looking like the following, with different times (timestamp,dhttemp,dhthumidity,bmetemp,bmehumidity,bmepressure)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 5                          | Create Test Sensor and Recording on Server                                                                                                    | 1. Using requests, register user on server, under username "A_square" 2. Similarly, get access token through requests  3. Using access token, create a new sensor called "testing"  4. Confirm "testing" exists under user using requests  5. Send a test recording {'sensor_id:{id},'value':0} to "testing" using requests  6. Get recordings on "testing" using requests | 1. answer should be printed, informing the successful creation of a new user 2. answer should be printed, an access token 3. answer should be printed, informing the successful creation of a new sensor "testing", and its id 4. answer should be printed, showing all of the sensors on the server. The most recent sensor added should be "testing" under user A_square 5. answer should be printed, showing the datetime, value, and sensor id recorded 0. answer should be printed, containing recording of {'value':0}                                                                                                                                                                               |
| 5                          | Check that readings can be sent to the server per certain amount of time                                                                      | Run program in PyCharm which reads the data from the Arduino each second for 30 seconds, and then sends the data {'sensor_id:{id}, 'value':{dhttemp}} to the sensor "testing" previously created on the server using a POST request each 10 seconds. Then, using a GET request, retrieve recordings on "testing" to confirm there are 5 variables.                         | The last 3 recordings in the sensor should contain key and value pairs of {'value':{dhttemp}}. The dhttemp value should correspond to the dhttemp value printed on the console at t=10, 20, and 30.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 6                          | Check that the graphs show the prediction for the next 12 hours based on cubic model for local data.                                          | 1. Open file graphs_local.py and run it. (see expected output to know which windows to refer to) 2. After all the windows of graphs_local.py are closed, open file graphs_remote.py and run it. (see expected output to know which windows to refer to)                                                                                                                    | When graphs_local.py is ran, the fifth window that pops up after the previous four are closed will have 3 graphs with smoothed data, raw data, and cubic model + dotted line extended from the cubic model (the prediction) for 12 hours on the graph as 3 distinct lines on it : average temperature, average humidity, pressure from BME.                                                                                                                                                                                                                                                                                                                                                                |                                                                            |
# Criteria C: Development
### Techniques:
* Nested loops structure.
* Modular structure with functions.
* Error Handling with try-except blocks.
* Data parsing and processing.
* Data mapping with dictionaries. 
* Local file and remote server (API) handling.
* Serial Communication
* List comprehension

### Development:
**Data Collection:**
 
Cited from the file `combined_arduino.ino`:
 
To collect data according to the client's needs, we first set up a connection between two sensors and the Arduino board connected to a computer. This configuration makes it easier to monitor and manage the incoming data.

We designed the setup function as follows:
 
```.C++
void setup() {
    Serial.begin(9600);
```
Initially, we researched about the Serial module, which is an instance of the HardwareSerial class that is part of the Arduino core and allows us to establish the desired connection (1). The `begin()` function is then called with a baud rate of 9600 bits per second (bps). We investigated why this rate is chosen instead of a higher one (for instance, 115200 baud), and found that 9600 bps has been around for  millennials and proved to be sufficient for most basic applications, such as debugging and simple data transmissions, as implemented in this project (2). Subsequently, we configured the Serial Monitor to send messages confirming the progress of the setup process.
 
```.C++
    // Initialize BME280
    Serial.println(F("Initializing BME280..."));
    bool bmeStatus = bme.begin(0x76);
    if (!bmeStatus) {
        Serial.println("Could not find a valid BME280 sensor; check wiring!");
        while (1);
    }
    Serial.println("BME280 initialized successfully!");
 
    // Initialize DHT11
    Serial.println("Initializing DHT11...");
    dht.begin();
    Serial.println("DHT11 initialized successfully!");
}
```
Next, we attempt to start the BME280 sensor. By using `Serial.println(F("Initializing BME280..."))`, a message is printed to indicate that the initialization process has begun. The `bme.begin(0x76)` method is called on the bme object, which tries to communicate with the BME280 sensor using the I2C address 0x76, which is the default for this sensor (3). The return value, stored in the boolean variable `bmeStatus`, is checked to confirm if the sensor was successfully detected. If the sensor is not found, an error message is printed, and the program enters an infinite loop (`while (1);`), halting further execution. If the sensor is found, a success message is printed to the Serial Monitor, similarly for the DHT11 sensor.
```.C++
void loop() {
    // Read BME280 Data
    float bmeTemperature = bme.readTemperature();
    float bmePressure = bme.readPressure() / 100.0F;
    float bmeHumidity = bme.readHumidity();


    // Read DHT11 Data
    float dhtHumidity = dht.readHumidity();
    float dhtTemperature = dht.readTemperature();


    // Handle potential read errors
    if (isnan(dhtHumidity) || isnan(dhtTemperature)) {
        Serial.println("DHT11,ERROR");
    } else {
        Serial.print("DHT11,");
        Serial.print(dhtHumidity);
        Serial.print(",");
        Serial.print(dhtTemperature);
    }
    Serial.println();
    // Output BME280 Data
    Serial.print("BME280,");
    Serial.print(bmeTemperature);
    Serial.print(",");
    Serial.print(bmePressure);
    Serial.print(",");
    Serial.print(bmeHumidity);
    Serial.println();
    delay(60000)
```
After that, we want to continuously collect and process data from the sensor every minute. Hence, for the main function of the program, we created a loop that runs every 60000 milliseconds (= 1 minute) – `delay(60000)`. The methods `bme.readTemperature()`, `bme.readPressure()`, and `bme.readHumidity()` retrieve the temperature (in Celsius), pressure (in Pascals, later converted to hectopascals), and relative humidity, respectively. A similar process applies to DHT11. To ensure the flow of the program, we also added a validation part to check whether there are invalid values (i.e., NaN or "not a number").

After processing the DHT11 data, the program prints the BME280 data in the format BME280,<temperature>,<pressure>,<humidity> to the Serial Monitor. Each piece of data is separated by a comma, allowing for easy parsing in the next steps.

**Success Criteria Addressed: 2**

Next, to save the data according to the client's needs, we wrote a Python program to store all the collected sensor readings in a local CSV file. Additionally, we decided to send the data to a remote storage location on the ISAK-S network as a backup to safeguard against risks associated with saving data locally, such as file corruption, accidental deletion, or hardware failure.

Cited from the file `solution.py`:
```.C++
def process_data(line):
    dht_data = None
    bme_data = None
```
We designed this function to process every single line of sensor data received from the Arduino. In order to avoid, unorganized data and mismatched timestamps, we want all values of both sensors to be collected, validated, and available before saving into the CSV file; therefore, we created 2 variables for temporary storage (`dht_data` and `bme_data`). 

_*function process_data() continued:_
```.C++
   try:
       parts = line.strip().split(',')
       sensor_type = parts[0]


       #timestamp
       current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
```
Since there are 5 different values being extracted from the Arduino file, we imagine there would be a lot of possibilities of getting an error. Therefore, for better error management, we decided to use the try-except statement to catch and handle exceptions that might occur during the execution of code, preventing the program from crashing abruptly as continuous data is especially important for the essence of this project to have the most accurate portrait of the situation.

In the line `line.strip().split(',')` , the received line is stripped of leading and trailing whitespace and separated into components based on commas. The first part of the line, `parts[0]`, identifies the sensor type ("DHT11" or "BME280"). Next, a timestamp is generated in the format `YYYY-MM-DD HH:MM:SS`, representing the current time when the data is processed. This timestamp will later be stored alongside the sensor data in the CSV file.

_*function process_data() continued:_
```.C++
       # Process DHT11 data
       if sensor_type == "DHT11":
           dht_humidity = float(parts[1]) if len(parts) > 1 else None
           dht_temp = float(parts[2]) if len(parts) > 2 else None
           dht_data = (dht_temp, dht_humidity)  #store the data temporarily
           print(f"DHT11 - Temperature: {dht_temp}, Humidity: {dht_humidity}")
       # Process BME280 data
       elif sensor_type == "BME280":
           bme_temp = float(parts[1]) if len(parts) > 1 else None
           bme_pressure = float(parts[2]) if len(parts) > 2 else None
           bme_humidity = float(parts[3]) if len(parts) > 3 else None
           bme_data = (bme_temp, bme_pressure, bme_humidity)  #store the data temporarily
           print(f"BME280 - Temperature: {bme_temp}, Pressure: {bme_pressure}, Humidity: {bme_humidity}")
```
This part is designated for specific data from the DHT11 sensor. According to the format created initially, if existing, the second and third parts of the line will correspond to the DHT11 readings. Therefore, `float(parts[1])` converts the second part of the line to a float and stores it as `dht_humidity`; if it does not exist, it is set to None. Similarly, the third part (parts[2]) is assigned to `dht_temp`. These values are temporarily stored in the global variable `dht_data` as a tuple. Then, a message is printed to the console for debugging purposes. A similar process applies for BME280.
```.C++
       if dht_data and bme_data: #when both of them are collected, then save in the local file
           dht_temp, dht_humidity = dht_data
           bme_temp, bme_pressure, bme_humidity = bme_data
           save_to_csv(current_time, dht_temp, dht_humidity, bme_temp, bme_pressure, bme_humidity)
           print(f"Logged data: {current_time}, {dht_temp}, {dht_humidity}, {bme_temp}, {bme_pressure}, {bme_humidity}")


           dht_data = None
           bme_data = None
```
For this next part, the overview is that once data from both sensors is available, it combines the values and saves them to the CSV file. The 2nd and 3rd line is the function extracting the temporarily stored data. Then, it calls the `save_to_csv` function, passing the timestamp and sensor data. Afterward, it should print a message confirming that the data has been logged successfully and reset 2 `dht_data`` and `bme_data to None to prepare for the next data collection cycle.

**Success Criteria Addressed: 5**

### Code in Pycharm - Graphing
To provide a clear overview of temperature, humidity, and atmospheric pressure data from both local and remote servers, we created individual graphs representing each dataset. For a more effective analysis, we organized the data into three distinct sets:
Raw data combined with smoothed data
Data with a non-linear trend line and prediction based on it
Data analysis that includes annotations for the standard deviation, minimum, maximum, and median values.

#### 1. Raw data combined with smoothed data and cubic model

We wanted to plot many graphs, but we realized that the code gets really repetitive and becomes hard to debug and change. Hence, we decided to create another file called `graph_lib.py` apart from the two identical graphing files: `graphs_local.py` and `graphs_remote.py`. `graph_lib.py` has all the functions for graphing. 

There are 3 functions relevant to this success criteria:
moving_average()
plot_cub_model()
plot_data()

Moving average:
```
def moving_average(windowSize:int, x:list) -> list:
    x_smoothed = []
    for i in range(0,len(x)-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section)/windowSize
        x_smoothed.append(x_average)
    return x_smoothed
```
This function takes two parameters: windowSize (an integer) and x (a list). It starts with creating a new list for the smoothed x values. Then it goes into a for loop and repeats for length of list x minus windowSize. The process being repeated includes making a variable called x_section which is the value of x from i to i+windowSize. It then takes the average of all these values (sum of everything in the list divided by windowSize). Then, that value is appended to the list x_smoothed and when the loop finishes, is returned. 

We created this function because it’s crucial when we want to graph smoothed data. This is from an exercise we did in class. 

Plot_cub_model():
```
def plot_cub_model(value):
    x = [i for i in range(len(value))]
    coefficients = np.polyfit(x, value, 3)
    x_model = np.linspace(min(x), max(x), 500)
    y_model = np.polyval(coefficients, x_model)
    plt.plot(x_model, y_model,color="#9b495d")
    return "Cubic model plotted successfully"
```
In the plot_cub_model(), it takes in 1 parameter: value, which is a list. It starts with initializing x as i for every i in the range of the length of value. Coefficients is also initialised as a list of cubic coefficients using np.polyfit. X_model is then set to 500 points between the smallest x and the biggest x, and y_model is set as the evaluated values of the cubic coefficients using the function numpy.polyval(). Then we plot the x and y model with the color “#9b495d" and return “Cubic model plotted successfully)

This is crucial for plotting the cubic model trendline for the data. We checked the numpy documentation  (8) to find polyval() which evaluates a polynomial at specific values. We choose to use this because it makes it easier to debug since we only need to change 2 parameters. We also decided to use list comprehension to avoid our code looking very confusing and long since we have 200 lines of code and it’s really difficult to scroll through them and find a specific part. 

Plot_data():
```
def plot_data(subplot,x:list,y:list, ylabel,yunits):
    subplot.plot(x,y,color = "#c7d9e5")
    subplot.set_title(ylabel)
    subplot.set_xlabel("Time (hr)")
    subplot.set_ylabel(ylabel+yunits)
    x_l = []
    for t in range(len(x)):
        if (t)%360 == 0 and t+13<=len(x):
            x_l.append(x[t+13][11:-3])
    subplot.set_xticklabels(x_l)
    subplot.set_xticks(np.arange(13, len(x) + 1,360))
    return("data plotted successfully")
```
plot_data() takes in 5 parameters: subplot, x, y, ylabel, yunits. This function plots on subplot using the values passed into the function, anda also set the xticks label to recurring once every 6 hours. It returns “dataa plotted successfully’’ for debugging reasons. See fig 5 for more details on this function. 

Creating this function makes it easier for us as it decreases the length of the main graphing files and is easy to make changes to since all we need to change are the parameters. This is the most frequently used function in our graphing files. 


Cited from file `graphs_local.py`:
```
g1 = fig.add_subplot(gs[0, 0])
xDT = data["time"]
yDT = data["temperature_DHT"]
yDT_smoothed = moving_average(ws,yDT)
print(plot_data(g1,xDT,yDT,"Temperature (DHT)"," (°C)"))
g1.plot(xDT[int(ws/2):len(yDT_smoothed)+int(ws/2)],yDT_smoothed,color="#577c8e")
print(plot_cub_model(yDT))
g1.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'lower right', fontsize = 'x-small')
```
This part uses all the values as parameters and pass them into the functions we just mentioned to create graphs. This is also used for many other graphs, whether they are remote data or local data. 

![image (12)](https://github.com/user-attachments/assets/0430af1b-e87b-44c2-a1eb-ad7a412311fd)

**Fig. 10** shows local temperature, humidity, and pressure measured by the DMT11 sensor on the left and BME280 on the right with raw and smoothed data and cubic model. 
#### Success Criteria Addressed: 1 & 3



#### 2. Data analysis that includes annotations for the minimum, maximum, and median values and standard deviation.
We want to show the minimum, maximum, and median values and standard deviation on each graph, but we realized that it would look too messy so we put standard deviation on another graph. 

We decided to use a dictionary to store the values such as min, max, and median for easier and more organized access.

Cited from `graph_lib.py`:
```
def calc_statistics(values):
    stats = {
        "min": np.min(values),
        "max": np.max(values),
        "median": np.median(values),
    }
    return stats
```
This function uses numpy to calculate the statistics values and return them as a dictionary with the corresponding keys. We use numpy instead of basic operations in Python because it saves us space and time on easy tasks and makes the code cleaner. 

We graphed these values as dotted lines to avoid it looking messy on the graphs and for easier analysis on data distribution. 

Cited from `graphs_local.py`:
```
tats_temp = calc_statistics(data["temperature"])

plt.subplots_adjust(hspace=0.7, wspace=0.1)

temp_stats = plt.subplot(3, 1, 1)
plot_data(temp_stats, data["time"], data["temperature"], "Temperature Statistics", " (°C)")
temp_stats.plot(data["time"][int(ws/2):len(yT_smoothed)+int(ws/2)],yT_smoothed,color="#577c8e")
temp_stats.axhline(stats_temp["median"], color='green', linestyle='--', label='median')
temp_stats.axhline(stats_temp["min"], color='purple', linestyle='--', label='min')
temp_stats.axhline(stats_temp["max"], color='orange', linestyle='--', label='max')
temp_stats.legend(['raw data', 'smoothed data','median', 'min','max'], loc='upper right', fontsize='x-small')
```
This uses the values and the functions in graph_lib.py to plot the dotted lines representing these values with different colors. 


![image (8)](https://github.com/user-attachments/assets/6c509fd3-6323-41eb-9e23-317deba5de95)

Fig.11 shows the median, minimum, and maximum values of the local temperature, humidity, and pressure data.

We then plotted the standard deviation on another set of graphs. I didn't really know how to do standard deviation until I realized that it's basically the error range so I used the code to shade the area between average line + standard deviation and average line - standard deviation. 

```
plt.subplots_adjust(hspace=0.7, wspace=0.1)
a1 = plt.subplot(3,1,1)
plot_data1(a1,data["time"],avg1,"Average Temperature"," (°C)")
a1.plot(data["time"][int(ws/2):len(a1_smoothed)+int(ws/2)],a1_smoothed,color="#577c8e")
a1.fill_between(data["time"], avg1 - stats_temp["std_dev"], avg1 + stats_temp["std_dev"], alpha=0.5, color="#91bcd9", label="Standard Deviation Region")
a1.legend(['raw data', 'smoothed data','error bars'],loc = 'lower right', fontsize = 'x-small')
```
This uses the standard deviation values and plot an area filled of the standard deviation as error bars using the fill_between() function from matplotlib. 

![image (5)](https://github.com/user-attachments/assets/d22b0bfe-3fea-4fe6-bf54-c168792e90bb)

Fig.12 shows the error bar of the local temperature, humidity, and pressure data.

#### Success Criteria Addressed: 4
#### 3. Graphs with prediction for the next 12 hours. 
We decided that to show our prediction, we should use a dotted line to show that it's not actually true. We realized that the axes are going to be messed up so we merged the current and the future axes together and set an interval. We had the line extend from the end of the cubic model for the current data so it looks clean. 

Cited from `graphs_local.py`:
```
current_time = len(data["time"])
future_time = np.arange(current_time, current_time + 12 * 60)
x_data1 = np.arange(len(data["time"]))
y_data1 = avg1
coefficients1 = np.polyfit(x_data1, y_data1, 3)
predicted_values1 = cub(coefficients1[0], coefficients1[1], coefficients1[2], coefficients1[3], future_time)

plt.subplots_adjust(hspace=0.7, wspace=0.1)
a1 = plt.subplot(3,1,1)
plot_data(a1,data["time"],avg1,"Average Temperature"," (°C)")
a1.plot(data["time"][int(ws/2):len(a1_smoothed)+int(ws/2)],a1_smoothed,color="#577c8e")
xticks = np.concatenate([data["time"], future_time])
# a1.set_xticks(xticks[::360])
# a1.set_xticklabels(xticks[::360])
plot_cub_model(avg1)
plt.plot(future_time, predicted_values1, color="#bf8f90", linestyle='--')
a1.legend(['raw data', 'smoothed data',"cubic model", "predicted data (next 12 hours)"],loc = 'lower right', fontsize = 'x-small')
```
This starts by merging the current time and future 12 hours together as the x-axis, then using the cubic model to predict the values, and using those values to graph the predicted values for the future 12 hours. 

![image (6)](https://github.com/user-attachments/assets/b367eb31-f10d-4e12-bfb8-a6f225ee7e90)

Fig.13 shows the prediction of the next 12 hours of the local temperature, humidity, and pressure data.
# Criteria D: Functionality

video:
https://drive.google.com/file/d/1flFR3hPgdADL09FVJwkAD0dLhgzMOXHi/view?usp=sharing

## Scientific Poster Investigating the Data
(PDF version for clearer graphs) [Project 2 Comp Sci Science Poster.pdf](https://github.com/user-attachments/files/18053541/Project.2.Comp.Sci.Science.Poster.pdf)
![Project 2 Comp Sci Science Poster](https://github.com/user-attachments/assets/26c06a02-5691-493e-830a-706d7a12689a)

# Source: 
(1) https://cattree.uk/humidifiers-and-their-impact-on-cats/#:~:text=Cats%20can%20experience%20various%20respiratory,easier%20and%20more%20comfortable%20breathing.
(2) https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/cat-health-news/cold-weather-tips-cats#:~:text=Winter%20impacts%20cats%20that%20spend,cats%20indoors%20at%20all%20times.
(3) https://community.openhab.org/t/dht11-results-vs-bme280-results/45177

# Appendix
![image](https://github.com/user-attachments/assets/c24adc42-9b54-4cd0-becc-65bd38c1caa5)


**Fig.9**Consultation with audience interview transcription

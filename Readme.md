Indoor localization problem using a WLAN fingerprint-based method.

Description: multiple Wap Access Points (WAP) are located in 3 buildings at different floors.
The signals of these WAPs are measured with smartphone by different users.
In this project I used various machine learning models to predict indoor position of a user:
    1. Building, floor (classification task)
    2. Longitude and latitude (regression task)
    
Methods used:
    - Building and floor prediction: Decision Tree, K Nearest Neighbors, Logistic Regression, Random Forest, SUpport Vector machines
    - Longitude and latitude: Random Forest Regressor, K Nearest Neighbors Regressor, Decision Tree Regressor

Original datasets: https://archive.ics.uci.edu/ml/datasets/ujiindoorloc#

Features:
Attribute 001 (WAP001): Intensity value for WAP001. Negative integer values from -104 to 0 and +100. Positive value 100 used if WAP001 was not detected.
....
Attribute 520 (WAP520): Intensity value for WAP520. Negative integer values from -104 to 0 and +100. Positive Vvalue 100 used if WAP520 was not detected.
Attribute 521 (Longitude): Longitude. Negative real values from -7695.9387549299299000 to -7299.786516730871000
Attribute 522 (Latitude): Latitude. Positive real values from 4864745.7450159714 to 4865017.3646842018.
Attribute 523 (Floor): Altitude in floors inside the building. Integer values from 0 to 4.
Attribute 524 (BuildingID): ID to identify the building. Measures were taken in three different buildings. Categorical integer values from 0 to 2.
Attribute 525 (SpaceID): Internal ID number to identify the Space (office, corridor, classroom) where the capture was taken. Categorical integer values.
Attribute 526 (RelativePosition): Relative position with respect to the Space (1 - Inside, 2 - Outside in Front of the door). Categorical integer values.
Attribute 527 (UserID): User identifier (see below). Categorical integer values.
Attribute 528 (PhoneID): Android device identifier (see below). Categorical integer values.
Attribute 529 (Timestamp): UNIX Time when the capture was taken. Integer value.
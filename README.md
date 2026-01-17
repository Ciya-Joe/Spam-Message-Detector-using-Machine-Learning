# Spam-Message-Detector-using-Machine-Learning

-> Spam messages are unwanted messages that usually contain fake offers, lottery prizes, or scam alerts. 
-> This project uses Machine Learning to automatically classify messages as Spam or Not Spam.  
-> The model learns patterns from previously labeled messages and predicts the category of new messages entered by the user.

🎯 Objectives:

-> To understand how machine learning works on text data
-> To build a spam detection system using Python
-> To classify SMS messages into spam and not spam
-> To demonstrate real-life applications of machine learning


🧠 Technologies Used:

-> Python
-> Machine Learning
-> VS Code
-> Libraries: Pandas ,Scikit-learn


📂 Project Structure

Spam_Message_Detector/
│
├── spam_detector.py
├── spam_messages_mixed.csv
└── README.md


📊 Dataset Description

-> The dataset is stored in a CSV file
-> Contains 120+ messages
-> Two columns: label → spam / not spam
                message → SMS text
-> Dataset is mixed to avoid bias
-> Includes real-life examples of: Prize offers , Free rewards , Normal conversations


⚙️ Methodology

-> Load the dataset using Pandas
-> Convert text messages into numerical form
-> Split the dataset into training and testing data
-> Train the machine learning model
-> Test the model with new user inputs


🤖 Machine Learning Algorithm Used

-> Naive Bayes Classifier  - Supervised learning algorithm  
                           - Best suited for text classification
                           - Fast and efficient
                           - Works well even with small datasets


🔍 Working of the Project

-> Messages are converted into numerical vectors using CountVectorizer
->The Naive Bayes model learns word patterns from training data

 When a new message is entered:
-> It is converted into numerical form
-> The model predicts whether it is spam or not spam
-> The system displays the prediction instantly


💻 How to Run the Project

Step 1: Install Required Libraries
pip install pandas scikit-learn

Step 2: Run the Python File
python spam_detector.py

Step 3: Test Messages
Enter messages in the terminal and view predictions:

Prediction: SPAM
Prediction: NOT SPAM


🧪 Sample Test Inputs

Spam Message:

Congratulations! You won a free prize

Not Spam Message:

Please send me the class notes


📈 Output

-> Displays model accuracy
-> Predicts spam or not spam for user-entered messages
-> Interactive command-line interface


✅ Conclusion

This project successfully demonstrates how machine learning can be used to detect spam messages.

It helped in understanding:
-> Text preprocessing
-> Machine learning classification
-> Real-life applications of ML


🚀 Future Scope

-> Use a larger real-world dataset
-> Improve accuracy using advanced algorithms

Develop a web or mobile application

Support multiple languages

Add deep learning models

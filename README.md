# Personalized-Content-Recommendations-using-Machine-Learning-and-Browser-History-Analysis (PCR-ML-BHA)
This project is a web extension or application that uses machine learning algorithms to analyze text and provide users with personalized content recommendations based on their browsing history. The extension monitors the user's browsing history, preprocesses it using techniques like cleaning, stemming, and tokenization, and generates a user profile. Using the user profile, the extension selects documents that have high cosine similarity scores with the user's profile and recommends them to the user. This project leverages the power of machine learning and natural language processing to deliver personalized content recommendations that reflect the user's interests and preferences.

![1111-e1573834183704](https://user-images.githubusercontent.com/68110223/219851008-f6981755-8fa3-48c0-bc59-d415dc4da65c.jpg)

The application you linked to is a machine learning-based content recommendation system that uses browser history analysis to personalize recommendations for each user. To use the application, you will need to follow these steps:

- Clone or download the code repository from GitHub to your local machine.
- Install the required dependencies and libraries by running the command "pip install -r requirements.txt" in the terminal/command prompt.
- Collect your browsing history data by running the command "python collect_data.py" in the terminal/command prompt. This will save your browsing history data in a CSV file named "history.csv" in the same directory.
- Preprocess the browsing history data by running the command "python preprocess.py" in the terminal/command prompt. This will clean and transform the raw data into a format that can be used for machine learning.
- Train the machine learning models by running the command "python train.py" in the terminal/command prompt. This will train several models and save the best one to a file named "model.pkl" in the same directory.
- Start the recommendation system by running the command "python app.py" in the terminal/command prompt. This will start the Flask server, and you can access the web interface by visiting http://localhost:5000/ in your web browser.
- Enter your name in the web form and click "Get Recommendations" to receive personalized content recommendations based on your browsing history.
- Note that this application is designed to work with Google Chrome browser history data on Windows operating system, and you may need to modify the code to work with other browsers or operating systems. Additionally, the quality of the recommendations will depend on the quality and quantity of your browsing history data.





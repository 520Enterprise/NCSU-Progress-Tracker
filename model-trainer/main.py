import os


# Function to calculate completion percentage
def calculate_completion(current_marker, total_markers):
    # 1 digit after the decimal point
    return round(current_marker / total_markers * 100, 1)


# Function to separate code blocks and store them
def separate_and_store_code(file_path, output_dir, filename):
    with open(file_path, 'r') as file:
        content = file.readlines()

    code_blocks = []
    current_block = []
    total_markers = 0
    for line in content:
        if line.strip() == "#@#":
            total_markers += 1

    for line in content:
        if line.strip() == "#@#":
            if current_block:
                code_blocks.append(current_block.copy())
        else:
            current_block.append(line)

    for idx, block in enumerate(code_blocks):
        completion = calculate_completion(idx + 1, total_markers)
        output_file_path = os.path.join(output_dir, f"{filename}_block_{idx + 1}_completion_{completion}.py")
        with open(output_file_path, 'w') as output_file:
            output_file.writelines(block)
        print(f"Stored {output_file_path} with completion {completion}%")


# Directory containing the homework files
data_dir = 'data'

# Directory to store the separated code blocks
output_base_dir = 'output'

# Create the output directory if it doesn't exist
os.makedirs(output_base_dir, exist_ok=True)

# Clear the output directory
for filename in os.listdir(output_base_dir):
    file_path = os.path.join(output_base_dir, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

# Loop through homework directories (hw1, hw2, etc.)
for homework_dir in os.listdir(data_dir):
    if not os.path.isdir(os.path.join(data_dir, homework_dir)):
        continue

    output_dir = os.path.join(output_base_dir, homework_dir)
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(os.path.join(data_dir, homework_dir)):
        if filename.endswith('.py'):
            file_path = os.path.join(data_dir, homework_dir, filename)
            separate_and_store_code(file_path, output_dir, filename)

import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error


# Function to load data
def load_data(data_folder):
    X = []
    y = []

    for file_name in os.listdir(data_folder):
        if file_name.endswith('.py'):
            completion = float(file_name.split('_')[-1].split('.py')[0])
            y.append(completion)

            with open(os.path.join(data_folder, file_name), 'r') as file:
                content = file.read()
                X.append(content)

    return X, y


# Function to train and save models
def train_and_save_models(data_directory, model_folder):
    data_folder = os.path.join('output', data_directory)
    X, y = load_data(data_folder)

    # Feature extraction using TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    X_tfidf = tfidf_vectorizer.fit_transform(X)

    print("data_features shape is: ", X_tfidf.shape)

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

    # Initialize and train models
    models = [
        ('ridge', Ridge()),
        ('lasso', Lasso()),
        ('random_forest', RandomForestRegressor()),
        ('svr', SVR())
    ]

    for model_name, model in models:
        print(f'Training {model_name} model...')
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Calculate RMSE
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        print(f'{model_name} RMSE: {rmse:.2f}%')

        # Save the trained model
        model_filename = os.path.join(model_folder, f'{data_directory}_completion_{model_name}_model.joblib')
        joblib.dump(model, model_filename)
        print(f'Saved {model_name} model to {model_filename}')

        # Save the TF-IDF vectorizer to disk
        vectorizer_filename = os.path.join(model_folder, f'{data_directory}_completion_{model_name}_model.joblib_tfidf_vectorizer.joblib')
        joblib.dump(tfidf_vectorizer, vectorizer_filename)
        print(f'Saved TF-IDF vectorizer to {vectorizer_filename}')





# Directory containing the homework files (e.g., 'output/hw1', 'output/hw2', ...)
data_directories = [f for f in os.listdir('output') if os.path.isdir(os.path.join('output', f))]

# Directory to store the trained models
model_base_dir = 'model'
os.makedirs(model_base_dir, exist_ok=True)

# Train and save models for each homework directory
for data_directory in data_directories:
    model_directory = os.path.join(model_base_dir, data_directory)
    os.makedirs(model_directory, exist_ok=True)

    train_and_save_models(data_directory, model_directory)

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import numpy as np
import pandas as pd
import parselmouth
import joblib
from sklearn.impute import SimpleImputer
from parselmouth.praat import call

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

# # Function to measure pitch and other voice features
# def measurePitch(sound, f0min, f0max, unit):
#     pitch = call(sound, "To Pitch", 0.0, f0min, f0max)
#     meanF0 = call(pitch, "Get mean", 0, 0, unit)
#     stdevF0 = call(pitch, "Get standard deviation", 0 ,0, unit)
#     harmonicity = call(sound, "To Harmonicity (cc)", 0.01, f0min, 0.1, 1.0)
#     hnr = call(harmonicity, "Get mean", 0, 0)
#     pointProcess = call(sound, "To PointProcess (periodic, cc)", f0min, f0max)
#     localJitter = call(pointProcess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
#     localabsoluteJitter = call(pointProcess, "Get jitter (local, absolute)", 0, 0, 0.0001, 0.02, 1.3)
#     rapJitter = call(pointProcess, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3)
#     ppq5Jitter = call(pointProcess, "Get jitter (ppq5)", 0, 0, 0.0001, 0.02, 1.3)
#     ddpJitter = call(pointProcess, "Get jitter (ddp)", 0, 0, 0.0001, 0.02, 1.3)
#     localShimmer = call([sound, pointProcess], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     localdbShimmer = call([sound, pointProcess], "Get shimmer (local_dB)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     apq3Shimmer = call([sound, pointProcess], "Get shimmer (apq3)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     aqpq5Shimmer = call([sound, pointProcess], "Get shimmer (apq5)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     apq11Shimmer = call([sound, pointProcess], "Get shimmer (apq11)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     ddaShimmer = call([sound, pointProcess], "Get shimmer (dda)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    
#     return meanF0, stdevF0, localJitter, localabsoluteJitter, rapJitter, ppq5Jitter, ddpJitter, localShimmer, localdbShimmer, apq3Shimmer, aqpq5Shimmer, apq11Shimmer, ddaShimmer, hnr

# @app.route('/', methods=['GET'])
# def hello():
#     return jsonify(message="Hello from Flask!")

# @app.route('/analyse_audio', methods=['POST'])
# def analyse_audio():
#     try:
#         # Check if an audio file is sent
#         if 'audio' not in request.files:
#             return jsonify({'error': 'No audio file sent'}), 400
        
#         audio_file = request.files['audio']
#         filename = secure_filename(audio_file.filename)

#         # Create the 'record' directory if it doesn't exist
#         if not os.path.exists('record'):
#             os.makedirs('record')

#         audio_path = os.path.join('record', filename)
#         audio_file.save(audio_path)

#         # Load the audio file and perform measurements
#         sound = parselmouth.Sound(audio_path)
        
#         # Measure pitch and other features
#         (meanF0, stdevF0, localJitter, localabsoluteJitter, rapJitter, ppq5Jitter, ddpJitter,
#         localShimmer, localdbShimmer, apq3Shimmer, aqpq5Shimmer, apq11Shimmer, ddaShimmer, hnr) = measurePitch(sound, 75, 300, "Hertz")
        
#         # Create a DataFrame for the results
#         df = pd.DataFrame({
#             'MDVP:Fo(Hz)': [meanF0],
#             'MDVP:Fhi(Hz)': [stdevF0],
#             'MDVP:Flo(Hz)': [meanF0],
#             'MDVP:Jitter(%)': [localJitter],
#             'MDVP:Jitter(Abs)': [localabsoluteJitter],
#             'MDVP:RAP': [rapJitter],
#             'MDVP:PPQ': [ppq5Jitter],
#             'Jitter:DDP': [ddpJitter],
#             'MDVP:Shimmer': [localShimmer],
#             'MDVP:Shimmer(dB)': [localdbShimmer],
#             'Shimmer:APQ3': [apq3Shimmer],
#             'Shimmer:APQ5': [aqpq5Shimmer],
#             'MDVP:APQ': [apq11Shimmer],
#             'Shimmer:DDA': [ddaShimmer],
#             'NHR': [localShimmer],
#             'HNR': [hnr]
#         })

#         # Preprocess the data
#         imputer = SimpleImputer(strategy='mean')
#         X_new = imputer.fit_transform(df)

#         # Load the trained SVM model
#         svm_model = joblib.load("svc_model.pkl")

#         # Make predictions
#         predictions = svm_model.predict(X_new)

#         # Convert predictions to 1 (malade) or 0 (non malade)
#         result = int(predictions[0])
#         return jsonify({'prediction': result}), 200
    
#     except Exception as e:
#         print("Error:", e)
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='192.168.4.105', port=8080)

# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename
# import os
# import numpy as np
# import pandas as pd
# import parselmouth
# from sklearn.impute import SimpleImputer
# from keras.models import load_model
# from parselmouth.praat import call 

# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['ENV'] = 'development'

# # Function to measure pitch and other voice features
# def measurePitch(sound, f0min, f0max, unit):
#     pitch = call(sound, "To Pitch", 0.0, f0min, f0max)
#     meanF0 = call(pitch, "Get mean", 0, 0, unit)
#     stdevF0 = call(pitch, "Get standard deviation", 0 ,0, unit)
#     harmonicity = call(sound, "To Harmonicity (cc)", 0.01, f0min, 0.1, 1.0)
#     hnr = call(harmonicity, "Get mean", 0, 0)
#     pointProcess = call(sound, "To PointProcess (periodic, cc)", f0min, f0max)
#     localJitter = call(pointProcess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
#     localabsoluteJitter = call(pointProcess, "Get jitter (local, absolute)", 0, 0, 0.0001, 0.02, 1.3)
#     rapJitter = call(pointProcess, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3)
#     ppq5Jitter = call(pointProcess, "Get jitter (ppq5)", 0, 0, 0.0001, 0.02, 1.3)
#     ddpJitter = call(pointProcess, "Get jitter (ddp)", 0, 0, 0.0001, 0.02, 1.3)
#     localShimmer = call([sound, pointProcess], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     localdbShimmer = call([sound, pointProcess], "Get shimmer (local_dB)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     apq3Shimmer = call([sound, pointProcess], "Get shimmer (apq3)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     aqpq5Shimmer = call([sound, pointProcess], "Get shimmer (apq5)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     apq11Shimmer = call([sound, pointProcess], "Get shimmer (apq11)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     ddaShimmer = call([sound, pointProcess], "Get shimmer (dda)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
#     rpde = call(sound, "Get resample", 1)
#     dfa = call(sound, "Get total duration", 1)
#     spread1 = call(sound, "Get standard deviation", 1)
#     spread2 = call(sound, "Get skewness", 1)
#     d2 = call(sound, "Get kurtosis", 1)
#     ppe = call(sound, "Get percentile 95", 1)
    
#     return meanF0, stdevF0, localJitter, localabsoluteJitter, rapJitter, ppq5Jitter, ddpJitter, localShimmer, localdbShimmer, apq3Shimmer, aqpq5Shimmer, apq11Shimmer, ddaShimmer, hnr, rpde, dfa, spread1, spread2, d2, ppe

# @app.route('/', methods=['GET'])
# def hello():
#     return jsonify(message="Hello from Flask!")

# @app.route('/analyse_audio', methods=['POST'])
# def analyse_audio():
#     try:
#         # Check if an audio file is sent
#         if 'audio' not in request.files:
#             return jsonify({'error': 'No audio file sent'}), 400
        
#         audio_file = request.files['audio']
#         filename = secure_filename(audio_file.filename)

#         # Create the 'record' directory if it doesn't exist
#         if not os.path.exists('record'):
#             os.makedirs('record')

#         audio_path = os.path.join('record', filename)
#         audio_file.save(audio_path)

#         # Load the audio file and perform measurements
#         sound = parselmouth.Sound(audio_path)
        
#         # Measure pitch and other features
#         (meanF0, stdevF0, localJitter, localabsoluteJitter, rapJitter, ppq5Jitter, ddpJitter,
#         localShimmer, localdbShimmer, apq3Shimmer, aqpq5Shimmer, apq11Shimmer, ddaShimmer, hnr, rpde, dfa, spread1, spread2, d2, ppe) = measurePitch(sound, 75, 300, "Hertz")
        
#         # Create a DataFrame for the results
#         df = pd.DataFrame({
#             'MDVP:Fo(Hz)': [meanF0],
#             'MDVP:Fhi(Hz)': [stdevF0],
#             'MDVP:Flo(Hz)': [meanF0],
#             'MDVP:Jitter(%)': [localJitter],
#             'MDVP:Jitter(Abs)': [localabsoluteJitter],
#             'MDVP:RAP': [rapJitter],
#             'MDVP:PPQ': [ppq5Jitter],
#             'Jitter:DDP': [ddpJitter],
#             'MDVP:Shimmer': [localShimmer],
#             'MDVP:Shimmer(dB)': [localdbShimmer],
#             'Shimmer:APQ3': [apq3Shimmer],
#             'Shimmer:APQ5': [aqpq5Shimmer],
#             'MDVP:APQ': [apq11Shimmer],
#             'Shimmer:DDA': [ddaShimmer],
#             'NHR': [localShimmer],
#             'HNR': [hnr],
#             'RPDE': [rpde],
#             'DFA': [dfa],
#             'spread1': [spread1],
#             'spread2': [spread2],
#             'D2': [d2],
#             'PPE': [ppe]
#         })

#         # Preprocess the data
#         imputer = SimpleImputer(strategy='mean')
#         X_new = imputer.fit_transform(df)

#         # Load the trained SVM model (replace this with your actual model loading)
#         # Assuming you have a Keras model saved as .h5, load it like this
#         model = load_model("svm_classifier_model.h5")

#         # Make predictions
#         predictions = model.predict(X_new)

#         # Convert predictions to 1 (malade) or 0 (non malade)
#         result = int(predictions[0][0])  # adjust this based on your model output format
#         return jsonify({'prediction': result}), 200
    
#     except Exception as e:
#         print("Error:", e)
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

import os
import numpy as np
import librosa
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from keras.models import load_model

# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['ENV'] = 'development'

# # Charger le modèle pré-entraîné
# model = load_model('hakima.h5')

# # Mapping des émotions
# emotion_mapping = {
#     1: 'neutral', 2: 'calm', 3: 'happy', 4: 'sad',
#     5: 'angry', 6: 'fearful', 7: 'disgust', 8: 'surprised'
# }

# # Fonction pour extraire les caractéristiques audio
# def extract_features(audio_path):
#     try:
#         y, sr = librosa.load(audio_path, res_type='kaiser_fast')
#         # Extraire les MFCCs
#         mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
#         mfccs_mean = np.mean(mfccs.T, axis=0)
#         # Extraire les caractéristiques Chroma
#         stft = np.abs(librosa.stft(y))
#         chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr).T, axis=0)
#         # Extraire le spectrogramme Mel
#         mel = np.mean(librosa.feature.melspectrogram(y=y, sr=sr).T, axis=0)
#         # Combiner les caractéristiques
#         combined_features = np.hstack([mfccs_mean, chroma, mel])
#         return combined_features
#     except Exception as e:
#         print(f"Error extracting features: {str(e)}")
#         return None

# @app.route('/analyse_audio', methods=['POST'])
# def analyse_audio():
#     try:
#         # Vérifier si un fichier audio est envoyé
#         if 'audio' not in request.files:
#             return jsonify({'error': 'Aucun fichier audio envoyé'}), 400
        
#         audio_file = request.files['audio']
#         filename = secure_filename(audio_file.filename)

#         # Créer le répertoire 'record' s'il n'existe pas
#         if not os.path.exists('record'):
#             os.makedirs('record')

#         audio_path = os.path.join('record', filename)
#         audio_file.save(audio_path)

#         # Extraire les caractéristiques à partir de l'audio
#         audio_features = extract_features(audio_path)

#         if audio_features is None:
#             return jsonify({'error': 'Erreur lors de l\'extraction des caractéristiques audio'}), 500

#         # Remodeler les caractéristiques pour correspondre au format d'entrée du CNN 1D
#         audio_features = audio_features.reshape(1, audio_features.shape[0], 1)

#         # Utiliser le modèle pour prédire l'émotion
#         prediction = model.predict(audio_features)
#         predicted_emotion_index = np.argmax(prediction, axis=1)[0] + 1
#         predicted_emotion = emotion_mapping[predicted_emotion_index]

#         return jsonify({'prediction': predicted_emotion}), 200
    
#     except Exception as e:
#         print("Error:", e)
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='192.168.4.105', port=8080)

import os
import numpy as np
import librosa
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from keras.models import load_model

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

# Load your pre-trained 1D CNN model
model = load_model('hakima.h5')

# Emotion mapping dictionary
emotion_mapping = {
    1: 'neutral', 2: 'calm', 3: 'happy', 4: 'sad',
    5: 'angry', 6: 'fearful', 7: 'disgust', 8: 'surprised'
}

# Function to extract audio features using MFCC, Delta, and Delta-Delta MFCC
def extract_features(audio_path):
    try:
        y, sr = librosa.load(audio_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        delta_mfccs = librosa.feature.delta(mfccs)
        delta_delta_mfccs = librosa.feature.delta(mfccs, order=2)
        
        mfccs = np.mean(mfccs.T, axis=0)
        delta_mfccs = np.mean(delta_mfccs.T, axis=0)
        delta_delta_mfccs = np.mean(delta_delta_mfccs.T, axis=0)
        
        # Extract Chroma
        stft = np.abs(librosa.stft(y))
        chroma = librosa.feature.chroma_stft(S=stft, sr=sr)
        chroma = np.mean(chroma.T, axis=0)
        
        # Extract Mel Spectrogram
        mel = librosa.feature.melspectrogram(y=y, sr=sr)
        mel = np.mean(mel.T, axis=0)
        
        # Combine features
        combined_features = np.hstack([mfccs, delta_mfccs, delta_delta_mfccs, chroma, mel])
        return combined_features
    
    except Exception as e:
        print(f"Error extracting features: {str(e)}")
        return None

# API endpoint for audio analysis
@app.route('/analyse_audio', methods=['POST'])
def analyse_audio():
    try:
        # Check if audio file is present in the request
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file uploaded'}), 400
        
        audio_file = request.files['audio']
        filename = secure_filename(audio_file.filename)

        # Save the uploaded audio file
        audio_path = os.path.join('record', filename)
        audio_file.save(audio_path)

        # Extract features from the audio file
        audio_features = extract_features(audio_path)

        if audio_features is None:
            return jsonify({'error': 'Error extracting audio features'}), 500

        # Reshape features to match the model input shape
        audio_features = audio_features.reshape(1, audio_features.shape[0], 1)

        # Predict emotion using the loaded model
        prediction = model.predict(audio_features)
        predicted_emotion_index = np.argmax(prediction, axis=1)[0] + 1
        predicted_emotion = emotion_mapping[predicted_emotion_index]

        return jsonify({'prediction': predicted_emotion}), 200
    
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='192.168.4.105', port=8080)
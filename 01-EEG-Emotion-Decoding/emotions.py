import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

class EEGEmotionDecoder:
    def __init__(self, file_path):
        print(f"Loading dataset from {file_path}...")
        self.df = pd.read_csv('emotions.csv')
        self.df.columns = self.df.columns.str.strip()
        self.le = LabelEncoder()
        # Encode labels
        self.df['label_encoded'] = self.le.fit_transform(self.df['label'])
    
    def plot_brainwaves(self):
        """Menampilkan potongan sinyal FFT untuk tiap emosi"""
        plt.figure(figsize=(12, 6))
        for emotion in self.le.classes_:
            # search for the first row matching the emotion
            subset = self.df[self.df['label'] == emotion].filter(like='fft').iloc[0, 0:100]
            plt.plot(subset.values, label=emotion, alpha=0.8)
        
        plt.title('Brainwave Patterns (FFT Snippet) by Emotional State')
        plt.xlabel('Frequency Bin (Sample)')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()

    def get_split_data(self):
        X = self.df.drop(['label', 'label_encoded'], axis=1)
        y = self.df['label_encoded']
        return train_test_split(X, y, test_size=0.2, random_state=42)

# --- initiate and run ---
if __name__ == "__main__":
    # initialize decoder
    decoder = EEGEmotionDecoder('emotions.csv')
    
    # 1. visualize brainwaves
    decoder.plot_brainwaves()
    
    # 2. Split data
    X_train, X_test, y_train, y_test = decoder.get_split_data()
    
    # 3. Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Evaluate
    y_pred = model.predict(X_test)
    print(f"\nDecoding Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=decoder.le.classes_))
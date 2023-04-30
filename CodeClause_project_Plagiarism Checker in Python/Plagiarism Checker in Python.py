import string

def preprocess_text(text):
    #Preprocess the input text by removing punctuation and converting to lowercase.
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    return text

def calculate_similarity(text1, text2):
    # Calculate the Jaccard similarity between two preprocessed texts.
    set1 = set(text1.split())
    set2 = set(text2.split())
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union
    return similarity

def main():
    # Main function for plagiarism checker 
    text1 = input("Enter first text : ")
    text2 = input("Enter second text : ")
    processedtext1 = preprocess_text(text1)
    processedtext2 = preprocess_text(text2)
    similarity = calculate_similarity(processedtext1, processedtext2)
    print("Similarity between two texts :", similarity)

if __name__ == "__main__":
    main()

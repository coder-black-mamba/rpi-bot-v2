import fasttext
import fasttext.util
import numpy as np

# fasttext.util.download_model('bn', if_exists='ignore')
print("Loading FastText model...Please wait.")
model = fasttext.load_model("model/cc.bn.300.bin")

def get_embedding(text):
    """
    Get the embedding of a text using FastText.
    :param text: The input text.
    :return: The embedding of the text.
    """
    # Get the embedding of the text
    # embedding = model.get_word_vector(text)
    
    # # Normalize the embedding
    # norm = np.linalg.norm(embedding)
    # if norm > 0:
    #     embedding = embedding / norm
    
    # return embedding

    return model.get_sentence_vector(text)


# if __name__ == "__main__":
#     print(get_embedding("ওই মামুর বিটা কোথাই "))
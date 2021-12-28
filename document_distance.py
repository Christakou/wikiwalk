import math

def word_vector(text):
    """
    Calculates a word frequency vector given text input
    :param input: string
    :return:
    """
    word_list = text.split()
    word_vector = {}
    for word in word_list:
        word = word.lower()
        if word in word_vector:
            word_vector[word] += 1
        else:
            word_vector[word] = 1
    return word_vector


def dot_product(word_vector_a,word_vector_b):
    sum = 0.0
    for key in word_vector_a:
        if key in word_vector_b:
                    sum +=(word_vector_a[key] * word_vector_b[key])
    return sum

def document_angle(word_vector_a, word_vector_b):
    numerator = dot_product(word_vector_a,word_vector_b)
    denominator = math.sqrt(dot_product(word_vector_a,word_vector_a)*dot_product(word_vector_b,word_vector_b))
    return math.acos(numerator/denominator)

def page_similarity(page_a, page_b):
    return document_angle(page_a.word_vector,page_b.word_vector)
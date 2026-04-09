# 🧠 Generative AI Learning Journey

Welcome to my repository for learning Generative AI. This section focuses on the foundational concepts of **Natural Language Processing (NLP)**, which are essential before diving into complex Large Language Models (LLMs).

## Road MAP

<img src = "./src/nlp/images/road_map.png" width = "80%">

## 📚 Module 1: NLP Fundamentals & Text Preprocessing

This module covers the essential steps to clean and prepare raw text data so that machines can understand it.

<img src="./src/nlp/images/nlp_pipeline.png" alt="HTML5 Logo" width="80%">

### 1. Tokenization
Tokenization is the very first step in NLP. It involves breaking down text into smaller units (tokens) like sentences or words.
* **[01_Tokenization_Basics](./src/nlp/preprocessing/tokenization_basic.ipynb)**
  * **Concepts Covered:** NLP Terminologies (Corpus, Documents, Vocabulary, Words).
  * **Objective:** Understand how text is represented and the theory behind building a vocabulary.
* **[02_Tokenization_Practical](./src/nlp/preprocessing/tokenization_practical.ipynb)**
  * **Concepts Covered:** Practical implementation using NLTK (`sent_tokenize`, `TreebankWordTokenizer`).
  * **Objective:** Write Python code to split paragraphs into sentences and sentences into individual words.

### 2. Stop Words Processing
Stop words are common words (like "the", "is", "in") that carry little meaning and can often be removed to reduce noise and save computation.
* **[03_Stopwords_Processing](./src/nlp/preprocessing/stopwords_processing.ipynb)**
  * **Concepts Covered:** What are stop words, why remove them, and how to filter them out.
  * **Objective:** Learn to clean tokenized arrays by removing unhelpful "glue" words using NLTK's stopwords list.

### 3. Text Normalization: Stemming & Lemmatization
Because words can appear in various forms (e.g., "run", "running", "ran"), text normalization reduces them to their base form, shrinking the vocabulary size.
* **[04_Stemming_and_Lemmatization](./src/nlp/preprocessing/stemming_lemmatization_basic.ipynb)**
  * **Concepts Covered:** * **Stemming:** Rule-based heuristic chopping of suffixes (e.g., *running* $\to$ *run*).
    * **Lemmatization:** Dictionary-based reduction to meaningful root words.
  * **Objective:** Understand the differences between the two methods and when to use which.

### 4. Text Normalization: Parts Of speech tagging
Process of reading text and assigning a grammatical category (like noun, verb, adjective, or adverb) to each individual word (token) based on its definition and its context within the sentence.
* **[04_POS_TAGGING](./src/nlp/preprocessing/parts_of_speech_tagging.ipynb)**
  * **Concepts Covered:** * **POS Tagging:**  Pos tagging with examples.
   * **Objective:** Understand different approach of applying pos tagging.


### 5. Text Normalization: Named Entity Reconization
 **Named Entity Recognition (NER)** is a sub-task of information extraction in Natural Language Processing (NLP). It involves scanning a text, locating proper nouns or key informational phrases, and classifying them into pre-defined categories (like People, Organizations, Locations, Dates, or Monetary Values).
* **[04_POS_TAGGING](./src/nlp/preprocessing/named_entity_reconization.ipynb)**
  * **Concepts Covered:** * **POS Tagging:**  NER with examples.
 

---

## 📊 Module 2: Text Representation & Vectorization

After preprocessing text, the next challenge is converting it into numerical vectors that machine learning models can understand. This module explores various techniques to represent text as numbers, from simple counting methods to sophisticated dense embeddings.

### 1. One-Hot Encoding
One-Hot Encoding is the most basic way to represent text numerically by converting categorical data into binary vectors.
* **[01_One_Hot_Encoding](./src/nlp/text_to_vectors/one_hot_encoding.ipynb)**
  * **Concepts Covered:**
    * Converting categories into binary representations
    * Why one-hot encoding prevents false hierarchies
    * The curse of dimensionality and sparsity problems
  * **Objective:** Understand the foundational encoding method and its limitations for large vocabularies.

### 2. Bag of Words (BoW)
The Bag of Words model represents text as unordered collections of word counts, creating feature vectors based on vocabulary frequency.
* **[02_Bag_of_Words](./src/nlp/text_to_vectors/bag_of_words.ipynb)**
  * **Concepts Covered:**
    * Building vocabulary from a corpus
    * Counting word frequencies to create feature vectors
    * Why BoW "forgets" word order and context
  * **Objective:** Learn how to transform documents into numerical feature vectors through word frequency counting.

### 3. N-grams
N-grams capture local context by grouping adjacent words together, preserving some word order information that Bag of Words loses.
* **[03_N-grams](./src/nlp/text_to_vectors/n-grams.ipynb)**
  * **Concepts Covered:**
    * Unigrams (N=1), Bigrams (N=2), and Trigrams (N=3)
    * How N-grams preserve context and semantic relationships
    * Vocabulary construction from overlapping word sequences
  * **Objective:** Understand how grouping adjacent words captures context that single-word models miss.

### 4. TF-IDF (Term Frequency-Inverse Document Frequency)
TF-IDF improves upon simple counting by weighting words based on their importance: frequent in a document but rare across all documents.
* **[04_TF-IDF](./src/nlp/text_to_vectors/td-idf.ipynb)**
  * **Concepts Covered:**
    * Term Frequency (TF): How often a word appears in a document
    * Inverse Document Frequency (IDF): How rare a word is across the corpus
    * Combining TF and IDF to score word importance
  * **Objective:** Learn how to weight words intelligently to emphasize meaningful terms while downplaying common words.

### 5. Word Embeddings & Word2Vec
Word embeddings represent words as dense vectors in continuous space, capturing semantic meaning and word relationships through deep learning.
* **[05_Word_Embeddings_&_Word2Vec](./src/nlp/text_to_vectors/word2vec.ipynb)**
  * **Concepts Covered:**
    * Dense vector representations vs. sparse vectors
    * Word2Vec: Skip-gram and CBOW architectures
    * Semantic relationships learned by neural networks (e.g., "king" - "man" + "woman" ≈ "queen")
    * The linguistic theory: "You shall know a word by the company it keeps"
  * **Objective:** Understand modern embedding techniques that capture mathematical relationships between words with similar meanings.

### 6. Practical Application: SMS Spam Classification
A hands-on project applying vectorization techniques to real-world data classification.
* **[06_Practical_Project](./src/nlp/text_to_vectors/practical.ipynb)**
  * **Concepts Covered:**
    * Loading and exploring the SMS Spam Collection Dataset
    * Preprocessing text with stemming, stopword removal, and regularization
    * Comparing different vectorization approaches (BoW, TF-IDF, embeddings)
    * Building and evaluating classification models
  * **Objective:** Apply learned vectorization techniques to classify spam vs. legitimate SMS messages.

---
*Stay tuned as I add more modules on Attention Mechanisms, Transformers, and LLMs!*
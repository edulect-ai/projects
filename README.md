# 🧠 Generative AI Learning Journey

Welcome to my repository for learning Generative AI. This section focuses on the foundational concepts of **Natural Language Processing (NLP)**, which are essential before diving into complex Large Language Models (LLMs).

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
*Stay tuned as I add more modules on Embeddings, Attention Mechanisms, and LLMs!*
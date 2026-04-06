import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Load skills dataset
skills_list = pd.read_csv("skills.csv")["skills"].tolist()

#  Step 5: Preprocessing
def preprocess(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc 
              if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

#  Step 6: Skill Extraction
def extract_skills(text):
    found_skills = []
    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills

# Step 7: Match Score
def match_score(resume, job_desc):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume, job_desc])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0] * 100, 2)

#  Step 8: Missing Skills
def missing_skills(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))

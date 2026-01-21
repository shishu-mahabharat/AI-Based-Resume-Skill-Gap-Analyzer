import spacy
from spacy.matcher import PhraseMatcher

# Predefined Skill Database
# Expanded to cover more industry-relevant skills
SKILLS_DB = [
    # Programming Languages
    "python", "java", "c++", "c", "c#", ".net", "javascript", "typescript", "html", "css", "sql", "r", "go", "ruby", "php", "swift", "kotlin", "rust", "dart", "scala", "perl", "bash", "shell", "powershell", "matlab",
    
    # AI/ML/Data Science
    "machine learning", "deep learning", "nlp", "natural language processing", "computer vision", "generative ai", "llm", "large language models", "gpt", "bert",
    "scikit-learn", "tensorflow", "pytorch", "keras", "pandas", "numpy", "matplotlib", "seaborn", "scipy", "statsmodels",
    "opencv", "huggingface", "transformers", "nltk", "spacy", "data analysis", "data visualization", "data engineering",
    "reinforcement learning", "supervised learning", "unsupervised learning", "xgboost", "lightgbm", "catboost",
    "jupyter", "colab", "databricks", "snowflake", "bigquery", "redshift",
    
    # Web Development (Frontend/Backend/Full Stack)
    "flask", "django", "fastapi", "react", "react.js", "angular", "vue", "vue.js", "node.js", "node", "express", "express.js", "spring", "spring boot", "hibernate", 
    "rest api", "restful api", "graphql", "soap", "json", "xml", "ajax", "jquery", "bootstrap", "tailwind css", "sass", "less",
    "asp.net", "laravel", "ruby on rails", "symfony",
    
    # Databases
    "mysql", "postgresql", "postgres", "mongodb", "sqlite", "redis", "oracle", "sql server", "mssql", "dynamodb", "cassandra", "couchdb", "mariadb", "neo4j", "elasticsearch",
    
    # DevOps/Cloud/Infrastructure
    "aws", "amazon web services", "azure", "gcp", "google cloud platform", "docker", "kubernetes", "k8s", "jenkins", "git", "github", "gitlab", "bitbucket",
    "ci/cd", "continuous integration", "continuous deployment", "terraform", "ansible", "chef", "puppet", "vagrant", 
    "linux", "unix", "ubuntu", "centos", "redhat", "nginx", "apache", "haproxy", "nagios", "prometheus", "grafana",
    "s3", "ec2", "lambda", "cloudformation",
    
    # Big Data
    "spark", "apache spark", "hadoop", "kafka", "apache kafka", "hive", "airflow", "apache airflow", "pig", "mapreduce", "hbase", "flink",
    
    # Mobile Development
    "android", "ios", "flutter", "react native", "xamarin", "ionic", "swiftui",
    
    # Software Engineering Practices & Tools
    "agile", "scrum", "kanban", "jira", "confluence", "trello", "sdlc", "oop", "object oriented programming", "design patterns", "microservices", "serverless", "tdd", "test driven development", "bdd",
    "selenium", "pytest", "junit", "mocha", "jest", "cypress",
    
    # Other Technical Skills
    "blockchain", "crypto", "smart contracts", "solidity", "ethereum",
    "iot", "internet of things", "embedded systems", "robotics", "arduino", "raspberry pi",
    "cybersecurity", "ethical hacking", "penetration testing", "network security", "cryptography",
    "tableau", "power bi", "excel", "google sheets", "sap", "salesforce"
]

def extract_skills(text: str) -> set:
    """
    Extracts skills from text using a predefined skill database and n-gram matching.
    
    Args:
        text (str): The input text (resume or job description).
        
    Returns:
        set: A set of unique extracted skills (lowercase).
    """
    if not text:
        return set()
        
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text.lower())
    
    matcher = PhraseMatcher(nlp.vocab)
    
    # Create patterns from the skills database
    patterns = [nlp.make_doc(skill) for skill in SKILLS_DB]
    matcher.add("SKILLS", patterns)
    
    matches = matcher(doc)
    
    extracted_skills = set()
    for match_id, start, end in matches:
        span = doc[start:end]
        extracted_skills.add(span.text)
        
    return extracted_skills

if __name__ == "__main__":
    # Test
    sample_txt = "I am a Python Developer with experience in Machine Learning and Docker. I know Java and SQL. Expert in AWS and React.js."
    print(f"Extracted: {extract_skills(sample_txt)}")

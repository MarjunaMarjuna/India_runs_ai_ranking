import json

AI_SKILLS = {
    "Recommendation Systems": 10,
    "Information Retrieval": 10,
    "Semantic Search": 10,
    "Vector Search": 10,
    "Embeddings": 10,
    "Pinecone": 10,
    "FAISS": 10,
    "Milvus": 10,
    "RAG": 10,

    "LLMs": 8,
    "Fine-tuning LLMs": 8,
    "Sentence Transformers": 8,
    "Hugging Face Transformers": 8,

    "Machine Learning": 6,
    "NLP": 6,
    "PyTorch": 6,
    "TensorFlow": 6,

    "AWS": 2,
    "GCP": 2,
    "Databricks": 2,
    "Airflow": 2
}

AI_SKILLS = {
    "Recommendation Systems": 10,
    "Information Retrieval": 10,
    "Semantic Search": 10,
    "Vector Search": 10,
    "Embeddings": 10,
    "Pinecone": 10,
    "FAISS": 10,
    "Milvus": 10,
    "RAG": 10,

    "LLMs": 8,
    "Fine-tuning LLMs": 8,
    "Sentence Transformers": 8,
    "Hugging Face Transformers": 8,

    "Machine Learning": 6,
    "NLP": 6,
    "PyTorch": 6,
    "TensorFlow": 6,

    "AWS": 2,
    "GCP": 2,
    "Databricks": 2,
    "Airflow": 2
}

# ADD HERE
JD_SKILLS = {
    "Recommendation Systems",
    "Information Retrieval",
    "Semantic Search",
    "Vector Search",
    "Embeddings",
    "Pinecone",
    "FAISS",
    "Milvus",
    "RAG",
    "LLMs",
    "Fine-tuning LLMs",
    "Sentence Transformers",
    "Hugging Face Transformers",
    "Machine Learning",
    "NLP"
}

def calculate_skill_score(skills):
    score = 0

    for skill in skills:
        for ai_skill, weight in AI_SKILLS.items():
            if ai_skill.lower() in skill.lower():
                score += weight

    return score

def experience_score(exp):

    if 5 <= exp <= 9:
        return 10

    elif 9 < exp <= 20:
        return 8

    elif 3 <= exp < 5:
        return 5

    else:
        return 0

def redrob_score(signals):

    score = 0

    if signals["open_to_work_flag"]:
        score += 2

    if signals["recruiter_response_rate"] > 0.5:
        score += 2

    if signals["github_activity_score"] > 50:
        score += 2

    if signals["interview_completion_rate"] > 0.5:
        score += 2

    if signals["profile_completeness_score"] > 80:
        score += 2

    return score
def career_score(career_history):

    score = 0

    positive_words = [
        "recommendation",
        "retrieval",
        "semantic search",
        "vector search",
        "embedding",
        "rag",
        "llm",
        "faiss",
        "pinecone",
        "milvus",
        "machine learning",
        "nlp",
        "transformer",
        "search",
        "ranking",
        "relevance",
        "recommendation systems",
        "vector database",
        "hybrid search",
        "learning-to-rank",
        "dense retrieval",
        "sentence transformer",
        "cross encoder",
        "reranking",
        "feature engineering"
    ]
    
    found_words = set()
    title_bonus = 0


    for job in career_history:

        title = job["title"].lower()
        description = job["description"].lower()

        if "ai engineer" in title:
            title_bonus = max(title_bonus, 40)

        elif "applied scientist" in title:
            title_bonus = max(title_bonus, 40)

        elif "applied ml engineer" in title:
            title_bonus = max(title_bonus, 40)

        elif "staff machine learning engineer" in title:
            title_bonus = max(title_bonus, 40)

        elif "senior applied scientist" in title:
            title_bonus = max(title_bonus, 40)

        elif "machine learning engineer" in title:
            title_bonus = max(title_bonus, 40)

        elif "nlp engineer" in title:
            title_bonus = max(title_bonus, 40)

        elif "data scientist" in title:
            title_bonus = max(title_bonus, 30)

        elif "recommendation" in title:
            title_bonus = max(title_bonus, 40)

        elif "search" in title:
            title_bonus = max(title_bonus, 40)

        elif "retrieval" in title:
            title_bonus = max(title_bonus, 40)

        if "marketing" in title:
            title_bonus -= 20

        elif "accountant" in title:
            title_bonus -= 20

        elif "graphic designer" in title:
            title_bonus -= 20

        elif "content writer" in title:
            title_bonus -= 15

        elif "operations manager" in title:
            title_bonus -= 10

        elif "sales" in title:
            title_bonus -= 15

        elif "hr manager" in title:
            title_bonus -= 20

        for word in positive_words:
            if word in description:
                found_words.add(word)

    score = len(found_words) * 5 + title_bonus

    return score



def generate_reasoning(candidate):

    exp = candidate["exp"]
    title = candidate["current_title"]
    skills = candidate["skills"]
    career = candidate["career_history"]
    red = candidate["red_score"]

    # ---------------- Top Skills ----------------
    top_skills = [s for s in skills if s in JD_SKILLS][:3]

    if top_skills:
        skill_text = ", ".join(top_skills)
    else:
        skill_text = "AI/ML technologies"


    evidence = None

    for job in career:

        text = (
            job.get("title", "") + " " +
            job.get("description", "")
        ).lower()

        if "recommendation" in text:
            evidence = "recommendation"
            break

        elif "retrieval" in text:
            evidence = "retrieval"
            break

        elif "ranking" in text:
            evidence = "ranking"
            break

        elif "semantic search" in text:
            evidence = "semantic"
            break

        elif "vector search" in text:
            evidence = "vector"
            break

        elif "embedding" in text:
            evidence = "embedding"
            break

        elif "rag" in text:
            evidence = "rag"
            break

        elif "llm" in text:
            evidence = "llm"
            break


    if evidence is None:

        if "Recommendation Systems" in skills:
            evidence = "recommendation"

        elif "Information Retrieval" in skills:
            evidence = "retrieval"

        elif "Semantic Search" in skills:
            evidence = "semantic"

        elif "Vector Search" in skills:
            evidence = "vector"

        elif "Embeddings" in skills:
            evidence = "embedding"

        elif "RAG" in skills:
            evidence = "rag"

        elif "LLMs" in skills:
            evidence = "llm"

        else:
            evidence = "general"



    if red >= 8:
        engagement = "Strong platform engagement."

    elif red >= 6:
        engagement = "Consistent recruiter engagement."

    else:
        engagement = "Active AI profile."



    templates = {

        "recommendation": [

            f"Built experience around recommendation systems supported by {skill_text}. {engagement}",

            f"Recommendation system background with {exp} years experience and strengths in {skill_text}.",

            f"Professional experience includes recommendation systems backed by {skill_text}.",

            f"Experience developing recommendation solutions supported by {skill_text}."

        ],

        "retrieval": [

            f"Experience includes retrieval systems with strengths in {skill_text}.",

            f"Professional background demonstrates retrieval engineering supported by {skill_text}.",

            f"Hands-on retrieval system experience combined with {skill_text}.",

            f"Career history reflects retrieval-focused work backed by {skill_text}."

        ],

        "ranking": [

            f"Experience spans ranking systems supported by {skill_text}.",

            f"Worked on ranking-related applications with expertise in {skill_text}.",

            f"Professional exposure to ranking systems combined with {skill_text}.",

            f"Ranking system experience strengthened by {skill_text}."

        ],

        "semantic": [

            f"Semantic search experience supported by {skill_text}.",

            f"Professional work includes semantic search using {skill_text}.",

            f"Background demonstrates semantic search expertise backed by {skill_text}.",

            f"Experience with semantic search strengthened through {skill_text}."

        ],

        "vector": [

            f"Vector search experience combined with {skill_text}.",

            f"Professional background includes vector search supported by {skill_text}.",

            f"Hands-on vector search expertise backed by {skill_text}.",

            f"Experience building vector search solutions using {skill_text}."

        ],

        "embedding": [

            f"Embedding-based retrieval experience supported by {skill_text}.",

            f"Professional work includes embedding pipelines with {skill_text}.",

            f"Hands-on experience with embedding technologies backed by {skill_text}.",

            f"Experience developing embedding-based search systems using {skill_text}."

        ],

        "rag": [

            f"Experience developing RAG pipelines supported by {skill_text}.",

            f"Professional background includes RAG applications using {skill_text}.",

            f"Hands-on RAG experience strengthened through {skill_text}.",

            f"RAG-focused AI engineering supported by {skill_text}."

        ],

        "llm": [

            f"Applied LLM experience backed by {skill_text}.",

            f"Professional work includes LLM applications supported by {skill_text}.",

            f"Hands-on experience with modern LLM workflows using {skill_text}.",

            f"Experience across LLM-based AI systems strengthened by {skill_text}."

        ],

        "general": [

            f"{exp} years experience with strengths in {skill_text}.",

            f"Professional AI background supported by {skill_text}.",

            f"Technical profile highlights {skill_text}.",

            f"Relevant AI engineering experience backed by {skill_text}."

        ]

    }

    template_list = templates[evidence]
    index = hash(candidate["candidate_id"]) % len(template_list)

    return template_list[index]


with open("../data/candidates.jsonl", "r", encoding="utf-8") as f:
    results = []

    for line in f:
        candidate = json.loads(line)

        skills = [skill["name"] for skill in candidate["skills"]]
        signals = candidate["redrob_signals"]
        career_history = candidate["career_history"]
        skill_score = calculate_skill_score(skills)

        exp = candidate["profile"]["years_of_experience"]
        headline = candidate["profile"]["headline"]
        exp_score = experience_score(exp)
        red_score = redrob_score(signals)
        career_sc = career_score(career_history)

        total_score = round(
            skill_score * 0.40
           + exp_score * 0.15
           + career_sc * 0.35
           + red_score * 0.10,
           2
           
        ) 

        results.append ({
            "candidate_id": candidate["candidate_id"],
            "score": total_score,
            "headline": candidate["profile"]["headline"],
            "skill_score": skill_score,
            "career_score": career_sc,
            "exp_score": exp_score,
            "red_score": red_score,
            "exp" : exp,
            "skills" : skills,
            "current_title": career_history[0]["title"] if career_history else "",
            "career_history": career_history
        })

    results.sort(
       key=lambda x: (-x["score"], x["candidate_id"])
    )

    import csv

    with open("../output/submission.csv", "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
           "candidate_id",
           "rank",
           "score",
           "reasoning"
        ])

        

        for rank, candidate in enumerate(results[:100], start=1):

            reasoning = generate_reasoning(candidate)

            print("\nCSV TOP 10\n")

            for i in results[:10]:
                print(i["candidate_id"], i["score"])
            writer.writerow([
               candidate["candidate_id"],
               rank,
               round(candidate["score"], 2),
               reasoning
            ])

    print("submission.csv created successfully!")
    

    print("\nTOP 10 CANDIDATES\n")

    for rank, candidate in enumerate(results[:20], start=1):
        print(
          rank,
          candidate["candidate_id"],
          candidate["score"],
          candidate["headline"]
        ) 
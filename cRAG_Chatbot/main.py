# main.py

from config import get_openai_client

# Get the OpenAI client (v1.x+)
client = get_openai_client()

# ---------------- STEP 1: CONTEXT EVALUATION ------------------
def evaluate_context(query, context):
    relevance = 0.5 if "sales" in context or "real estate" in context else 0.3
    completeness = 0.4
    accuracy = 0.7
    specificity = 0.4

    avg_score = (relevance + completeness + accuracy + specificity) / 4

    if avg_score >= 0.85:
        quality = "Excellent"
    elif avg_score >= 0.7:
        quality = "Good"
    elif avg_score >= 0.5:
        quality = "Fair"
    else:
        quality = "Poor"

    return {
        "Relevance": relevance,
        "Completeness": completeness,
        "Accuracy": accuracy,
        "Specificity": specificity
    }, quality

# ---------------- STEP 2: CORRECTIVE DECISION ------------------
def corrective_decision(overall_quality, user_query):
    if overall_quality in ["Poor", "Fair"]:
        return {
            "Action": "Retrieve_Again",
            "New_Query": refine_query(user_query),
            "Confidence": "Low",
            "Reasoning": "Initial context quality is insufficient to deliver a complete answer."
        }
    else:
        return {
            "Action": "Proceed_With_Answer",
            "New_Query": user_query,
            "Confidence": "High",
            "Reasoning": "Retrieved context quality is sufficient."
        }

def refine_query(query):
    return "What are the most effective strategies to successfully close sales deals in residential real estate for plots and apartments?"

# ---------------- STEP 3: CALL OPENAI ------------------
def call_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a real estate sales expert helping agents close successful property deals."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=700
    )
    return response.choices[0].message.content

# ---------------- EXECUTE CHATBOT FLOW ------------------

def generate_final_answer(user_query):
    # Simulated initial retrieval
    retrieved_context = (
        "To close real estate deals, highlight location, explain legal process, and create urgency."
    )

    print("🔍 Evaluating Retrieved Context...")
    scores, quality = evaluate_context(user_query, retrieved_context)

    print(f"Context Evaluation Scores: {scores}")
    print(f"Overall Quality: {quality}")

    decision = corrective_decision(quality, user_query)
    print(f"Correction Decision: {decision['Action']}")

    if decision["Action"] == "Retrieve_Again":
        print("🔄 Fetching improved context from OpenAI...\n")
        final_answer = call_openai(decision["New_Query"])
        context_quality = "Excellent"
    else:
        print("✅ Proceeding with existing context...\n")
        final_answer = call_openai(user_query)
        context_quality = quality

    return {
        "Context Quality": context_quality,
        "Confidence Level": decision["Confidence"],
        "Answer": final_answer
    }

# ---------------- MAIN RUNNER ------------------

if __name__ == "__main__":
    print("\n🏠 Welcome to the Real Estate Sales Closure Chatbot")
    print("---------------------------------------------")
    user_query = input("🧑‍💼 Enter your query: ").strip()
    result = generate_final_answer(user_query)

    print("\n🎯 FINAL RESULT:")
    for key, value in result.items():
        print(f"{key}:\n{value}\n")

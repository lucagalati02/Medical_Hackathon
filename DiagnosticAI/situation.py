import openai

API_KEY = "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"
openai.api_key = API_KEY


def situation():
    sit = openai.Completion.create(
        engine="text-davinci-003", prompt="I playing a complex game where I do diagnostic medicine, give me a description of a patient to diagnose, and give me a short diagnosis. Format it as such... Patient Symptoms: patient symptoms listed here / Patient Diagnosis: the diagnosis of the patient is said here", max_tokens=1000)
    symptoms = ""
    diagnosis = ""
    for data in sit.choices[0].text.split("/"):
        if "Patient Symptoms:" in data:
            symptoms = data
        if "Patient Diagnosis:" in data:
            diagnosis = data

    return symptoms, diagnosis


def diagnosing(diagnosis, diagnosis_attempt):
    attempt = openai.Completion.create(engine="text-davinci-003", prompt=(
        "Can you tell me if these 2 patient diagnoses match? Answer in 'True' or 'False'.\n1. " + diagnosis + "\n2. " + diagnosis_attempt))
    if "True" in attempt.choices[0].text:
        return "True"
    elif "False" in attempt.choices[0].text:
        return "False..." + diagnosis


if __name__ == "__main__":
    symptoms, diagnosis = situation()
    print(diagnosing(diagnosis, "The patient has a broken leg."))

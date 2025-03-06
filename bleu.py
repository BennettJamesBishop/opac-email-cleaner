import evaluate


# Load Hugging Face's BLEU metric
bleu = evaluate.load("bleu")

def calculate_bleu_score(reference_links, generated_links):
    """
    Calculates BLEU score between reference (manual) and generated link names using Hugging Face.
    
    :param reference_links: List of manually created link names
    :param generated_links: List of generated link names
    :return: BLEU score
    """
    if len(reference_links) != len(generated_links):
        raise ValueError("Reference and generated lists must have the same length.")

    # Hugging Face's BLEU requires each reference sentence as a list of lists
    references = [[ref] for ref in reference_links]

    # Compute BLEU
    bleu_score = bleu.compute(predictions=generated_links, references=references)

    return bleu_score["bleu"]

# Example: Replace these with your actual reference and generated outputs
# #for @UCSB Newsletter
# reference_links = [
#     "Feature 2: UC Santa Barbara Shines",
#     "Travel: Austria",
#     "Feature 3: River Movement",
#     "Feature 1: Promoting Latine Excellence",
#     "Feature 4: Voting is Easy",
#     "News 3: Your Brain on Fitness",
#     "News 2: Shark Science",
#     "Events 1: Women's Volleyball",
#     "Header: Alumni Lockup",
#     "Footer: The Current",
#     "Events: View All",
#     "Events 2: Homebuying Workshop",
#     "News 1: Math of Democracy",
#     "Footer: Subscribe to the Magazine",
#     "Advertisement: GoGoleta",
#     "Footer: LinkedIn",
#     "Footer: Facebook"
# ]

# #For @UCSB Newsletter
# generated_links = [
#     "Feature 2: UCSB Rankings",
#     "Travel: Austria",
#     "Feature 3: The Shape of Water",
#     "Feature 1: Promoting Latiné Excellence",
#     "Feature 4: Register to Vote",
#     "News 3: Brain Fitness",
#     "News 2: Shark Science",
#     "Events 1: Women's Volleyball",
#     "Header: Alumni Lockup",
#     "Footer: The Current",
#     "Events: View all events",
#     "Events 2: Homebuying Workshop",
#     "News 1: Math of Democracy",
#     "Footer: Subscribe to the Magazine",
#     "Advertisement: GoGoleta",
#     "Footer: LinkedIn",
#     "Footer: Facebook"
# ]

#For Monthly Events Email
reference_links = [
    "Current Month 2: Grand Slam",
    "Current Month 1: UC Day",
    "Current Month 8: First Time Homebuyer",
    "Footer: Opt Out",
    "Current Month 6: New Venture",
    "Current Month 4: Spring Mixer",
    "View All Button",
    "Current Month 5: Gaucho Academy",
    "Current Month 7: Baseball",
    "Current Month 3: Opera",
    "Header: Alumni Lockup",
    "Footer: Manage Preferences",
]


#For Monthly Events Email
generated_links = [
    "Current Month 2: Grad Slam",
    "Current Month 1: UC Day Reception",
    "Current Month 8: Homebuying Workshop",
    "Footer: Opt Out",
    "Current Month 6: New Venture Finals",
    "Current Month 4: Olé LA Mixer",
    "View All Button",
    "Current Month 5: Gaucho Academy Job Search",
    "Current Month 9: UCSB Baseball",
    "Current Month 3: Opera Gala",
    "Header: Alumni Lockup",
    "Footer: Manage Preferences,"
]



# Compute BLEU score
bleu_score = calculate_bleu_score(reference_links, generated_links)

# Print results
print(f"BLEU Score: {bleu_score:.4f}")

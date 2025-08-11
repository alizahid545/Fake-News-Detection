#!/usr/bin/env python3
"""
Enhanced Data Generator for Fake News Detection System
Generates comprehensive training data to improve model accuracy
"""

import pandas as pd
import random
import re

def generate_fake_news_examples():
    """Generate comprehensive fake news examples with realistic patterns"""
    
    fake_news_templates = [
        "BREAKING: {subject} discovered to {action}! {conspiracy}",
        "SHOCKING: {subject} finally admits {conspiracy}. {sensational}",
        "ALERT: {subject} causes {disease}! {miracle_cure}",
        "EXPOSED: {subject} is actually {conspiracy}. {evidence}",
        "MIRACLE: {subject} cures {disease} in {time}! {hidden}",
        "CONFIRMED: {subject} responsible for {event}. {coverup}",
        "URGENT: {subject} linked to {conspiracy}. {warning}",
        "REVEALED: {subject} admits {truth}. {shocking}",
        "WARNING: {subject} causes {problem}! {solution}",
        "DISCOVERED: {subject} is {conspiracy}. {proof}",
        "JUST IN: {subject} {action}! {sensational}",
        "EXCLUSIVE: {subject} {conspiracy}. {evidence}",
        "EMERGENCY: {subject} {warning}! {solution}",
        "CRITICAL: {subject} {problem}! {miracle_cure}",
        "DEVELOPING: {subject} {action}. {conspiracy}"
    ]
    
    subjects = [
        "Scientists", "Doctors", "Government", "Big Pharma", "NASA", 
        "The Media", "Tech Companies", "Vaccines", "5G Networks", 
        "Chemicals", "Food Industry", "Oil Companies", "Banks",
        "The Deep State", "Global Elites", "Mainstream Media",
        "Pharmaceutical Companies", "Tech Giants", "Social Media",
        "The Establishment", "The System", "The Powers That Be"
    ]
    
    actions = [
        "cure all diseases", "reverse aging", "control minds", 
        "predict the future", "communicate with aliens", 
        "time travel", "read thoughts", "teleport objects",
        "control the weather", "manipulate DNA", "create life",
        "access parallel universes", "bend reality", "stop time",
        "erase memories", "implant thoughts", "control emotions"
    ]
    
    conspiracies = [
        "hidden by the government for decades",
        "suppressed by big corporations",
        "covered up by mainstream media",
        "kept secret by scientists",
        "hidden from the public",
        "concealed by authorities",
        "buried by the establishment",
        "suppressed by the deep state",
        "hidden by global elites",
        "covered up by the system"
    ]
    
    sensational = [
        "This changes everything we know!",
        "The truth is finally out!",
        "This will shock the world!",
        "Everything you've been told is a lie!",
        "The evidence is undeniable!",
        "This proves the conspiracy!",
        "The world will never be the same!",
        "This is the biggest revelation ever!",
        "The truth has been hidden for years!",
        "This will change history forever!"
    ]
    
    diseases = [
        "cancer", "diabetes", "heart disease", "Alzheimer's", 
        "autism", "depression", "obesity", "allergies",
        "COVID-19", "flu", "common cold", "headaches",
        "insomnia", "anxiety", "arthritis", "asthma"
    ]
    
    miracle_cures = [
        "This natural remedy has been hidden for years!",
        "Big pharma doesn't want you to know this!",
        "This simple solution cures everything!",
        "The medical industry is hiding this cure!",
        "This ancient remedy works instantly!",
        "Doctors don't want you to know about this!",
        "This secret cure has been suppressed!",
        "The cure has been available all along!",
        "This natural treatment is 100% effective!",
        "The medical establishment is hiding the truth!"
    ]
    
    events = [
        "global warming", "pandemics", "economic crashes", 
        "natural disasters", "social unrest", "technological failures",
        "climate change", "food shortages", "water crises",
        "energy crises", "population control", "mind control"
    ]
    
    coverups = [
        "The evidence has been destroyed!",
        "Witnesses have been silenced!",
        "Documents have been classified!",
        "The truth is being suppressed!",
        "This is the biggest coverup in history!",
        "All evidence has been erased!",
        "The truth has been buried!",
        "This conspiracy goes to the top!",
        "The coverup is massive!",
        "The truth is being hidden at all costs!"
    ]
    
    warnings = [
        "Stop using this immediately!",
        "This is dangerous to your health!",
        "Protect yourself and your family!",
        "This could be deadly!",
        "The risks are enormous!",
        "This is a health emergency!",
        "Your life is at risk!",
        "This is extremely dangerous!",
        "The consequences are severe!",
        "This threatens everyone!"
    ]
    
    truths = [
        "the Earth is flat", "aliens exist", "time travel is real",
        "mind control is possible", "the moon landing was fake",
        "chemtrails are real", "vaccines cause autism",
        "the Earth is hollow", "dinosaurs never existed",
        "gravity is a hoax", "the sun is artificial",
        "reality is a simulation", "we live in a matrix"
    ]
    
    shocking = [
        "This is absolutely shocking!",
        "The implications are enormous!",
        "This will change history!",
        "Nothing will ever be the same!",
        "This is the biggest revelation ever!",
        "The world is not what we thought!",
        "Everything we know is wrong!",
        "This changes everything!",
        "The truth is unbelievable!",
        "This is beyond shocking!"
    ]
    
    problems = [
        "cancer", "autism", "infertility", "memory loss", 
        "personality changes", "genetic mutations",
        "brain damage", "organ failure", "premature aging",
        "immune system damage", "reproductive issues"
    ]
    
    solutions = [
        "Stop using this immediately!",
        "Switch to natural alternatives!",
        "Protect yourself with this simple method!",
        "This ancient remedy prevents all problems!",
        "Use this natural solution instead!",
        "This alternative is completely safe!",
        "This natural method works perfectly!",
        "This traditional remedy is the answer!",
        "This simple solution prevents everything!",
        "This natural approach is foolproof!"
    ]
    
    proofs = [
        "The evidence is overwhelming!",
        "Thousands of witnesses confirm this!",
        "Documents prove everything!",
        "The truth cannot be denied!",
        "This is scientifically proven!",
        "The proof is undeniable!",
        "Evidence is everywhere!",
        "The facts speak for themselves!",
        "This is beyond dispute!",
        "The evidence is conclusive!"
    ]
    
    fake_news = []
    
    # Generate 200 fake news examples for better training
    for _ in range(200):
        template = random.choice(fake_news_templates)
        
        # Fill in the template
        news_text = template.format(
            subject=random.choice(subjects),
            action=random.choice(actions),
            conspiracy=random.choice(conspiracies),
            sensational=random.choice(sensational),
            disease=random.choice(diseases),
            miracle_cure=random.choice(miracle_cures),
            event=random.choice(events),
            coverup=random.choice(coverups),
            warning=random.choice(warnings),
            truth=random.choice(truths),
            shocking=random.choice(shocking),
            problem=random.choice(problems),
            solution=random.choice(solutions),
            proof=random.choice(proofs),
            time="24 hours",
            hidden="This has been hidden by big pharma for years!",
            evidence="Shocking new evidence reveals everything."
        )
        
        fake_news.append(news_text)
    
    return fake_news

def generate_real_news_examples():
    """Generate comprehensive real news examples with factual patterns"""
    
    real_news_templates = [
        "{organization} reports that {discovery} has been {achievement}.",
        "Scientists at {institution} have {discovery} that could {benefit}.",
        "New research shows that {finding} may help {improvement}.",
        "{organization} announces {development} in {field}.",
        "Study published in {journal} reveals {finding} about {topic}.",
        "{institution} researchers develop {technology} for {purpose}.",
        "Clinical trials show {treatment} is {effective} for {condition}.",
        "{organization} confirms {fact} based on {evidence}.",
        "Scientists discover {discovery} during {research}.",
        "New study indicates {finding} related to {phenomenon}.",
        "Research team at {institution} finds {discovery}.",
        "{organization} releases {report} on {topic}.",
        "Study conducted by {institution} shows {finding}.",
        "{organization} publishes {analysis} of {phenomenon}.",
        "Scientists report {discovery} in {field}."
    ]
    
    organizations = [
        "The World Health Organization", "NASA", "The Centers for Disease Control",
        "The National Institutes of Health", "The European Space Agency",
        "The American Medical Association", "The National Science Foundation",
        "The United Nations", "The International Space Station",
        "The World Meteorological Organization", "The National Academy of Sciences",
        "The Royal Society", "The American Association for the Advancement of Science",
        "The European Commission", "The National Oceanic and Atmospheric Administration"
    ]
    
    institutions = [
        "Harvard University", "MIT", "Stanford University", "Oxford University",
        "Cambridge University", "Johns Hopkins University", "Yale University",
        "Princeton University", "Columbia University", "University of California",
        "University of Michigan", "University of Pennsylvania", "Duke University",
        "University of Chicago", "Cornell University", "University of Washington"
    ]
    
    discoveries = [
        "a new species of bacteria", "an effective treatment method",
        "a breakthrough in renewable energy", "a novel approach to data analysis",
        "an innovative medical device", "a sustainable material",
        "a new understanding of climate patterns", "an advanced algorithm",
        "a promising vaccine candidate", "a new diagnostic technique",
        "an improved drug delivery system", "a novel cancer treatment",
        "a breakthrough in quantum computing", "an innovative water purification method"
    ]
    
    achievements = [
        "successfully implemented", "thoroughly tested", "clinically proven",
        "scientifically validated", "peer-reviewed", "widely accepted",
        "officially recognized", "internationally approved", "rigorously tested",
        "comprehensively studied", "extensively researched", "carefully evaluated"
    ]
    
    benefits = [
        "improve public health", "reduce environmental impact",
        "enhance technological capabilities", "advance medical treatments",
        "increase energy efficiency", "solve complex problems",
        "provide better solutions", "support scientific progress",
        "improve quality of life", "reduce healthcare costs",
        "advance scientific understanding", "promote sustainability"
    ]
    
    findings = [
        "regular exercise improves mental health", "diet affects longevity",
        "sleep quality impacts productivity", "social connections reduce stress",
        "learning new skills maintains brain health", "meditation reduces anxiety",
        "green spaces improve well-being", "music therapy helps with recovery",
        "artificial intelligence improves diagnosis", "renewable energy reduces emissions"
    ]
    
    improvements = [
        "prevent chronic diseases", "enhance cognitive function",
        "improve quality of life", "reduce healthcare costs",
        "increase life expectancy", "promote overall wellness",
        "reduce environmental pollution", "improve energy efficiency",
        "enhance educational outcomes", "strengthen community health"
    ]
    
    developments = [
        "a new vaccine", "an innovative treatment", "a breakthrough technology",
        "an advanced diagnostic tool", "a sustainable solution",
        "an improved methodology", "a novel therapy", "a new medication",
        "an innovative procedure", "a breakthrough device"
    ]
    
    fields = [
        "medicine", "technology", "environmental science", "space exploration",
        "renewable energy", "artificial intelligence", "climate research",
        "public health", "materials science", "genetics", "neuroscience",
        "biotechnology", "nanotechnology", "robotics", "cybersecurity"
    ]
    
    journals = [
        "Nature", "Science", "The Lancet", "Cell", "PNAS",
        "The New England Journal of Medicine", "JAMA", "PLOS ONE",
        "Nature Medicine", "Science Translational Medicine", "Cell Reports",
        "Nature Biotechnology", "Science Advances", "Nature Communications"
    ]
    
    topics = [
        "climate change", "human health", "space exploration", "renewable energy",
        "artificial intelligence", "genetics", "neuroscience", "ecology",
        "biotechnology", "nanotechnology", "quantum computing", "sustainability"
    ]
    
    technologies = [
        "a new diagnostic system", "an advanced monitoring device",
        "an innovative treatment platform", "a sustainable energy solution",
        "an improved data analysis tool", "a novel research methodology",
        "a breakthrough imaging technique", "an advanced sensor network",
        "an innovative drug delivery system", "a new computational model"
    ]
    
    purposes = [
        "early disease detection", "environmental monitoring",
        "medical treatment", "scientific research", "public health",
        "space exploration", "climate research", "drug development",
        "genetic analysis", "neural mapping", "protein folding"
    ]
    
    treatments = [
        "the new medication", "the experimental therapy", "the innovative procedure",
        "the novel treatment approach", "the advanced medical intervention",
        "the breakthrough therapy", "the new surgical technique", "the innovative drug"
    ]
    
    effective = [
        "safe and effective", "well-tolerated", "clinically beneficial",
        "promising", "successful", "reliable", "efficacious", "well-received",
        "clinically significant", "statistically significant"
    ]
    
    conditions = [
        "chronic diseases", "mental health disorders", "infectious diseases",
        "autoimmune conditions", "cardiovascular problems", "neurological disorders",
        "cancer", "diabetes", "hypertension", "depression", "anxiety"
    ]
    
    facts = [
        "the effectiveness of vaccines", "the safety of approved medications",
        "the benefits of renewable energy", "the importance of biodiversity",
        "the impact of climate change", "the value of scientific research",
        "the benefits of exercise", "the importance of nutrition",
        "the effectiveness of public health measures", "the value of early detection"
    ]
    
    evidence = [
        "extensive research", "clinical trials", "peer-reviewed studies",
        "scientific data", "empirical observations", "statistical analysis",
        "longitudinal studies", "randomized controlled trials", "meta-analyses",
        "systematic reviews", "epidemiological studies"
    ]
    
    research = [
        "field studies", "laboratory experiments", "clinical trials",
        "observational studies", "longitudinal research", "cross-sectional analysis",
        "randomized controlled trials", "systematic reviews", "meta-analyses",
        "epidemiological studies", "genome-wide association studies"
    ]
    
    phenomena = [
        "climate patterns", "human behavior", "disease progression",
        "ecosystem dynamics", "technological advancement", "social development",
        "genetic expression", "neural plasticity", "immune responses",
        "metabolic processes", "cellular signaling"
    ]
    
    real_news = []
    
    # Generate 200 real news examples for better training
    for _ in range(200):
        template = random.choice(real_news_templates)
        
        # Fill in the template
        news_text = template.format(
            organization=random.choice(organizations),
            discovery=random.choice(discoveries),
            achievement=random.choice(achievements),
            institution=random.choice(institutions),
            benefit=random.choice(benefits),
            finding=random.choice(findings),
            improvement=random.choice(improvements),
            development=random.choice(developments),
            field=random.choice(fields),
            journal=random.choice(journals),
            topic=random.choice(topics),
            technology=random.choice(technologies),
            purpose=random.choice(purposes),
            treatment=random.choice(treatments),
            effective=random.choice(effective),
            condition=random.choice(conditions),
            fact=random.choice(facts),
            evidence=random.choice(evidence),
            research=random.choice(research),
            phenomenon=random.choice(phenomena)
        )
        
        real_news.append(news_text)
    
    return real_news

def create_expanded_dataset():
    """Create an expanded dataset with generated examples"""
    
    # Generate additional examples
    fake_news = generate_fake_news_examples()
    real_news = generate_real_news_examples()
    
    # Create DataFrame
    data = {
        'text': fake_news + real_news,
        'label': [1] * len(fake_news) + [0] * len(real_news)  # 1 for fake, 0 for real
    }
    
    df = pd.DataFrame(data)
    
    # Shuffle the data
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Save to CSV
    df.to_csv('expanded_dataset.csv', index=False)
    
    print(f"✅ Generated expanded dataset with {len(df)} examples")
    print(f"   - Fake news: {len(fake_news)} examples")
    print(f"   - Real news: {len(real_news)} examples")
    print(f"   - Saved to: expanded_dataset.csv")
    
    return df

if __name__ == "__main__":
    create_expanded_dataset()

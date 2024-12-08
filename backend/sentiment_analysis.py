from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import json
import torch

def load_finbert_model():
    tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
    model = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone')
    return tokenizer, model

def load_llm_model():
    sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
    return sentiment_analyzer

def load_summarization_model():
    summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")
    return summarizer

def financial_sentiment_analysis(tokenizer, model, text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    financial_score = torch.softmax(logits, dim=-1)[0][1].item()
    return financial_score

def normal_sentiment_analysis(llm_analyzer, text):
    truncated_text = text[:512]
    sentiment_result = llm_analyzer(truncated_text)
    sentiment_score = 0.0
    if sentiment_result[0]['label'] == 'POSITIVE':
        sentiment_score = 1.0
    elif sentiment_result[0]['label'] == 'NEGATIVE':
        sentiment_score = 0.0
    else:
        sentiment_score = 0.5
    return sentiment_score

def classify_sentiment(score):
    if score >= 0.7:
        return "true"
    elif score <= 0.4:
        return "false"
    else:
        return "neutral"

def summarize_text(summarizer, text):
    truncated_text = text[:200]
    summary = summarizer(truncated_text, max_length=30, min_length=10, do_sample=False)
    return summary[0]['summary_text']

def adjust_score(normal_score, financial_score):
    weighted_score = (normal_score * 1 + financial_score * 2) / 3 
    return weighted_score

def process_financial_news(input_json):
    tokenizer, model = load_finbert_model()
    llm_analyzer = load_llm_model()
    summarizer = load_summarization_model()

    output_data = []

    for news_item in input_json:
        title = news_item.get("title", "")
        description = news_item.get("description", "")

        combined_text = title + " " + description

        normal_sentiment_score = normal_sentiment_analysis(llm_analyzer, combined_text)

        financial_sentiment_score = financial_sentiment_analysis(tokenizer, model, combined_text)

        final_score = adjust_score(normal_sentiment_score, financial_sentiment_score)

        summary = summarize_text(summarizer, combined_text)

        news_item["summary"] = summary
        news_item["sentimentalScore"] = final_score
        news_item["isGoodNews"] = classify_sentiment(final_score)

        output_data.append(news_item)

    return output_data

def read_input_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def write_output_json(output_data, output_path):
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=4)

input_json_file = '/content/concatenated (1).json'
output_json_file = 'processed_financial_news_with_fast_summary.json'

input_json = read_input_json(input_json_file)

output_json = process_financial_news(input_json)

write_output_json(output_json, output_json_file)
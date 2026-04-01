import google.generativeai as genai

genai.configure(api_key="AIzaSyCJrltRRDvVv9uNuhQOVGZRZGsHtEwEL7s")

for m in genai.list_models():
    print(m.name)
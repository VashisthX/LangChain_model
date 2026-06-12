from langchain_text_splitters import CharacterTextSplitter

text = """
Artificial Intelligence (AI) is one of the most transformative technologies of the modern era. It refers to the ability of machines and computer systems to perform tasks that normally require human intelligence, such as learning, reasoning, problem-solving, decision-making, and understanding language. AI has evolved rapidly over the past few decades and is now an integral part of everyday life, influencing industries, businesses, and personal experiences around the world.
The foundation of AI lies in data and algorithms. By processing large amounts of information, AI systems can identify patterns, make predictions, and improve their performance over time. A major branch of AI is Machine Learning (ML), which enables computers to learn from data without being explicitly programmed for every task. Another important area is Deep Learning, which uses neural networks inspired by the human brain to solve complex problems such as image recognition, speech processing, and natural language understanding.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result)
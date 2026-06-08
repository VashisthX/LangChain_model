from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Explain the research paper {paper_input}
in a {style_input} style.
Keep the explanation {length_input}.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save('template.json')
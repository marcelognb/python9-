import streamlit as st



#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#loader = CSVLoader(file_path='knowledge_base.csv') #, encoding="utf-8"
#documents = loader.load()


#embeddings = OpenAIEmbeddings()
#db = FAISS.from_documents(documents, embeddings)

    #similar_response = db.similarity_search(query, k=1)
    #return [doc.page_content for doc in similar_response]

#, model='gpt=3.5-turbo-16k-0613'
#llm = ChatOpenAI(temperature=0)

##AI focada na linguagem Python

#best_practice = retrieve_info(message)

def main():
    st.set_page_config(
        page_title="Controle de Mensagens",
        page_icon=":bird:"
    )
    st.header("Controle de Mensagens")
    message = st.text_area("Mensagem principal")


if __name__ == '__main__':
    main()

# from flask import Flask, render_template, request, redirect
# from dotenv import load_dotenv
# from werkzeug.utils import secure_filename  # Add this line
# from PyPDF2 import PdfReader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.chat_models import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationalRetrievalChain
# import os

# app = Flask(__name__)

# # Load environment variables from .env file
# load_dotenv()

# # Get your OpenAI API key from environment variables
# openai_api_key = os.getenv("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")

# # Define the upload folder
# app.config['UPLOAD_FOLDER'] = 'uploads'


# def get_pdf_text(pdf_docs):
#     text = ""
#     for pdf in pdf_docs:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#     return text

# def get_text_chunks(text):
#     text_splitter = CharacterTextSplitter(
#         separator="\n",
#         chunk_size=1000,
#         chunk_overlap=200,
#         length_function=len
#     )
#     chunks = text_splitter.split_text(text)
#     return chunks

# def get_vectorstore(text_chunks):
#     embeddings = OpenAIEmbeddings(api_key=openai_api_key)
#     vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
#     return vectorstore

# def get_conversation_chain(vectorstore):
#     llm = ChatOpenAI(api_key=openai_api_key)
#     memory = ConversationBufferMemory(
#         memory_key='chat_history', return_messages=True)
#     conversation_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=vectorstore.as_retriever(),
#         memory=memory
#     )
#     return conversation_chain

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         print(request.form)  # Add this line for debugging
#         user_question = request.form.get('user_question')

#         if user_question:
#             response = app.config['conversation']({'question': user_question})
#             app.config['chat_history'] = response['chat_history']

#             return render_template('index.html', chat_history=app.config['chat_history'], user_question=user_question)

#     return render_template('index.html', chat_history=None, user_question=None)


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Check if the post request has the file part
#         if 'pdf_file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)

#         file = request.files['pdf_file']
#         # If the user does not select a file, the browser submits an empty file without a filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)

#         # Handle the file upload (you can use your existing code here)
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)

#         # Extract text from the PDF and process as needed
#         pdf_text = get_pdf_text([file_path])
#         text_chunks = get_text_chunks(pdf_text)
#         vectorstore = get_vectorstore(text_chunks)
#         conversation_chain = get_conversation_chain(vectorstore)

#         user_question = request.form.get('user_question')
#         if user_question:
#             response = conversation_chain({'question': user_question})
#             chat_history = response['chat_history']
#             return render_template('index.html', chat_history=chat_history, user_question=user_question)

#     return render_template('index.html', chat_history=None, user_question=None)




# if __name__ == '__main__':
#     app.config['conversation'] = None
#     app.config['chat_history'] = None
#     app.run(debug=True)

import tkinter
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from punkt import PunktLanguageVars
import string
from gensim.parsing.preprocessing import remove_stopwords



tokenize = PunktLanguageVars()


root = tkinter.Tk()
root.title("Plagiarism Checker")
root.geometry("1000x600")
label1 = tkinter.Label(root,text="Plagiarism Checker",fg="black",font=("helvetica",15))
label2 = tkinter.Label(root,text="Enter your first paragraph :-",font=("helvetica",11))
label3 = tkinter.Label(root,text="")
text_box = tkinter.Text(root,width="100",height="10")
label4 = tkinter.Label(root,text="Enter your second paragraph :- ",font=("helvetica",11))
label5 = tkinter.Label(root,text="")
text_box2 = tkinter.Text(root,width="100",height="10")
label6 = tkinter.Label(root,text="")


def checker():
    doc1 = text_box.get("1.0", "end-1c")
    doc2 = text_box2.get("1.0", "end-1c")
    doc1_without_stopwords = remove_stopwords(doc1)
    doc2_without_stopwords = remove_stopwords(doc2)
    doc1_words = tokenize.word_tokenize(doc1_without_stopwords.lower())
    doc2_words = tokenize.word_tokenize(doc2_without_stopwords.lower())
    new_doc1 = [token for token in doc1_words if token not in string.punctuation]
    new_doc2 = [token for token in doc2_words if token not in string.punctuation]
    

    docs = []
    docs.append(TaggedDocument(new_doc1, tags = ['Doc1']))
    docs.append(TaggedDocument(new_doc2, tags = ['Doc2']))
    
    model = Doc2Vec(docs, vector_size=50, window=2, min_count=1, workers=4, epochs=100)
    
    doc1_embedding = model.docvecs['Doc1']
    doc2_embedding = model.docvecs['Doc2']

    similarity = model.docvecs.similarity('Doc1', 'Doc2')
    result = ((similarity + 1) / 2) * 100
    
    label = tkinter.Label(root,text=f"Plagiarism is {result:.2f}%",font=("helvetica",13),fg="blue")
    label.pack()


button1 = tkinter.Button(root,text="Check",command= checker,width=5,height=2,font=("helvetica",11))


label1.pack()
label3.pack()
label2.pack()
text_box.pack()
label5.pack()
label4.pack()
text_box2.pack()
label6.pack()
button1.pack()
root.mainloop()

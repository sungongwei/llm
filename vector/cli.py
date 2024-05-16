from base import answer_question


def main():
    print("Welcome to the Q&A system!")
    while True:
        question = input("Enter your question: ")
        if question.lower() == "":
          print("Exiting the Q&A system. Goodbye!")
          break
        answer = answer_question(question)
        for question, answer, similarity in answer:
          print("Question:", question)
          print("Answer:", answer)
          print("Similarity:", similarity)
          print()

if __name__ == "__main__":
    main()

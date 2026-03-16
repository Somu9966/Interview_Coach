from dotenv import load_dotenv
# from chains.interviewer import create_interviewer_chain
from memory.conversation import create_memory
from chains.interviewer import create_interviewer_chain_with_memory
from langchain_core.messages import HumanMessage, AIMessage


load_dotenv()

# # Create the chain
# interviewer = create_interviewer_chain()

# # Start the interview
# response = interviewer.invoke({
#     "interview_type": "technical Python",
#     "level": "senior",
#     "focus_area": "Python fundamentals and best practices",
#     "question_number": 1,
#     "total_questions": 5,
#     "input": "Please start the interview with your first question."
# })

# print(f"Interviewer: {response}")


# def run_basic_interview():
#     interviewer = create_interviewer_chain()

#     config = {
#         "interview_type": "technical Python",
#         "level": "senior",
#         "focus_area": "Python fundamentals, OOP, and best practices",
#         "total_questions": 5,
#     }

#     print("=" * 50)
#     print("AI Interview Coach - Basic Mode")
#     print("=" * 50)
#     print("Type 'quit' to exit\n")

#     # Get first question
#     response = interviewer.invoke({
#         **config,
#         "question_number": 1,
#         "input": "Start the interview with your first question."
#     })
#     print(f"\nInterviewer: {response}\n")

#     question_num = 1
#     while question_num < config["total_questions"]:
#         # Get candidate's answer
#         answer = input("You: ")
#         if answer.lower() == 'quit':
#             break

#         question_num += 1

#         # Get next question (acknowledging previous answer)
#         response = interviewer.invoke({
#             **config,
#             "question_number": question_num,
#             "input": f"The candidate answered: {answer}\n\nAcknowledge briefly and ask question {question_num}."
#         })
#         print(f"\nInterviewer: {response}\n")

#     print("\nInterview complete! Thank you for participating.")

# if __name__ == "__main__":
#     run_basic_interview()


def run_interview_with_memory():
    # Create memory instance
    memory = create_memory()

    # Create chain with memory
    interviewer = create_interviewer_chain_with_memory(memory)

    config = {
        "interview_type": "technical Python",
        "level": "senior",
        "focus_area": "Python fundamentals and design patterns",
    }

    print("=" * 50)
    print("AI Interview Coach - With Memory")
    print("=" * 50)
    print("Type 'quit' to exit, 'history' to see conversation\n")

    # Initial prompt
    user_input = "Please start the interview."

    while True:
        # Get response
        response = interviewer.invoke({
            **config,
            "input": user_input
        })

        # Save to memory
        memory.add_user_message(user_input)
        memory.add_ai_message(response)

        print(f"\nInterviewer: {response}\n")

        # Get next input
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'history':
            print("\n--- Conversation History ---")
            for msg in memory.messages:
                role = "You" if isinstance(msg, HumanMessage) else "Interviewer"
                print(f"{role}: {msg.content[:100]}...")
            print("--- End History ---\n")
            user_input = input("You: ")

    print("\nInterview complete!")
    return memory

if __name__ == "__main__":
    run_interview_with_memory()
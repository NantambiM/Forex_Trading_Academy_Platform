= 0

        print(request.form)

        for question in questions:
            selected_option = request.form.get(f"question_{question.id}")

            print("Question ID:", question.id)
            print("Selected:", selected_option)
            print("Correct :", question.correct_option)

            if selected_option == question.correct_option:
                score += 1

        print("Final score:", score)
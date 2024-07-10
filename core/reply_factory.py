def record_current_answer(self, user_id, answer):
    if user_id not in self.user_data:
        self.user_data[user_id] = {'current_question': 0, 'answers': []}

    current_question_index = self.user_data[user_id]['current_question']
    current_question = self.questions[current_question_index]
    
    # Validate the answer (if necessary)
    # For example, if the answer must be an integer and within a specific range
    if current_question['type'] == 'multiple_choice':
        if answer.isdigit() and 0 <= int(answer) < len(current_question['options']):
            self.user_data[user_id]['answers'].append(int(answer))
        else:
            return "Invalid answer. Please provide a valid option."
    else:
        self.user_data[user_id]['answers'].append(answer)
    
    self.user_data[user_id]['current_question'] += 1
    return "Answer recorded."

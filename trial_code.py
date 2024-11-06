class CourseBot:
    def __init__(self):
        # Dictionary of course-related information
        self.course_info = {
            "schedule": "The course runs Monday and Wednesday, 2:00-3:30 PM",
            "syllabus": "The course covers: Week 1-4: Basics, Week 5-8: Advanced Topics, Week 9-12: Projects",
            "assignments": "There are 3 main assignments and 1 final project",
            "office_hours": "Office hours are Tuesday 1-3 PM and Thursday 2-4 PM",
            "prerequisites": "Basic programming knowledge is required",
            "grading": "Assignments: 60%, Final Project: 30%, Participation: 10%"
        }
        
        # Common patterns and their responses
        self.patterns = {
            "hello": ["Hi! How can I help you with the course?", 
                     "Hello! What would you like to know about the course?"],
            "bye": ["Goodbye! Feel free to ask more questions later.",
                   "See you later! Let me know if you need more help."],
            "thank": ["You're welcome!", "Happy to help!"]
        }
        
        # Synonyms mapping
        self.synonyms = {
            "schedule": ["timetable", "calendar", "classes"],
            "syllabus": ["curriculum", "outline"],
            "assignments": ["homework", "tasks"],
            "office_hours": ["consultation hours", "availability"]
        }
    
    def get_response(self, user_input):
        # Convert input to lowercase for easier matching
        user_input = user_input.lower()
        
        # Check for common greetings/farewells
        for pattern, responses in self.patterns.items():
            if pattern in user_input:
                return responses[0] # For simplicity, using first response
        
        # Check for course-related keywords and their synonyms
        for topic, info in self.course_info.items():
            if topic in user_input:
                return info
            for synonym in self.synonyms.get(topic, []):
                if synonym in user_input:
                    return info
        
        # Handle unknown queries
        return "I'm not sure about that. You can ask me about the schedule, syllabus, assignments, office hours, prerequisites, or grading."

def main():
    chatbot = CourseBot()
    print("Course Assistant Bot (type 'quit' to exit)")
    print("What would you like to know about the course?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Bot: Goodbye! Have a great day!")
            break
            
        response = chatbot.get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
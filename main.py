from manage_database.logic_question.build_database import BuildDatabase


def main():
    manage_database = BuildDatabase("http://localhost:8000/logicQuestions/")
    manage_database.post_list_of_json('C:\\Users\\jmess\\Documents\\questoes.json')


if __name__ == '__main__':
    main()

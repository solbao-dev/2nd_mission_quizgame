import json

# 1. Quiz 클래스 (붕어빵 틀)
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return str(self.answer) == str(user_answer)

# 2. QuizGame 클래스 (전체 관리자 점장님!)
class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes  # 코디세이 특별판 퀴즈 5개를 점장님한테 전달!
        self.best_score = 0     # 최고 점수는 일단 0점으로 시작

    # 🌟 [새로운 기능 1] 퀴즈 추가하기 기능!
    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = input("문제를 입력하세요: ").strip()
        
        choices = [] # 선택지 4개를 담을 빈 바구니
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            choices.append(choice) # 바구니에 하나씩 쏙쏙 넣기! (.append)
            
        # 정답 번호 방어막 (1, 2, 3, 4 중에 하나만 입력할 때까지 계속 물어봄!)
        while True:
            answer = input("정답 번호 (1-4): ").strip()
            if answer in ['1', '2', '3', '4']:
                break
            print("⚠️ 잘못된 입력입니다. 1에서 4 사이의 숫자를 입력하세요.")
            
        # 새로운 붕어빵(퀴즈)을 구워서 점장님의 퀴즈 목록에 추가!
        new_quiz = Quiz(question, choices, int(answer))
        self.quizzes.append(new_quiz)
        print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")

    # 🌟 [새로운 기능 2] 등록된 퀴즈 목록 보기 기능!
    def show_list(self):
        # len()은 바구니 안에 퀴즈가 몇 개 있는지 숫자를 세어주는 마법의 단어예요!
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")
        # enumerate()는 퀴즈들에 [1], [2], [3] 처럼 순서대로 번호표를 붙여줘요.
        for i, quiz in enumerate(self.quizzes):
            print(f"[{i+1}] {quiz.question}")
        print("----------------------------------------")


    # 메뉴판을 보여주고 입력을 받는 기능
    def show_menu(self):
        try:
            while True:
                print("\n========================================")
                print("        🎯 솔바오의 코디세이 퀴즈 🎯        ")
                print("========================================")
                print("1. 퀴즈 풀기")
                print("2. 퀴즈 추가")
                print("3. 퀴즈 목록")
                print("4. 점수 확인")
                print("5. 종료")
                print("========================================")
                
                choice = input("선택: ").strip()

                if choice == '1':
                    print("\n📝 퀴즈 풀기 기능은 곧 만들 거예요!")
                elif choice == '2':
                    self.add_quiz() # 🌟 아까 만든 퀴즈 추가 기능 실행!
                elif choice == '3':
                    self.show_list() # 🌟 아까 만든 퀴즈 목록 보기 기능 실행!
                elif choice == '4':
                    print("\n🏆 점수 확인 기능은 곧 만들 거예요!")
                elif choice == '5':
                    print("\n게임을 종료합니다. 수고했어요 솔바오! 👋")
                    break
                else:
                    print("\n⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")
        
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 앗! 갑자기 나가셨군요. 데이터를 안전하게 보호하며 식당 문을 닫습니다. 안녕히 가세요! 👋")

# 3. 기본 퀴즈 데이터 5개 구워내기! (코디세이 특별판✨)
quiz_data = [
    Quiz("1. 코디세이 미션에서 강조하는, 프로그래밍 언어를 배우는 가장 확실한 방법은 무엇일까요?", 
         ["문법 달달 외우기", "동작하는 프로그램을 처음부터 끝까지 직접 만들기", "유명한 강의 반복해서 보기", "남이 짠 코드 복사하기"], 2),
    Quiz("2. 미션 2에서 퀴즈 문제들을 쉽게 찍어내기 위해 우리가 만든 '붕어빵 틀'의 파이썬 문법 이름은 무엇일까요?", 
         ["변수(Variable)", "함수(Function)", "클래스(Class)", "리스트(List)"], 3),
    Quiz("3. 프로그램을 껐다 켜도 솔바오의 퀴즈 데이터와 점수가 날아가지 않게 보존해 주는 파일의 확장자는?", 
         [".txt", ".pdf", ".json", ".png"], 3),
    Quiz("4. 방금 전 로컬(내 컴퓨터)에 있는 파일들을 인터넷(GitHub)으로 쏘아 올릴 때 사용했던 마법의 명령어는?", 
         ["git clone", "git add", "git commit", "git push"], 4),
    Quiz("5. 우리가 GitHub에 첫 집터(저장소)를 만들 때, 충돌 에러를 막기 위해 절대 체크하지 않았던 것은?", 
         ["Public 설정", "Repository name", "Add a README file", "Create 버튼"], 3)
]

# 4. 진짜로 게임을 실행시키는 마법의 주문!
if __name__ == "__main__":
    game = QuizGame(quiz_data)
    game.show_menu()
    
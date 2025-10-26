from datetime import datetime
import random 
ZODIAC_DATES = [
    (1, 20, "Aquarius ♒"), (2, 19, "Pisces ♓"), (3, 21, "Aries ♈"),
    (4, 20, "Taurus ♉"), (5, 21, "Gemini ♊"), (6, 21, "Cancer ♋"),
    (7, 23, "Leo ♌"), (8, 23, "Virgo ♍"), (9, 23, "Libra ♎"),
    (10, 23, "Scorpio ♏"), (11, 22, "Sagittarius ♐"), (12, 22, "Capricorn ♑"),
]
DAILY_PREDICTIONS = {
    "Aries ♈": [
        "A sudden spark of energy will lead to a minor professional victory today.",
        "Expect a conflict over priorities, especially in a group setting.",
        "Money matters stabilize, allowing you to breathe easier regarding recent expenses."
    ],
    "Taurus ♉": [
        "A quiet, reliable effort will solidify your domestic harmony and well-being.",
        "Your financial plans receive a stroke of unexpected luck this afternoon.",
        "You might feel stubborn about a small change; try to go with the flow."
    ],
    "Gemini ♊": [
        "An important communication leads to crisp decisions that save you time and money.",
        "Your intellectual curiosity is peaked by an unexpected meeting or text message.",
        "Avoid making promises you can't easily keep; social demands are high."
    ],
    "Cancer ♋": [
        "Emotional bonds are strengthened through a heartfelt, intimate conversation.",
        "Trust your gut instinct even if the situation feels slightly unsettling.",
        "A domestic chore or family situation requires your immediate, empathetic attention."
    ],
    "Leo ♌": [
        "A spotlight is on you today; success and recognition at work are possible.",
        "Creative projects gain momentum, drawing positive attention from others.",
        "An opportunity to lead will arise, demanding confidence and clear communication."
    ],
    "Virgo ♍": [
        "Meticulous attention to detail helps you solve a long-standing, nagging problem.",
        "Mercury guides you to insightful choices regarding health and routine management.",
        "Avoid overthinking a simple matter; sometimes, the simplest answer is the best."
    ],
    "Libra ♎": [
        "Harmonious energies stabilize a relationship you deeply value.",
        "A financial opportunity related to partnership or collaboration presents itself.",
        "You may be tempted to ignore a conflict; addressing it gently is key to peace."
    ],
    "Scorpio ♏": [
        "Your determination is focused, allowing you to blast through a wall of self-doubt.",
        "An intense discussion leads to powerful clarity in a personal goal.",
        "Trust issues may surface; rely on resilience and loyalty to navigate them."
    ],
    "Sagittarius ♐": [
        "Jupiter inspires innovation; think bigger than your first idea for a better outcome.",
        "An unexpected travel or educational opportunity may suddenly materialize.",
        "Avoid overindulgence and keep your philosophical optimism grounded in reality."
    ],
    "Capricorn ♑": [
        "Saturn demands you keep a promise you made to yourself regarding a long-term goal.",
        "Clarity arrives concerning a career partnership or professional commitment.",
        "A slight tension regarding money may require conservative, disciplined spending."
    ],
    "Aquarius ♒": [
        "Rahu wants you to avoid risky investments or impulsive, unconventional social choices.",
        "A friend group or collaborative effort benefits from your unique, humanitarian perspective.",
        "Take a moment for personal space; your independent nature needs a refresh today."
    ],
    "Pisces ♓": [
        "Jupiter brings an unexpected growth or clarity in financial security.",
        "Intuition is high; meditation or quiet reflection brings gains and insights.",
        "Avoid the temptation to escape minor responsibilities; set limits and face reality."
    ]
}
DAILY_GUIDANCE = {
    "Aries ♈": [
        "Be real about your needs and limits to clear the air.",
        "Trust your courage in teamwork and step into leadership.",
        "Focus on honest self-expression across all life areas."
    ],
    "Taurus ♉": [
        "Embrace harmony and stabilize everything you value today.",
        "It's recommended not to be stubborn; go with the flow of change.",
        "Seek stability and comfort, but don't resist necessary movement."
    ],
    "Gemini ♊": [
        "Take a breath before hoping onto a new journey or making a quick decision.",
        "Today, your versatility supports insightful choices and progress.",
        "Use your communication skills to express gratitude and appreciation."
    ],
    "Cancer ♋": [
        "The Moon wants you to trust your gut, even if it feels risky.",
        "Strengthen intimacy and emotional bonds by being present.",
        "Don't get upset when you confront a tricky situation; confront it with softness."
    ],
    "Leo ♌": [
        "The Sun wants you to stand up where everyone can see you.",
        "Make your life more sublime by enjoying the richer grandeur of infinite life.",
        "Bring recognition to your work by speaking clearly and confidently."
    ],
    "Virgo ♍": [
        "Mercury wants you to slow down and take your time before acting.",
        "Support relationship growth by offering practical help, not just criticism.",
        "Avoid conflict as overthinking may worsen your overall well-being."
    ],
    "Libra ♎": [
        "Venus inspires healthy lifestyle choices and balanced decisions.",
        "Do not avoid dealing with conflicts; address them directly for long-term peace.",
        "Value harmony, but ensure you stand up for yourself where needed."
    ],
    "Scorpio ♏": [
        "Use your extra time today in pursuing hobbies or things that you enjoy.",
        "Let go of control in one minor area to build trust and lessen intensity.",
        "Mars fuels loyalty and passion in love; direct this energy positively."
    ],
    "Sagittarius ♐": [
        "Maintain optimism, but manage financial tensions with caution.",
        "Seek a guru or visionary perspective to give direction and meaning to your goals.",
        "Don't let money worries distract you from finding joy in the current moment."
    ],
    "Capricorn ♑": [
        "Prioritize long-term partnerships and seek clarity in your commitments.",
        "Control your weight and stress levels by ensuring you get enough exercise.",
        "Ensure discipline in your planning to achieve long-term success."
    ],
    "Aquarius ♒": [
        "Use your independent streak to champion a cause that matters to you.",
        "Rahu warns you to avoid taking on too many problems from other people.",
        "Smile as it is the best antidote for all your current emotional problems."
    ],
    "Pisces ♓": [
        "Meditation and yoga will bring gains; focus on the inner world.",
        "Compassionate action is favored; help a loved one without expectation.",
        "Avoid the temptation to escape minor responsibilities; set limits and face reality."
    ]
}
class Person:
    def __init__(self, name: str, birth_date_str: str):
        self._name = name
        try:
            self._birth_date = datetime.strptime(birth_date_str, '%d-%m-%Y')
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")
    def get_name(self) -> str:
        return self._name
    def get_birth_month_day(self) -> tuple[int, int]:
        return (self._birth_date.month, self._birth_date.day)
class Astrologer:
    def __init__(self, zodiac_data, predictions_data, guidance_data):
        self._zodiac_data = zodiac_data
        self._predictions = predictions_data
        self._guidance = guidance_data
    def find_zodiac_sign(self, person: Person) -> str:
        birth_month, birth_day = person.get_birth_month_day()
        birth_date_tuple = (birth_month, birth_day)
        if birth_month == 1 and birth_day < self._zodiac_data[0][1]:
            return "Capricorn ♑"
        correct_sign = "Capricorn ♑"
        for month_start, day_start, sign in self._zodiac_data:
            sign_start_date_tuple = (month_start, day_start)

            if birth_date_tuple >= sign_start_date_tuple:
                correct_sign = sign
            else:
                break
        return correct_sign
    def get_daily_reading(self, sign: str) -> tuple[str, str]:
        prediction = random.choice(self._predictions.get(sign, ["No prediction available."]))
        guidance = random.choice(self._guidance.get(sign, ["Seek inner peace today."]))
        return prediction, guidance
def get_user_data():
    """Dynamically asks the user for name and full birth date in DD-MM-YYYY format."""
    print("✨ Welcome to the Zodiac Sign Finder! ✨")
    name = input("Please enter your name: ").strip()
    while True:
        birth_date_str = input(
            "Please enter your FULL birth date (e.g., 21-05-1990) [DD-MM-YYYY]: "
        ).strip()
        try:
            datetime.strptime(birth_date_str, '%d-%m-%Y')
            break
        except ValueError:
            print("❌ Invalid format. Please make sure you use DD-MM-YYYY (e.g., 23-10-1995).")
    return name, birth_date_str
if __name__ == "__main__":
    name, birth_date_str = get_user_data()
    master_astro = Astrologer(ZODIAC_DATES, DAILY_PREDICTIONS, DAILY_GUIDANCE)
    try:
        user_person = Person(name, birth_date_str)
        sign = master_astro.find_zodiac_sign(user_person)
        prediction, guidance = master_astro.get_daily_reading(sign)
        print("\n--- Your Astrological Reading ---")
        print(f"Hello, {user_person.get_name()}!")
        print(f"Your Birth Date: {birth_date_str}")
        print(f"Your Western Zodiac Sign is: {sign}")
        print("-" * 33)
        print(f"⭐ Today's Prediction: {prediction}")
        print(f"💡 Daily Guidance: {guidance}")
        print("-" * 33)
    except ValueError as e:
        print(f"\nAn error occurred: {e}")
        print("Could not complete the reading.")
from flask import Flask, render_template, request

app = Flask(__name__)

# 10 Difficult MCQ's regarding Nepal
QUESTIONS = [
    {"q": "What is the only place in Nepal where the 'Kusunda' language is still spoken?", "options": ["Tanahun", "Gorkha", "Dang", "Surkhet"], "ans": "Dang"},
    {"q": "Which Nepali king is known as the 'Father of the Nation'?", "options": ["Prithvi Narayan Shah", "Tribhuvan", "Mahendra", "Birendra"], "ans": "Tribhuvan"},
    {"q": "What is the altitude of the highest point of the world's deepest gorge, Dana?", "options": ["1200m", "2500m", "4000m", "5000m"], "ans": "1200m"},
    {"q": "In which year did Nepal formally become a Federal Democratic Republic?", "options": ["2006", "2007", "2008", "2015"], "ans": "2008"},
    {"q": "Who was the first woman to scale Mt. Everest from Nepal?", "options": ["Pasang Lhamu Sherpa", "Lhakpa Sherpa", "Phurba Tashi", "Junko Tabei"], "ans": "Pasang Lhamu Sherpa"},
    {"q": "Which protected area of Nepal is famous for the 'Red Panda'?", "options": ["Chitwan", "Langtang", "Bardia", "Rara"], "ans": "Langtang"},
    {"q": "What is the standard time of Nepal based on?", "options": ["Mt. Everest", "Mt. Gaurishankar", "Mt. Annapurna", "Mt. Machhapuchhre"], "ans": "Mt. Gaurishankar"},
    {"q": "The 'Kumari' tradition is primarily associated with which ethnic group?", "options": ["Gurung", "Newar", "Sherpa", "Tharu"], "ans": "Newar"},
    {"q": "Which treaty ended the Anglo-Nepal War in 1816?", "options": ["Sugauli Treaty", "Peace and Friendship Treaty", "Mahakali Treaty", "Delhi Agreement"], "ans": "Sugauli Treaty"},
    {"q": "Who is the author of the national anthem of Nepal, 'Sayaun Thunga Phool Ka'?", "options": ["Laxmi Prasad Devkota", "Pradeep Kumar Rai (Byakul Maila)", "Amber Gurung", "Bhanubhakta Acharya"], "ans": "Pradeep Kumar Rai (Byakul Maila)"}
]

@app.route('/', methods=['GET', 'POST'])
def quiz():
    score = None
    if request.method == 'POST':
        score = 0
        for i, q in enumerate(QUESTIONS):
            # We use q0, q1, etc. as keys from the form
            selected = request.form.get(f"q{i}")
            if selected == q['ans']:
                score += 10
    return render_template('index.html', questions=QUESTIONS, score=score)

if __name__ == '__main__':
    # host='0.0.0.0' is required for Docker to expose the app
    app.run(host='0.0.0.0', port=5000)

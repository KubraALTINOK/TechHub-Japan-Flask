from flask import Flask, render_template

app = Flask(__name__)

# 1. Ana Sayfa
@app.route('/')
def home():
    return render_template('index.html')

# 2. Ülke Tanıtımı Sayfası
@app.route('/hakkinda')
def about():
    return render_template('about.html')

# 3. Yazılım Olanakları Sayfası
@app.route('/olanaklar')
def jobs():
    job_opportunities = [
        {
            "icon": "🤖",
            "title": "Yapay Zeka ve Robotik",
            "description": "Tokyo, AI ve makine öğrenmesi projeleri için dünyanın en büyük AR-GE merkezlerine ev sahipliği yapar."
        },
        {
            "icon": "🎮",
            "title": "Oyun Geliştirme",
            "description": "Dünyanın en köklü oyun şirketlerinde çalışarak Nintendo, Sony gibi devlerin ekosistemini yakından tanıyın."
        },
        {
            "icon": "🌐",
            "title": "Web 3.0 & Blockchain",
            "description": "Merkeziyetsiz finans ve yeni nesil web teknolojilerinde öncü girişimlerde yer alın."
        }
    ]
    return render_template('jobs.html', jobs=job_opportunities)

# 4. İletişim Sayfası
@app.route('/iletisim')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
<p align="center">
<a href="" target="blank">
<img alt="GitHub deployments" src="https://img.shields.io/github/deployments/shahriarshafin/ubot/production?label=vercel&logo=vercel&logoColor=vercel&style=flat-square">
</a>
<a href="https://github.com/shahriarshafin/ubot/blob/master/LICENSE" target="blank">
<img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="licence" />
</a>
<a href="https://github.com/shahriarshafin/softavia/commits/master" target="blank">
<img alt="GitHub commit merge status" src="https://img.shields.io/github/commit-status/shahriarshafin/softavia/master/efc47576d96123509711d275c6fe613a3bfe4b94?style=flat-square"/>
</a>
</p>

<br/>

# Introducing `Ubot`

<p align="center">
    <img src="https://github.com/shahriarshafin/ubot/raw/master/assets/images/screenshot.png" alt="SS" width="" height="">
</p>

If an admitted student needs any information about our university, they do not know where to go or who to ask and do not get any immediate answers to these questions.

To solve this problem we developed a chatbot, where they can chat with an AI-powered bot that will provide all the information they need.

## Set up and run

1. Clone the repository

```bash
https://github.com/ingenuity-2-0/ubot-backend.git
```

2. Change the working directory

```bash
cd ubot-backend
```

3. Install dependencies

```bash
pip insatll -r requirements.txt
```

4. Run the app in development mode

```bash
flask --app app run
```

That's All! Now open [localhost:5000](http://localhost:5000/) to see the app.

## Dependencies

```
it requires python version >=3.7
click==8.0.3
colorama==0.4.4
Flask==2.0.3
Flask-Cors==3.0.10
itsdangerous==2.1.2
Jinja2==3.1.1
joblib==1.1.0
MarkupSafe==2.1.1
nltk==3.6.7
numpy==1.22.1
Pillow==9.0.0
regex==2022.1.18
six==1.16.0
torch==1.10.1
torchaudio==0.10.1
torchvision==0.11.2
tqdm==4.62.3
typing_extensions==4.0.1
Werkzeug==2.0.3

```

Looking for back-end build setup -> [`ubot-frontend`](https://github.com/ingenuity-2-0/ubot_frontend)

## License

This project is licensed under the MIT License - see the [`LICENSE`](LICENSE) file for details.

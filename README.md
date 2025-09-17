# 📚 Study Assistant

An AI-powered study assistant that helps students interact with study material, answer questions, and manage learning tasks efficiently using Google Gemini API.
Demo Video Link : 
(https://drive.google.com/drive/folders/1yIl2nzZjOyX5EPD3LbCaiZ9rw_cX8eSG?usp=sharing)

---

## ✨ Features

- 🤖 Interactive Q&A with your study content
- 👥 Multiple AI agents communicating for enhanced responses
- 🖥️ Built using Python and Streamlit for a seamless web interface
- 🔌 Easy integration with Google Gemini API
- 📄 Support for multiple document formats
- 🎯 Smart content relevance ranking

---

## 📁 Folder Structure

```
study-assistant/
│
├── agents/                 # Contains AI agents logic and communication scripts
│   ├── agent1.py
│   └── agent2.py
│
├── app/                    # Main Streamlit application
│   └── main.py
│
├── utils/                  # Utility functions for processing, file handling, etc.
│   └── helpers.py
│
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment variables
└── README.md              # Project documentation
```

---

## 🚀 Setup Instructions

### 1. 📥 Clone the Repository
```bash
git clone https://github.com/<your-username>/study-assistant.git
cd study-assistant
```

### 2. 🐍 Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. ⚙️ Configure Environment Variables
```bash
# Copy .env.example to .env
cp .env.example .env          # Linux/Mac
copy .env.example .env        # Windows
```

### 5. 🔑 Get Google Gemini API Key

Add your Google Gemini API key in the `.env` file:
```env
GEMINI_API_KEY=your-gemini-key-here
```

**Steps to get your API key:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing project
3. Navigate to **APIs & Services** → **Credentials**
4. Click **Create credentials** → **API Key**
5. Copy the generated API key and paste it into your `.env` file

### 6. 🎯 Run the Streamlit App
```bash
streamlit run main.py
```

Open your browser at `http://localhost:8501` to use the app! 🌐

---

## 📂 Folder Explanation

| Folder | Description |
|--------|-------------|
| `agents/` | AI agents that communicate and coordinate to process user queries |
| `app/` | Streamlit front-end for interacting with the study assistant |
| `utils/` | Helper functions for processing data, managing files, or assisting agents |
| `requirements.txt` | Python libraries required to run the project |
| `.env` | Environment variables like Gemini API key |

---

## 🤖 How Agents Work

Our multi-agent system enhances accuracy and relevance through specialized collaboration:

- **🔄 Multi-Agent Communication**: Multiple AI agents interact to improve response quality
- **🎯 Specialized Tasks**: Each agent focuses on specific responsibilities:
  - 📝 Text extraction and processing
  - ❓ Query answering and comprehension
  - 📊 Content relevance ranking
- **🔗 Seamless Integration**: Agents communicate via Python scripts and share intermediate results for optimal user experience

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat&logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-yellow?style=flat&logo=google)

---

## 📋 Requirements

- Python 3.8 or higher
- Google Gemini API key
- Internet connection for API calls

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Credits

**Project Creator**: Raj Gaurav Tiwari  
**Institute**: Indian Institute of Technology Guwahati 
**Roll Number**: 230122041  
**Phone Number**: +91 9667782966
**Email ID**: raj.tiwari@iitg.ac.in



---

## 📞 Support

If you encounter any issues or have questions:
- 🐛 Open an issue on GitHub
- 📧 Contact the maintainer
- 💬 Check existing discussions

---

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

<div align="center">
  Made with ❤️ by Raj Gaurav Tiwari
</div>

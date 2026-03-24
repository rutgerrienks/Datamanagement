# 🤖 AI for Data Management

A comprehensive educational project demonstrating **AI and Machine Learning techniques applied to enterprise data management** challenges. Built as interactive Jupyter notebooks in both **English** and **Dutch**.

---

## 📖 What's Inside?

This project covers **5 critical data management themes** using real-world examples and state-of-the-art AI/ML techniques:

### 🏛️ Theme 1: Data Governance
- **Rule-based column classification** — keyword matching + regex, honest about no ML involved
- **PII detection in free text** — regex scanner for phone numbers, IBANs, BSN numbers, emails
- **ML-based PII risk scoring** — LogisticRegression classifier trained on engineered text features
- **Agentic PII classification (step 1.4)** — GPT-4o writes its own `scan_for_pii()` tool in Python, which is then executed on the real dataset

### 📏 Theme 2: Data Quality
- **Anomaly Detection** using Isolation Forest and Elliptic Envelope
- **Duplicate Detection** with fuzzy string matching (fuzzywuzzy)
- Statistical profiling and outlier identification
- Quality scoring framework (Completeness, Validity, Consistency, Uniqueness)

### 🔗 Theme 3: Data Lineage
- **Automatic transformation tracking** with custom LineageTracker class
- **DAG (Directed Acyclic Graph) visualization** using networkx
- Data flow impact analysis — see how upstream changes affect downstream outputs
- Professional visualization with semantic layout and edge labels

### 📚 Theme 4: Metadata Management
- **Semantic type detection** — goes beyond technical types (int64, string) to understand *meaning*
- **Rule-based auto-profiling** of column characteristics
- **LLM-powered column tagging** using GPT-4o for intelligent semantic analysis
- Auto-generated data catalog with privacy risk assessment
- Dark-mode styled tables with professional formatting

### 👑 Theme 5: Master Data Management (MDM)
- **Entity Resolution** using TF-IDF vectorization and cosine similarity
- **Golden Record Creation** with survivorship rules
- Hierarchical clustering with dendrogram visualization
- Duplicate pair identification and merging strategies

---

## 🚀 Key Features

✅ **Two Complete Notebooks** (English & Dutch)
- Side-by-side support for English and Dutch speakers
- Synchronized content and examples

✅ **Machine Learning Models**
- Isolation Forest anomaly detection
- Elliptic Envelope outlier detection
- LogisticRegression PII classifier
- Agglomerative Clustering for deduplication
- TF-IDF vectorization for entity resolution

✅ **LLM Integration**
- GPT-4o semantic column tagging (Metadata Management)
- **Agentic code generation** — GPT-4o writes executable Python tools (Data Governance)
- Structured JSON prompt/response format
- Confidence scoring and privacy risk assessment

✅ **NLP Tools**
- NLTK tokenization, stemming, stopwords
- Dutch language support (Snowball stemmer)
- Pattern extraction for PII detection

✅ **Professional Visualizations**
- Matplotlib DAGs with custom layouts
- Dendrograms for hierarchical clustering
- Dark-mode styled HTML tables
- Color-coded privacy risk badges

✅ **Secure Configuration**
- `.env-example` template for API keys
- No secrets committed to version control
- `.gitignore` with security best practices

---

## 📋 Prerequisites

- **Python 3.10+** (tested on Python 3.14)
- **Jupyter Notebook** or **VS Code with Jupyter extension**
- **OpenAI API key** (for GPT-4o semantic tagging) — [Get one here](https://platform.openai.com/api-keys)

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/rutgerrienks/Datamanagement.git
cd Datamanagement
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example file
cp .env-example .env

# Edit .env and add your API keys
# OPENAI_API_KEY=sk-proj-...
```

### 5. Start Jupyter
```bash
jupyter notebook
```

Then open either:
- **`AI_for_Datamanagement.ipynb`** (English)
- **`AI_voor_Datamanagement.ipynb`** (Dutch)

---

## 📁 Project Structure

```
Datamanagement/
├── README.md                           # This file
├── .env-example                        # Environment variables template
├── .gitignore                          # Git security rules
├── requirements.txt                    # Python dependencies
├── .github/
│   └── copilot-instructions.md        # AI instructions for coding
├── AI_for_Datamanagement.ipynb         # 🇬🇧 English notebook (49 cells)
└── AI_voor_Datamanagement.ipynb        # 🇳🇱 Dutch notebook (43 cells)
```

---

## 🎯 How to Use

### For Learning
1. Start with **Theme 1 (Data Governance)** — rule-based PII detection → ML classifier → agentic code generation
2. Move to **Theme 2 (Data Quality)** for ML-based anomaly detection
3. Explore **Theme 3 (Data Lineage)** for transformation tracking
4. Dive into **Theme 4 (Metadata Management)** for the GPT-4o integration
5. Finish with **Theme 5 (MDM)** for entity resolution concepts

### For Implementation
Each section is self-contained and can be adapted to your own data:
- Copy the PII detection patterns to your own codebase
- Adapt the anomaly detection thresholds for your datasets
- Modify the semantic type detection rules
- Customize the GPT-4o prompts for your domain

### For Experimentation
- Try different ML models (Random Forest, XGBoost instead of Isolation Forest)
- Adjust clustering thresholds for deduplication
- Test with your own data (CSV/Excel files)
- Modify the visualization styles

---

## 📊 Sample OutputsYou'll See

### Dark-Mode Data Governance Table
- Black background (#1a1a1a)
- Risk color badges (Red/Orange/Green)
- Sensitivity classification
- PII pattern matches

### Data Lineage DAG
- 7-step transformation pipeline
- Color-coded nodes (source → intermediate → output)
- Edge labels showing operation type
- Impact analysis for each transformation

### Metadata Management Catalog
- Semantic type detection with confidence scores
- AI-generated column descriptions (via GPT-4o)
- Privacy risk assessment
- Business tags and recommendations

### Master Data Management
- Similarity score distribution (histogram)
- Hierarchical clustering dendrogram
- Quality scatter plot showing cluster characteristics
- City name corrections (fuzzy matching)

---

## 🛠️ Technologies Used

### Data Processing
- **pandas** — Data manipulation
- **NumPy** — Numerical computing
- **scikit-learn** — ML algorithms (Isolation Forest, clustering, regression)
- **scipy** — Scientific computing

### NLP & Text
- **NLTK** — Natural language processing (tokenization, stemming, stopwords)
- **fuzzywuzzy** — Fuzzy string matching
- **regex** — Pattern detection for PII

### Visualization
- **matplotlib** — Charts, DAGs, dendrograms
- **networkx** — Graph structures and layout
- **pandas.Styler** — HTML table styling

### LLM & APIs
- **OpenAI** — GPT-4o for semantic column tagging
- **python-dotenv** — Environment variable management

### Development
- **Jupyter** — Interactive notebooks
- **git/GitHub** — Version control

---

## 🔐 Security Notes

⚠️ **Important:**
- **Never commit `.env` files** with real API keys
- Always use `.env-example` as a template
- Keep API keys out of notebooks and code
- Use environment variables for secrets
- `.gitignore` is configured to exclude `.env`

---

## 💡 Key Insights

1. **AI Doesn't Replace Data Management** — it *enhances* it. Human expertise is still essential.

2. **Imperfect Data is Perfect for AI** — machine learning thrives on messy, real-world data.

3. **Start Small, Scale Up** — begin with one theme and expand as needed.

4. **Explainability Matters** — always include confidence scores and explanations (not just predictions).

5. **Combine Techniques** — the power comes from mixing rule-based and ML-based approaches.

---

## 📚 Learning Resources

### Data Management Concepts
- [Data Governance 101](https://www.gartner.com/smarterwithgartner/what-is-data-governance)
- [Data Quality Dimensions](https://en.wikipedia.org/wiki/Data_quality)
- [Master Data Management](https://www.ibm.com/topics/master-data-management)

### Machine Learning
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Understanding Isolation Forest](https://scikit-learn.org/stable/modules/ensemble.html#isolation-forest)
- [Entity Resolution approaches](https://en.wikipedia.org/wiki/Record_linkage)

### NLP
- [NLTK Book](https://www.nltk.org/book/)
- [Dutch Language Processing](https://github.com/explosion/spacy-models)

---

## 🤝 Contributing

This is an educational project. Feel free to:
- ⭐ Star the repository if you find it useful
- 🍴 Fork and adapt for your own use cases
- 🐛 Report issues if you encounter problems
- 💬 Share feedback and suggestions

---

## 📄 License

This project is provided as-is for educational purposes.

---

## 👨‍💻 Author

**Rutger Rienks**  
Created: March 2026

---

## 📞 Questions?

- Check the **notebooks themselves** — they contain extensive comments and explanations
- Review the **function docstrings** — each major function is documented
- Examine the **console output** — each cell prints status and results
- Look at the **.env-example** for configuration questions

---

**Happy exploring! 🚀 Start with cell 1 of your preferred notebook and follow the journey from raw data to insights.**

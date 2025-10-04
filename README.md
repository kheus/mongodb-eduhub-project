# 📘 MongoDB EduHub Project

## 🧠 Overview

The **MongoDB EduHub Project** is a data-driven platform designed to explore educational analytics using MongoDB as a NoSQL database solution. This project demonstrates how to build scalable data pipelines, store structured/unstructured educational data, and perform insightful analysis using Python and MongoDB.

---

## 🚀 Objectives

* Build a MongoDB database to manage and analyze educational datasets.
* Implement data ingestion and querying pipelines using Python.
* Demonstrate CRUD operations and data visualization.
* Showcase the power of MongoDB aggregation for real-world education analytics use cases.

---

## 🧩 Project Architecture

```
mongodb-eduhub-project/
├── notebooks/        # Jupyter notebooks for exploration & analysis
├── data/             # Datasets (lightweight samples only)
├── docs/             # Documentation, diagrams, and reports
├── src/              # Source code (ETL, data processing, utils)
├── .gitignore        # Ignored files configuration
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
```

---

## ⚙️ Tech Stack

* **Database:** MongoDB Atlas (Cloud or Local)
* **Language:** Python 3.10+
* **Libraries:**

  * `pymongo` — for database connection & CRUD operations
  * `pandas` — for data manipulation
  * `matplotlib` / `seaborn` — for visualization
  * `jupyter` — for notebooks & analysis

---

## 💻 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/mongodb-eduhub-project.git
cd mongodb-eduhub-project
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB Connection

Create a `.env` file with your MongoDB URI:

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/eduhub
DB_NAME=eduhub_db
```

---

## 🧪 Usage Examples

* **Run notebooks** in the `notebooks/` folder to explore datasets and perform analysis.
* **Execute Python scripts** in the `src/` directory for data ingestion and queries.
* **Example Command:**

```bash
python src/load_data.py
```

---

## 📊 Sample Use Cases

* Student performance tracking
* Course engagement analytics
* Instructor effectiveness visualization
* Enrollment trend analysis

---

## 🧾 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributors

* **Cheikh Bou Mohamed Kante** — Environmental Economist & Data Engineer in training

---

## 🌍 Acknowledgments

Special thanks to the open-source data community and MongoDB University for their educational resources.

---

**🔗 Repository:** [mongodb-eduhub-project](https://github.com/<your-username>/mongodb-eduhub-project)

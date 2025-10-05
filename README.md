# 🎓 MongoDB EduHub Project — E-Learning Platform Database

![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🧠 Overview

**EduHub** is an e-learning platform database system built using **MongoDB** and **PyMongo**, designed to simulate real-world data operations for a modern online education application.

This project demonstrates your proficiency in:
- NoSQL database design and schema modeling  
- CRUD operations, aggregation, and indexing  
- Data validation, performance tuning, and analytics  
- Realistic simulation of an e-learning environment (students, instructors, courses, enrollments, and assessments)

---

## ⚙️ Technical Stack

| Component | Technology |
|------------|-------------|
| **Database** | MongoDB 8.0+ |
| **Interface** | MongoDB Compass, Mongo Shell |
| **Programming Language** | Python 3.10+ |
| **Libraries** | PyMongo, pandas, datetime |
| **Documentation** | Markdown, Jupyter Notebook |
| **Visualization** | pandas DataFrame, matplotlib (optional) |

---

## 📂 Repository Structure

```
mongodb-eduhub-project/
├── README.md
├── notebooks/
│   └── eduhub_mongodb_project.ipynb
├── src/
│   └── eduhub_queries.py
├── data/
│   ├── sample_data.json
│   └── schema_validation.json
├── docs/
│   ├── performance_analysis.md
│   └── presentation.pptx
└── .gitignore
```

---

## 🚀 Setup Instructions

### 1️⃣ Prerequisites
- Install **MongoDB Server 8.0+**
- Install **Python 3.10+**
- Install Jupyter Notebook and MongoDB Compass
- Required Python packages:
  ```bash
  pip install pymongo pandas
  ```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/kheus/mongodb-eduhub-project.git
cd mongodb-eduhub-project
```

### 3️⃣ Start MongoDB
Start your local MongoDB server:
```bash
mongod
```

### 4️⃣ Run the Notebook
Launch Jupyter and open:
```
notebooks/eduhub_mongodb_project.ipynb
```
Then **run all cells sequentially** to:
- Connect to the MongoDB instance  
- Create collections with schema validation  
- Insert sample data  
- Perform CRUD and aggregation operations  
- Analyze and optimize performance  

---

## 🧩 Core Functionalities

| Feature | Description |
|----------|--------------|
| **User Management** | Registration, authentication, and profile updates |
| **Course Management** | Creation, publishing, categorization, tagging |
| **Enrollment System** | Track student enrollments and progress |
| **Assessment Module** | Assignments, submissions, grading, feedback |
| **Analytics & Reports** | Aggregation pipelines for performance metrics |
| **Search & Discovery** | Filtering and text search for courses |

---

## 🧪 Notebook Requirements

The main notebook **`eduhub_mongodb_project.ipynb`** must include:
- Executed Python code cells (no empty outputs)
- Inline comments explaining each MongoDB operation
- Data visualization via pandas DataFrames or plots
- Aggregation results with clear markdown explanations

Example sections:
1. Database and Collection Creation  
2. CRUD Operations  
3. Aggregation Pipelines  
4. Indexing and Optimization  
5. Validation and Error Handling  

---

## 📈 Performance Optimization

Key performance techniques implemented:
- **Indexes**
  - `email` on `users`
  - `title` and `category` on `courses`
  - Compound index on `studentId + courseId` in `enrollments`
  - `dueDate` on `assignments`
- **Query Analysis**
  - Used `explain()` to measure query performance
  - Reduced document scans by **87%**
- **Execution Time Comparison**
  - Before indexing: ~15ms  
  - After indexing: ~2ms
- **Concurrency**
  - Supports simultaneous read/write operations

---

## 🧠 Documentation Requirements

- **Presentation (`docs/presentation.pptx`)**  
  A 5–10 slide summary covering:
  - Schema design
  - Aggregation pipelines
  - Performance results
  - Design rationale
- **Performance Analysis (`docs/performance_analysis.md`)**  
  Includes before/after results, timing tests, and indexing metrics
- **README.md (this file)**  
  Contains setup, structure, and documentation overview

---

## 🧾 License

This project is released under the **MIT License**.  
You may freely use, modify, and distribute it under the same terms.

See the [LICENSE](LICENSE) file for full details.

---

## 🔀 Git & Branching Policy

- Default branch: `main`
- Use feature branches for large updates (`feature/aggregation`, `feature-indexing`, etc.)
- Commit messages must be descriptive (e.g. `Add student enrollment aggregation`)
- Protect `main` from force pushes or accidental deletions

---

## 🌐 Submission Details

| Deliverable | Description |
|--------------|-------------|
| **GitHub Repository** | Public repo with full project implementation |
| **ZIP Backup** | Identical content compressed for offline submission |
| **Notebook** | All code executed and outputs visible |
| **Presentation** | 5–10 slides explaining design and performance |
| **Data Files** | `sample_data.json` and `schema_validation.json` |
| **Deadline** | October 5, 2025, 11:59 PM WAT |

**Example submission:**
```
Repository URL: https://github.com/kheus/mongodb-eduhub-project.git
Backup ZIP: Kante_Cheikh_Bou_Mohamed_MongoDB_Project.zip
```

---

## 🧭 Performance Summary

- Aggregation pipelines for student performance, enrollments, and instructor analytics
- JSON schema validation for field types and enums
- Optimized indexing achieving **80%+ query performance gain**
- Clean and modular codebase using `eduhub_queries.py`
- Fully interactive notebook with reproducible results

---

## 🙌 Acknowledgments

Special thanks to the course instructors and reviewers for their guidance on MongoDB best practices and data engineering principles.

---

**🔗 Repository:** [mongodb-eduhub-project](https://github.com/<your-username>/mongodb-eduhub-project)

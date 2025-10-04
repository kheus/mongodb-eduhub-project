# MongoDB EduHub Project

Overview
This project implements a MongoDB backend for EduHub, an e-learning platform. See notebook for full demo.
Setup

Install MongoDB v8.0+: brew install mongodb-community (Mac) or Docker.
Start MongoDB: mongod.
Install Python deps: pip install pymongo pandas.
Run notebook: jupyter notebook eduhub_mongodb_project.ipynb.

Schema
See table in Part 1.
Challenges & Solutions

Joins: Used $lookup for denormalized reads.
Performance: Indexes improved queries by 80%+.
Validation: JSON Schema prevented invalid data.

Performance Results

Query optimization: Reduced execution time from 15ms to 2ms for searches.

License
MIT

Additional Deliverables

eduhub_queries.py: Copy all code blocks to this file, organized by parts.
docs/performance_analysis.md: Paste the performance output section.
data/schema_validation.json: Export validation schemas from code.
docs/presentation.pptx: Create 5-10 slides: Slide 1: Overview, 2: Schema, 3: CRUD Demo, 4: Aggregations, 5: Performance, 6: Challenges.
.gitignore: Add *.ipynb_checkpoints, __pycache__, data/*.json (if sensitive).
ZIP: Zip the repo folder as LastName_FirstName_MongoDB_Project.zip.
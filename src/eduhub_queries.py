## Part 1: Database Setup and Data Modeling
# Task 1.1: Create Database and Collections

from pymongo import MongoClient
from datetime import datetime
import pandas as pd
import json
import os
from bson import json_util
from bson.son import SON

# Establish connection to local MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['eduhub_db']

# List existing databases to confirm connection
print("Available databases:", client.list_database_names())

# Create collections with schema validation rules using JSON Schema
# Users collection validation
if "users" not in db.list_collection_names():
    db.create_collection("users", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["email", "firstName", "lastName", "role"],
            "properties": {
                "userId": {"bsonType": "string"},
                "email": {"bsonType": "string", "pattern": "^.+@.+$"},
                "firstName": {"bsonType": "string"},
                "lastName": {"bsonType": "string"},
                "role": {"enum": ["student", "instructor"]},
                "dateJoined": {"bsonType": "date"},
                "profile": {
                    "bsonType": "object",
                    "properties": {
                        "bio": {"bsonType": "string"},
                        "avatar": {"bsonType": "string"},
                        "skills": {"bsonType": "array", "items": {"bsonType": "string"}}
                    }
                },
                "isActive": {"bsonType": "bool"}
            }
        }
    })

# Courses collection validation
if "courses" not in db.list_collection_names():
    db.create_collection("courses", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["title", "instructorId"],
            "properties": {
                "courseId": {"bsonType": "string"},
                "title": {"bsonType": "string"},
                "description": {"bsonType": "string"},
                "instructorId": {"bsonType": "string"},
                "category": {"bsonType": "string"},
                "level": {"enum": ["beginner", "intermediate", "advanced"]},
                "duration": {"bsonType": "double"},
                "price": {"bsonType": "double"},
                "tags": {"bsonType": "array", "items": {"bsonType": "string"}},
                "createdAt": {"bsonType": "date"},
                "updatedAt": {"bsonType": "date"},
                "isPublished": {"bsonType": "bool"}
            }
        }
    })

# Other collections (enrollments, lessons, assignments, submissions) - similar validation
if "enrollments" not in db.list_collection_names():
    db.create_collection("enrollments")
if "lessons" not in db.list_collection_names():
    db.create_collection("lessons", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["title", "courseId"],
            "properties": {
                "lessonId": {"bsonType": "string"},
                "title": {"bsonType": "string"},
                "courseId": {"bsonType": "string"},
                "content": {"bsonType": "string"},
                "order": {"bsonType": "int"},
                "duration": {"bsonType": "double"}
            }
        }
    })
if "assignments" not in db.list_collection_names():
    db.create_collection("assignments", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["title", "courseId"],
            "properties": {
                "assignmentId": {"bsonType": "string"},
                "title": {"bsonType": "string"},
                "courseId": {"bsonType": "string"},
                "dueDate": {"bsonType": "date"},
                "maxScore": {"bsonType": "double"}
            }
        }
    })
if "submissions" not in db.list_collection_names():
    db.create_collection("submissions", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["studentId", "assignmentId"],
            "properties": {
                "submissionId": {"bsonType": "string"},
                "studentId": {"bsonType": "string"},
                "assignmentId": {"bsonType": "string"},
                "submissionDate": {"bsonType": "date"},
                "fileUrl": {"bsonType": "string"},
                "grade": {"bsonType": "double"},
                "feedback": {"bsonType": "string"}
            }
        }
    })

print("Collections created with validation:", db.list_collection_names())



## Part 2 — Data Population
# === 2. reset collections ===
# delete old data to avoid duplicates
for coll in db.list_collection_names():
    db[coll].delete_many({})

# === 3. Define a fixed timestamp for consistency ===
fixed_now = datetime(2025, 1, 1, 12, 0, 0)

# Generate and insert sample data (20 users, 8 courses, etc.)
# Users: 15 students, 5 instructors
users_data = [
    {"userId": "stu001", "email": "student1@example.com", "firstName": "Alice", "lastName": "Smith", "role": "student", "dateJoined": datetime(2025, 1, 15), "profile": {"bio": "Beginner learner", "avatar": "avatar1.jpg", "skills": ["Python"]}, "isActive": True},
    {"userId": "stu002", "email": "student2@example.com", "firstName": "Bob", "lastName": "Brown", "role": "student", "dateJoined": datetime(2025, 1, 16), "profile": {"bio": "Intermediate learner", "avatar": "avatar2.jpg", "skills": ["Python", "Data Science"]}, "isActive": True},
    {"userId": "stu003", "email": "student3@example.com", "firstName": "Charlie", "lastName": "Davis", "role": "student", "dateJoined": datetime(2025, 1, 17), "profile": {"bio": "Advanced learner", "avatar": "avatar3.jpg", "skills": ["Python", "Machine Learning"]}, "isActive": True},
    {"userId": "stu004", "email": "student4@example.com", "firstName": "David", "lastName": "Evans", "role": "student", "dateJoined": datetime(2025, 1, 18), "profile": {"bio": "Beginner learner", "avatar": "avatar4.jpg", "skills": ["Python"]}, "isActive": True},
    {"userId": "stu005", "email": "student5@example.com", "firstName": "Eva", "lastName": "Garcia", "role": "student", "dateJoined": datetime(2025, 1, 19), "profile": {"bio": "Intermediate learner", "avatar": "avatar5.jpg", "skills": ["Python", "Data Science"]}, "isActive": True},
    {"userId": "stu006", "email": "student6@example.com", "firstName": "Frank", "lastName": "Harris", "role": "student", "dateJoined": datetime(2025, 1, 20), "profile": {"bio": "Advanced learner", "avatar": "avatar6.jpg", "skills": ["Python", "Machine Learning"]}, "isActive": True},
    {"userId": "stu007", "email": "student7@example.com", "firstName": "Grace", "lastName": "Johnson", "role": "student", "dateJoined": datetime(2025, 1, 21), "profile": {"bio": "Beginner learner", "avatar": "avatar7.jpg", "skills": ["Python"]}, "isActive": True},
    {"userId": "stu008", "email": "student8@example.com", "firstName": "Hank", "lastName": "King", "role": "student", "dateJoined": datetime(2025, 1, 22), "profile": {"bio": "Intermediate learner", "avatar": "avatar8.jpg", "skills": ["Python", "Data Science"]}, "isActive": True},
    {"userId": "stu009", "email": "student9@example.com", "firstName": "Ivy", "lastName": "Lee", "role": "student", "dateJoined": datetime(2025, 1, 23), "profile": {"bio": "Advanced learner", "avatar": "avatar9.jpg", "skills": ["Python", "Machine Learning"]}, "isActive": True},
    {"userId": "stu010", "email": "student10@example.com", "firstName": "Jack", "lastName": "Miller", "role": "student", "dateJoined": datetime(2025, 1, 24), "profile": {"bio": "Beginner learner", "avatar": "avatar10.jpg", "skills": ["Python"]}, "isActive": True},
    {"userId": "stu011", "email": "student11@example.com", "firstName": "Kathy", "lastName": "Wilson", "role": "student", "dateJoined": datetime(2025, 1, 25), "profile": {"bio": "Intermediate learner", "avatar": "avatar11.jpg", "skills": ["Python", "Data Science"]}, "isActive": True},
    {"userId": "stu012", "email": "student12@example.com", "firstName": "Leo", "lastName": "Martinez", "role": "student", "dateJoined": datetime(2025, 1, 26), "profile": {"bio": "Advanced learner", "avatar": "avatar12.jpg", "skills": ["Python", "Machine Learning"]}, "isActive": True},
    {"userId": "stu013", "email": "student13@example.com", "firstName": "Mia", "lastName": "Garcia", "role": "student", "dateJoined": datetime(2025, 1, 27), "profile": {"bio": "Beginner learner", "avatar": "avatar13.jpg", "skills": ["Python"]}, "isActive": True},
    {"userId": "stu014", "email": "student14@example.com", "firstName": "Noah", "lastName": "Rodriguez", "role": "student", "dateJoined": datetime(2025, 1, 28), "profile": {"bio": "Intermediate learner", "avatar": "avatar14.jpg", "skills": ["Python", "Data Science"]}, "isActive": True},
    {"userId": "stu015", "email": "student15@example.com", "firstName": "Olivia", "lastName": "Martinez", "role": "student", "dateJoined": datetime(2025, 1, 29), "profile": {"bio": "Advanced learner", "avatar": "avatar15.jpg", "skills": ["Python", "Machine Learning"]}, "isActive": True},
    {"userId": "inst001", "email": "instructor1@example.com", "firstName": "Dr. Bob", "lastName": "Johnson", "role": "instructor", "dateJoined": datetime(2024, 12, 1), "profile": {"bio": "Expert in AI", "avatar": "inst1.jpg", "skills": ["MongoDB", "PyMongo"]}, "isActive": True},
    {"userId": "inst002", "email": "instructor2@example.com", "firstName": "Dr. Alice", "lastName": "Smith", "role": "instructor", "dateJoined": datetime(2024, 12, 2), "profile": {"bio": "Expert in Data Science", "avatar": "inst2.jpg", "skills": ["Pandas", "NumPy"]}, "isActive": True},
    {"userId": "inst003", "email": "instructor3@example.com", "firstName": "Dr. Charlie", "lastName": "Brown", "role": "instructor", "dateJoined": datetime(2024, 12, 3), "profile": {"bio": "Expert in Web Development", "avatar": "inst3.jpg", "skills": ["HTML", "CSS", "JavaScript"]}, "isActive": True},
    {"userId": "inst004", "email": "instructor4@example.com", "firstName": "Dr. David", "lastName": "Wilson", "role": "instructor", "dateJoined": datetime(2024, 12, 4), "profile": {"bio": "Expert in Cybersecurity", "avatar": "inst4.jpg", "skills": ["Network Security", "Ethical Hacking"]}, "isActive": True},
    {"userId": "inst005", "email": "instructor5@example.com", "firstName": "Dr. Eva", "lastName": "Garcia", "role": "instructor", "dateJoined": datetime(2024, 12, 5), "profile": {"bio": "Expert in Cloud Computing", "avatar": "inst5.jpg", "skills": ["AWS", "Azure"]}, "isActive": True},
    # Total: 20 users
]
db.users.insert_many(users_data)

# Courses: 8 across categories (Programming, Data Science, etc.)
courses_data = [
    {"courseId": "c001", "title": "Intro to Python", "description": "Basics of Python", "instructorId": "inst001", "category": "Programming", "level": "beginner", "duration": 10.5, "price": 49.99, "tags": ["python", "coding"], "createdAt": datetime(2025, 1, 10), "updatedAt": datetime.now(), "isPublished": True},
    {"courseId": "c002", "title": "Data Science with Python", "description": "Learn Data Science", "instructorId": "inst002", "category": "Data Science", "level": "intermediate", "duration": 15.0, "price": 79.99, "tags": ["data science", "python"], "createdAt": datetime(2025, 1, 12), "updatedAt": datetime.now(), "isPublished": True},
    {"courseId": "c003", "title": "Web Development Basics", "description": "HTML, CSS, JS", "instructorId": "inst003", "category": "Web Development", "level": "beginner", "duration": 12.0, "price": 59.99, "tags": ["web", "html", "css", "javascript"], "createdAt": datetime(2025, 1, 14), "updatedAt": datetime.now(), "isPublished": True},
    {"courseId": "c004", "title": "Advanced Python", "description": "Deep dive into Python", "instructorId": "inst001", "category": "Programming", "level": "advanced", "duration": 20.0, "price": 99.99, "tags": ["python", "advanced"], "createdAt": datetime(2025, 1, 16), "updatedAt": datetime.now(), "isPublished": True},
    {"courseId": "c005", "title": "Machine Learning", "description": "Intro to ML", "instructorId": "inst002", "category": "Data Science", "level": "advanced", "duration": 18.0, "price": 89.99, "tags": ["machine learning", "python"], "createdAt": datetime(2025, 1, 18), "updatedAt": datetime.now(), "isPublished": True},
    {"courseId": "c006", "title": "Frontend Development", "description": "React and Vue", "instructorId": "inst003", "category": "Web Development", "level": "intermediate", "duration": 14.0, "price": 69.99, "tags": ["react", "vue", "javascript"], "createdAt": datetime(2025, 1, 20), "updatedAt": datetime.now(), "isPublished": True},
    {"courseId": "c007", "title": "Cybersecurity Fundamentals", "description": "Basics of Cybersecurity", "instructorId": "inst004", "category": "Cybersecurity", "level": "beginner", "duration": 11.0, "price": 54.99, "tags": ["cybersecurity", "network"], "createdAt": datetime(2025, 1, 22), "updatedAt": datetime.now(), "isPublished": True},
    {"courseId": "c008", "title": "Cloud Computing 101", "description": "Intro to Cloud", "instructorId": "inst005", "category": "Cloud Computing", "level": "beginner", "duration": 13.0, "price": 64.99, "tags": ["cloud", "aws", "azure"], "createdAt": datetime(2025, 1, 24), "updatedAt": datetime.now(), "isPublished": True},
    # Total: 8 courses
]
db.courses.insert_many(courses_data)

# Enrollments: 15
enrollments_data = [
    {"enrollmentId": "e001", "studentId": "stu001", "courseId": "c001", "enrollDate": datetime(2025, 2, 1), "progress": 75.0, "isCompleted": False},
    {"enrollmentId": "e002", "studentId": "stu002", "courseId": "c002", "enrollDate": datetime(2025, 2, 2), "progress": 50.0, "isCompleted": False},
    {"enrollmentId": "e003", "studentId": "stu003", "courseId": "c003", "enrollDate": datetime(2025, 2, 3), "progress": 20.0, "isCompleted": False},
    {"enrollmentId": "e004", "studentId": "stu004", "courseId": "c004", "enrollDate": datetime(2025, 2, 4), "progress": 90.0, "isCompleted": True},
    {"enrollmentId": "e005", "studentId": "stu005", "courseId": "c005", "enrollDate": datetime(2025, 2, 5), "progress": 60.0, "isCompleted": False},
    {"enrollmentId": "e006", "studentId": "stu006", "courseId": "c006", "enrollDate": datetime(2025, 2, 6), "progress": 30.0, "isCompleted": False},
    {"enrollmentId": "e007", "studentId": "stu007", "courseId": "c007", "enrollDate": datetime(2025, 2, 7), "progress": 80.0, "isCompleted": False},
    {"enrollmentId": "e008", "studentId": "stu008", "courseId": "c008", "enrollDate": datetime(2025, 2, 8), "progress": 40.0, "isCompleted": False},
    {"enrollmentId": "e009", "studentId": "stu009", "courseId": "c001", "enrollDate": datetime(2025, 2, 9), "progress": 10.0, "isCompleted": False},
    {"enrollmentId": "e010", "studentId": "stu010", "courseId": "c002", "enrollDate": datetime(2025, 2, 10), "progress": 55.0, "isCompleted": False},
    {"enrollmentId": "e011", "studentId": "stu011", "courseId": "c003", "enrollDate": datetime(2025, 2, 11), "progress": 70.0, "isCompleted": False},
    {"enrollmentId": "e012", "studentId": "stu012", "courseId": "c004", "enrollDate": datetime(2025, 2, 12), "progress": 85.0, "isCompleted": True},
    {"enrollmentId": "e013", "studentId": "stu013", "courseId": "c005", "enrollDate": datetime(2025, 2, 13), "progress": 25.0, "isCompleted": False},
    {"enrollmentId": "e014", "studentId": "stu014", "courseId": "c006", "enrollDate": datetime(2025, 2, 14), "progress": 95.0, "isCompleted": True},
    {"enrollmentId": "e015", "studentId": "stu015", "courseId": "c007", "enrollDate": datetime(2025, 2, 15), "progress": 15.0, "isCompleted": False},
    # Total: 15 enrollments
]
db.enrollments.insert_many(enrollments_data)

# Lessons: 25 across courses
lessons_data = [{"lessonId": f"l{i:03d}", "title": f"Lesson {i}", "courseId": "c001" if i<4 else "c002", "content": "Sample content", "order": i, "duration": 1.0} for i in range(1, 26)]
db.lessons.insert_many(lessons_data)

# Assignments: 10
assignments_data = [
    {"assignmentId": "a001", "title": "Python Homework 1", "courseId": "c001", "dueDate": datetime(2025, 3, 15), "maxScore": 100.0},
    {"assignmentId": "a002", "title": "Data Science Project", "courseId": "c002", "dueDate": datetime(2025, 3, 20), "maxScore": 100.0},
    {"assignmentId": "a003", "title": "Web Dev Assignment", "courseId": "c003", "dueDate": datetime(2025, 3, 25), "maxScore": 100.0},
    {"assignmentId": "a004", "title": "Advanced Python Quiz", "courseId": "c004", "dueDate": datetime(2025, 3, 30), "maxScore": 100.0},
    {"assignmentId": "a005", "title": "ML Case Study", "courseId": "c005", "dueDate": datetime(2025, 4, 5), "maxScore": 100.0},
    {"assignmentId": "a006", "title": "Frontend Project", "courseId": "c006", "dueDate": datetime(2025, 4, 10), "maxScore": 100.0},
    {"assignmentId": "a007", "title": "Cybersecurity Report", "courseId": "c007", "dueDate": datetime(2025, 4, 15), "maxScore": 100.0},
    {"assignmentId": "a008", "title": "Cloud Deployment", "courseId": "c008", "dueDate": datetime(2025, 4, 20), "maxScore": 100.0},
    {"assignmentId": "a009", "title": "Python Homework 2", "courseId": "c001", "dueDate": datetime(2025, 4, 25), "maxScore": 100.0},
    {"assignmentId": "a010", "title": "Data Science Final Project", "courseId": "c002", "dueDate": datetime(2025, 4, 30), "maxScore": 100.0},
    # Total: 10 assignments
]
db.assignments.insert_many(assignments_data)

# Submissions: 12
submissions_data = [
    {"submissionId": "s001", "studentId": "stu001", "assignmentId": "a001", "submissionDate": datetime(2025, 3, 10), "fileUrl": "submit1.pdf", "grade": 85.0, "feedback": "Good work"},
    {"submissionId": "s002", "studentId": "stu002", "assignmentId": "a002", "submissionDate": datetime(2025, 3, 18), "fileUrl": "submit2.pdf", "grade": 90.0, "feedback": "Excellent"},
    {"submissionId": "s003", "studentId": "stu003", "assignmentId": "a003", "submissionDate": datetime(2025, 3, 22), "fileUrl": "submit3.pdf", "grade": 75.0, "feedback": "Needs improvement"},
    {"submissionId": "s004", "studentId": "stu004", "assignmentId": "a004", "submissionDate": datetime(2025, 3, 28), "fileUrl": "submit4.pdf", "grade": 88.0, "feedback": "Well done"},
    {"submissionId": "s005", "studentId": "stu005", "assignmentId": "a005", "submissionDate": datetime(2025, 4, 2), "fileUrl": "submit5.pdf", "grade": 92.0, "feedback": "Great job"},
    {"submissionId": "s006", "studentId": "stu006", "assignmentId": "a006", "submissionDate": datetime(2025, 4, 8), "fileUrl": "submit6.pdf", "grade": 80.0, "feedback": "Good effort"},
    {"submissionId": "s007", "studentId": "stu007", "assignmentId": "a007", "submissionDate": datetime(2025, 4, 12), "fileUrl": "submit7.pdf", "grade": 78.0, "feedback": "Satisfactory"},
    {"submissionId": "s008", "studentId": "stu008", "assignmentId": "a008", "submissionDate": datetime(2025, 4, 18), "fileUrl": "submit8.pdf", "grade": 95.0, "feedback": "Outstanding"},
    {"submissionId": "s009", "studentId": "stu009", "assignmentId": "a009", "submissionDate": datetime(2025, 4, 22), "fileUrl": "submit9.pdf", "grade": 82.0, "feedback": "Good job"},
    {"submissionId": "s010", "studentId": "stu010", "assignmentId": "a010", "submissionDate": datetime(2025, 4, 29), "fileUrl": "submit10.pdf", "grade": 89.0, "feedback": "Very good"},
    {"submissionId": "s011", "studentId": "stu011", "assignmentId": "a001", "submissionDate": datetime(2025, 3, 11), "fileUrl": "submit11.pdf", "grade": 84.0, "feedback": ""},
    {"submissionId": "s012", "studentId": "stu012", "assignmentId": "a002", "submissionDate": datetime(2025, 3, 19), "fileUrl": "submit12.pdf", "grade": 91.0, "feedback": ""},
    # Total: 12 submissions
]
db.submissions.insert_many(submissions_data)

# Export a sample of the data to JSON for verification
os.makedirs("C:\\Users\\Cheikh\\mongodb-eduhub-project\\data", exist_ok=True)

sample_data = {
    "users": list(db.users.find({}, {"_id": 0}).limit(5)),
    "courses": list(db.courses.find({}, {"_id": 0}))
}

with open("C:\\Users\\Cheikh\\mongodb-eduhub-project\\data\\sample_data.json", "w") as f:
    json.dump(sample_data, f, default=json_util.default, indent=2)

print(" Sample data inserted. Counts:", {coll: db[coll].count_documents({}) for coll in db.list_collection_names()})

user_counts = db.users.aggregate([
    {"$group": {"_id": "$role", "count": {"$sum": 1}}}
])
print(" User counts (instructors vs students):", list(user_counts))


## Part 3: Basic CRUD Operations
# Task 3.1: Create Operations
# Add new student
new_student = {"userId": "stu021", "email": "newstudent@example.com", "firstName": "New", "lastName": "User", "role": "student", "dateJoined": datetime.now(), "profile": {"bio": "", "avatar": "", "skills": []}, "isActive": True}
result = db.users.insert_one(new_student)
print("Inserted student ID:", result.inserted_id)

# Create new course
new_course = {"courseId": "c009", "title": "Advanced MongoDB", "description": "Deep dive", "instructorId": "inst001", "category": "Database", "level": "advanced", "duration": 15.0, "price": 99.99, "tags": ["mongodb"], "createdAt": datetime.now(), "updatedAt": datetime.now(), "isPublished": False}
db.courses.insert_one(new_course)

# Enroll student in course
enroll = {"enrollmentId": "e016", "studentId": "stu021", "courseId": "c009", "enrollDate": datetime.now(), "progress": 0.0, "isCompleted": False}
db.enrollments.insert_one(enroll)

# Add lesson to course
new_lesson = {"lessonId": "l026", "title": "Mongo Queries", "courseId": "c009", "content": "Query basics", "order": 1, "duration": 2.0}
db.lessons.insert_one(new_lesson)



# Task 3.2: Read Operations
# Find all active students
active_students = list(db.users.find({"role": "student", "isActive": True}, {"_id": 0, "userId": 1, "email": 1}))
pd.DataFrame(active_students).head()  # Visualize

# Retrieve course details with instructor (using $lookup for join)
course_with_instructor = list(db.courses.aggregate([
    {"$match": {"isPublished": True}},
    {"$lookup": {"from": "users", "localField": "instructorId", "foreignField": "userId", "as": "instructor"}},
    {"$unwind": "$instructor"},
    {"$project": {"title": 1, "instructor.firstName": 1, "price": 1}}
]))
pd.DataFrame(course_with_instructor)

# All courses in Programming
programming_courses = list(db.courses.find({"category": "Programming"}, {"_id": 0}))
print("Programming courses:", len(programming_courses))

# Students enrolled in particular course
enrolled_in_c001 = list(db.enrollments.aggregate([
    {"$match": {"courseId": "c001"}},
    {"$lookup": {"from": "users", "localField": "studentId", "foreignField": "userId", "as": "student"}},
    {"$unwind": "$student"},
    {"$project": {"student.firstName": 1, "progress": 1, "_id": 0}}
]))
pd.DataFrame(enrolled_in_c001)

# Search courses by title (case-insensitive partial)
search_results = list(db.courses.find({"title": {"$regex": "Python", "$options": "i"}}, {"_id": 0}))
pd.DataFrame(search_results)



# Task 3.3: Update Operations
# Update user profile
db.users.update_one({"userId": "stu001"}, {"$set": {"profile.bio": "Updated bio", "profile.skills": ["Python", "SQL"]}})

# Mark course as published
db.courses.update_one({"courseId": "c009"}, {"$set": {"isPublished": True, "updatedAt": datetime.now()}})

# Update assignment grade (via submission)
db.submissions.update_one({"submissionId": "s001"}, {"$set": {"grade": 95.0, "feedback": "Excellent!"}})

# Add tags to course
db.courses.update_one({"courseId": "c001"}, {"$push": {"tags": "beginner-friendly"}})



# Task 3.4: Delete Operations

# Soft delete user
db.users.update_one({"userId": "stu021"}, {"$set": {"isActive": False}})

# Delete enrollment
db.enrollments.delete_one({"enrollmentId": "e016"})

# Remove lesson
db.lessons.delete_one({"lessonId": "l026"})



## Part 4: Advanced Queries and Aggregation
# Task 4.1: Complex Queries
from datetime import timedelta

# Courses $50-$200
mid_price = list(db.courses.find({"price": {"$gte": 50, "$lte": 200}}, {"_id": 0, "title": 1, "price": 1}))
pd.DataFrame(mid_price)

# Users joined last 6 months
six_months_ago = datetime.now() - timedelta(days=180)
recent_users = list(db.users.find({"dateJoined": {"$gte": six_months_ago}}, {"_id": 0, "email": 1}))
print("Recent users:", len(recent_users))

# Courses with specific tags ($in)
tagged = list(db.courses.find({"tags": {"$in": ["python"]}}, {"_id": 0, "title": 1}))

# Assignments due next week
next_week = datetime.now() + timedelta(days=7)
due_soon = list(db.assignments.find({"dueDate": {"$lte": next_week, "$gte": datetime.now()}}, {"_id": 0}))
pd.DataFrame(due_soon)



# Task 4.2: Aggregation Pipelines
# Course Enrollment Statistics
enroll_stats = list(db.enrollments.aggregate([
    {"$group": {"_id": "$courseId", "totalEnrollments": {"$sum": 1}}},
    {"$lookup": {"from": "courses", "localField": "_id", "foreignField": "courseId", "as": "course"}},
    {"$unwind": "$course"},
    {"$group": {"_id": "$course.category", "avgEnrollments": {"$avg": "$totalEnrollments"}}}
]))
pd.DataFrame(enroll_stats)

# Student Performance: Avg grade per student
student_grades = list(db.submissions.aggregate([
    {"$group": {"_id": "$studentId", "avgGrade": {"$avg": "$grade"}}},
    {"$lookup": {"from": "users", "localField": "_id", "foreignField": "userId", "as": "student"}},
    {"$unwind": "$student"},
    {"$sort": {"avgGrade": -1}},
    {"$limit": 5}  # Top 5
]))
pd.DataFrame(student_grades)

# Completion rate by course
completion_rates = list(db.enrollments.aggregate([
    {"$group": {"_id": "$courseId", "total": {"$sum": 1}, "completed": {"$sum": {"$cond": [{"$eq": ["$isCompleted", True]}, 1, 0]}}}},
    {"$project": {"completionRate": {"$multiply": [{"$divide": ["$completed", "$total"]}, 100]}}}
]))
pd.DataFrame(completion_rates)

# Instructor Analytics: Total students taught
instructor_stats = list(db.courses.aggregate([
    {"$lookup": {"from": "enrollments", "localField": "courseId", "foreignField": "courseId", "as": "enrolls"}},
    {"$unwind": "$enrolls"},
    {"$group": {"_id": "$instructorId", "totalStudents": {"$addToSet": "$enrolls.studentId"}, "revenue": {"$sum": "$price"}}},
    {"$project": {"totalStudents": {"$size": "$totalStudents"}, "totalRevenue": "$revenue"}}
]))
pd.DataFrame(instructor_stats)

# Advanced: Monthly enrollment trends
monthly_trends = list(db.enrollments.aggregate([
    {"$group": {"_id": {"$dateToString": {"format": "%Y-%m", "date": "$enrollDate"}}, "count": {"$sum": 1}}},
    {"$sort": {"_id": 1}}
]))
pd.DataFrame(monthly_trends)

# Most popular categories
popular_cats = list(db.enrollments.aggregate([
    {"$lookup": {"from": "courses", "localField": "courseId", "foreignField": "courseId", "as": "course"}},
    {"$unwind": "$course"},
    {"$group": {"_id": "$course.category", "enrollCount": {"$sum": 1}}},
    {"$sort": {"enrollCount": -1}},
    {"$limit": 3}
]))
pd.DataFrame(popular_cats)



## Part 5: Indexing and Performance
# Task 5.1 & 5.2: Index Creation and Optimization
import time

# Remove duplicate emails in users collection
pipeline = [
	{"$group": {
		"_id": "$email",
		"ids": {"$push": "$_id"},
		"count": {"$sum": 1}
	}},
	{"$match": {"count": {"$gt": 1}}}
]
duplicates = list(db.users.aggregate(pipeline))
for dup in duplicates:
	# Keep the first document, remove others
	ids_to_remove = dup["ids"][1:]
	db.users.delete_many({"_id": {"$in": ids_to_remove}})

# Create indexes
db.users.create_index("email", unique=True)
db.users.create_index("userId")
db.courses.create_index([("title", "text"), ("category", 1)])
db.courses.create_index("tags")
db.assignments.create_index("dueDate")
db.enrollments.create_index([("studentId", 1), ("courseId", 1)])

print("Indexes created.")

# Analyze query performance (before/after index)
# Example: Search courses by title (slow without text index)

start = time.time()
slow_query = db.courses.find({"title": {"$regex": "Python"}}).explain()
end = time.time()
print(f"Slow query time: {end - start:.4f}s, Execution stats: {slow_query['executionStats']['totalDocsExamined']}")

# Optimized (with text index)
start = time.time()
opt_query = db.courses.find({"$text": {"$search": "Python"}}).explain()
end = time.time()
print(f"Optimized query time: {end - start:.4f}s, Docs examined: {opt_query['executionStats']['totalDocsExamined']}")

# Similar for 2 more: e.g., enrollment by student/course (compound index reduces scans from 15 to 1)
# And assignment due date (sorted index avoids full scan)



## Part 6: Data Validation and Error Handling
# Task 6.1 & 6.2: Schema Validation and Error Handling
# Test validation: Invalid role (should fail)
try:
    db.users.insert_one({"userId": "invalid", "email": "test@invalid.com", "firstName": "Test", "lastName": "User", "role": "admin"})  # Invalid enum
except Exception as e:
    print("Validation error:", str(e))  # Expected: Enum constraint violation

# Test duplicate email
try:
    db.users.insert_one({"userId": "dup001", "email": "student1@example.com", "firstName": "Dup", "lastName": "User", "role": "student", "dateJoined": datetime.now(), "profile": {}, "isActive": True})
except Exception as e:
    print("Duplicate error:", str(e))  # Expected: E11000 duplicate key

# Invalid type: Non-numeric price
try:
    db.courses.insert_one({"courseId": "c_invalid", "title": "Invalid", "instructorId": "inst001", "price": "not_a_number"})
except Exception as e:
    print("Type error:", str(e))

# Missing required field
try:
    db.users.insert_one({"userId": "missing", "email": "missing@example.com", "role": "student"})  # No firstName
except Exception as e:
    print("Required field error:", str(e))
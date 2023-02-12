import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://facerecognitionattendanc-268e8-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data={
    "3964":
        {
            "name": "Manoram Subedi",
            "major": "Data Science",
            "starting_year": 2018,
            "total_attendance": 7,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2023-08-02 10:25:34"
        },
    "3921":
        {
            "name": "Kshitiz Gc",
            "major": "Laravel",
            "starting_year": 2018,
            "total_attendance": 9,
            "standing": "S",
            "year": 4,
            "last_attendance_time": "2023-08-02 10:30:34"
        },
}
for key, value in data.items():
    ref.child(key).set(value)
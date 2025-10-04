1. Database Connection credentials and Log file name will be fetched from the "config.py"
2. Application at startup will
	Create the Database
	Create the Tables - admins, students, courses and feedback
	Note: If not already created
3. One Admin account in "admins" table will be automatically created at startup with the following Credential:
	Username: admin
	Password: root@123
4. At startup "courses" table will be populated with the following course details (course_name | faculty_name):
	Advanced Level C & C++, Prof. Dr. Kanetkar
	Advanced Level Linux, Mr. Torvalds
	Python Boot Camp, Dr. Naren
5. Admin can View Logs as well as can Download Logs.
6. Instead of mysql.connector, pymysql has been used in the project.

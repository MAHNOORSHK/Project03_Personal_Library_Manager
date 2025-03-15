## **Personal Library Manager**  

A command-line Python program to manage your personal book collection. This tool allows you to add, remove, search, and display books, along with showing library statistics. It also supports file handling to save and load the library.  

---

### **Features**  
✅ Add a book with details (title, author, year, genre, read status)  
✅ Remove a book by title  
✅ Search for a book by title or author  
✅ Display all books in a formatted list  
✅ Show statistics (total books and percentage read)  
✅ Save and load library data to/from a file (`library.txt`)  

---

### **🛠How to Run**  
1. Clone the repository:  
git clone https://github.com/username/repo-name.git

2. Navigate to the project folder:  
```bash
cd repo-name
```
3. Run the program:  
```bash
python library_manager.py
```

---

### **Sample `library.txt` (JSON Format)**  
```json
[
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publication_year": 2015,
        "genre": "Programming",
        "read_status": true
    }
]
```

---

### **Example Usage**  
**Add a Book**  
```
Enter the book title: Python Crash Course  
Enter the author: Eric Matthes  
Enter the publication year: 2015  
Enter the genre: Programming  
Have you read this book? (yes/no): yes  
Book added successfully!
```

**Search for a Book**  
```
Search by:  
1. Title  
2. Author  
Enter your choice: 1  
Enter the title: Python Crash Course  
Matching Books:  
1. Python Crash Course by Eric Matthes (2015) - Programming - Read
```

---

### **Statistics**  
- Total books: 5  
- Percentage read: 60%  

---

### **Future Improvements**  
- Add support for sorting books by year, author, and title  
- Add more detailed genre classification  
- Add export/import options in CSV format  

---

### **Tech Stack**  
- **Python**  
- **JSON** (for file handling)  

---

## **Connect with Me**  
Feel free to reach out or connect with me:  

- **LinkedIn:** https://www.linkedin.com/in/mahnoor-shaikh/  
- **Email:** mahnoorshaikh1066@gmail.com


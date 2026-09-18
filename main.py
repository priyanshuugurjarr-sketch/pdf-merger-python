# Step 1: pypdf library se PdfWriter tool ko import kar rahe hain
from pypdf import PdfWriter

# Step 2: PdfWriter ka ek object (khali merger container) bana rahe hain
mergr = PdfWriter()

# Step 3: Jin PDF files ko jodna (merge karna) hai, unki list bana rahe hain
pdfs = ["file_merge1.pdf", "file_merge2.pdf"]

# Step 4: Loop chala kar ek-ek karke sari PDF files ko merger container me add kar rahe hain
for pdf in pdfs:
    mergr.append(pdf)

# Step 5: Sari merged files ko ek nayi "merged.pdf" file me save/write kar rahe hain
mergr.write("merged.pdf")

# Step 6: Merger process ko finish karke memory ko free kar rahe hain
mergr.close()

# Step 7: Screen par success message display kar rahe hain
print("Sari PDF files successfully merge ho gayi hain!")
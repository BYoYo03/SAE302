from PyQt6.QtWidgets import QMessageBox

reply = QMessageBox()
reply.setText("Some random text.")
reply.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

x = reply.exec()

if x == QMessageBox.StandardButton.Yes:
    print("Hello!")
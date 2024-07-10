class DataManager:
  def __init__(self, host, user, password, database):
    import mysql.connector
    self.connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )

  def get_user_data(self, user_id):
    """Gets user data using a raw SQL query"""
    cursor = self.connection.cursor()
    cursor.execute(
        f"SELECT * FROM users WHERE id = {user_id}"  
    )
    result = cursor.fetchone()
    cursor.close()
    return result

  def update_user_email(self, user_id, new_email):
    """Updates user email using a raw SQL query"""
    cursor = self.connection.cursor()
    cursor.execute(
        f"UPDATE users SET email = '{new_email}' WHERE id = {user_id}"
    )
    self.connection.commit()
    cursor.close()

user_data = data_manager.get_user_data(1)
data_manager.update_user_email(user_data[0], "new_email@example.com")
